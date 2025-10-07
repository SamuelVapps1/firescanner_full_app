# FireScanner Frontend

This directory contains the React web application for the FireScanner
full project.  The UI lets users select a venue and timeframe and
displays the top‑50 results returned by the backend API.

## Development

1. Install dependencies with `npm install`.
2. Start the development server with `npm start`.  The application
   will run at `http://localhost:3000` and automatically proxy API
   requests to `http://localhost:8000` during development.
3. Open your browser and navigate to `http://localhost:3000`.
4. Select a venue and timeframe from the dropdown lists and click
   **Scan** to fetch results from the backend.  The results will be
   displayed in a table with columns for rank, symbol, score,
   badges and freshness.

## Building for Production

To create a production build, run:

```bash
npm run build
```

The output will be saved in the `dist/` folder with `bundle.js`.  You
can then serve `public/index.html` from a static web server and
configure your reverse proxy to forward `/scan` requests to the
backend server.