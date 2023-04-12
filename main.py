from tkinter import Tk, Frame, Button, Label

root = Tk()
root.title('Primitive Calculator')
root.configure(background='grey')

display_frame = Frame()
display_frame.grid(row=0)
display = Label(display_frame)
display.grid()
button_frame = Frame()
button_frame.grid(row=1)
buttons = []
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']
for index, char in enumerate(chars):
    buttons.append(Button(button_frame, text=char))
    buttons[index].grid(row=index // 4, column=index % 4)

root.mainloop()
