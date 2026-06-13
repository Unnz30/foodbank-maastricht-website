const path = require("node:path");
const cors = require("cors");
const dotenv = require("dotenv");
const express = require("express");
const { connectDatabase } = require("./db");
const submissionRoutes = require("./routes/submissions");

dotenv.config();

const app = express();
const port = Number(process.env.PORT || 3000);
const publicDir = path.join(__dirname, "..");
const corsOrigin = process.env.CORS_ORIGIN;

if (corsOrigin) {
  app.use(cors({ origin: corsOrigin }));
}

app.use(express.json({ limit: "1mb" }));
app.use(express.urlencoded({ extended: true }));

app.get("/api/health", (_req, res) => {
  res.json({ ok: true, service: "foodbank-maastricht-api" });
});

app.use("/api", submissionRoutes);
app.use(express.static(publicDir, { extensions: ["html"] }));

app.use((req, res) => {
  if (req.path.startsWith("/api/")) {
    res.status(404).json({ error: "API route not found." });
    return;
  }

  res.status(404).sendFile(path.join(publicDir, "index.html"));
});

app.use((error, _req, res, _next) => {
  const status = error.status || 500;
  const message = error.publicMessage || "Something went wrong. Please try again later.";

  if (status >= 500) {
    console.error(error);
  }

  res.status(status).json({ error: message });
});

connectDatabase()
  .then(() => {
    app.listen(port, () => {
      console.log(`Foodbank Maastricht site running on http://localhost:${port}`);
    });
  })
  .catch((error) => {
    console.error("Unable to start Foodbank Maastricht API.");
    console.error(error.message);
    process.exit(1);
  });
