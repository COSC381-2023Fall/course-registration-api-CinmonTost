from fastapi.testclient import TestClient
from main import app
from test_course import courseA
from course import courses
from course import Course
from student import Student
from student import students

client = TestClient(app)

def test_get_courses(courseA):
    courses.append(courseA)             

    response = client.get("/courses/COSC")
    assert response.status_code == 200
    assert response.json() == [
        {
            "_prefix":"COSC",
            "_course_number":"381",
            "_cap":30,
            "_instructor":"Mr Smith",
            "_name":"Software Solutions",
            "_place":"PH 503",
            "_meeting_times":"TH 9:00"
        }]

    courses.pop()

def fill_student_info(courseA):
    courses.append(courseA)

    student = Student("001", "Test Student")
    student.register_course("COSC", "381", courses)
    return student

def test_get_student_courses(courseA):
    Dummy_student = fill_student_info(courseA)

    students.append(Dummy_student)

    response = client.get(f"/student_courses/{Dummy_student.eid}")
    assert response.status_code == 200
    assert response.json() == ["Software Solutions (COSC 381)"]

    students.remove(Dummy_student)