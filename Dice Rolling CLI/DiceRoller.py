import random

def roll_dice():
    """Simulate rolling two dice and return the results."""
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    print(f"({x}, {y})")
    return x, y

def main():
    while True:
        choice = input("Roll the dice? (y/n) ").lower()
        if choice == 'y':
            roll_dice()
        elif choice == 'n':
            exit_choice = input("Do you want to exit? (y/n) ").lower()
            if exit_choice == 'y':
                print("Goodbye!")
                break
            elif exit_choice == 'n':
                continue
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()