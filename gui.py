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

old_data = [ ["    ", "", "                  ", "",
         "    ", "                         ", ""] ]
headings = ["No."] + text_names

right_column = [ [sg.Text("Student Directory", size=(100, 1),
                  justification="center")],
                 [sg.Table(values=old_data, headings=headings, num_rows=20,
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
data = []
data_index = -1

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-ADD-":
        for key in input_keys:
            window[key].update(disabled=False)
            window["-ENTER-"].update(disabled=False)

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

window.close()