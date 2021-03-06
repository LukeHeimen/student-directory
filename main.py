import sys

import studentdirectory as sd
import gui

def main_for_command_line():
    stud_dir = sd.StudentDirectory()

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
            detail1 = input("    Enter new student's course and year: ")
            detail2 = input("    Enter new student's age: ")
            detail3 = input("    Enter new student's email address: ")
            detail4 = input("    Enter new student's contact number: ")

            value = [detail0, detail1, detail2, detail3, detail4]
            stud_dir.add_new_student(key, value)

            print("\nNew student added to directory successfully.\n")
        elif choice == "b":
            print("\nVIEW STUDENT DETAILS")
            key = input("    Enter student number: ")
            stud_dir.view_student_details(key)
            print(" ")
        elif choice == "c":
            print("\nSHOW STUDENT DIRECTORY")
            stud_dir.show_student_directory()
            print(" ")
        elif choice == "d":
            print("\nEDIT STUDENT DETAILS")
            key = input("    Enter student number: ")
            if stud_dir.check_if_student_exist(key):
                detail0 = input("    Enter student's new name: ")
                detail1 = input("    Enter student's new course and year: ")
                detail2 = input("    Enter student's new age: ")
                detail3 = input("    Enter student's new email address: ")
                detail4 = input("    Enter student's new contact number: ")

                value = [detail0, detail1, detail2, detail3, detail4]
                stud_dir.edit_student_details(key, value)

                print("\nStudent's details edited successfully.\n")
            else:
                print("Student number does not exist in "
                      + "the student directory.")
        elif choice == "e":
            print("\nDELETE STUDENT")
            key = input("    Enter student number: ")
            if stud_dir.check_if_student_exist(key):
                stud_dir.delete_student(key)

                print("\nStudent removed from the student "
                      + "directory successfully.\n")
            else:
                print("Student number does not exist in "
                      + "the student directory.")
        elif choice == "f":
            print("\nCLEAR STUDENT DIRECTORY")
            print("    WARNING! This will delete all entries in the "
                  +  "student directory. Do you really want to proceed?")
            decision = input("        [y]es or [n]o: ")

            if decision == "y":
                print("\nClearing student directory...")
                stud_dir.clear_student_directory()
                print("Clearing student directory successful.\n")
            elif decision == "n":
                print("\n    Good call. Going back to the menu...")
            else:
                print("\nNonexistent decision. Going back to the menu...")
        elif choice == "g":
            print("\nSaving student directory changes to JSON file.")
            stud_dir.save_changes()
            print("Done. Bye.")

            sys.exit(0)
        else:
            print("\nNonexistent choice.")

def main():
    # main_for_command_line()
    gui.GUI()

if __name__ == "__main__": main()