# Estrutura de classes da Emap

class Student:

    #Static Atribbute
    total_students = 0

    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        Student.total_students += 1

    @staticmethod 
    def total_student_count():
        return Student.total_students

    def study(self, subject):
        return f"{self.name} is studying {subject}"

    def get_student_info(self):
        return f"{self.name}, ID: {self.student_id}, Major: {self.major}"

    def party(self):
        return f"{self.name} is partying!"
    
    def drink(self, beverage):
        return f"{self.name} is drinking {beverage}"
    
class GraduateStudent(Student):

    def __init__(self, name, student_id, major, research_topic):
        super().__init__(name, student_id, major) #puxa os atributos da classe mãe
        self.research_topic = research_topic

    def research(self):
        return f"{self.name} is conducting research on {self.research_topic}"
    
    def party(self):
        return f"{self.name} is attending a sophisticated research conference party!"
    
    def drink(self, beverage):
        return f"{self.name} is sipping {beverage} while discussing {self.research_topic}"
    
class UndergraduateStudent(Student):

    def __init__(self, name, student_id, major, year):
        super().__init__(name, student_id, major)
        self.year = year

    @staticmethod
    def is_freshman(year):
        return year == 1

    def attend_lecture(self, course):
        return f"{self.name} is attending the {course} lecture."
    
    def get_student_info(self):
        return f"{self.name}, ID: {self.student_id}, Major: {self.major}, Year: {self.year}"
    
    def procrastinate(self):
        return f"{self.name} is procrastinating. instead of studying"
    
class MathStudent(UndergraduateStudent):

    def __init__(self, name, student_id, year, specialization):
        super().__init__(name, student_id, major = "Mathematics", year=year)
        self.specialization = specialization

    def solve_math_problems(self, problem):
        return f"{self.name} is solving a {self.specialization} math problem: {problem}."
    
#Creating instances
base_student = Student("Uriel Liann", "S12345", "MAp") 
graduation_student = GraduateStudent("Jeann Rocha", "S12346", "MAp", "Topology")
undergrad_student = UndergraduateStudent("Sillas Rocha", "S12347", "CdD", 1)
math_student = MathStudent("Mariana Rocha", "M12345", 1, "Linear Algebra")

#Demonstrating functionality
print(base_student.study("Math"))
print(graduation_student.study("Math"))
print(undergrad_student.study("Math"))
print(math_student.study("Math"))

print("#"*40)

print(graduation_student.research())
print(undergrad_student.attend_lecture("Prog, Lang."))
print(undergrad_student.procrastinate())
print(math_student.solve_math_problems("Ex. 3, pg. 7"))

print("#"*40)

print(base_student.get_student_info())
print(graduation_student.get_student_info())
print(undergrad_student.get_student_info())
print(math_student.get_student_info())

print("#"*40)

print(base_student.party())
print(graduation_student.party())
print(undergrad_student.party())
print(math_student.party())

print("#"*40)

print(base_student.drink("Tequila"))
print(graduation_student.drink("51"))
print(undergrad_student.drink("..."))
print(math_student.drink("Water"))

print("#"*40)

#Acess static methods and attributes
print(f"Total Students: {Student.total_student_count()}")
print(UndergraduateStudent.is_freshman(undergrad_student.year))