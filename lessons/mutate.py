"""Mutating functions."""

__author__ = "730522247"


def manual_append(x: list[int], y: int) -> None:
    """Append an integer to a list"""
    x.append(y)


def double(z: list[int]) -> None:
    """Double the integers in a list"""
    idx = 0
    while idx < len(z):
        z[idx] = 2 * z[idx]
        idx += 1