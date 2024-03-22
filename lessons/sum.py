"""Summing the elements of a list using different loops."""

__author__ = "730522247"


def w_sum(vals: list[float]) -> float:
    """Summation using a while loop."""
    idx = 0 
    total = 0.0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Summation using a for loop."""
    total = 0.0
    for elem in vals:
        total += elem
    return total


def f_range_sum(vals: list[float]) -> float:
    """Summation using a for loop using range."""
    total = 0.0
    for idx in range(0, len(vals)):
        total += vals[idx]
    return total 