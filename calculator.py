# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:34:38 2023

@author: Dom
"""

# import the tkinter GUI module
import tkinter as tk

# import the Decimal module for precision in working with numbers
from decimal import Decimal

# initialize input variables
first_num = ''
operator_used = ''
second_num = ''

# initialize output variable
result = ''

# initialize invalid inputs boolean variable
invalid_inputs = False

# function to create and run the input window
def run_input_window():
    
    # function to extract input values
    def extract_inputs():
        global first_num, operator_used, second_num
        first_num = first_num_field.get()
        operator_used = operator.get()
        second_num = second_num_field.get()
    
    # initialize the window
    input_window = tk.Tk()
    input_window.title('Calculator')
    input_window.geometry('600x300+470+200')
    
    # create and place the instruction text
    instruction_label = tk.Label(input_window, text=
                                 'Please enter a number, choose an operator, and enter another number\nto perform a calculation. Please write out the numbers as integers or\ndecimals or use scientific notation in this format: 10E2.\nAlso, please do not use parentheses or commas.', font=('Arial', 12))
    instruction_label.place(x=55, y=50)
    
    # create the entry field for the first number
    first_num_field = tk.Entry(input_window, font=('Arial', 12), width=10)
    first_num_field.place(x=150, y=150)
    
    # set the default value for the operator
    operator = tk.StringVar(input_window)
    operator.set('+')
    
    # create the drop-down menu for the operator
    operator_menu = tk.OptionMenu(input_window, operator, '+', '-', '*', '/', '%', '**')
    operator_menu.config(font=('Arial', 10))
    operator_menu.place(x=275, y=145)
    
    # create the entry field for the second number
    second_num_field = tk.Entry(input_window, font=('Arial', 12), width=10)
    second_num_field.place(x=360, y=150)
    
    # create the button to get inputs and close the window
    ok_button = tk.Button(input_window, text='OK', font=('Arial', 10), width=10, 
                          command=lambda: [extract_inputs(), input_window.destroy()])
    ok_button.place(x=260, y=250)
    
    # run the input window
    input_window.mainloop()
    
# function to check validity of inputs
def check_input_validity():
    
    # run the input window function
    run_input_window()
    
    # these variables initialized outside this function will be modified in the function
    global invalid_inputs, result
    
    # test whether both numbers are written as integers, as decimals, or in scientific
    # notation; these can be converted to Decimal values
    #
    # also test whether division by 0 or modulo by 0 is occurring
    #
    # inputs are invalid if an exception is raised
    try:
        Decimal(first_num)
        Decimal(second_num)
        if Decimal(second_num) == 0 and operator_used in ['/', '%']:
            raise
        else:
            invalid_inputs = False
    except:
        invalid_inputs = True
    
    # once the inputs are valid, set the result variable
    #
    # this variable is the numerical Decimal result converted to a string and formatted
    # with commas as the thousands separator
    if invalid_inputs == False:
        if operator_used == '+':
            result = f'{Decimal(first_num)+Decimal(second_num):,}'
        elif operator_used == '-':
            result = f'{Decimal(first_num)-Decimal(second_num):,}'
        elif operator_used == '*':
            result = f'{Decimal(first_num)*Decimal(second_num):,}'
        elif operator_used == '/':
            result = f'{Decimal(first_num)/Decimal(second_num):,}'
        elif operator_used == '%':
            result = f'{Decimal(first_num)%Decimal(second_num):,}'
        else:
            result = f'{Decimal(first_num)**Decimal(second_num):,}'
        
# run the function to check input validity
check_input_validity()

# ask the user for different inputs whenever inputs are invalid
while invalid_inputs == True:
    error_window = tk.Tk()
    error_window.title('Please enter valid numbers')
    error_window.geometry('525x200+475+250')
    error_label = tk.Label(error_window, text='Please make sure each entry is an integer or a decimal,\neither written out or in scientific notation in this format: 10E2.\nIf doing division or modulo, please make sure the second\nnumber is not 0. Calculations using very large numbers\nmay not work.',
                           font=('Arial', 12))
    error_label.place(x=50, y=20)
    ok_button = tk.Button(error_window, text='OK', font=('Arial', 10), width=10, 
                          command=error_window.destroy)
    ok_button.place(x=215, y=150)
    error_window.mainloop()
    
    # run the input window again, then check validity of new inputs
    check_input_validity()
    
# create and run UI window to display the result
result_window = tk.Tk()
result_window.title('Result of the calculation')
result_window.geometry('450x200+525+250')
result_label = tk.Label(result_window, text='Here is the result of the calculation.', 
                        font=('Arial', 12))
result_label.place(x=100, y=40)
text_box = tk.Text(result_window, height=1, width=12)
text_box.place(x=165, y=100)
text_box.insert(tk.END, result)
text_box.config(state=tk.DISABLED, # this makes the text box displaying the result read-
                                   # only, though the user can still copy and paste the
                                   # result
                font=('Arial', 12))
ok_button = tk.Button(result_window, text='OK', font=('Arial', 10), width=10, 
                      command=result_window.destroy)
ok_button.place(x=180, y=150)
result_window.mainloop()
