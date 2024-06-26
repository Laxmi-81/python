class Student:
  students=dict()
  n=int(input("enter the number of students:"))
  for i in range(n):
      name=input("enter the name of the student:")
      reg=int(input("enter register number:"))
      marks=[]
      for j in range(n):
         mark=int(input("enter marks:"))
         marks.append(mark)
         students[name]=reg,marks
  print(students)
Student()
