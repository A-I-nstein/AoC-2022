'''
Fails to work if directories have same name
'''

# imports
from treelib import Tree

# main function
def find_big_directories(input_file):

    # read input from file
    with open(input_file, 'r') as input_buffer:
        input_lines = input_buffer.readlines()

    # program variables
    directory_tree = Tree()
    directory_tree.create_node("root", "root", parent = None)
    files = {}
    directories = {"root": 0}
    cd = "root"
    i = 1

    # iterating through the input lines to form the structure of the directories
    while i < len(input_lines):
        # find if the line has a command
        if '$' in input_lines[i]:
            # change directory command
            if 'cd' in input_lines[i]:
                # go back to the parent directory
                if '..' not in input_lines[i]:
                    cd = input_lines[i].split()[-1]
                # go to a particular directory
                else:
                    cd = directory_tree.parent(cd).tag
            # list all in a directory
            elif 'ls' in input_lines[i]:
                # populate directories
                while (i+1 <= len(input_lines)-1 and '$' not in input_lines[i+1]):
                    i = i+1
                    # if the current artifact is a directory
                    if 'dir' in input_lines[i]:
                        dir_info = input_lines[i].split()
                        directory_tree.create_node(dir_info[-1], dir_info[-1], cd)
                        directories[dir_info[-1]] = 0
                    # if the current artifact is a file
                    else:
                        file_info = input_lines[i].split()
                        directory_tree.create_node(file_info[-1], file_info[-1], cd, int(file_info[0]))
                        files[file_info[-1]] = int(file_info[0])
        i = i+1

    # show the tree
    #directory_tree.show()

    # find the size of files in a directory
    for file in files.keys():
        directories[directory_tree.parent(file).tag] += (files[file])

    # find the size of a single directory
    for directory in directories.keys():
        if directory != 'root':
            if directory_tree.parent(directory).tag != 'root':
                directories[directory_tree.parent(directory).tag] += (directories[directory])

    # find the total sizes of directories < 100000
    total_size = 0
    for directory in directories.keys():
        if directories[directory] < 100000:
            total_size += directories[directory]
    
    print(total_size)

find_big_directories('input1.txt')