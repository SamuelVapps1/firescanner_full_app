# FireScanner Backend

This directory contains the backend services for the FireScanner full
application.  It is a FastAPI server providing a `/scan` endpoint
that implements the WebSocket‑first + REST fallback intake pattern
outlined in the specifications.  The backend also includes a
black‑box scoring engine that returns only composite scores, badges
and freshness flags.

## Key Components

- **`app.py`** – Defines the FastAPI app and the `/scan` endpoint.
- **`scoring/`** – Contains the `ScoringEngine` used to produce
  composite scores and metadata.
- **`ingestion/`** – Contains WebSocket and REST connectors which
  simulate data ingestion for different venues and timeframes.
- **`manifest/`** – Holds the `connectorsmanifest.yaml` file that
  defines per‑venue intake settings, discovery universe lists and
  rate limits.
- **`scoring_rules.yaml`** – Contains placeholder tunable parameters
  for the scoring engine.  In production these should be loaded
  dynamically and not hard‑coded in code.

## Running the Server

Follow the instructions in the root `README.md` to set up a virtual
environment, install dependencies, and start the server with
Uvicorn.  Once running, access the interactive documentation at
`http://localhost:8000/docs` to explore the API.