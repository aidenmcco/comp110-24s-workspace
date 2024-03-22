"""Splitting a dictionary into two list."""

__author__ = "730522247"


def get_keys(d: dict[str, int]) -> list[str]:
    """Produces keys in a dictionary."""
    idx: list[str] = []
    for key in d:
        idx.append(key)  
    return idx     


def get_values(g: dict[str, int]) -> list[int]:
    """Produce values in a dictionary."""
    idx: list[int] = []
    for value in g:
        idx.append(g[value])
    return idx