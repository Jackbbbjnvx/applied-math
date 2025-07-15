# Ask highest degree from the usre
highest_degree = int(input("What is the highest degree of your equation? \n"))
# highest_degree = 4

def get_equation(list_of_coefficients):
    equation = ""

    for index,value in enumerate(list_of_coefficients):
        sign = "-" if value < 0 else "+"
        isPlus = sign if index else ""
        if value != 0:
            if index == 0:
                sign = "-" if value < 0 else "+"
                equation = equation + f" {sign} {value}"
            elif index == len(list_of_coefficients) - 1 and value > 0:
                equation = f"{abs(value)}*x^{index}" + equation
            else:
                equation = f" {isPlus} {abs(value)}*x^{index}" + equation


    return(equation)

def calculate_derivative(coefficients):
    derivitive_coefficients = [1,2,4]
    return derivitive_coefficients;


# Initialize an empty list
list_of_coefficients = []

# Loop over higest degree
for i in range(highest_degree + 1):
    print(i)
    # Ask user for the nth coefficient
    coefficient = int(input(f"Provide the value of {i}th coefficient \n"))
    # Store coefficient to the array/list
    list_of_coefficients.append(coefficient)
    print(list_of_coefficients)

# equation= ''
# for i,coefficient in enumerate(list_of_coefficients):
#     print(f"Your coefficent for x^{i} is {coefficient}")
#     equation = equation + str(i)
#
#  # Print equation to the user
# print(len(list_of_coefficients))
# list_in_reverse=[]
# for x in range(len(list_of_coefficients)):
#     list_in_reverse.append(list_of_coefficients[-x-1])

# Store the equation in a variable
#for v in range(highest_degree):
#    print(f'{list_in_reverse[v]}x^{highest_degree-v}+',end="")
#print(f'{list_in_reverse[-1]}')
# print(list_in_reverse)
#
# equation = ""
#
# for index,value in enumerate(list_of_coefficients):
#     isPlus = "+" if index else ""
#     equation = f"{value}*x^{index}  {isPlus} " + equation
#
# print(equation)

#print(f'your equation is {list_of_coefficients[i]}x^{i}+{list_of_coefficients[i-1]}x^{i-1}')
# derivative of equation 
# what can i do derivative of cofficient from given equation..
# there is a problem with sign in the equation...
#formula for derivative is nax^(n-1)

print(f"Your equation is : {get_equation(list_of_coefficients)}")
print(f"Your derivative equation is : {get_equation(calculate_derivative(list_of_coefficients))}")
