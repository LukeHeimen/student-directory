class StudentDirectory(object):

    def __init__(self, dict):
        """
            key: student number
            value: [name, course and year, age, email address, contact number]
        """
        self.studDirDict = dict

    def add_new_student(self, key, value):
        self.studDirDict[key] = value

    def view_student_details(self):
        # todo
        pass

    def show_student_directory(self):
        # todo
        pass

    def edit_student_details(self):
        # todo
        pass

    def delete_student(self):
        # todo
        pass

    def clear_student_directory(self):
        # todo
        pass