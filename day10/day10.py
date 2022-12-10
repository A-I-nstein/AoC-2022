# main function
def find_intersting_signal_strengths(input):
    
    # reading input lines
    with open(input, 'r') as input_buffer:
        input_lines = input_buffer.readlines()

    # function variables
    interesting_signals = [20, 60, 100, 140, 180, 220]
    current_cycle = 1
    register_x = 1
    interesting_signal_values = []

    # traversing through the signals
    for line in input_lines:
        if 'noop' in line:
            if current_cycle in interesting_signals:
                interesting_signal_values.append(register_x)
                print(interesting_signal_values, current_cycle)
            current_cycle += 1
        elif 'addx' in line:
            value = int(line.split()[1])
            if current_cycle in interesting_signals:
                interesting_signal_values.append(register_x)
                print(interesting_signal_values, current_cycle)
            current_cycle += 1
            if current_cycle in interesting_signals:
                interesting_signal_values.append(register_x)
                print(interesting_signal_values, current_cycle)
            register_x += value
            current_cycle +=1

        #print(register_x, interesting_signal_values)
    sum_of_signals = 0
    for i in range(len(interesting_signals)):
        sum_of_signals += interesting_signals[i] * interesting_signal_values[i]
    print(sum_of_signals)
# calling main function
find_intersting_signal_strengths('input1.txt')