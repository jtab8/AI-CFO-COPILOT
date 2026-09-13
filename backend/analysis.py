"""
Finance logic — variance, trend, and anomaly analysis.

SCAFFOLD. Replace with your hackathon implementation.
This module holds the accounting judgment; keep it separate from the model calls
so it can be tested on its own.
"""


def variance(actual: float, budget: float) -> dict:
    """Return absolute and percentage variance between an actual and a budget figure."""
    delta = actual - budget
    pct = (delta / budget) if budget else None
    return {"delta": delta, "pct": pct}


def flag_anomalies(series: list[float], threshold: float = 2.0) -> list[int]:
    """Return indices of values more than `threshold` standard deviations from the mean."""
    # TODO: replace with your implementation
    raise NotImplementedError
