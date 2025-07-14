# Ask highest degree from the usre
highest_degree = int(input("What is the highest degree of your equation? \n"))

# Initialize an empty list
list_of_coefficients = []

# Loop over higest degree
for i in range(highest_degree + 1):
    # Ask user for the nth coefficient
    coefficient = int(input(f"Provide the value of {i}th coefficient \n"))
    # Store coefficient to the array/list
    list_of_coefficients.append(coefficient)
    print(list_of_coefficients)

print(f"Your coefficients are : \n {list_of_coefficients}")

equation= ''
for i,coefficient in enumerate(list_of_coefficients):
    print(f"Your coefficent for x^{i} is {coefficient}")
    equation = equation + str(i)

 # Print equation to the user
print(equation)
