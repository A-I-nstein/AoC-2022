# imports
from ast import literal_eval

# function to find if two lists are in proper order
def order(left, right):
    # function varibles
    ind = 0
    lj = len(left)
    rj = len(right)

    while (ind < lj and ind < rj):
        if type(left[ind]) is int:
            if type(right[ind]) is int:
                if left[ind] > right[ind]:
                    #print('Right is smaller')
                    return False
                elif left[ind] < right[ind]:
                    return True
            elif  order([left[ind]], right[ind]) != None: 
                return order([left[ind]], right[ind])
        elif type(right[ind]) is int:
                if order(left[ind], [right[ind]]) != None:
                    return order(left[ind], [right[ind]])
        else:
            if order(left[ind], right[ind]) != None:
                return order(left[ind], right[ind])

        ind += 1
    
    if (lj > rj):
        #print('Right side ran out')
        return False
    elif (rj > lj):
        return True
    
    return None

# main function
def find_right_packets(input_file):

    # reading input from file
    with open(input_file, 'r') as input_buffer:
        input = input_buffer.read()

    # rephrasing inputs
    input_lines = input.split('\n\n')
    input_lines = [line.split('\n') for line in input_lines]
    input_pairs = [[literal_eval(line[0]), literal_eval(line[1])] for line in input_lines]

    # part b

    inputs = []
    [inputs.extend(i) for i in input_pairs]
    inputs.extend([[[2]], [[6]]])

    left = 0
    right = 0

    for i in inputs:
        if i != [[2]]:
            if order(i, [[2]]) == False:
                right += 1
            else:
                left +=1
    
    two = left+1

    left = 0
    right = 0

    for i in inputs:
        if i != [[6]]:
            if order(i, [[6]]) == False:
                right += 1
            else:
                left +=1
    
    six = left+1

    print(two * six)

    # part B over

    # part a
'''    
    # program varibles
    sum = 0

    # finding the packets that are in the right order
    for ind in range(len(input_pairs)):
        left = input_pairs[ind][0]
        right = input_pairs[ind][1]
        if order(left, right):
            print('Right Order')
            sum += ind+1
    
    print(sum)
'''

    # part a over

find_right_packets('input2.txt')