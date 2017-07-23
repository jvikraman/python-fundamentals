students = []

class Student:

    # class attribute
    school_name = "Springfield Elementary"

    # default constructor
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    # custom override to return valid class name in english
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name