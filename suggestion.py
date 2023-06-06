from tkinter import Tk, Frame, Button, Label

root = Tk()
root.title('Primitive Calculator')
root.geometry("+50+300")
root.configure(background='grey')
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=4)
root.columnconfigure(0, weight=1)

##display_frame = Frame(root)
##display_frame.grid(row=0, column=0, sticky="nsew")

##display = Label(display_frame)
##display.grid(row=0, column=0, sticky="nsew")

button_frame = Frame(root)
button_frame.grid(row=1, column=0, sticky="nsew")

buttons = {}
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']

# button_frame.columnconfigure(tuple(range(4)), weight=1)
# button_frame.rowconfigure(tuple(range(4)), weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)
    button_frame.rowconfigure(i, weight=1)

for index, char in enumerate(chars):
    buttons[char] = (Button(button_frame, text=char))
    buttons[char].grid(row=index // 4, column=index % 4,
                  sticky="nsew")
    print(char, divmod(index, 4))

root.mainloop()