
length = int(input("How many students do you have?"))
students ={}

while length:
    name = input("Students name: ")
    if not name:
        print("Invalid name, try again..")
        name = input("Students name: ")
    students[name] = {"Name": name}
    grade = input("Students garde: ")
    while not grade.isnumeric():
        print("Please enter the number")
        grade = input("Students garde: ")
    grade = int(grade)
    students[name]["Grade"] = grade
    print(grade)
    course = input("Select a course: 1 - Math, 2 - Science, 3 - History: ")
    while not course.isnumeric():
        print("Please enter the number")
        course = input("Students garde: ")
    course = int(course)
    if course == 1:
        students[name]["Course"] = 'Math'
    elif course == 2:
        students[name]["Course"] = 'Science'
    elif course == 3:
        students[name]["Course"] = 'History'
    else:
        input("Try again")       
    print(course)
    length -=1
    
for val in students.values():
    print(val)