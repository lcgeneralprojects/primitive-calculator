from main import display
import vars


def read_input(char):
    print('entry - yes')        # Currently, we are unable to get here
    vars.state = vars.automaton_graph[vars.state][char]['new_state']
    vars.automaton_graph[vars.state][char]['command']()
    # TODO: I should put vars.res into vars.nums to simplify this
    if vars.state == 0:
        vars.cur_num = vars.nums[0]
    elif vars.state == 1:
        vars.cur_num = vars.nums[1]
    elif vars.state == 2:
        vars.cur_num = vars.res
    display.configure(text=vars.cur_num)


def modify_num(char):
    if vars.state == 0:
        vars.nums[0] = vars.nums[0]*10 + int(char)
    elif vars.state == 1:
        vars.nums[1] = vars.nums[1]*10 + int(char)
    else:
        vars.nums = [0, 0]
        vars.nums[0] = int(char)


def modify_operation(char):
    # TODO: consider a good way of making the input number negative. Either via pressing '-' while the current number
    #  is 0, or by introducing an additional '+/-' button
    vars.operation = char


# This one is for when we have calculated something and want to keep the result
def keep_and_modify_operation(char):
    nums = [vars.res, 0]
    vars.operation = char


def calculate():
    # TODO: check for division by zero
    if vars.operation == '+':
        vars.res = vars.nums[0] + vars.nums[1]
    elif vars.operation == '-':
        vars.res = vars.nums[0] - vars.nums[1]
    elif vars.operation == '*':
        vars.res = vars.nums[0] * vars.nums[1]
    elif vars.operation == '/':
        if vars.nums[1] == 0:
            vars.res = 'ERR: div by 0'
        else:
            vars. res = vars.nums[0] / vars.nums[1]


def clear_entry():
    if vars.state == 0:
        vars.nums[0] = vars.nums[0] // 10
    elif vars.state == 1:
        if vars.nums[1] == 0:
            vars.state = 1

    elif vars.state == 2:
        pass
    pass


for state in range(vars.num_of_states):
    vars.automaton_graph[state] = {}
    for char in vars.alphabet:
        if char.isdigit():
            if state != 2:
                vars.automaton_graph[state][char]: {'new_state': state, 'command': lambda: modify_num(char)}
            else:
                vars.automaton_graph[state][char]: {'new_state': 0, 'command': lambda: modify_num(char)}
        elif char in ['+', '-', '*', '/']:
            if state == 0:
                vars.automaton_graph[state][char]: {'new_state': 1, 'command': lambda: modify_operation(char)}
            elif state == 1:
                vars.automaton_graph[state][char]: {'new_state': 1, 'command': lambda: modify_operation(char)}
            elif state == 2:
                vars.automaton_graph[state][char]: {'new_state': 1, 'command': lambda: keep_and_modify_operation(char)}
        elif char == '=':
            if state != 1:
                vars.automaton_graph[state][char]: {'new_state': state, 'command': lambda: None}
            else:
                vars.automaton_graph[state][char]: {'new_state': 2, 'command': lambda: calculate()}
        elif char == 'CE':
            vars.automaton_graph[state][char]: {'new_state': state, 'command': lambda: clear_entry()}