# Foodbank Maastricht Website

Bilingual Foodbank Maastricht website with a lightweight Node.js/Express backend for form submissions.

## Local Setup

1. Install dependencies:

   ```sh
   npm install
   ```

2. Create your local environment file:

   ```sh
   cp .env.example .env
   ```

3. Update `.env` with your MongoDB connection string. Keep `.env` local and private.

4. Start the site and backend:

   ```sh
   npm run dev
   ```

The website will run at `http://localhost:3000`.

## Backend Endpoints

- `POST /api/contact` stores general contact form submissions.
- `POST /api/volunteer` stores volunteer sign-up form submissions.
- `POST /api/food-donations` stores surplus food donation enquiries.
- `GET /api/instagram` returns the latest Instagram media for the homepage feed when Instagram credentials are configured.
- `GET /api/health` checks that the API is running.

## Deploying to Render

This repo includes `render.yaml`, which defines one Render web service for the full website and Express API.

1. Create a MongoDB Atlas database and copy its connection string.
2. In Render, create a new Blueprint from this GitHub repository.
3. Render will read `render.yaml` and create the web service from the `main` branch.
4. When prompted, add:

   ```text
   MONGODB_URI=your_mongodb_atlas_connection_string
   CORS_ORIGIN=https://your-render-site-url.onrender.com
   INSTAGRAM_ACCESS_TOKEN=your_instagram_or_meta_access_token
   INSTAGRAM_USER_ID=your_instagram_business_or_creator_user_id
   ```

5. Deploy the service.

After deployment, Render provides a public URL ending in `.onrender.com`. That URL serves the website and the form API.

## Environment Variables

Use `.env.example` as the template:

- `PORT` sets the local server port.
- `MONGODB_URI` stores the MongoDB connection string.
- `CORS_ORIGIN` allows a separate frontend origin when needed.
- `INSTAGRAM_ACCESS_TOKEN` lets the backend fetch the latest Instagram media.
- `INSTAGRAM_USER_ID` is needed for the Instagram Graph API. If it is omitted, the backend tries the Instagram `me/media` endpoint for compatible access tokens.
- `INSTAGRAM_GRAPH_VERSION` sets the Meta Graph API version. The default is `v23.0`.
- `INSTAGRAM_CACHE_SECONDS` controls how long the backend caches Instagram responses. The default is `900`.

Do not commit `.env` or real credentials.

## Git Workflow

- `main` is the production branch.
- `dev` is the active development branch.
- Use `feature/short-description` branches for individual changes.
- Merge feature branches into `dev` through pull requests.
- Merge `dev` into `main` for production releases.
- Update `CHANGELOG.md` with every future merge.
