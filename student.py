class Student:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name
        self.registered_courses = []

    def register_course(self, prefix, course_number, courses):
        registered_course = self.find_course(prefix, course_number, courses)

        if registered_course:
            return self.handle_registration(registered_course)
        else:
            return ("Course not found")

    def find_course(self, prefix, course_number, courses):
        for course in courses:
            if course._prefix == prefix and course._course_number == course_number:
                return course
        return None

    def handle_registration(self, course):
        if course in self.registered_courses:
            return ("Already registered in this course")

        self.registered_courses.append(course)
        return ("Registered in " + str(course._name))

    def get_registered_courses(self):
        registered_courses_list = []
        for course in self.registered_courses:
            course_info = course._name + " (" + course._prefix + " " + str(course._course_number) + ")"
            registered_courses_list.append(course_info)
        return registered_courses_list
    
students = []