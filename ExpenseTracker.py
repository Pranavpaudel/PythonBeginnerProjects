"""Build a simple expense tracker application to manage your finances. The application should allow users to add, delete,
 and view their expenses. The application should also provide a summary of the expenses."""
import csv

# A global list to store collection of expense
expense_collection = []


# Define a function to add a new expense to the collection
def add_expense(user_input):
        try:
            # Create an empty dictionary to store the expense
            expense_dict = {}

            # Split the user input into amount and description
            parts = user_input.split(',')

            # Check if the input format is correct
            if len(parts) != 2:
                print("Invalid format. Please use 'amount, description' ")
            else:
                # Extract the amount and description from the input
                expense_dict['amount'] = float(parts[0])
                expense_dict['description'] = parts[1]

                # Check if the amount is valid
                if expense_dict['amount'] <= 0:
                    print("Invalid amount. Please enter a positive number.")
                else:
                    # Add the expense to the collection
                    expense_collection.append(expense_dict)
                    print("Expense added successfully")
        except ValueError:
            # Handle invalid input format
            print("Invalid input format. Please use 'amount, description'.")
        with open("expenses.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([expense_dict['amount'], expense_dict['description']])

# Main program loop
while True:
    # Display the main menu
    print("1. Open the app")
    print("2. Exit")

    try:
        # Get the user's choice
        choice = int(input("Enter your choice: "))

        # Handle the user's choice
        if choice == 1:
            # Display the app menu
            print("Menu: ")
            print("1. Add expense")
            print("2. Update expense")
            print("3. View expenses")
            print("4. View summary")
            print("5. Delete expense")

            try:
                # Get the user's command
                command = int(input("Enter your choice: "))

                # Handle the user's command
                if command == 1:
                    # Add a new expense
                    while True:
                        # Get the user input
                        user_input = input("Enter the amount and the description (e.g. amount, description): ")

                        # Add the expense
                        add_expense(user_input)

                        # Ask the user if they want to add another expense
                        cont = input("Do you want to add another expense? (y/n): ")

                        # Break the loop if the user doesn't want to add another expense
                        if cont.lower() != 'y':
                            break

            except Exception as e:
                # Handle any exceptions
                print(str(e))
        elif choice == 2:
            print("Thank you!!")
            break
    except ValueError:
        # Handle invalid input
        print("Error!! Enter only number")