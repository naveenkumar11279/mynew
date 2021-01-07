from tkinter import *

window = Tk()
window.geometry('450x600')
window.title("Calculator")
window.resizable(0, 0)


def btn_clicked(item):
    global expression
    expression = expression+str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ""
    input_text.set(" ")


def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression=""


expression = ""

input_text = StringVar()

# input_frame = Frame(window, bd=2, bg='#2C3E50', width=440, height=130, cursor='circle')
# input_frame.pack(side=TOP)
# input_field = Entry(input_frame, font=('Bell MT', 50), textvariable=input_text, width=440, fg='#3498DB')
# input_field.grid(column=0, row=0)
# input_field.pack()
#
# bottom_frame= Frame(window, bd=2, bg='#5D6D7E', width=450, height=500)
# bottom_frame.pack(side=BOTTOM)
top_part = Frame(window, width=440, height=100, bg='black', cursor='hand1',highlightcolor='grey')
top_part.pack(pady=5, side=TOP)
input_field = Entry(top_part, font=('Bell MT', 50), width=200, bg='black',fg='white', textvariable=input_text)
input_field.pack(pady=5, padx=5)

bottom_part = Frame(window, width=440, height=500, bg='black', cursor='hand2')
bottom_part.pack()

#first row
bt1 = Button(bottom_part, text='C', fg='black', width=13, height=6, bd=2, command=btn_clear)
bt1.grid(row=0, column=0,padx=1,pady=1)
bt2 = Button(bottom_part, text='+', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked('+'))
bt2.grid(row=0, column=1,padx=1,pady=1)
bt3 = Button(bottom_part, text='-', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked('-'))
bt3.grid(row=0, column=2,padx=1,pady=1)
bt4 = Button(bottom_part, text='=', fg='black', width=13, height=6, bd=2, command=btn_equal)
bt4.grid(row=0, column=3,padx=1,pady=1)

#second row
bt5 = Button(bottom_part, text='7', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(7))
bt5.grid(row=1, column=0,padx=1,pady=1)
bt6 = Button(bottom_part, text='8', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(8))
bt6.grid(row=1, column=1,padx=1,pady=1)
bt7 = Button(bottom_part, text='9', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(9))
bt7.grid(row=1, column=2,padx=1,pady=1)
bt8 = Button(bottom_part, text='*', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked('*'))
bt8.grid(row=1, column=3,padx=1,pady=1)
#third row
bt9 = Button(bottom_part, text='4', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(4))
bt9.grid(row=2, column=0,padx=1)
bt10 = Button(bottom_part, text='5', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(5))
bt10.grid(row=2, column=1)
bt11 = Button(bottom_part, text='6', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(6))
bt11.grid(row=2, column=2,padx=1)
bt12 = Button(bottom_part, text='/', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked('/'))
bt12.grid(row=2, column=3,pady=1)
# forth row

bt13 = Button(bottom_part, text='1', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(1))
bt13.grid(row=3, column=0,padx=1)
bt14 = Button(bottom_part, text='2', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(2))
bt14.grid(row=3, column=1)
bt15 = Button(bottom_part, text='3', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(3))
bt15.grid(row=3, column=2,padx=1)
bt16 = Button(bottom_part, text='0', fg='black', width=13, height=6, bd=2, command=lambda:btn_clicked(0))
bt16.grid(row=3, column=3,pady=1)

window.mainloop()
