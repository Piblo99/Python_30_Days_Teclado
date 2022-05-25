from charts import create_chart

def handle_chart():
    column = int(input(charting_menu))
    create_chart(
        [1, 2, 3, 4, 5],
        [5.5, 6.4, 5.3, 4.4, 7.9]
    )

user_menu = """Please choose from the following options:

- Enter 'c' to chart a new graph.
- Enter 'q' to quit.

Your selection: """

charting_menu = "Enter the column you'd like to chart: "

def handle_chart():
    column = int(input(charting_menu))

while True:
    user_selection = input(user_menu)
    if user_selection == "q":
        break
    elif user_selection == "c":
        handle_chart()
    else:
        print(f"Sorry, '{user_selection}' is not a valid option.")