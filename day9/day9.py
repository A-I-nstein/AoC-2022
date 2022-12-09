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
            else:
                t_pos[0] += 1
            t_pos[1] += 1
        elif dir == 'D':
            if (h_pos[0]<t_pos[0]):
                t_pos[0] -= 1
            else:
                t_pos[0] += 1
            t_pos[1] -= 1
        elif dir == 'L':
            t_pos[0] -= 1
            if (h_pos[1]<t_pos[1]):
                t_pos[1] -= 1
            else:
                t_pos[1] += 1
        elif dir == 'R':
            t_pos[0] += 1
            if (h_pos[1]<t_pos[1]):
                t_pos[1] -= 1
            else:
                t_pos[1] += 1
    
    #print(t_pos)
    return t_pos

# main function
def find_visited_positions(input):

    with open(input, 'r') as input_buffer:
        input_lines = input_buffer.readlines()

    t_pos = [0, 0]
    h_pos = [0, 0]
    t_visited_pos = []

    for line in input_lines:
        dir, steps = line.split()[0], int(line.split()[1])
        if dir == 'U':
            for i in range(steps):
                h_pos[1] +=1
                temp = deepcopy(t_pos)
                t_pos = []
                t_pos = move_t(h_pos, temp, dir)
                if t_pos not in t_visited_pos:
                    t_visited_pos.append(t_pos)
                    #print(t_visited_pos)
        elif dir == 'D':
            for i in range(steps):
                h_pos[1] -=1
                temp = deepcopy(t_pos)
                t_pos = []
                t_pos = move_t(h_pos, temp, dir)
                if t_pos not in t_visited_pos:
                    t_visited_pos.append(t_pos)
                    #print(t_visited_pos)
        elif dir == 'R':
            for i in range(steps):
                h_pos[0] +=1
                temp = deepcopy(t_pos)
                t_pos = []
                t_pos = move_t(h_pos, temp, dir)
                if t_pos not in t_visited_pos:
                    t_visited_pos.append(t_pos)
                    #print(t_visited_pos)
        elif dir == 'L':
            for i in range(steps):
                h_pos[0] -=1
                temp = deepcopy(t_pos)
                t_pos = []
                t_pos = move_t(h_pos, temp, dir)
                if t_pos not in t_visited_pos:
                    t_visited_pos.append(t_pos)
                    #print(t_visited_pos)
    
    print(len(t_visited_pos))
    #print(t_visited_pos)

# calling main function
find_visited_positions('input2.txt')