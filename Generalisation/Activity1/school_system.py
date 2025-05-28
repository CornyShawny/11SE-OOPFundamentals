import datetime


class Person:
    def __init__(self, first_name, surname, dob, gender, email):
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.gender = gender
        self.email = email

    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.dob.year
        print(f"{self.first_name} {self.surname} is {age} years old.")

    def display_details(self):
        print(f"First Name: {self.first_name}, Surname: {self.surname}, Dob: {self.dob}, Gender: {self.gender}, Email: {self.email}")


class Teacher(Person):
    def __init__(self, first_name, surname, dob, gender, email, staff_id, faculty):
        super().__init__(first_name, surname, dob, gender, email)
        self.staff_id = staff_id
        self.faculty = faculty

    def get_faculty(self):
        print(f"{self.first_name} is part of the {self.faculty} faculty.")

    def get_id(self):
        print(f"{self.first_name} {self.surname} with ID: {self.staff_id} is a teacher at this school.")

class Student(Person):
    def __init__(self, first_name, surname, dob, gender, email, student_id, year_co, house):
        super().__init__(first_name, surname, dob, gender, email)
        self.student_id = student_id
        self.year_co = year_co
        self.house = house

    def get_id(self):
        print(f"{self.first_name} {self.surname} with ID: {self.student_id} is a student at this school.")

class Parent(Person):
    def __init__(self, first_name, surname, dob, gender, email, child):
        super().__init__(first_name, surname, dob, gender, email)
        self.child = child
    
    def get_child(self):
        print(f"{self.first_name} {self.surname} is the parent of {self.child}, who is a student at this school.")