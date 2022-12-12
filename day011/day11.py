# imports
from re import findall

# main function
def find_level_of_monkey_business(input):

    # reading input from file
    with open(input, 'r') as input_buffer:
        input_lines = input_buffer.readlines()
    input_lines = [line for line in input_lines if line != '\n']

    # program variables
    monkeys = {}
    total_test_num = 1 # comment for part a

    # iterating through input
    monkey = 0
    for i in range(0, len(input_lines), 6):
        
        operation = []
        operation.append(findall(r'[*+]', input_lines[i+2])[0])
        operation.append([int(num) for num in findall(r'\d+', input_lines[i+2])])
        
        monkeys[str(monkey)] = {
            'items' : [int(num) for num in findall(r'\d+', input_lines[i+1])],
            'operation' : operation,
            'test' : [int(num) for num in findall(r'\d+', input_lines[i+3])],
            'true' : [num for num in findall(r'\d+', input_lines[i+4])],
            'false' : [num for num in findall(r'\d+', input_lines[i+5])],
            'inspection' : 0
        }
        total_test_num *= [int(num) for num in findall(r'\d+', input_lines[i+3])][0] # comment for part a
        monkey += 1

    # start keep away game (10000 rounds)
    for round in range(10000):
        for monkey in monkeys:
            
            items = [monkeys[monkey]['items'].pop(0) for _ in range(len(monkeys[monkey]['items']))]
            operation_num = monkeys[monkey]['operation'][1]
            operation_sym = monkeys[monkey]['operation'][0]
            test = monkeys[monkey]['test'][0]
            true = monkeys[monkey]['true'][0]
            false = monkeys[monkey]['false'][0]

            for item in items:
                worry_level = item

                # perform operation
                if len(operation_num) != 0:
                    if operation_sym == '*':
                        worry_level *= operation_num[0]
                    elif operation_sym == '+':
                        worry_level += operation_num[0]
                else:
                    if operation_sym == '*':
                        worry_level *= worry_level
                    elif operation_sym == '+':
                        worry_level += worry_level

                # decrease worry level
                # worry_level //= 3 # uncomment for part a

                # decide which monkey gets the item
                if worry_level%test == 0:
                    monkeys[true]['items'].append(worry_level%total_test_num) # remove %total_test_num for part a
                else:
                    monkeys[false]['items'].append(worry_level%total_test_num) # remove %total_test_num for part a
                
                # increasing the number of times a monkey inspected an item
                monkeys[monkey]['inspection'] += 1

    # find the no of times a monkey inspected the items
    inspection = [monkeys[monkey]['inspection'] for monkey in monkeys]
    inspection.sort(reverse=True)
    print(inspection)
    # find level of monkey business
    print(inspection[0]*inspection[1])

# calling the main function
find_level_of_monkey_business('input2.txt')