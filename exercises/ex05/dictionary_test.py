"""EX05 - `dict` Unit Tests."""

__author__ = "730522247"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_use_case() -> None:
    """Test use case for invert function."""
    input_dict = {"f": "fortnite", "p": "piano", "a": "ahhhh"}
    expected_output = {"fortnite": "f", "piano": "p", "ahhhh": "a"}
    assert invert(input_dict) == expected_output


def test_invert_use_case2() -> None:
    """Test another use case for invert function."""
    input_dict = {"a": "awesome", "d": "dope", "c": "cool", "s": "sick"}
    expected_output = {"awesome": "a", "cool": "c", "dope": "d", "sick": "s"}
    assert invert(input_dict) == expected_output


def test_invert_edge_case() -> None:
    """Test edge case for invert function."""
    input_dict = {"a": "ahhhh", "f": "fortnite", "p": "piano", "c": "cool", "s": "sick", "d": "dope", "x": "fortnite"}
    with pytest.raises(KeyError):
        invert(input_dict)


def test_favorite_color_use_case() -> None:
    """Test use case for favorite_color function."""
    input_dict = {"Claudio": "orange", "John": "red", "Big Nick": "yellow", "Marky": "red"}
    expected_output = "red"
    assert favorite_color(input_dict) == expected_output


def test_favorite_color_use_case2() -> None:
    """Test another use case for favorite_color function."""
    input_dict = {"Aiden": "silver", "Claudio": "silver", "Lebron": "gold"}
    expected_output = "silver"
    assert favorite_color(input_dict) == expected_output


def test_favorite_color_edge_case() -> None:
    """Test edge case for favorite_color function."""
    input_dict = {"Claudio": "orange", "John": "red", "Big Nick": "yellow", "Marky": "purple", "Aiden": "red"}
    expected_output = "red" 
    assert favorite_color(input_dict) == expected_output


def test_count_use_case() -> None:
    """Test use case for count function."""
    input_list = ["a", "b", "a", "c", "a", "b"]
    expected_output = {"a": 3, "b": 2, "c": 1}
    assert count(input_list) == expected_output


def test_count_use_case2() -> None:
    """Test additional use case for count function."""
    input_list = ["x", "y", "z", "x", "y", "z", "x", "y", "z"]
    expected_output = {"x": 3, "y": 3, "z": 3}
    assert count(input_list) == expected_output


def test_count_edge_case() -> None:
    """Test edge case for count function."""
    input_list = []
    expected_output = {}
    assert count(input_list) == expected_output


def test_alphabetizer_use_case() -> None:
    """Test use case for alphabetizer function."""
    input_list = ["fortnite", "piano", "ahhhh"]
    expected_output = {"a": ["ahhhh"], "f": ["fortnite"], "p": ["piano"]}
    assert alphabetizer(input_list) == expected_output


def test_alphabetizer_use_case2() -> None:
    """Test another use case for alphabetizer function."""
    input_list = ["apple", "banana", "apricot"]
    expected_output = {"a": ["apple", "apricot"], "b": ["banana"]}
    assert alphabetizer(input_list) == expected_output


def test_alphabetizer_edge_case() -> None:
    """Test edge case for alphabetizer function."""
    input_list = []
    expected_output = {}
    assert alphabetizer(input_list) == expected_output


def test_update_attendance_use_case() -> None:
    """Test use case for update_attendance function."""
    attendance_dict = {"Monday": ["Aiden", "Claudio"], "Tuesday": ["Big Nick"]}
    day = "Tuesday"
    student = "Aiden"
    expected_output = {"Monday": ["Aiden", "Claudio"], "Tuesday": ["Big Nick", "Aiden"]}
    update_attendance(attendance_dict, day, student)
    assert attendance_dict == expected_output


def test_update_attendance_use_case2() -> None:
    """Test another use case for update_attendance function."""
    attendance_dict = {"Monday": ["Aiden", "Claudio"], "Tuesday": ["Big Nick"]}
    day = "Wednesday"
    student = "Lebron"
    expected_output = {"Monday": ["Aiden", "Claudio"], "Tuesday": ["Big Nick"], "Wednesday": ["Lebron"]}
    update_attendance(attendance_dict, day, student)
    assert attendance_dict == expected_output


def test_update_attendance_edge_case() -> None:
    """Test edge case for update_attendance function."""
    attendance_dict = {}
    day = "Monday"
    student = "John"
    expected_output = {"Monday": ["John"]}
    update_attendance(attendance_dict, day, student)
    assert attendance_dict == expected_output