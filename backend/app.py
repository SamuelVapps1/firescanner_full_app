# SPDX-License-Identifier: MIT

"""FastAPI server for the FireScanner full application.

This module defines the main API endpoints for the FireScanner MVP.  It
implements the WebSocket‑first + REST fallback intake strategy,
interfaces with a scoring engine, and returns a top‑50 list of
composite scores, badges, freshness flags and optional risk flags.

The `/scan` endpoint accepts two query parameters:

- `venue`: identifier for the venue (e.g. exchange code) to scan.
- `timeframe`: timeframe for the scan (`1h`, `4h` or `1d`).

The endpoint first attempts to fetch items via a WebSocket connector.
If no items are returned it falls back to the REST connector.  It
then scores the items and returns the top 50 results sorted by score.
"""

from fastapi import FastAPI, HTTPException, Query
from typing import Any, Dict, List

from scoring.scoring_engine import ScoringEngine
from ingestion.ws_connector import WebSocketConnector
from ingestion.rest_connector import RestConnector


app = FastAPI(
    title="FireScanner API",
    description="FireScanner MVP API exposing a /scan endpoint with WS‑first intake.",
    version="1.0.0",
)

# Instantiate the scoring engine once with the default rules file.
engine = ScoringEngine("scoring_rules.yaml")


@app.get("/scan")
async def scan(
    venue: str = Query(..., description="Venue identifier, e.g. sample_venue"),
    timeframe: str = Query("1h", description="Time frame for the scan (1h, 4h, or 1d)"),
) -> Dict[str, List[Dict[str, Any]]]:
    """Scan a venue and return the top 50 scored items.

    Parameters
    ----------
    venue: str
        Identifier of the venue to scan.
    timeframe: str, optional
        Time frame to evaluate; defaults to `1h`.  Only the values
        `1h`, `4h` and `1d` are accepted.

    Returns
    -------
    dict
        A dictionary containing a single key `results` mapping to a
        list of scored items.
    """
    if timeframe not in {"1h", "4h", "1d"}:
        raise HTTPException(
            status_code=400,
            detail="Invalid timeframe. Use 1h, 4h or 1d.",
        )
    # Fetch items via WebSocket
    ws_connector = WebSocketConnector(venue=venue, timeframe=timeframe)
    items = ws_connector.fetch()
    # Fallback to REST if no items from WS
    if not items:
        rest_connector = RestConnector(venue=venue, timeframe=timeframe)
        items = rest_connector.fetch()
    # If still empty, return error
    if not items:
        raise HTTPException(
            status_code=404,
            detail="No data available for the given venue and timeframe",
        )
    # Score items
    scored_items = engine.score_items(items)
    # Sort by composite score descending
    top50 = sorted(scored_items, key=lambda x: x["score"], reverse=True)[:50]
    return {"results": top50}