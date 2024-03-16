import functions
import PySimpleGUI as sg

label = sg.Text("Type in To-Do")
input_box = sg.InputText(tooltip="Enter your Todo", key="todo")
add_button = sg.Button('Add')
complete_button = sg.Button('Complete')
edit_button = sg.Button('Edit')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box], [list_box], [add_button, edit_button, complete_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, 'todos')
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
