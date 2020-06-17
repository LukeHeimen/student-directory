import json

class StudentDirectory(object):

    def __init__(self):
        """
            key: student number
            value: [name, course and year, age, email address, contact number]
        """
        try:
            # open JSON file and get its contents
            json_file = open("student-list.json", "r")
            self.stud_dir_dict = json.load(json_file)
        except json.decoder.JSONDecodeError:
            # JSON file is empty, proceeds to making an empty dict
            self.stud_dir_dict = {}
        finally:
            json_file.close()

    def add_new_student(self, key, value):
        self.stud_dir_dict[key] = value

    def view_student_details(self, key):
        if self.check_if_student_exist(key):
            value = self.stud_dir_dict[key]
            print("    Student Number:", key)
            print("      Name:", value[0])
            print("      Course and Year:", value[1])
            print("      Age:", value[2])
            print("      Email Address:", value[3])
            print("      Contact Number:", value[4])
        else:
            print("Student number does not exist in the student directory.")

    def show_student_directory(self):
        for key, value in self.stud_dir_dict.items():
            print("    Student Number:", key)
            print("      Name:", value[0])
            print("      Course and Year:", value[1])
            print("      Age:", value[2])
            print("      Email Address:", value[3])
            print("      Contact Number:", value[4])

    def edit_student_details(self, key, value):
        # because the method is just the same as adding a new student,
        # the add_new_student method is called instead
        # method to be changed if the student number of the student
        # also needs to be edited
        self.add_new_student(key, value)

    def delete_student(self, key):
        del self.stud_dir_dict[key]

    def clear_student_directory(self):
        self.stud_dir_dict.clear()

    def save_changes(self):
        json_file = open("student-list.json", "w")
        json.dump(self.stud_dir_dict, json_file, indent = 4)
        json_file.close()

    def check_if_student_exist(self, student_number):
        return self.stud_dir_dict.get(student_number) != None