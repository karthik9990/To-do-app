import PySimpleGUI as sg
from ex7_convertors import convert

sg.theme("Black")
label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter Inches:")
input2 = sg.Input(key="inches")

button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text("", key="output", text_color="green")

window = sg.Window("Convertor", [[label1, input1],
                                 [label2, input2],
                                 [button, exit_button,  output_label]])
while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()
