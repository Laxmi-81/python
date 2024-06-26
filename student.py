class Student:
    def __init__(self, name, usn, m1,m2):
        self.name = name
        self.usn = usn
        self.m1 = m1
        self.m2 = m2


    def __str__(self):
        return f"Name: {self.name}, USN: {self.usn}, Mark1: {self.m1},Mark2: {self.m2}"

st_dict = {}

num = int(input("Enter the number of student:"))

for i in range(num):
    name = input(f"Enter name for student {i+1}: ")
    age = input(f"Enter usn for student {i+1}: ")
    m1 = input(f"Enter marks of student subject 1: ")
    m2 = input(f"Enter marks of student subject 2: ")

    student = Student(name, age, m1,m2)
    st_dict[f"Student {i+1}"] = student

print("\nStudents are :")
for key, student in st_dict.items():
    print(f"{key}: {student}")
