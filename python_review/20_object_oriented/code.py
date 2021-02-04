class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)
        

student = Student("James", (98, 90, 95, 93, 90))

print(student.name)

print(student.grades)

print(student.average())