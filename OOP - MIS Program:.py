class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def get_course_details(self):
        return f"Course Code: {self.course_code}\nCourse Name: {self.course_name}"


class INSS500(Course):
    def __init__(self):
        super().__init__("INSS 500", "Introduction to Information Systems")
        self.professor = None

    def set_professor(self, professor):
        self.professor = professor

    def get_course_details(self):
        return f"{super().get_course_details()}\nProfessor: {self.professor}"


class INSS573(Course):
    def __init__(self):
        super().__init__("INSS 573", "Digital Innovation and Entrepreneurship")
        self.professor = None

    def set_professor(self, professor):
        self.professor = professor

    def get_course_details(self):
        return f"{super().get_course_details()}\nProfessor: {self.professor}"


class INSS615(Course):
    def __init__(self):
        super().__init__("INSS 615", "Principles and Practices of IS Development")
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
#Classes INSS500, INSS573, and INSS615 are the three class names under Course class and add another attribute which is Professor. 
#In my example, three  classes are created and I used the set_professor() method to set the professor for each of the three classes. 
#Lastly, I use the get_course_details() method in order to display the course details, which include the professors for each class and it looks like this: 

#Course Code: INSS 500
#Course Name: Introduction to Information Systems
#Professor: Dr. Calloway
#Course Code: INSS 573
#Course Name: Digital Innovation and Entrepreneurship
#Professor: Dr. Mangle
#Course Code: INSS 615
#Course Name: Principles and Practices of IS Development
#Professor: Dr. Chike
