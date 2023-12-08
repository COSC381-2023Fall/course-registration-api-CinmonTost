from unittest.mock import patch
import pytest
from course import Course

@pytest.fixture
def courseA():
    courseA = Course("COSC", "381", 30, "Mr Smith", 
        "Software Solutions", "PH 503", "TH 9:00")
    return courseA

def test_is_prefix(courseA):
    assert courseA.is_prefix("COSC")
    assert not courseA.is_prefix("ABC")

def test_request_for_changing_room(courseA, mocker):
    with patch.object(courseA, 'confirmation'):
        courseA.request_for_changing_room("New Place")
        assert courseA._place == "New Place"
