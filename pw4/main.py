class Main

def main()
    while
        screen.display("Add students & courses ?")
        screen.addoptparse(1, "Go")
        screen.addoptparse(2, "Decline")

        if option1 == 1 
            screen.clear()
            NoS = int(StudentNum())
            screen.clear()
            for i in range(NoS)
            screen.addstr("Student ID: " + get("id"), "Student name: " + get("name"), "Student DOB: " + get("dob"))
            add_student()
            screen_clear()
            screen_refresh()
    
            screen.clear()
            NoC = int(CourseNum())
            screen.clear()
            for i in range(NoC)
            screen.addstr("Course ID: " + get("id"), "Course name: " + get("name"))
            add_course()
            screen_clear()
            screen_refresh()

        break 
        else
            screen.dislay("Exit program?")
            screen.addoptparse(1, "Exit")
            screen.addoptparse(2, "Decline")
                if option2 == 1
                    exit()
                else option2 == 2
                    return main()
    screen.clear()
    screen.refresh()