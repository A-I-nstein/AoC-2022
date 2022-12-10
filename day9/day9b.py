from copy import deepcopy

# function to move t
def move_t(h_pos, t_pos, dir):

    dist = ((h_pos[0]-t_pos[0])**2 + (h_pos[1]-t_pos[1])**2)**0.5

    if dist <= 1:
        pass

    elif (dist > 1 and dist < 2):
        pass

    elif dist == 2:
        if dir == 'U':
            t_pos[1] += 1
        elif dir == 'D':
            t_pos[1] -= 1
        elif dir == 'L':
            t_pos[0] -= 1
        elif dir == 'R':
            t_pos[0] += 1 

    else:
        if dir == 'U':
            if (h_pos[0]<t_pos[0]):
                t_pos[0] -= 1
                dir = 'L'
            else:
                t_pos[0] += 1
                dir = 'R'
            t_pos[1] += 1
        elif dir == 'D':
            if (h_pos[0]<t_pos[0]):
                t_pos[0] -= 1
                dir = 'L'
            else:
                t_pos[0] += 1
                dir = 'R'
            t_pos[1] -= 1
        elif dir == 'L':
            t_pos[0] -= 1
            if (h_pos[1]<t_pos[1]):
                t_pos[1] -= 1
                dir = 'D'
            else:
                t_pos[1] += 1
                dir = 'U'
        elif dir == 'R':
            t_pos[0] += 1
            if (h_pos[1]<t_pos[1]):
                t_pos[1] -= 1
                dir = 'D'
            else:
                t_pos[1] += 1
                dir = 'U'
    
    #print(t_pos)
    return t_pos, dir

# main function
def find_visited_positions(input):

    with open(input, 'r') as input_buffer:
        input_lines = input_buffer.readlines()

    pos = [[0, 0] for _ in range(10)]
    t_visited_pos = []

    for line in input_lines:
        dir, steps = line.split()[0], int(line.split()[1])
        if dir == 'U':
            for _ in range(steps):
                pos[0][1] +=1
                for i in range(1, len(pos)):
                    temp1 = deepcopy(pos[i])
                    temp2 = deepcopy(dir)
                    dir = []
                    pos[i] = []
                    pos[i], dir = move_t(pos[i-1], temp1, temp2)
                if pos[-1] not in t_visited_pos:
                    t_visited_pos.append(pos[-1])
                    #print(pos[-1])
        elif dir == 'D':
            for _ in range(steps):
                pos[0][1] -=1
                for i in range(1, len(pos)):
                    temp1 = deepcopy(pos[i])
                    temp2 = deepcopy(dir)
                    dir = []
                    pos[i] = []
                    pos[i], dir = move_t(pos[i-1], temp1, temp2)
                if pos[-1] not in t_visited_pos:
                    t_visited_pos.append(pos[-1])
                    #print(pos[-1])
        elif dir == 'R':
            for _ in range(steps):
                pos[0][0] +=1
                for i in range(1, len(pos)):
                    temp1 = deepcopy(pos[i])
                    temp2 = deepcopy(dir)
                    dir = []
                    pos[i] = []
                    pos[i], dir = move_t(pos[i-1], temp1, temp2)
                if pos[-1] not in t_visited_pos:
                    t_visited_pos.append(pos[-1])
                    #print(pos[-1])
        elif dir == 'L':
            for _ in range(steps):
                pos[0][0] -=1
                for i in range(1, len(pos)):
                    temp1 = deepcopy(pos[i])
                    temp2 = deepcopy(dir)
                    dir = []
                    pos[i] = []
                    pos[i], dir = move_t(pos[i-1], temp1, temp2)
                if pos[-1] not in t_visited_pos:
                    t_visited_pos.append(pos[-1])
                    #print(pos[-1])
        #print(t_visited_pos)
        #print()
        #print(pos)
        #print()
        #print()
    print(len(t_visited_pos))

# calling main function
find_visited_positions('input2.txt')