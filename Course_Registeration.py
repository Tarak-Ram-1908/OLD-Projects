import sys


class Course:
    def __init__(self, cid, name, credits, max_students):
        self.course_id = cid
        self.name = name
        self.credits = credits
        self.max_students = max_students
        self.enrolled_students = []

    def details(self):
        print("Course ID\t-\t", str(self.course_id))
        print("Course Name\t-\t", str(self.name))
        print("Credits\t\t-\t", str(self.credits))
        print("Max Students\t-\t", str(self.max_students))
        print("Enrolled\t-\t", str(len(self.enrolled_students)))
        print("\n")



class OnlineCourse(Course):
    def __init__(self, cid, name, credits, max_students, platform):
        super().__init__(cid, name, credits, max_students)
        self.platform = platform



class OfflineCourse(Course):
    def __init__(self, cid, name, credits, max_students, room):
        super().__init__(cid, name, credits, max_students)
        self.room = room



class Student:
    def __init__(self, sid, name):
        self.student_id = sid
        self.name = name
        self.enrolled_courses = []

    def total_credits(self):
        total = 0
        for c in self.enrolled_courses:
            total += c.credits
        return total



class University:
    def __init__(self): 
        self.courses = []
        self.students = []

    def add_course(self):
        cid = input("Enter Course ID\t-\t")
        if cid.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        name = input("Enter Course Name\t-\t")
        if name.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        credits = int(input("Enter Credits\t-\t"))
        if credits.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        max_students = int(input("Enter Max Students\t-\t"))
        if max_students.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        print("1 - Online Course")
        print("2 - Offline Course")
        t = input("Enter Type\t-\t")
        if t.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        if(t == '1'):
            platform = input("Enter Platform\t-\t")
            if platform.strip().lower() == 'exit':
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            c = OnlineCourse(cid, name, credits, max_students, platform)
        elif(t == '2'):
            room = input("Enter Room No\t-\t")
            if room.strip().lower() == 'exit':
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
                c = OfflineCourse(cid, name, credits, max_students, room)
        elif(t.strip().lower() == 'exit'):
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        else:
            print("\tInvalid Choice\n\n")
            self.add_course()
        self.courses.append(c)
        print("\tCourse Added Successfully\n\n")

    def add_student(self):
        sid = input("Enter Student ID\t-\t")
        if sid.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        name = input("Enter Student Name\t-\t")
        if name.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        s = Student(sid, name)
        self.students.append(s)
        print("\tStudent Registered Successfully\n\n")

    def choose_student(self):
        if len(self.students) == 0:
            print("\tNo Students Available\n\n")
            return -1
        i = 1
        for s in self.students:
            print(i, "\t-\t", s.name)
            i += 1
        c = int(input("Enter Choice\t-\t"))
        if c.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        if((c <= 0)or(c > len(self.students))):
            return -1
        return c-1

    def choose_course(self):
        if(len(self.courses) == 0):
            print("\tNo Courses Available\n")
            return -1
        i = 1
        for c in self.courses:
            print(i, "\t-\t", c.name)
            i += 1
        c = int(input("Enter Choice\t-\t"))
        if(len(self.courses) == 0):
            print("\tNo Courses Available\n")
            return -1
        if((c<=0)or(c>len(self.courses))):
            return -1
        return c-1

    def enroll(self):
        s = self.choose_student()
        if(s==-1):
            print("\tNot Found\n\n")
            return
        c = self.choose_course()
        if(c==-1):
            print("\tNot Found\n\n")
            return
        student = self.students[s]
        course = self.courses[c]
        if(len(course.enrolled_students) >= course.max_students):
            print("\tCourse is Full\n")
            return
        if(student.total_credits()+course.credits > 30):
            print("\tCredit Limit Exceeded (30 Max)\n")
            return
        course.enrolled_students.append(student)
        student.enrolled_courses.append(course)
        print("\tStudent Enrolled Successfully\n\n")

    def drop(self):
        s = self.choose_student()
        if s==-1:            
            print("\tNot Found\n\n")
            return
        student = self.students[s]
        if(len(student.enrolled_courses) == 0):
            print("\tStudent Not Enrolled in Any Course\n")
            return
        i = 1
        for c in student.enrolled_courses:
            print(i, "\t-\t", c.name)
            i += 1
        ch = int(input("Enter Choice\t-\t"))
        if(ch.strip().lower() == 'exit'):
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        if((ch <= 0)or(ch > len(student.enrolled_courses))):
            print("\tInvalid Choice\n\n")
            return
        course = student.enrolled_courses[ch - 1]
        student.enrolled_courses.remove(course)
        course.enrolled_students.remove(student)
        print("\tCourse Dropped Successfully\n\n")

    def student_details(self):
        s = self.choose_student()
        if s == -1:
            print("\tNot Found\n\n")
            return

        student = self.students[s]
        print("\nStudent Name\t-\t", student.name)
        print("Total Credits\t-\t", student.total_credits())
        print("Courses\t-\n")
        a = 1
        for c in student.enrolled_courses:
            print(str(a) + "\t-\t", c.name)
            a += 1
        print()

    def course_details(self):
        c = self.choose_course()
        if c == -1:
            print("\tNot Found\n\n")
            return
        course = self.courses[c]
        course.details()
        print("Students:\t-\n")
        a = 1
        for s in course.enrolled_students:
            print(str(a) + "\t-\t", s.name)
            a += 1
        print()





U = University()
while True:
    print("1 - Add Course")
    print("2 - Add Student")
    print("3 - Enroll Student")
    print("4 - Drop Course")
    print("5 - Student Details")
    print("6 - Course Details")
    print("exit - Exit Program")

    ch = input("Enter Choice\t-\t")

    if ch == '1':
        U.add_course()
    elif ch == '2':
        U.add_student()
    elif ch == '3':
        U.enroll()
    elif ch == '4':
        U.drop()
    elif ch == '5':
        U.student_details()
    elif ch == '6':
        U.course_details()
    elif ch.lower() == 'exit':
        print("\n\t***Exiting Program***\n")
        break
    else:
        print("\tInvalid Choice\n")