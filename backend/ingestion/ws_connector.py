# SPDX-License-Identifier: MIT

"""Simulated WebSocket ingestion for the FireScanner application.

In a production environment this module would open a WebSocket
connection to a data provider defined in the connector manifest and
stream incoming messages.  For demonstration purposes it returns a
synthetic data set containing random items representing a universe of
symbols for a given venue.
"""

from typing import Dict, List
import random


class WebSocketConnector:
    """A simple WebSocket connector stub.

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
        """Return a batch of synthetic items.

        The returned list contains dictionaries representing raw
        instrument data.  Each dictionary has at least a `symbol`
        field.  This stub simulates data arrival via WebSockets.
        """
        # Simulate occasional empty result to trigger REST fallback
        if random.random() < 0.2:
            return []
        # Generate a pseudo universe of symbols
        symbols = [f"SYM{index:03d}" for index in range(1, 101)]
        items = []
        for sym in symbols:
            item = {
                "symbol": sym,
                # Additional attributes could be included here
                "timestamp": self.timeframe,
                "venue": self.venue,
            }
            items.append(item)
        # Shuffle to simulate random arrival
        random.shuffle(items)
        return items