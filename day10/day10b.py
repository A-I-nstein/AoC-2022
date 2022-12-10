# main function
def render_CRT(input):
    
    # reading input lines
    with open(input, 'r') as input_buffer:
        input_lines = input_buffer.readlines()

    # function variables
    interesting_signals = [40, 80, 120, 160, 200, 240]
    current_cycle = 1
    register_x = 1
    CRT = ''
    
    # traversing through the signals
    for line in input_lines:

        if 'noop' in line:
            if (current_cycle-1)%40 in [register_x-1, register_x, register_x+1]:
                CRT += '#'
            else:
                CRT += '.'
            if current_cycle in interesting_signals:
                CRT += '\n'
            current_cycle += 1

        elif 'addx' in line:

            value = int(line.split()[1])
            if (current_cycle-1)%40 in [register_x-1, register_x, register_x+1]:
                CRT += '#'
            else:
                CRT += '.'
            if current_cycle in interesting_signals:
                CRT += '\n'
            current_cycle += 1

            if (current_cycle-1)%40 in [register_x-1, register_x, register_x+1]:
                CRT += '#'
            else:
                CRT += '.'
            if current_cycle in interesting_signals:
                CRT += '\n'
            register_x += value
            current_cycle +=1

    print(CRT)

# calling main function
render_CRT('input2.txt')