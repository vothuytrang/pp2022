class students:
    
    def get_StudentNum():
        s = int(input("How many students are there in the course ?"))
        return s

    def get_StudentInfo():
        print("Student Informations : ")
        id = input(" ID : ")
        name = input(" Name : ")
        birthday = input(" DOB : ")
        A = {"id":id,"name":name,"DOB":birthday}
        return A

    def Students_List(Students):
        for A in Students:
            print(f"id: {A['id']},name is {A['name']},birthday is {A['birthday']} ")


# main 
    Students = []
    s = get_StudentNum()
    for i in range(0,s):
        A = get_StudentInfo()
        Students += [ A ] 

class courses: 
              
    def get_CourseNum():
        c = int(input("Number of courses: "))
        return c

    def get_CourseInfo():
        print("Enter Course Infor : ")
        id = input(" ID : ")
        name = input(" Name : ")
        B = {"id":id,"name":name}
        return B
                  
    def Courses_List(Courses):
        for B in Courses:
            print(f"id {B['id']},name is {B['name']} ")



# main 
    Courses = []
    c = get_CourseNum()
    for i in range(0,c):
        B =  get_CourseInfo()
        Courses += [ B ] 
                  
class Marks:

    def get_Marks():
        for i in range(0, len(student)):
            marks.append("course: ")
            mark = m
            m = float(input("Enter Mark: "))
            marks[i].update({course: mark})

    Marks = []
    def display_marks():
        for i in range(0, len(student))
            print("Student marks: " + course[i].get("c"))
   

    Students_List(Students)
    Courses_List(Courses)