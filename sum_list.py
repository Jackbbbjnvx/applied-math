# Ask users to provide numbers until they enter 0 and store them in list_of_numbers variable
list_of_numbers= []

while True:
    numbers = int(input('Either provide the number for the list or enter 0 to exit: \n'))
    if numbers == 0:
        break
    list_of_numbers.append(numbers)
# Given variable "a", print out the last, first and third item if third item exists
print(f" First Number : {list_of_numbers[0]}, Last Number : {list_of_numbers[-1]}")
if len(list_of_numbers)>=4:
    print(f"Third Number : {list_of_numbers[3]}")
# How many numbers are there in the list
print(f"Number of items : {len(list_of_numbers)}")

# Given variable "a", print out the sum of the numbers in the list
sum = 0
for numbers in list_of_numbers:
    sum = sum + numbers

print(f"Sum : {sum}")

# Print the list in reversed order
list_to_reverse = []

# Algorithm 1
for i in range(len(list_of_numbers)):
    list_to_reverse.append(list_of_numbers[-i-1])
print(f"Algorithm 1 : {list_to_reverse}")

# Algorithm 2
list_to_reverse=[0 for i in range(len(list_of_numbers))]
for index,value in enumerate(list_of_numbers):
    list_to_reverse[len(list_of_numbers) - index - 1] = value

print(f"Algorithm 2 : {list_to_reverse}")

# Print pattern as bellow
 #    *
 #   * *
 #  * * *
 # * * * *

