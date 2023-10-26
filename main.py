from tkinter import Tk, Frame, Button, Label
from functools import partial
from common import root, display_frame, button_frame, display, buttons, alphabet, extractor_read_input, read_input

# root = Tk()
root.title('Primitive Calculator')
root.configure(background='grey')
root.geometry('350x500')
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=4)
root.columnconfigure(0, weight=1)

# display_frame = Frame()
display_frame.grid(row=0, column=0, padx=5, ipadx=5, sticky='nsew')

# display = Label(display_frame, text=0)
display.configure(text=0)
display.grid(sticky='nsew')

# button_frame = Frame()
button_frame.grid(row=1, column=0, padx=5, ipadx=5, sticky='nsew')

# buttons = {}
# alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#             '+', '-', '*', '/', '=', 'CE', 'C', '⌫', '+/-', ',']

# button_frame.columnconfigure(tuple(range(4)), weight=1)
# button_frame.rowconfigure(tuple(range(4)), weight=1)

for i in range(5): button_frame.columnconfigure(i, weight=1)
for i in range(4): button_frame.rowconfigure(i, weight=1)

for index, char in enumerate(alphabet):
    buttons[char] = (Button(button_frame, text=char, command=lambda c=char: read_input(c)))
    if char.isdigit():
        if char != '0':
            buttons[char].grid(row=(9-int(char)) // 3, column=(int(char)-1) % 3, sticky='nsew')
        else:
            buttons[char].grid(row=3, column=1, sticky='nsew')
    else:
        if char == '+':
            buttons[char].grid(row=0, column=3, sticky='nsew')
        elif char == '-':
            buttons[char].grid(row=1, column=3, sticky='nsew')
        elif char == '*':
            buttons[char].grid(row=2, column=3, sticky='nsew')
        elif char == '/':
            buttons[char].grid(row=3, column=3, sticky='nsew')
        elif char == '=':
            buttons[char].grid(row=3, column=4, sticky='nsew')
        elif char == 'CE':
            buttons[char].grid(row=1, column=4, sticky='nsew')
        elif char == 'C':
            buttons[char].grid(row=2, column=4, sticky='nsew')
        elif char == '⌫':
            buttons[char].grid(row=0, column=4, sticky='nsew')
        elif char == '+/-':
            buttons[char].grid(row=4, column=0, sticky='nsew')
        elif char == '.':
            buttons[char].grid(row=4, column=2, sticky='nsew')

root.mainloop()
