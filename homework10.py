# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject, faculty):
        super().__init__(name, age)
        self.subject = subject
        self.faculty = faculty

    def teach(self):
        print(f"{self.name} is teaching {self.subject} at the faculty of {self.faculty}.")

class Student(Person):
    def __init__(self, name, age, group, faculty):
        super().__init__(name, age)
        self.faculty = faculty
        self.group = group

    def study(self):
        print(f"{self.name} to study at the faculty of {self.faculty} in a group {self.group}")

class Subject:
    def __init__(self, name):
        self.name = name


class University:

    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []


    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def list_teachers(self):
        print("Teachers:")
        for teacher in self.teachers:
            print(f"- {teacher.name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"- {student.name}")

class Faculty(University):
    def __init__(self, name):
        super().__init__(name)

chemistry_teacher = Teacher("Vasilenko Julia", 35, "Bio-Chemistry", "Chemistry")
ornotology_teacher = Teacher("Ponomariov Alexandr", 55, "Ornitology", "Zoology")
university = University("Oles Honchar National University")
university.add_teacher(chemistry_teacher)
university.add_teacher(ornotology_teacher)
student1 = Student("Dei Diana", 20, 11, "Chemistry")
student2 = Student("Beloval Andrrii", 21, 10, "Ecology")
university.add_student(student1)
university.add_student(student2)
chemistry_teacher.teach()
student1.study()
