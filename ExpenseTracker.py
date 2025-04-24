"""Build a simple expense tracker application to manage your finances. The application should allow users to add,
delete, and view their expenses. The application should also provide a summary of the expenses."""
#create a list to hold expenses
expenses = []

def add_expense(expenses):
    with open("Expense.txt","w") as file:
        file.write(expenses)

while True:
    print("1. Open Task Tracker \n2. Exit program")
    try:
        user_choice = int(input("Enter '1' to open task tracker or '2' to exit the program: "))
        if user_choice == 1:
            print("\nMenu: ")
            print("1. Add expense")
            print("2. Update expense")
            print("3. View All expense")
            print("4. View Summary of expense")
            print("5. Delete expense")

            try:
                menu_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Enter only numbers ")
        elif user_choice == 2:
            print("Bye, bye")
            break
        else:
            print("Enter either '1' or '2' ")
    except ValueError:
        print("Enter only numbers ")

