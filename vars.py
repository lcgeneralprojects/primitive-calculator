# Automata theoretical implementation for the purpose of scalability and ease of maintenance of code
from functions import modify_num, modify_operation, keep_and_modify_operation, calculate, clear_entry

alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=', 'CE']

# The graph of state transitions for the automaton should have
# the following format: {state: {char: {'new_state': integer, 'command': command}}}
automaton_graph = {}
num_of_states = 3
for state in range(num_of_states):
    automaton_graph[state] = {}
    for char in alphabet:
        if char.isdigit():
            if state != 2:
                automaton_graph[state][char]: {'new_state': state, 'command': lambda: modify_num(char)}
            else:
                automaton_graph[state][char]: {'new_state': 0, 'command': lambda: modify_num(char)}
        elif char in ['+', '-', '*', '/']:
            if state == 0:
                automaton_graph[state][char]: {'new_state': 1, 'command': lambda: modify_operation(char)}
            elif state == 1:
                automaton_graph[state][char]: {'new_state': 1, 'command': lambda: modify_operation(char)}
            elif state == 2:
                automaton_graph[state][char]: {'new_state': 1, 'command': lambda: keep_and_modify_operation(char)}
        elif char == '=':
            if state != 1:
                automaton_graph[state][char]: {'new_state': state, 'command': lambda: None}
            else:
                automaton_graph[state][char]: {'new_state': 2, 'command': lambda: calculate()}
        elif char == 'CE':
            automaton_graph[state][char]: {'new_state': state, 'command': lambda: clear_entry()}

state = 0

nums = [0, 0]
cur_num = nums[0]
operation = ''

res = 0 # TODO: put this into the nums list
