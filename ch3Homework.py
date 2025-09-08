# Chase Stern Chapter 3 Homework
# Title for homework
print("Chase's Calculator")
# Making inputs for numbers and operators
number_1 = int(input('Enter your first number: '))
operator = input('Enter the operator (+,-,*,/): ')
number_2 = int(input('Enter your second number: '))

# Printing the calculation formula
print(f'Calculating {number_1} {operator} {number_2}')


# Using if/elif statements for operations
if operator == '+':
    add = number_1 + number_2
    print(f'Your total is: {add}')
elif operator == '-':
    sub = number_1 - number_2
    print (f'Your total is: {sub}')
elif operator == '*':
    mult = number_1 * number_2
    print (f'Your total is: {mult}')
elif operator == '/':
    # Making sure you cannot divide by zero
    if number_2 == 0:
        print ('Cannot divide by zero. Please try again')
    else:
        div = number_1 / number_2
        print (f'Your total is: {div}')
# Making error for any other operators other than main four
else:
    print ('Invalid Operator. Please try again.')
