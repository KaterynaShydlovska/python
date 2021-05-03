
length = int(input("How many students do you have?"))
listOfStudents = []

while length:
    students = {}
    name = input("Students name: ")
    if not name:
        print("Invalid name, try again..")
        name = input("Students name: ")
    students["name"] = name
    grade = input("Students garde: ")
    while not grade.isnumeric():
        print("Please enter the number")
        grade = input("Students garde: ")
    grade = int(grade)
    students["Grade"] = grade
    course = input("Select a course: 1 - Math, 2 - Science, 3 - History: ")
    while not course.isnumeric():
        print("Please enter the number")
        course = input("Students garde: ")
    course = int(course)
    if course == 1:
        students["Course"] = 'Math'
    elif course == 2:
        students["Course"] = 'Science'
    elif course == 3:
        students["Course"] = 'History'
    else:
        input("Try again")       
    listOfStudents.append(students)
    length -=1


for el in listOfStudents:
    print(el)