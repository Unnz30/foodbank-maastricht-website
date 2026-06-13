const express = require("express");

const router = express.Router();
const defaultLimit = 6;
const maxLimit = 12;
const defaultCacheSeconds = 900;
let cachedFeed = null;
let cacheExpiresAt = 0;

function getLimit(value) {
  const requested = Number(value || defaultLimit);
  if (!Number.isFinite(requested)) return defaultLimit;
  return Math.min(Math.max(Math.trunc(requested), 1), maxLimit);
}

function getInstagramEndpoint(limit) {
  const accessToken = process.env.INSTAGRAM_ACCESS_TOKEN;
  const instagramUserId = process.env.INSTAGRAM_USER_ID;
  const graphVersion = process.env.INSTAGRAM_GRAPH_VERSION || "v23.0";

  if (!accessToken) return null;

  const baseUrl = instagramUserId
    ? `https://graph.facebook.com/${graphVersion}/${encodeURIComponent(instagramUserId)}/media`
    : "https://graph.instagram.com/me/media";

  const params = new URLSearchParams({
    access_token: accessToken,
    fields: "id,caption,media_type,media_url,permalink,thumbnail_url,timestamp",
    limit: String(limit)
  });

  return `${baseUrl}?${params.toString()}`;
}

function normalizePost(post) {
  const imageUrl = post.media_type === "VIDEO" ? post.thumbnail_url || post.media_url : post.media_url;

  if (!imageUrl || !post.permalink) return null;

  return {
    id: post.id,
    caption: post.caption || "",
    imageUrl,
    mediaType: post.media_type,
    permalink: post.permalink,
    timestamp: post.timestamp || ""
  };
}

router.get("/instagram", async (req, res) => {
  const limit = getLimit(req.query.limit);
  const cacheMs = Number(process.env.INSTAGRAM_CACHE_SECONDS || defaultCacheSeconds) * 1000;
  const endpoint = getInstagramEndpoint(limit);

  if (!endpoint) {
    res.json({ ok: false, configured: false, posts: [] });
    return;
  }

  if (cachedFeed && cacheExpiresAt > Date.now()) {
    res.json({ ok: true, configured: true, cached: true, posts: cachedFeed.slice(0, limit) });
    return;
  }

  try {
    const response = await fetch(endpoint);
    const payload = await response.json();

    if (!response.ok) {
      throw new Error(payload.error && payload.error.message ? payload.error.message : "Instagram request failed.");
    }

    const posts = Array.isArray(payload.data)
      ? payload.data.map(normalizePost).filter(Boolean).slice(0, limit)
      : [];

    cachedFeed = posts;
    cacheExpiresAt = Date.now() + cacheMs;

    res.set("Cache-Control", `public, max-age=${Math.max(Math.floor(cacheMs / 1000), 60)}`);
    res.json({ ok: true, configured: true, posts });
  } catch (error) {
    console.error("Instagram feed unavailable.");
    console.error(error.message);

    if (cachedFeed && cachedFeed.length) {
      res.json({ ok: true, configured: true, stale: true, posts: cachedFeed.slice(0, limit) });
      return;
    }

    res.status(502).json({ ok: false, configured: true, posts: [], error: "Instagram feed unavailable." });
  }
});

module.exports = router;
