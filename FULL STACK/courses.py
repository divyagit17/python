avaliable_courses= {"Math", "Physics", "Chemistry", "Biology", "Computer science", "History"}

completed_courses = set()

course1 = input("Enter completed course 1: ")
completed_courses.add(course1)

course2 = input("Enter completed course 2: ")
completed_courses.add(course2)

course3 = input("Enter completed course 3: ")
completed_courses.add(course3)

course4 = input("Enter completed course 4: ")
completed_courses.add(course4)

course5 = input("Enter completed course 5: ")
completed_courses.add(course5)

new_courses_to_enroll = avaliable_courses - completed_courses

print("courses to enroll in :")
for course in new_courses_to_enroll:
    print(course)

