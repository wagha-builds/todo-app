# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
while True:
    user_action = input("Type add/new, show/display, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("display"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("display"):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}-{item}")

    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:])
            index = index - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Invalid command.")
            continue

    elif user_action.startswith("complete"):
        try:
            index = int(user_action[9:])
            index = index - 1
            todo_to_remove = todos[index].strip("\n")

            todos = functions.get_todos()

            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list.")
        except IndexError:
            print("Invalid number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid command.")

print("Bye!")