'''
code not working properly
'''

# imports
from copy import deepcopy

# function to find all possible next steps
def find_next_steps(i, j, matrix):
    all_steps = []
    if i == 0:
        if j == 0:
            all_steps.extend([[i, j+1], [i+1, j]])
        elif (j < len(matrix[0])-1):
            all_steps.extend([[i, j-1], [i, j+1], [i+1, j]])
        else:
            all_steps.extend([[i, j-1], [i+1, j]])
    elif (i < len(matrix)-1):
        if j == 0:
            all_steps.extend([[i, j+1], [i-1, j], [i+1, j]])
        elif (j < len(matrix[0])-1):
            all_steps.extend([[i, j-1], [i, j+1], [i-1, j], [i+1, j]])
        else:
            all_steps.extend([[i, j-1], [i-1, j], [i+1, j]])
    else:
        if j == 0:
            all_steps.extend([[i, j+1], [i-1, j]])
        elif (j < len(matrix[0])-1):
            all_steps.extend([[i, j-1], [i, j+1], [i-1, j]])
        else:
            all_steps.extend([[i, j-1], [i-1, j]])        

    cur = matrix[i][j]
    print('all steps', all_steps)
    all_possible_steps = [pos for pos in all_steps if (cur-1 == matrix[pos[0]][pos[1]] or cur == matrix[pos[0]][pos[1]])]
    print('possible steps', all_possible_steps)
    return(all_possible_steps)
 
# main function
def find_min_steps(input):

    # reading input from file
    with open(input, 'r') as input_buffer:
        input_lines = input_buffer.readlines()

    # program variables
    cur = []
    start = []
    end = []
    
    # constructing matrix and finding start and end point
    matrix = [[0 for _ in range(len(input_lines[0])-1)] for _ in range(len(input_lines))]
    reference_matrix = [[0 for _ in range(len(input_lines[0])-1)] for _ in range(len(input_lines))]
    for i in range(len(input_lines)):
        temp = list(input_lines[i].split()[0])
        for j in range(len(temp)):
            matrix[i][j] = ord(temp[j])
            if matrix[i][j] == 83:
                start = [i, j]
                matrix[i][j] = 96
            elif matrix[i][j] == 69:
                end = [i, j]
                matrix[i][j] = 123

    #for i in range(len(matrix)):
    #    for j in range(len(matrix[0])):
    #        print(find_next_steps(i, j, matrix))

    #print(matrix, start, end)

   
    count = 0
    length = move_next(end, start, count, matrix, reference_matrix)
    print(length)


# function to find the number of moves
def move_next(cur, end, count, matrix, reference_matrix):
    i, j = cur[0], cur[1]
    print('pos', i, j)
    if (i == end[0] and j == end[1]):
        print(count)
        exit(0)
    elif reference_matrix[i][j] != 1:
        count += 1
        reference_matrix[i][j] = 1
        next_steps = find_next_steps(i, j, matrix)
        for step in next_steps:
            print('chosen step', step)
            if reference_matrix[step[0]][step[1]] != 1:
                move_next(step, end, count, matrix, reference_matrix)   

# calling main function
find_min_steps('input2.txt')