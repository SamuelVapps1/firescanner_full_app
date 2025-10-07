# SPDX-License-Identifier: MIT

"""Simulated REST ingestion for the FireScanner application.

This module provides a fallback data source when the WebSocket
connector does not return any data.  It generates a synthetic data set
using a different mechanism to simulate a REST backfill.  In a real
implementation this would perform HTTP requests to the venue's REST
endpoint defined in the connector manifest and handle rate limits and
jittered backoff.
"""

from typing import Dict, List
import random


class RestConnector:
    """A simple REST connector stub.

    Parameters
    ----------
    venue: str
        The venue code (e.g. exchange identifier).
    timeframe: str
        The timeframe for which to fetch data (1h, 4h, or 1d).
    """

    def __init__(self, venue: str, timeframe: str) -> None:
        self.venue = venue
        self.timeframe = timeframe

    def fetch(self) -> List[Dict[str, object]]:
        """Return a batch of synthetic items for REST backfill.

        This stub constructs data similarly to the WebSocket connector
        but can be modified independently to simulate differences in
        REST intake (e.g. batch size, fields).  It always returns a
        non‑empty list to ensure the API responds if the WebSocket
        returns nothing.
        """
        symbols = [f"SYMR{index:03d}" for index in range(1, 51)]
        items: List[Dict[str, object]] = []
        for sym in symbols:
            item = {
                "symbol": sym,
                "timestamp": self.timeframe,
                "venue": self.venue,
            }
            items.append(item)
        random.shuffle(items)
        return items