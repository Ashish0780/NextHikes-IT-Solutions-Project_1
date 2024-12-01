
from tkinter import *

import math

import numpy as np

def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)


def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)
    
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op
def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)


def third_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)



tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("NexthikeCalculator Project")

calc_operator = ""
text_input = StringVar()


text_display = Entry(tk_calc, font=('arial', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth = 5, bg='#FFBF00', justify='right').grid(columnspan=5, padx = 10, pady = 15)

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#8B8000', 'font':('arial', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#3C3636', 'font':('arial', 20, 'bold')}

button_1 = Button(tk_calc, button_params_main, text='1',
                  command=lambda:button_click('1')).grid(row=8, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2',
                  command=lambda:button_click('2')).grid(row=8, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3',
                  command=lambda:button_click('3')).grid(row=8, column=2, sticky="nsew")
add = Button(tk_calc, button_params_main, text='+',
             command=lambda:button_click('+')).grid(row=8, column=3, sticky="nsew")
sub = Button(tk_calc, button_params_main, text='-',
             command=lambda:button_click('-')).grid(row=8, column=4, sticky="nsew")

button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda:button_click('4')).grid(row=7, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda:button_click('5')).grid(row=7, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda:button_click('6')).grid(row=7, column=2, sticky="nsew")
mul = Button(tk_calc, button_params_main, text='*',
             command=lambda:button_click('*')).grid(row=7, column=3, sticky="nsew")
div = Button(tk_calc, button_params_main, text='/',
             command=lambda:button_click('/')).grid(row=7, column=4, sticky="nsew")

button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda:button_click('7')).grid(row=6, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda:button_click('8')).grid(row=6, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda:button_click('9')).grid(row=6, column=2, sticky="nsew")
delete_one = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='DEL', command=button_delete, bg='#db701f').grid(row=6, column=3, sticky="nsew")
delete_all = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='AC', command=button_clear_all, bg='#db701f').grid(row=6, column=4, sticky="nsew")

button_0 = Button(tk_calc, button_params_main, text='0',
                  command=lambda:button_click('0')).grid(row=9, column=0, sticky="nsew")
point = Button(tk_calc, button_params_main, text='.',
               command=lambda:button_click('.')).grid(row=9, column=1, sticky="nsew")

equal = Button(tk_calc, button_params_main, text='=',
               command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")

percentage = Button(tk_calc, button_params, text='%',
               command=percent).grid(row=9, column=2, sticky="nsew")


sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin).grid(row=1, column=0, sticky="nsew")

cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos).grid(row=1, column=1, sticky="nsew")

tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan).grid(row=1, column=2, sticky="nsew")


pi_num = Button(tk_calc, button_params, text='π',
                command=lambda:button_click(str(math.pi))).grid(row=1, column=4, sticky="nsew")


factorial_button = Button(tk_calc, button_params, text='x!',
                   command=fact_func).grid(row=1, column=3, sticky="nsew")


second_power = Button(tk_calc, button_params, text='x\u00B2',
             command=lambda:button_click('**2')).grid(row=2, column=0, sticky="nsew")

third_power = Button(tk_calc, button_params, text='x\u00B3',
             command=lambda:button_click('**3')).grid(row=2, column=1, sticky="nsew")


square_root = Button(tk_calc, button_params, text='\u00B2\u221A',
                     command=square_root).grid(row=2, column=3, sticky="nsew")

third_root = Button(tk_calc, button_params, text='\u00B3\u221A',
                    command=third_root).grid(row=2, column=4, sticky="nsew")

nth_root = Button(tk_calc, button_params, text='\u221A',
                  command=lambda:button_click('**(1/')).grid(row=2, column=2, sticky="nsew")



tk_calc.mainloop()