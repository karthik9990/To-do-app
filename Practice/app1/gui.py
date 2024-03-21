import functions
import PySimpleGUI as sg
import time

sg.theme("LightGrey1")
clock = sg.Text('', key='clock')
label = sg.Text("Type in To-Do")
input_box = sg.InputText(tooltip="Enter your Todo", key="todo")
add_button = sg.Button(size=10, image_source="add.png", tooltip="Add Todo", key="Add")
edit_button = sg.Button(size=10, image_source="edit.png", tooltip="Edit", key="Edit")
complete_button = sg.Button(size=10, image_source="complete.png", tooltip="Complete or Delete", key="Complete")
exit_button = sg.Button(size=10, image_source="exit.png", tooltip="Exit", key="Exit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
layout = [[clock],
          [label],
          [input_box],
          [list_box],
          [add_button, edit_button, complete_button, exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b-%d,%Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select any Item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select any Item first", font=("Helvetica", 20))
        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
