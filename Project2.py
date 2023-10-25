def convert_length():
    try:
        length = float(input("Enter a length in kilometers: "))
        miles = length * 0.621371
        print(f"{length} kilometers is equal to {miles} miles")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def convert_weight():
    try:
        weight = float(input("Enter a weight in pounds: "))
        kilograms = weight * 0.453592
        print(f"{weight} pounds is equal to {kilograms} kilograms")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Convert kilometers to miles")
        print("2. Convert pounds to kilograms")
        print("3. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            convert_length()
        elif choice == '2':
            convert_weight()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
