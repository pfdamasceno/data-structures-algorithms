'''
P-1.32 Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
'''
def calculator():
    user_inputs = ""
    my_input = input('in each new line, enter a number or operation. Finish by a line with the equal sign (=)')
    while my_input != '=':
        user_inputs += my_input
        my_input = input()

    print(eval(user_inputs))

calculator()
