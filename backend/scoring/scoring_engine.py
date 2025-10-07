# SPDX-License-Identifier: MIT

"""Black‑box scoring engine for the FireScanner application.

This engine reads tunable parameters from a YAML file and returns
composite scores, badges and freshness indicators for each item
without exposing any underlying formulas.  The implementation here
uses random scores to avoid disclosing proprietary logic.  The
engine also demonstrates how badges and freshness can be derived
based on configurable thresholds.
"""

from pathlib import Path
from typing import Any, Dict, Iterable, List
import random
import yaml


class ScoringEngine:
    """Compute composite scores and metadata for items.

    Parameters
    ----------
    rules_path: str
        Path to a YAML file containing scoring rules.  The rules file
        should define the keys `weights`, `thresholds` and `badges`.
        The actual values are not used in this demo but may be
        referenced by production implementations.
    """

    def __init__(self, rules_path: str) -> None:
        path = Path(rules_path)
        if path.exists():
            try:
                self.rules = yaml.safe_load(path.read_text())
            except Exception:
                self.rules = {}
        else:
            self.rules = {}

    def _compute_score(self) -> float:
        """Generate a pseudo‑random composite score between 0 and 100."""
        return random.uniform(0, 100)

    def _compute_badges(self, score: float) -> List[str]:
        """Determine badges based on the score.

        The logic is simplified: if the score exceeds 90 the item
        receives an `elite` badge; if the score exceeds 75 it
        receives a `high` badge.  Developers can extend this with
        more complex criteria using the `badges` section of the
        rules file.
        """
        badges: List[str] = []
        if score > 90:
            badges.append("elite")
        elif score > 75:
            badges.append("high")
        return badges

    def _compute_freshness(self) -> str:
        """Return a freshness indicator.

        Freshness is randomly chosen from a small set.  Real
        implementations should compute this based on the age of
        underlying data and configured thresholds.
        """
        return random.choice(["fresh", "moderate", "stale"])

    def score_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Score a single item and return its metadata.

        Only approved fields are returned: `symbol`, `score`, `badges`,
        `freshness` and `flags`.  No weights or factor values are
        exposed.
        """
        score = self._compute_score()
        badges = self._compute_badges(score)
        freshness = self._compute_freshness()
        return {
            "symbol": item.get("symbol"),
            "score": round(score, 2),
            "badges": badges,
            "freshness": freshness,
            "flags": {},
        }

    def score_items(self, items: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Score multiple items.

        Parameters
        ----------
        items: iterable of dict
            Raw items containing at least a `symbol` key.

        Returns
        -------
        List[Dict[str, Any]]
            A list of scored item dictionaries.
        """
        return [self.score_item(item) for item in items]