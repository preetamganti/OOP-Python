class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def get_course_details(self):
        return f"Course Code: {self.course_code}\nCourse Name: {self.course_name}"


class INSS500(Course):
    def __init__(self):
        super().__init__("INSS 500", "Introduction to Management Information Systems")
        self.professor = None

    def set_professor(self, professor):
        self.professor = professor

    def get_course_details(self):
        return f"{super().get_course_details()}\nProfessor: {self.professor}"


class INSS573(Course):
    def __init__(self):
        super().__init__("INSS 573", "Database Management Systems")
        self.professor = None

    def set_professor(self, professor):
        self.professor = professor

    def get_course_details(self):
        return f"{super().get_course_details()}\nProfessor: {self.professor}"


class INSS615(Course):
    def __init__(self):
        super().__init__("INSS 615", "Information Systems Analysis and Design")
        self.professor = None

    def set_professor(self, professor):
        self.professor = professor

    def get_course_details(self):
        return f"{super().get_course_details()}\nProfessor: {self.professor}"


# Example usage:
course1 = INSS500()
course1.set_professor("Dr. Calloway")
print(course1.get_course_details())

course2 = INSS573()
course2.set_professor("Dr. Mangle")
print(course2.get_course_details())

course3 = INSS615()
course3.set_professor("Dr. Chike")
print(course3.get_course_details())

#This code sample defines the class Course with two attributes which are course_code and course_name. 
#Classes INSS500, INSS573, and INSS615 inherit from Course class and add another attribute which is Professor. 
#In my example, three instances of the classes are created and the set_professor() method is used to set the professor for each class. 
#Lastly, I use the get_course_details() method in order to display the course details, which include the professors for each class.
