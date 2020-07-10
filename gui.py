import PySimpleGUI as sg

import studentdirectory as sd

class GUI(object):

    def __init__(self):
        """
            window: main window of GUI
            data: array for all data in table
            input_keys: array for keys parameter of sg.InputText
            stud_dir: 
        """
        self.window = None
        # data: No. | StudNum | Name | C&Y | Age | Email | ContactNum
        self.data = [ ["    ", "", "                  ", "",
                 "    ", "                         ", ""] ]
        self.input_keys = ["-SN-", "-NAME-", "-CY-", "-AGE-",
                           "-EMAIL-", "-CN-"]
        self.stud_dir = sd.StudentDirectory()

        self.gui_init_components()
        self.gui_loop()

    def gui_init_components(self):
        sg.theme('Reds')   # Add a touch of color

        button_names = ["Add New Student", "View Student Details",
                        "Edit Student Details", "Delete Student",
                        "Clear Student Directory"]
        button_keys = ["-ADD-", "-VIEW-", "-EDIT-", "-DELETE-", "-CLEAR-"]
        button_column = [[sg.Button(button_names[i],
                          key=button_keys[i])] for i in range(5)]

        text_names = ["Student Number", "Name", "Course & Year", "Age",
                      "Email Address", "Contact Number"]
        text_column = [[sg.Text(text_names[i])] for i in range(6)]
        text_column += [[sg.Button("Enter", disabled=True, key="-ENTER-")]]

        input_column = [ [sg.InputText(size=(30, 1), disabled=True,
                          key=self.input_keys[i], enable_events=True)]
                          for i in range(6)]

        search_column = [[sg.Button("Search", disabled=True, key="-SEARCH-")]]

        left_column = [ [sg.Column(button_column)],
                        [sg.Column(text_column), sg.Column(input_column),
                         sg.Column(search_column)] ]

        headings = ["No."] + text_names
        right_column = [ [sg.Text("Student Directory", size=(100, 1),
                          justification="center")],
                         [sg.Table(values=self.data, headings=headings,
                          num_rows=20, justification="left",
                          auto_size_columns=True,
                          key="-TABLE-", vertical_scroll_only=False)] ]

        layout = [ [sg.Column(left_column, size=(430, 500)),
                    sg.VerticalSeparator(),
                    sg.Column(right_column, size=(870, 500))] ]

        # Create the Window
        self.window = sg.Window('Student Directory', layout,
                                size=(1300, 500), use_default_focus=False)
        self.window.finalize()

        # remove empty entry in table and replace it
        # with data in the student directory
        self.data.pop()
        for key, values in self.stud_dir.get_stud_dir_dict().items():
            self.data += [ [str(len(self.data) + 1)] ]
            self.data[len(self.data) - 1] += [key]
            for value in values:
                self.data[len(self.data) - 1] += [value]
        self.window["-TABLE-"].update(values=self.data)

    def gui_loop(self):
        # Event Loop to process "events" and get the "values" of the inputs
        data_index = len(self.data)
        operation = 0 # 0 = -VIEW-; 1 = -EDIT-; 2 = -DELETE-
        row_no = 0 # the location of data to be edited

        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            # primary buttons operation
            if event == "-ADD-":
                self.reset(False, False, False, True)
            if event in ("-VIEW-", "-EDIT-", "-DELETE-"):
                if self.data:
                    self.reset(False, True, True, False)
                    self.window["-SN-"].update(disabled=False)
                else:
                    sg.popup("Student directory is empty!")

                if event == "-VIEW-":
                    operation = 0
                elif event == "-EDIT-":
                    operation = 1
                elif event == "-DELETE-":
                    operation = 2
            if event in "-CLEAR-":
                self.reset(False, True, True, True)

                choice = sg.popup_yes_no("WARNING! This will"
                                + " delete all entries\n"
                                + "in the student directory. "
                                + "Do you want to proceed?")
                if choice == "Yes":
                    self.data.clear()
                    self.window["-TABLE-"].update(values=self.data)
                    self.stud_dir.clear_student_directory()
                    data_index = -1
                elif choice == "No":
                    pass

            # secondary buttons operation
            if event == "-ENTER-":
                if operation == 1: # EDIT
                    for i in range(len(self.input_keys)):
                        if values[self.input_keys[i]]:
                            self.data[row_no][i+1] = values[
                                                        self.input_keys[i] ]
                        else:
                            self.empty_form_popup(data_index, False)
                            break

                        if i == (len(self.input_keys) - 1):
                            self.window["-TABLE-"].update(values=self.data)
                            self.stud_dir.edit_student_details(
                                    self.data[row_no][1],
                                    self.data[row_no][2:7])
                            self.reset(False, True, True, True)
                else: # ADD STUDENT
                    broken = False # checker if for loop is broken
                    if data_index == -1:
                        data_index += 1
                    self.data += [ [str(data_index+1)] ]
                    for key in self.input_keys:
                        if values[key]:
                            self.data[data_index] += [values[key]]
                        else:
                            self.empty_form_popup(data_index, True)
                            broken = True
                            break

                    if not broken:
                        self.window["-TABLE-"].update(values=self.data)
                        self.reset(False, True, True, True)
                        self.stud_dir.add_new_student(
                                    self.data[data_index][1],
                                    self.data[data_index][2:7])
                        data_index += 1
            if event == "-SEARCH-":
                if operation in (0, 1):
                    value = values["-SN-"]
                    counter = 0
                    broken = False # checker if for loop is broken
                    if value:
                        for data_row in self.data:
                            if value == data_row[1]:
                                row_no = int(data_row[0]) - 1
                                for i in range(len(self.input_keys)):
                                    self.window[self.input_keys[i]].update(
                                                          value=data_row[i+1],
                                                          disabled=True)
                                self.window["-SEARCH-"].update(disabled=True)
                                counter = 0
                                broken = True
                                break
                            else:
                                counter += 1
                    else:
                        sg.popup("Student number cannot be empty!")

                    if counter > 0:
                        sg.popup("Student number does not exist!")

                    if operation == 1 and broken: # EDIT
                        self.reset(True, False, False, True)
                        self.window["-SN-"].update(disabled=True)
                elif operation == 2: # DELETE
                    value = values["-SN-"]
                    counter = 0
                    if value:
                        for data_row in self.data:
                            if value == data_row[1]:
                                row_no = int(data_row[0]) - 1
                                data_index = self.student_delete_popup(
                                                value, row_no, data_index)
                                self.stud_dir.delete_student(value)
                                counter = 0
                                break
                            else:
                                counter += 1
                    else:
                        sg.popup("Student number cannot be empty!")

                    if counter > 0:
                        sg.popup("Student number does not exist!")

        self.stud_dir.save_changes()
        self.window.close()

    def reset(self, is_edit, keys_dis, enter_dis, search_dis):
        """
            Desc: Reset buttons and inputs
            Params:
                self
                is_edit: checker if operation is edit
                keys_dis: checker if window[key] is disabled
                enter_dis: checker if enter button is disabed
                search_dis: checker if search button is disabled
        """
        for key in self.input_keys:
            if is_edit:
                self.window[key].update(disabled=keys_dis)
            else:
                self.window[key].update(value="", disabled=keys_dis)
        self.window["-ENTER-"].update(disabled=enter_dis)
        self.window["-SEARCH-"].update(disabled=search_dis)

    def empty_form_popup(self, data_index, is_add):
        """
            Desc: Error popup when an input field is empty
            Params:
                self
                data_index: index of data array
                is_add: checker if operation is add
        """
        sg.popup("Fill out all forms first!")
        if is_add:
            self.data.pop(data_index)

    def student_delete_popup(self, value, row_no, data_index):
        """
            Desc: Choice popup when deleting student
            Params:
                self
                value: table row values of student to be deleted
                row_no: row number of student to be deleted in table
                data_index: index of data array
        """
        choice = sg.popup_yes_no("Student %s will be deleted.\n" % value
                                 + "Do you want to proceed?")
        if choice == "Yes":
            self.data.pop(row_no)
            for j in range(row_no, len(self.data)):
                self.data[j][0] = str(j + 1)
            self.window["-TABLE-"].update(values=self.data)
            self.window["-SN-"].update(value="",disabled=True)
            self.window["-SEARCH-"].update(disabled=True)
            data_index -= 1
        if choice == "No":
            pass

        return data_index