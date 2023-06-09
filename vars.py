# Automata theoretical implementation for the purpose of scalability and ease of maintenance of code

#from functions import modify_num, modify_operation, keep_and_modify_operation, calculate, clear_entry

alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=', 'CE']

# The graph of state transitions for the automaton should have
# the following format: {state: {char: {'new_state': integer, 'command': command}}}
automaton_graph = {}
num_of_states = 3


state = 0

nums = [0, 0]
cur_num = 0
operation = ''

res = 0     # TODO: put this into the nums list
