import sys

import studentdirectory as sd

def main():
    studDir = sd.StudentDirectory()

    while(1):
        print("\nSTUDENT DIRECTORY MENU")
        print("    [a] Add New Student")
        print("    [b] View Student Details")
        print("    [c] Show Student Directory")
        print("    [d] Edit Student Details")
        print("    [e] Delete Student")
        print("    [f] Clear Student Directory")
        print("    [g] Exit")
        choice = input("Enter choice: ")

        if choice == "a":
            print("\nADD NEW Student")
            key = input("    Enter new student's student number: ")
            detail0 = input("    Enter new student's name: ")
            detail1 = input("    Enter new student's couse and year: ")
            detail2 = input("    Enter new student's age: ")
            detail3 = input("    Enter new student's email address: ")
            detail4 = input("    Enter new student's contact number: ")

            value = [detail0, detail1, detail2, detail3, detail4]
            studDir.add_new_student(key, value)

            print("\nNew student added to directory successfully.\n")
        elif choice == "b":
            print("\nVIEW STUDENT DETAILS")
            key = input("    Enter student number: ")
            studDir.view_student_details(key)
            print(" ")
        elif choice == "c":
            print("\nSHOW STUDENT DIRECTORY")
            studDir.show_student_directory()
            print(" ")
        elif choice == "d":
            print("\nEDIT STUDENT DETAILS")
            key = input("    Enter student number: ")
            if studDir.check_if_student_exist(key):
                detail0 = input("    Enter student's new name: ")
                detail1 = input("    Enter student's new couse and year: ")
                detail2 = input("    Enter student's new age: ")
                detail3 = input("    Enter student's new email address: ")
                detail4 = input("    Enter student's new contact number: ")

                value = [detail0, detail1, detail2, detail3, detail4]
                studDir.edit_student_details(key, value)

                print("\nStudent's details edited successfully.\n")
            else:
                print("Student number does not exist in the student directory.")
        elif choice == "e":
            pass
        elif choice == "f":
            pass
        elif choice == "g":
            print("\nSaving student directory changes to JSON file.")
            studDir.save_changes()
            print("Done. Bye.")

            sys.exit(0)

if __name__ == "__main__": main()