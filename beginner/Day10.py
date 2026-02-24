#Calculator project


# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"

# print(format_name("fatima", "mEhDIZADE"))

# def is_leap_year(year):
#     # Write your code here. 
#     if year % 4 == 0:
#         if year % 100 != 0:
#             print(True)
#         elif year % 100 == 0:
#             if year % 400 == 0:
#                 print(True)
#             elif year % 400 != 0:
#                 print(False)
#     elif year % 4 != 0:
#         print(False)    
#     # Don't change the function name.
    
    
# is_leap_year(1989)

def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
desicion = "yes"
while desicion == "yes":
    number1 = int(input("Type the first number:\n"))
    operator = input("Type the operator\n")
    number2 = int(input("Type the second number:\n"))
    if operator == "+":
        print(f"{number1} plus {number2} is {operations[operator](number1, number2)}\n")
    elif operator == "-":
        print(f"{number1} minus {number2} is {operations[operator](number1, number2)}\n")
    elif operator == "/":
        print(f"{number1} divided by {number2} is {operations[operator](number1, number2)}\n")
    elif operator == "*":
        print(f"{number1} times {number2} is {operations[operator](number1, number2)}\n")
    desicion = input("want to continue? Press 'yes' to continue and 'no' to stop\n").lower()



