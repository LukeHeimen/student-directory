import PySimpleGUI as sg

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

input_keys = ["-SN-", "-NAME-", "-CY-", "-AGE-", "-EMAIL-", "-CN-"]
input_column = [[sg.InputText(size=(30, 1), disabled=True,
                 key=input_keys[i], enable_events=True)] for i in range(6)]

search_column = [[sg.Button("Search", disabled=True, key="-SEARCH-")]]

left_column = [ [sg.Column(button_column)],
                [sg.Column(text_column), sg.Column(input_column),
                 sg.Column(search_column)] ]

data = [ ["    ", "", "                  ", "",
         "    ", "                         ", ""] ]
headings = ["No."] + text_names

right_column = [ [sg.Text("Student Directory", size=(100, 1),
                  justification="center")],
                 [sg.Table(values=data, headings=headings, num_rows=20,
                  justification="left", auto_size_columns=True,
                  key="-TABLE-",vertical_scroll_only=False)] ]

layout = [ [sg.Column(left_column, size=(430, 500)),
            sg.VerticalSeparator(),
            sg.Column(right_column, size=(870, 500))] ]

# Create the Window
window = sg.Window('Student Directory', layout, size=(1300, 500),
                   use_default_focus=False)
window.finalize()

# Event Loop to process "events" and get the "values" of the inputs
data.pop()
data_index = -1

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-ADD-":
        for key in input_keys:
            window[key].update(value="", disabled=False)
            window["-ENTER-"].update(disabled=False)
            window["-SEARCH-"].update(disabled=True)
    if event == "-VIEW-":
        for key in input_keys:
            window[key].update(value="", disabled=True)
            window["-ENTER-"].update(disabled=True)

        if data:
            window["-SN-"].update(disabled=False)
            window["-SEARCH-"].update(disabled=False)
        else:
            sg.popup("Student directory is empty!")

    if event == "-ENTER-":
        if data_index == -1:
            data_index += 1
        data += [ [str(data_index+1)] ]
        for key in input_keys:
            if values[key]:
                data[data_index] += [values[key]]
            else:
                sg.popup("Fill out all forms first!")
                data.pop(data_index)
                data_index -= 1
                break

        if data_index > -1:
            window["-TABLE-"].update(values=data)
        for key in input_keys:
            window[key].update(value="", disabled=True)
            window["-ENTER-"].update(disabled=True)
        data_index += 1
    if event == "-SEARCH-":
        value = values["-SN-"]
        counter = 0
        if value:
            for data_row in data:
                if value == data_row[1]:
                    for i in range(len(input_keys)):
                        window[input_keys[i]].update(value=data_row[i+1],
                                                     disabled=True)
                    window["-SEARCH-"].update(disabled=True)
                    break
                else:
                    counter += 1
        else:
            sg.popup("Student number cannot be empty!")

        if counter > 0:
            sg.popup("Student number does not exist!")

window.close()