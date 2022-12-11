def day5(input):

    # read input
    input = open(input, 'r')
    input_lines = input.readlines()

    # split input, reference line, rearrangement procedure
    for i in range(len(input_lines)):
        if input_lines[i] == '\n':
            break
    input_raw = ''.join(input_lines[:i-1])
    ref_raw = ''.join(input_lines[i-1:i])
    move_raw = input_lines[i+1:]

    # finding size of stack
    for i in range(len(ref_raw)-1, 0, -1):
        if ref_raw[i].isnumeric():
            n = int(ref_raw[i])
            break
    
    # forming the stack template
    stack = []
    for i in range(n):
        stack.append([])

    # forming the stack
    for i in range(1, len(input_raw), 4*n):
        temp = 0
        temp2 = i+0
        while temp<n:
            stack[temp].insert(0, input_raw[temp2])
            temp = temp+1
            temp2 = temp2+4

    # removing empty spaces in the end
    for i in range(n):
        for j in range(len(stack[i])-1, 0, -1):
            if stack[i][j] == " ":
                stack[i].pop()
            else:
                break

    # moving crates
    for ins in move_raw:
        temp = ins.split()
        temp2 = []
        q = int(temp[1])
        src = int(temp[3])
        dst = int(temp[5])
        for i in range(q):
            temp2.insert(0, stack[src-1].pop())
        stack[dst-1].extend(temp2)

    # getting the top crates
    for i in range(n):
        print(stack[i].pop())

day5('input2.txt')