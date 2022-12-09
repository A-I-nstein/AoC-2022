
# main function
def find_big_directories(input_file):

    # read input from file
    with open(input_file, 'r') as input_buffer:
        input_lines = input_buffer.readlines()

    # directory stacks
    directories = []
    popped_directories = []

    # find total size of individual directories
    for line in input_lines:
        if 'cd ' in line:
            if '..' in line:
                popped_directories.append(directories.pop())
            else:
                directories.append([line.split()[-1], 0])
        elif (' ls' in line or 'dir ' in line):
            pass
        else:
            for i in range(len(directories)):
                directories[i][1] += int(line.split()[0])
    
    while (len(directories)>0):
        popped_directories.append(directories.pop())

    # find the total sizes of directories < 100000
    total_size_less_than_100k = 0
    for directory in popped_directories:
        if directory[1] < 100000:
            total_size_less_than_100k += directory[1]
    
    print(total_size_less_than_100k)

    space_used = popped_directories[-1][1]
    available_space = 70000000 - space_used
    space_required = 30000000 - available_space
    space_acquired = 70000000
    candidate_dir = ''

    for directory in popped_directories:
        if ( directory[1]-space_required > 0 and directory[1]-space_required < space_acquired):
            space_acquired = directory[1]-space_required
            candidate_dir = directory[1]

    print(candidate_dir)

find_big_directories('input2.txt')