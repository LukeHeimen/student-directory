import json
import sys

import studentdirectory as sd

def main():

    try:
        # open JSON file and get its contents
        jsonFile = open("student-list.json", "r")
        fileDict = json.load(jsonFile)
    except json.decoder.JSONDecodeError:
        # JSON file is empty, proceeds to making an empty dict
        fileDict = {}
    finally:
        jsonFile.close()

    studDict = sd.StudentDirectory(fileDict)

    while(1):
        print("STUDENT DIRECTORY MENU")
        print("    [a] Add New Student")
        print("    [b] View Student Details")
        print("    [c] Show Student Directory")
        print("    [d] Edit Student Details")
        print("    [e] Delete Student")
        print("    [f] Clear Student Directory")
        print("    [g] Exit")
        choice = input("Enter choice: ")

        if choice == "a":
            pass
        elif choice == "b":
            pass
        elif choice == "c":
            pass
        elif choice == "d":
            pass
        elif choice == "e":
            pass
        elif choice == "f":
            pass
        elif choice == "g":
            pass


    # json_file_w = open("student-list.json", "w")
    # json.dump(data_dict, json_file_w, indent = 4)
    # json_file_w.close()

if __name__ == "__main__": main()