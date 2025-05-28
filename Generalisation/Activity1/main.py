from school_system import *

# Usage
teacher_dob = datetime.date(1985, 6, 15) # Assuming the format for dob is year, month, day
teacher = Teacher("John", "Doe", teacher_dob, "Male", "johndoe@example.com", "T12345", "Mathematics")

student_dob = datetime.date(2005, 8, 20)
student = Student("Alice", "Smith", student_dob, "Female", "alicesmith@example.com", "S12345", 2023, "Red House")

parent_dob = datetime.date(1984, 2, 2)
parent = Parent("Jane", "Doe", parent_dob, "Female, ", "janedoe@example.com", "Alice Smith")

teacher.display_details()
teacher.get_age()
teacher.get_faculty()
teacher.get_id()

student.display_details()
student.get_age()
student.get_id()

parent.display_details()
parent.get_age()
parent.get_child()