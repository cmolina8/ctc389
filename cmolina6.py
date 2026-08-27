#Ceiry Molina
#Lab 6

students = ["Alma", "Gilbert", "Rafael", "Noe", "Savannah"]
print(students)

print("\nMenu")
print("1 ~ Add student to list")
print("2 ~ Modify a student name")
print("3 ~ Remove a student")

choices = int(input("\n Please a choice between 1-3:"))

if choices ==1:
    newstudent = input("Enter the student's name please:")
    students.append(newstudent)

    print(students)

elif choices ==2:
    print(0,students[0])
    print(1,students[1])
    print(2,students[2])
    print(3,students[3])
    print(4,students[4])

    x= int(input("Please enter the number before the student's name that you want to change:"))
    newname= input("Enter the new student's name please")

    students[x] = newname
    
    print(students)

elif choices ==3: 
    print(0, students[0])
    print(1, students[1])
    print(2, students[2])
    print(3, students[3])
    print(4, students[4])

    y = int(input("Please enter the number before the student's name that you want to remove:"))

    students.pop(y)

    print(students) 

