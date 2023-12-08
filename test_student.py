from student import Student
from course import Course, courses
from test_course import courseA
import pytest

@pytest.fixture
def student():
    return Student("001", "Test Student")

def test_register_course(student, courseA):
    courses.append(courseA)
    assert student.register_course("COSC", "381", courses) == "Registered in Software Solutions"
    assert student.get_registered_courses() == ["Software Solutions (COSC 381)"]

def test_get_registered_courses(student, courseA):
    courses.append(courseA)
    student.register_course("COSC", "381", courses)
    registered_courses = student.get_registered_courses()
    assert registered_courses == ["Software Solutions (COSC 381)"]