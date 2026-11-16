# This is a python program

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get two numbers from the user
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

# Add the numbers
total = num1 + num2

# Display the result
print(f"The sum of {num1} and {num2} is {total}")
