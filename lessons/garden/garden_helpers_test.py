"""Test my garden functions."""

__author__ = "730522247"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date
import pytest


def test_add_by_kind_use_case() -> None:
    """Test use case for add item under its kind function."""
    by_kind: dict = {"math class": ["geometry, trigonometry"]}
    new_class_kind: str = "math class"
    new_class: str = "biology"
    new_by_kind: dict = {"math class": ["geometry, trigonometry", "biology"]}
    add_by_kind(by_kind, new_class_kind, new_class)
    assert by_kind == new_by_kind


def test_add_by_kind_edge_case() -> None:
    """Test edge case for add item under its kind function."""
    class_by_kind: dict = {"math class": ["geometry, trigonometry"]}
    new_class_kind: str = "science class"
    new_class: str = "biology"
    new_class_by_kind: dict = {"math class": ["geometry, trigonometry"], "science class": ["biology"]}
    add_by_kind(class_by_kind, new_class_kind, new_class)
    assert class_by_kind == new_class_by_kind


def test_add_by_date_use_case() -> None:
    """Test use case for add_by_date function."""
    class_by_semester: dict = {"fall 2024": ["comp 116", "psychology"]}
    new_semester: str = "fall 2024"
    new_class: str = "another comp class :)"
    new_class_by_semester: dict = {"fall 2024": ["comp 116", "psychology", "another comp class :)"]}
    add_by_date(class_by_semester, new_semester, new_class)
    assert class_by_semester == new_class_by_semester


def test_add_by_date_edge_case() -> None:
    """Test edge case for add_by_date function."""
    class_by_semester: dict = {"fall 2024": ["comp 116", "psychology"]}
    new_semester: str = "summer ii 2024"
    new_class: str = "clown class"
    new_class_by_semester: dict = {"fall 2024": ["comp 116", "psychology"], "summer ii 2024": ["clown class"]}
    add_by_date(class_by_semester, new_semester, new_class)
    assert class_by_semester == new_class_by_semester


def test_lookup_by_kind_and_date_use_case() -> None:
    """Test use case for the lookup_by_kind_and_date function."""
    class_by_kind = {"math class": ["geometry", "trigonometry"], "science class": ["biology"]}
    class_by_semester = {"summer ii 2024": ["math class", "geometry"], "fall 2024": ["science class", "biology"]}
    assert lookup_by_kind_and_date(class_by_kind, class_by_semester, "math class", "summer ii 2024") == "math classs to plant in summer ii 2024: ['geometry']"


def test_lookup_by_kind_and_date_edge_case() -> None:
    """Test basic edge case for the lookup_by_kind_and_date function."""
    class_by_kind = {"math class": ["geometry", "trigonometry"], "science class": ["biology"]}
    class_by_semester = {"summer ii 2024": ["math class", "geometry"], "fall 2024": ["science class", "biology"]}
    with pytest.raises(AssertionError):
        lookup_by_kind_and_date(class_by_kind, class_by_semester, "class kind", "summer ii 2024")