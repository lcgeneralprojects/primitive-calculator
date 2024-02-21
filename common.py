# Automata theoretical implementation for the purpose of scalability and ease of maintenance of code

# The graph of state transitions for the automaton should have
# the following format: {state: {char: {'new_state': integer, 'command': command}}}
from tkinter import Tk, Frame, Label, StringVar

num_of_states = 3
automaton_state = 0

# nums = [0, 0]
# cur_num = 0
# operation = ''

# res = 0

root = Tk()
display_frame = Frame()
button_frame = Frame()
nums_string_1 = StringVar(root, value='0')
nums_string_2 = StringVar(root, value='0')
operation_string = StringVar(root, value='+')

displays = []
displays.append(Label(display_frame, textvariable=nums_string_1, relief='sunken', anchor='se', justify='right'))
# TODO: add display_2 and display_operation and make them invisible in state 0
buttons = {}

ALPHABET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '+', '-', '*', '/', '=', 'CE', 'C', '⌫', '+/-', '.']
DEFAULTS = {'nums_string_1': '0', 'nums_string_2': '0', 'operation_string': '+', 'automaton_state': 0}

automaton_graph = {}

for state in range(num_of_states):
    automaton_graph[state] = {}
    for char in ALPHABET:
        if char.isdigit():
            if state != 2:
                automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: modify_num(c)}
            else:
                automaton_graph[state][char] = {'new_state': 0, 'command': lambda c=char: modify_num(c)}
        elif char in ['+', '-', '*', '/']:
            if state == 0:
                automaton_graph[state][char] = {'new_state': 1, 'command': lambda c=char: modify_operation(c)}
            elif state == 1:
                automaton_graph[state][char] = {'new_state': 1, 'command': lambda c=char: modify_operation(c)}
            elif state == 2:
                automaton_graph[state][char] = {'new_state': 1, 'command': lambda c=char: keep_and_modify_operation(c)}
        elif char == '=':
            if state != 1:
                automaton_graph[state][char] = {'new_state': state, 'command': lambda: None}
            else:
                automaton_graph[state][char] = {'new_state': 2, 'command': lambda c=char: calculate()}
        elif char == 'CE':
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: clear_entry()}
        elif char == 'C':
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: full_reset()}
        elif char == '⌫':
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: backspace()}
        elif char == '+/-':
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: additive_inverse()}
        elif char == '.':
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: modify_num(c)}


def extractor_read_input(character):
    return lambda c=char: read_input(c)


def read_input(character):
    global automaton_state
    # global cur_num
    global automaton_graph
    automaton_graph[automaton_state][character]['command']()
    automaton_state = automaton_graph[automaton_state][character]['new_state']
    # # TODO: I should put res into nums to simplify this
    # if automaton_state == 0:
    #     cur_num = nums[0]
    # elif automaton_state == 1:
    #     cur_num = nums[1]
    # elif automaton_state == 2:
    #     cur_num = res
    # display_1.configure(text=cur_num)


def modify_num(character):
    # global nums
    global nums_string_1
    global automaton_state
    # # TODO: translate the current number into a string, append the number, and then back
    # if automaton_state == 0:
    #     nums[0] = nums[0]*10 + int(character)
    # elif automaton_state == 1:
    #     nums[1] = nums[1]*10 + int(character)
    # else:
    #     nums = [0, 0]
    #     nums[0] = int(character)
    nums_value_1 = nums_string_1.get()
    if automaton_state != 2 and nums_value_1 != '0':
        nums_string_1.set(nums_value_1 + character)
    else:
        if automaton_state == 2:
            full_reset()
        nums_string_1.set(character)


def modify_operation(character):
    # # TODO: consider a good way of making the input number negative. Either via pressing '-' while the current number
    # #  is 0, or by introducing an additional '+/-' button
    # global operation
    global nums_string_1
    global nums_string_2
    global operation_string
    # operation = character
    operation_string.set(character)
    nums_string_2.set(nums_string_1.get())
    nums_string_1.set(DEFAULTS['nums_string_1'])


