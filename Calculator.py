import tkinter as tk

# GUI setup
root = tk.Tk()
root.title('Calculator')

# Variables
height = 400
width = 300
list = []
firstNum = ''
secondNum = ''
operator = ''
textVar = ''

# functions
def b9():
    list.append('9')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def b8():
    list.append('8')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def b7():
    list.append('7')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def b6():
    list.append('6')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def b5():
    list.append('5')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def b4():
    list.append('4')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def b3():
    list.append('3')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def b2():
    list.append('2')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def b1():
    list.append('1')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def b0():
    list.append('0')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def bc():
    list.clear()
    global firstNum
    global secondNum
    global textVar
    firstNum = ''
    secondNum = ''
    textVar = ''
    label['text'] = textVar

def bp():
    list.append('.')
    j = 0
    global textVar
    textVar = ''
    for i in list:
        textVar += list[j]
        j += 1
    label['text'] = textVar

def bplus():
    j = 0
    global firstNum
    firstNum = ''
    for i in list:
        firstNum += list[j]
        j += 1
    global operator
    operator = '+'
    label['text'] = textVar + '+'
    list.clear()

def bminus():
    j = 0
    global firstNum
    firstNum = ''
    for i in list:
        firstNum += list[j]
        j += 1
    global operator
    operator = '-'
    label['text'] = textVar + '-'
    list.clear()

def btimes():
    j = 0
    global firstNum
    firstNum = ''
    for i in list:
        firstNum += list[j]
        j += 1
    global operator
    operator = '*'
    label['text'] = textVar + '*'
    list.clear()

def bdiv():
    j = 0
    global firstNum
    firstNum = ''
    for i in list:
        firstNum += list[j]
        j += 1
    global operator
    operator = '/'
    label['text'] = textVar + '/'
    list.clear()

def bequal():
    j = 0
    global secondNum
    secondNum = ''
    for i in list:
        secondNum += list[j]
        j += 1
    if operator == '+':
        result = float(firstNum) + float(secondNum)
        label['text'] = result
    elif operator == '-':
        result = float(firstNum) - float(secondNum)
        label['text'] = result
    elif operator == '*':
        result = float(firstNum) * float(secondNum)
        label['text'] = result
    elif operator == '/':
        result = float(firstNum) / float(secondNum)
        label['text'] = result
    list.clear()
    textVar = ''

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame = tk.Frame(root, bg='#0ab1c7', bd=5)
frame.place(relx=0.1, rely=0.07, relwidth= 0.8, relheight=0.2)

buttonframe = tk.Frame(root, bg='#0ab1c7', bd=5)
buttonframe.place(relx=0.1, rely=0.37, relwidth= 0.8, relheight=0.55)

label = tk.Label(frame, font=60)
label.place(relwidth=1, relheight=1)

button = tk.Button(buttonframe, text='7', command = b7)
button.place(relx=0, rely=0, relwidth=0.2, relheight=0.2)

button2 = tk.Button(buttonframe, text='8', command = b8)
button2.place(relx=0.26, rely=0, relwidth=0.2, relheight=0.2)

button3 = tk.Button(buttonframe, text='9', command = b9)
button3.place(relx=0.52, rely=0, relwidth=0.2, relheight=0.2)

button4 = tk.Button(buttonframe, text='/', command = bdiv)
button4.place(relx=0.78, rely=0, relwidth=0.2, relheight=0.2)

button5 = tk.Button(buttonframe, text='4', command = b4)
button5.place(relx=0, rely=0.26, relwidth=0.2, relheight=0.2)

button6 = tk.Button(buttonframe, text='5', command = b5)
button6.place(relx=0.26, rely=0.26, relwidth=0.2, relheight=0.2)

button7 = tk.Button(buttonframe, text='6', command = b6)
button7.place(relx=0.52, rely=0.26, relwidth=0.2, relheight=0.2)

button8 = tk.Button(buttonframe, text='*', command = btimes)
button8.place(relx=0.78, rely=0.26, relwidth=0.2, relheight=0.2)

button9 = tk.Button(buttonframe, text='1', command = b1)
button9.place(relx=0, rely=0.52, relwidth=0.2, relheight=0.2)

button10 = tk.Button(buttonframe, text='2', command = b2)
button10.place(relx=0.26, rely=0.52, relwidth=0.2, relheight=0.2)

button11 = tk.Button(buttonframe, text='3', command = b3)
button11.place(relx=0.52, rely=0.52, relwidth=0.2, relheight=0.2)

button12 = tk.Button(buttonframe, text='-', command = bminus)
button12.place(relx=0.78, rely=0.52, relwidth=0.2, relheight=0.2)

button13 = tk.Button(buttonframe, text='.', command = bp)
button13.place(relx=0, rely=0.78, relwidth=0.1, relheight=0.2)

buttonp = tk.Button(buttonframe, text='0', command = b0)
buttonp.place(relx=0.1, rely=0.78, relwidth=0.1, relheight=0.2)

button14 = tk.Button(buttonframe, text='=', command = bequal)
button14.place(relx=0.26, rely=0.78, relwidth=0.2, relheight=0.2)

button15 = tk.Button(buttonframe, text='C', command = bc)
button15.place(relx=0.52, rely=0.78, relwidth=0.2, relheight=0.2)

button16 = tk.Button(buttonframe, text='+', command = bplus)
button16.place(relx=0.78, rely=0.78, relwidth=0.2, relheight=0.2,)

root.mainloop()
