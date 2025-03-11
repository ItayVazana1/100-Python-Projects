# Day 10 - Calculator App
from art import logo,result_box_top,result_box_bottom
import math

print("Welcome to my calculator app!")
print(logo)

def calc(a, b, op):
    def add(fn,sn):
        return fn + sn

    def sub(fn, sn):
        return fn - sn

    def mult(fn, sn):
        return fn * sn

    def div(fn, sn):
        return fn / sn

    def itp(fn, sn):
        return math.pow(fn, sn)

    def mod(fn, sn):
        return fn % sn

    dic_list = {
        '+': add(a, b),
        '-': sub(a, b),
        '*': mult(a, b),
        '/': div(a, b),
        'a^b': itp(a, b),
        '%': mod(a, b)
    }

    for key in dic_list:
        if key == op:
            return dic_list[key]


continue_flag = True

while continue_flag:
    f_number = float(input("Please insert the first number --> a = "))
    print("+ = add\n- = sub\n* = multiply\n/ = divide\na^b = a in the power of b\n% = modulo (reminder only)")
    operation = input("insert operation symbol -->  ")
    while operation not in ['+', '-', '*', '/', 'a^b', '%']:
        print("Invalid operation symbol - try again!")
        print("+ = add\n- = sub\n* = multiply\n/ = divide\na^b = a in the power of b\n% = modulo (reminder only)")
        operation = input("insert operation symbol -->  ")
    s_number = float(input("Please insert the second number --> b = "))
    result = calc(a=f_number, b=s_number, op=operation)
    print(result_box_top)
    print(f"= {float(round(result,3))}")
    print(result_box_bottom)
    user_ans = input("for more calculations type 'yes' , otherwise 'no' - ")
    while user_ans not in ['yes', 'no']:
        print("Invalid Input - try again!")
        user_ans = input("for more calculations type 'yes' , otherwise 'no' - ")

    if user_ans == 'no':
        print("Thank you , and goodbye! :)")
        continue_flag = False