# This one is for when we have calculated something and want to keep the result
def keep_and_modify_operation(character):
    # global nums
    # global operation
    global automaton_state
    global nums_string_1
    global nums_string_2
    global operation_string
    # nums = [res, 0]
    # operation = character
    nums_string_2.set(nums_string_1.get())
    nums_string_1.set(DEFAULTS[nums_string_1])
    operation_string.set(character)
    automaton_state = 1


def calculate():
    # global operation
    # global res
    global operation_string
    global nums_string_1
    global nums_string_2
    # if operation == '+':
    #     res = nums[0] + nums[1]
    # elif operation == '-':
    #     res = nums[0] - nums[1]
    # elif operation == '*':
    #     res = nums[0] * nums[1]
    # elif operation == '/':
    #     if nums[1] == 0:
    #         res = 'ERR: div by 0'
    #     else:
    #         res = nums[0] / nums[1]
    operation = operation_string.get()
    res = 0
    if operation == '+':
        res = float(nums_string_2.get()) + float(nums_string_1.get())
    elif operation == '-':
        res = float(nums_string_2.get()) - float(nums_string_1.get())
    elif operation == '*':
        res = float(nums_string_2.get()) * float(nums_string_1.get())
    elif operation == '/':
        try:
            res = float(nums_string_2.get()) / float(nums_string_1.get())
        except ZeroDivisionError:
            res = 'Error: division by 0'
    nums_string_2.set(nums_string_1.get())
    nums_string_1.set(res)
    nums_value_1 = nums_string_1.get()
    # The following is done to present integers without the decimal dot and trailing zero
    if nums_value_1[-2:] == '.0':
        nums_string_1.set(nums_value_1[:-2])



# This function is meant to set nums_string_1 to 0
# If nums_string_1 == 0, then we set everything to default
def clear_entry():
    global automaton_state
    # global nums
    global nums_string_1
    global nums_string_2
    global operation_string
    # if automaton_state == 0:
    #     nums[0] = nums[0] // 10
    # elif automaton_state == 1:
    #     if nums[1] == 0:
    #         automaton_state = 1
    #
    # elif automaton_state == 2:
    #     pass
    # pass
    if nums_string_1.get() != '0':
        nums_string_1.set('0')
    elif automaton_state != 0:
        partial_reset()


# This function is meant to delete the last inputted character
def backspace():
    global automaton_state
    global nums_string_1
    global nums_string_2
    global operation_string
    nums_value_1 = nums_string_1.get()
    if nums_value_1 != '0':
        nums_value_1 = nums_value_1[:-1]
        if nums_value_1 == '':
            nums_value_1 = '0'
        nums_string_1.set(nums_value_1)
    elif automaton_state == 1:
        partial_reset()
    elif automaton_state == 2:
        # Here we simply set nums_string_2 and operation_string to their defaults
        # This is done to mirror the behaviour of the default Windows calculator
        nums_string_2.set(nums_string_1.get()) # This is done so that nums_string_1 does not change
        partial_reset()


# The following function turns nums_string_1 into its additive inverse
def additive_inverse():
    global nums_string_1
    nums_value_1 = nums_string_1.get()
    if nums_value_1[0] == '-':
        nums_value_1 = nums_value_1[1:]
    else:
        nums_value_1 = '-'+nums_value_1
    nums_string_1.set(nums_value_1)


# The following function resets the state of the calculator to automaton state 0,
# with default values for operation_string and nums_string_2,
# but leaves nums_string_1 untouched
def partial_reset():
    global automaton_state
    global nums_string_1
    global nums_string_2
    global operation_string
    nums_string_1.set(nums_string_2.get())
    nums_string_2.set(DEFAULTS['nums_string_2'])
    operation_string.set(DEFAULTS['operation_string'])
    automaton_state = DEFAULTS['automaton_state']


# The following function completely resets the state of the calculator
def full_reset():
    global nums_string_1
    partial_reset()
    nums_string_1.set(DEFAULTS['nums_string_1'])