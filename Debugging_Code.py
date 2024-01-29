# Code with error
'''num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

average = num1 + num2 + num3 / 3

print("The average of the three numbers is: ", average)'''
# Outcome = TypeError: unsupported operand type(s) for: 'str' and 'int'



# Code without error
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
print("The average of the three numbers is: ", average)
# Here we inroduced int() to convert the input to an integer
# Then we added brackets to the sum of the three numbers because maths 
# And BOOM ! It works!
# Outcome = The average of the three numbers is:  Whatevet the average is



# 2nd Code with error
'''numbers = [input("Enter a number: ") for _ in range(5)]

max_num = None
min_num = None

for num in numbers:
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

print("The maximum number is: " + max_num)
print("The minimum number is: " + min_num)'''
# Outcome = TypeError: '>' not supported between instances of 'str' and 'NoneType'



# 2nd Code without error
numbers = [int(input("\nEnter a number: "))]
for i in range(5):
    numbers.append(int(input("Enter a number: ")))

max_num = max(numbers)
min_num = min(numbers)

print("The maximum number is: " + str(max_num))
print("The minimum number is: " + str(min_num))
# Here we introduced int() to convert the input to an integer
# Then we introduced max() and min() to find the maximum and minimum numbers which is a whole lot easier
# Then we introduced str() to convert the max and min numbers to strings
# And BOOM ! It works!
# Outcome = The maximum number is: Whatevet the maximum number is
