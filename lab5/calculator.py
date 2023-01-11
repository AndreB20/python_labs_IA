from tkinter import *
expression = ""
def press(num):
    try:
        global expression
        expression = expression + str(num)
        equation.set(expression)
    except:
        equation.set("EROARE")
        expression = ""

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("EROARE")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == '__main__':
    gui = Tk()
    gui.configure(background="black")
    gui.title("Calculator")
    gui.geometry("470x250")
    equation = StringVar()
    expression_field = Entry(gui,textvariable = equation)
    expression_field.grid(columnspan=4,ipadx=4)

    button1 = Button(gui,text = ' 1 ', fg = 'black', bg = 'red', command=lambda:press(1), height = 1, width = 7)
    button1.grid(row = 2, column = 0)
    button2 = Button(gui,text = ' 2 ', fg = 'black', bg = 'red', command=lambda:press(2), height = 1, width = 7)
    button2.grid(row = 2, column = 1)
    button3 = Button(gui,text = ' 3 ', fg = 'black', bg = 'red', command=lambda:press(3), height = 1, width = 7)
    button3.grid(row = 2, column = 2)
    button4 = Button(gui,text = ' 4 ', fg = 'black', bg = 'red', command=lambda:press(4), height = 1, width = 7)
    button4.grid(row = 3, column = 0)
    button5 = Button(gui,text = ' 5 ', fg = 'black', bg = 'red', command=lambda:press(5), height = 1, width = 7)
    button5.grid(row = 3, column = 1)
    button6 = Button(gui,text = ' 6 ', fg = 'black', bg = 'red', command=lambda:press(6), height = 1, width = 7)
    button6.grid(row = 3, column = 2)
    button7 = Button(gui,text = ' 7 ', fg = 'black', bg = 'red', command=lambda:press(6), height = 1, width = 7)
    button7.grid(row = 4, column = 0)
    button8 = Button(gui,text = ' 8 ', fg = 'black', bg = 'red', command=lambda:press(6), height = 1, width = 7)
    button8.grid(row = 4, column = 1)
    button9 = Button(gui,text = ' 9 ', fg = 'black', bg = 'red', command=lambda:press(6), height = 1, width = 7)
    button9.grid(row = 4, column = 2)
    
    plus = Button(gui,text = ' + ', fg = 'black', bg = 'red', command=lambda:press("+"), height = 1, width = 7)
    plus.grid(row = 2, column = 3)

    minus = Button(gui, text = ' - ', fg = 'black', bg = 'red', command=lambda:press("-"), height = 1, width = 7)
    minus.grid(row = 3, column = 3)

    egal = Button(gui, text = ' = ', fg = 'black', bg = 'red', command= equalpress, height = 1, width = 7)
    egal.grid(row = 3, column = 3)

    clear = Button(gui, text = ' - ', fg = 'black', bg = 'red', command=lambda:press("clear"), height = 1, width = 7)
    clear.grid(row = 6, column = 1)

    gui.mainloop()