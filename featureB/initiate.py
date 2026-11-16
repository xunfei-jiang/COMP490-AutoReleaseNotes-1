# This is the initial program for the feature B

def get_valid_dimension(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Dimension must be greater than zero.")
        except ValueError:
            print("Error: Please enter a valid number.")

# Get validated dimensions from the user
length = get_valid_dimension("Enter the length of the rectangle: ")
width = get_valid_dimension("Enter the width of the rectangle: ")

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display the results
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
