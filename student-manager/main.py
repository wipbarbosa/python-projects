
students = []

while True:

    print (

    f"===== STUDENT MANAGER =====\n"
    f"1 - Add student\n"
    f"2 - Show students\n"
    f"3 - Search student\n"
    f"4 - Remove student\n"
    f"5 - Exit"
    )

    choice = int(input("Request:"))

    if choice == 1:
        print("Adding Student")
        new_student = {
            "name": input("Student name: ").lower(),
            "age" : int(input("student age: ")),
            "course" : input("Student course: ").lower()
        
        }
        students.append(new_student)
        print(f"Student added successfully!")
       

    elif choice == 2:
        if len(students) == 0:
            print("No students registered.")
        
        else:
            for student in students:
                print("=" * 25)

                for key, value in student.items():
                    print(f"{key.capitalize():<8}: {value}")

                print("=" * 25)

             

    elif choice == 3:

        if len(students) == 0:
            print("No students registered.")
        
        else:
            print("Search Student")
            search_student = input(f"search for the student's name: ").lower()
            found = False
            for student in students:
                if search_student == student["name"]:
                    print("\nStudent found!")
                    print("=" * 25)
                    
                    for key, value in student.items():
                            print(f"{key}: {value}")
                            print("=" * 25)

                    found = True
                    break
                    
            if not found:
                print("Student not found")
    
    elif choice == 4:
        if len(students) == 0:
            print("No students registered.")

        else:
            print ("Remove Student")
            delete_student = input("search for the student's name:").lower()
            found = False
            for student in students:
                if delete_student == student["name"]:
                    print("Student found!")
                    students.remove(student)
                    print("Student removed successfully!")
                    found = True
                    break
        
            if not found:
                print("Student not found")
    
    elif choice == 5:
        print("ending program")
        break