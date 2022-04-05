import math
import numpy as np
import curses

Students = []
StudentID = []
Course = []
Marks = []

def get_StudentNum() 
    StudentNum = int(input("Enter students number: "))
    return StudentNum

def get_StudentInfo(studentNum)
    for i in range (0, StudentNum):
        id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Student birthday: ")
        student = {
            "id": id, 
            "name": name,
            "birthday": dob
        }
    return students
        
def get_CourseNum
    CoursetNum = int(input("Enter courses number: "))
    return CourseNum

def get_CourseInfo(courseNum):
for i in range (0, courseNum):
        id = input("Course ID: ")
        name = input("Courses name: ")
        student = {
            "id": id, 
            "name": name
        }
    return courses
    

def get_Marks(students, courseid):
    print(f"Marks of the course {courseid} ")
    for student in students:
        mark = float(input(f"Student: student.get("name")") 
 

def students_list(students):
    print("Class's Student:\n" + student[i].get("StudentNum"))
    for i in range(0,len(marks))
        print("Student ID: " + student[i].get("id"), "Student name: " + student[i].get("name"), "Student DOB: " + student[i].get("dob"))
    screen.refresh()

def courses_list(courses):
    print("Number of courses : \n" + course[i].get("courseNum"))
    for i in range(0,len(course))
        print("Course ID: " + course[i].get("id"), "Course name: " + course[i].get("name"))
    screen.refresh()

def display_marks()
    for student in students:
        print("Student marks: " + course.get("mark"))
    screen.refresh()
class GPA
    
    def get_GPA(self, courses)
        sum_credits = 0
        for i in range(0, len(courses))
            sum_credits = int(self.marks[i][2])
            self.gpa = int(self.marks[i][1] * self.marks[i][2])

        self.GPA = math.floor((self.GPA / sum_credits) * 20) / 20
    self_course = input("Select course: ")
    display_marks()
    screen.refresh()


        return self_GPA

studentNum = get_StudentNum()
students = get_StudentInfo(studentNum)
students_list(students)

courseNum = get_CourseNum()
courses = get_CourseInfo()
courses_list(courses)

def main()
    while
        screen.display("Add students & courses ?")
        screen.addoptparse(1, "Go")
        screen.addoptparse(2, "Decline")

        if option1 == 1 
            screen.clear()
            SN = int(get_StudentNum())
            screen.clear()
            for i in range(SN)
            screen.addstr("Student ID: " + get("id"), "Student name: " + get("name"), "Student DOB: " + get("dob"))
           
            screen_clear()
            screen_refresh()
    
            screen.clear()
            CN = int(get_CourseNum())
            screen.clear()
            for i in range(CN)
            screen.addstr("Course ID: " + get("id"), "Course name: " + get("name"))
            screen_clear()
            screen_refresh()
