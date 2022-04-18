class students

def get_StudentNum():
    StudentNum = int(input("Enter students number: "))
    return StudentNum

def get_StudentInfo(studentNum):
    for i in range (0, StudentNum):
        self.Student_ID = input("Student ID: ")
        self.Student_name = input("Student name: ")
        self.Student_DOB = input("Student birthday: ")
        student = {
            "id": id, 
            "name": name,
            "birthday": dob
        }
    return students
        
def get_CourseNum():
    CoursetNum = int(input("Enter courses number: "))
    return CourseNum

def get_CourseInfo(courseNum):
for i in range (0, courseNum):
        self.Course_ID = input("Course ID: ")
        self.Course_Name = input("Courses name: ")
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
    for i in range(0,len(marks)):
        print("Student ID: " + student[i].get("id"), "Student name: " + student[i].get("name"), "Student DOB: " + student[i].get("dob"))
    screen.refresh()

def courses_list(courses):
    print("Number of courses : \n" + course[i].get("courseNum"))
    for i in range(0,len(course)):
        print("Course ID: " + course[i].get("id"), "Course name: " + course[i].get("name"))
    screen.refresh()

def display_marks():
    for student in students:
        print("Student marks: " + course.get("mark"))
    screen.refresh()

class GPA
    
    def get_GPA(self, courses):
        sum_credits = 0
        for i in range(0, len(courses)):
            sum_credits = int(self.marks[i][2])
            self.gpa = int(self.marks[i][1] * self.marks[i][2])

        self.GPA = math.floor((self.GPA / sum_credits) * 20) / 20
    self_course = input("Select course: ")
    display_marks()
    screen.refresh()


        return self_GPA