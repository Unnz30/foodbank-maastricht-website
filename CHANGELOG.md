# Changelog

All notable changes to this project should be documented here. Update this file with every future merge.

## [1.2.3] — 2026-06-13
### Changed
- Removed the surplus food donation form from the Get Involved page and linked the CTA to the Contact page form
- Increased footer and contact page social icon sizes to 32px

## [1.2.2] — 2026-06-13
### Added
- Dynamic Instagram feed endpoint for the homepage
- Frontend rendering for latest Instagram media with fallback placeholder images
- Instagram environment variables for Render and local setup

### Changed
- Website can start even when MongoDB is not configured, while form submissions remain unavailable until the database is connected

## [1.2.1] — 2026-06-13
### Added
- Render deployment blueprint for the website and Express API
- README deployment instructions for Render and MongoDB Atlas

## [1.2.0] — 2026-06-13
### Added
- Lightweight Node.js and Express backend for website form submissions
- MongoDB storage for contact, volunteer, and food donation enquiries
- API endpoints for contact, volunteer, and food donation forms
- `.env.example` template for local environment variables
- Frontend form submissions connected to backend API endpoints
- Git workflow notes for `main`, `dev`, and `feature/` branches

## [1.1.0] — 2026-06-13
### Changed
- Redesigned homepage based on the moodboard and Figma direction
- Reduced navigation to 4 links
- Moved How It Works content into the About page
- Refined typography, spacing, footer, blog cards, social sections, and mobile layouts

### Added
- Instagram feed section
- Blog/news cards
- Volunteer and donate CTA banner
- Editable SVG design exports

## [1.0.0] — 2026-06-13
### Added
- Initial frontend build with 4 primary pages
- NL/EN language toggle
- Contact, volunteer, and food donation form areas
- Responsive navigation and footer
