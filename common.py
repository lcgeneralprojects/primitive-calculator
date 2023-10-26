# Automata theoretical implementation for the purpose of scalability and ease of maintenance of code

# The graph of state transitions for the automaton should have
# the following format: {state: {char: {'new_state': integer, 'command': command}}}
from tkinter import Tk, Frame, Label

num_of_states = 3
automaton_state = 0

nums = [0, 0]
cur_num = 0
operation = ''

res = 0     # TODO: put this into the nums list

root = Tk()
display_frame = Frame()
button_frame = Frame()
display = Label(display_frame)
buttons = {}

alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '+', '-', '*', '/', '=', 'CE', 'C', '⌫', '+/-', '.']

automaton_graph = {}

for state in range(num_of_states):
    automaton_graph[state] = {}
    for char in alphabet:
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
            # TODO: make a case for state == 2
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: clear_entry()}
        elif char == 'C':
            # TODO: make a complete reset of the state
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: clear_entry()}
        elif char == '⌫':
            # TODO: implement the backspace function
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: clear_entry()}
        elif char == '+/-':
            # TODO: implement the inversion with regards to addition
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: clear_entry()}
        elif char == '.':
            # TODO: implement fractional inputs
            automaton_graph[state][char] = {'new_state': state, 'command': lambda c=char: clear_entry()}


def extractor_read_input(character):
    return lambda c=char: read_input(c)


def read_input(character):
    global automaton_state
    global cur_num
    global automaton_graph
    global display
    automaton_graph[automaton_state][character]['command']()       # TODO: the commands don't seem to be run properly
    automaton_state = automaton_graph[automaton_state][character]['new_state']
    # TODO: I should put res into nums to simplify this
    if automaton_state == 0:
        cur_num = nums[0]
    elif automaton_state == 1:
        cur_num = nums[1]
    elif automaton_state == 2:
        cur_num = res
    display.configure(text=cur_num)


def modify_num(character):
    global nums
    global automaton_state
    # TODO: translate the current number into a string, append the number, and then back
    if automaton_state == 0:
        nums[0] = nums[0]*10 + int(character)
    elif automaton_state == 1:
        nums[1] = nums[1]*10 + int(character)
    else:
        nums = [0, 0]
        nums[0] = int(character)


def modify_operation(character):
    # TODO: consider a good way of making the input number negative. Either via pressing '-' while the current number
    #  is 0, or by introducing an additional '+/-' button
    global operation
    operation = character


# This one is for when we have calculated something and want to keep the result
def keep_and_modify_operation(character):
    global nums
    global operation
    nums = [res, 0]
    operation = character


def calculate():
    global operation
    global res
    if operation == '+':
        res = nums[0] + nums[1]
    elif operation == '-':
        res = nums[0] - nums[1]
    elif operation == '*':
        res = nums[0] * nums[1]
    elif operation == '/':
        if nums[1] == 0:
            res = 'ERR: div by 0'
        else:
            res = nums[0] / nums[1]


def clear_entry():
    global automaton_state
    global nums
    if automaton_state == 0:
        nums[0] = nums[0] // 10
    elif automaton_state == 1:
        if nums[1] == 0:
            automaton_state = 1

    elif automaton_state == 2:
        pass
    pass
