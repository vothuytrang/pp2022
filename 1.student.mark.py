StudentID = []
Marks = []

def StudentNum():
    a = int(input("Number of students "))
    return a
    
def StudentInfor(StudentNum):
    a1 = input(" ID : ")
    a2 = input(" Name : ")
    a3 = input("DOB: ")
    return a1, a2, a3
    
Students = []
student = {
    "id" : None
    "name": None
    "DOB":None
}

def CourseNum():
    b = int(input("Enter Number of Courses"))
    return b

def CourseInfor():
    b1 = ("Enter Course ID ")
    b2 = ("Enter Course Name ")
    return b1, b2

Courses = []

course = {
    "id" 
    "name"
}

def get_Marks():
    for i in range(0, len(student)):
        marks.append({course })
        mark = c
        c = float(input("Enter Mark: "))
        marks[i].update({course: mark})

def display_StudentInfor():
    print("Class's Student:\n" + student[i].get("a"))
    for i in range(0,len(marks)):
        print("Student ID: " + students[i].get("a1"), "Student name: " + student[i].get("a2"), "Student DOB: " + student[i].get("a3"))

def display_CourseInfor():
    print("Number of courses : \n" + course[i].get("b"))
    for i in range(0,len(course)):
        print("Course ID: " + course[i].get("b1"), "Course name: " + course[i].get("b2"))

def display_marks():
    for i in range(0, len(student)):
        print("Student marks: " + course[i].get("c"))
        
def add_student():
    a1, a2, a3 = StudentInfor(StudentNum)
    for i in range(0,StudentNum()):
        StudentID = input(a1)
        StudentName = input(a2)
        StudentDOB = input(a3)
    students.append(student)

def list_student():
    print ("There %s students in the class" % len(student))
    for i in student:
        print("Student infor ", i)

def add_course():
    for i in range(0,CourseNum()):
        CourseID = input(b1)
        CourseName = input (b2)
    courses.append(course)

def list_student():
    print ("There %s courses in the class" % len(course))
    for i in courses:
        print("Course infor ", i)

if __name__ == '__main__':
    add_student()
    list_student()
        
    add_course()
    list_student()
        
    display_student()
    display_course()

