import PySimpleGUI as sg

sg.theme('Reds')   # Add a touch of color

window = sg.Window('Student Directory', size=(1300, 500),
                   use_default_focus=False)

button_names = ["Add New Student", "View Student Details",
                "Edit Student Details", "Delete Student",
                "Clear Student Directory"]
button_column = [[sg.Button(button_names[i])] for i in range(5)]

text_names = ["Student Number", "Name", "Course & Year", "Age",
              "Email Address", "Contact Number"]
text_column = [[sg.Text(text_names[i])] for i in range(6)]
text_column += [[sg.Button("Enter")]]

input_column = [[sg.InputText(size=(30, 1))] for i in range(6)]

search_column = [[sg.Button("Search")]]

left_column = [ [sg.Column(button_column)],
                [sg.Column(text_column), sg.Column(input_column),
                 sg.Column(search_column)] ]

# data_text = [["1", "201512658", "Luke Heimen", "BSCS 4", "21", "lukeheimen@gmail.com", "+639456160641"],
#              ["2", "201504445", "Kael Mitsuhiko", "BSCS 4", "21", "kaelmitsuhiko11@gmail.com", "+639456160641"]]
# data = [[data_text[row][col] for col in range(7)] for row in range(2)]
data = [["    ", "", "                  ", "", "    ", "                         ", ""]]
headings = ["No."] + text_names

right_column = [ [sg.Text("Student Directory", size=(100, 1),
                  justification="center")],
                 [sg.Table(values=data, headings=headings, num_rows=20,
                  justification="left", auto_size_columns=True,
                  key="-TABLE-")] ]

layout = [ [sg.Column(left_column, size=(430, 500)),
            sg.VerticalSeparator(),
            sg.Column(right_column, size=(870, 500))] ]

# Create the Window
window.layout(layout)
window.finalize()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
      break
    # if event == "Search":
    #   data_text.append(data_text[0])
    #   window["-TABLE-"].update(values=data_text)
    # if i == 0:

    # print(values[0])

window.close()