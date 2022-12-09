# main function
def find_visible_trees(input_file):

    # read input from file
    with open(input_file, 'r') as input_buffer:
        input_lines = input_buffer.readlines()

    # program variables
    tree_grid = []
    visible_trees = []

    # populating the grid
    for line in input_lines:
        tree_grid.append([int(char) for char in line if char.isnumeric()])

    # findind the trees that are visible
    for i in range(1, len(tree_grid)-1):
        for j in range(1, len(tree_grid[0])-1):
            visible = [True, True, True, True]
            for x in range(i):
                #print(tree_grid[x][j])
                if tree_grid[i][j] <= tree_grid[x][j]:
                    visible[0] = False
            for x in range(i+1, len(tree_grid)):
                #print(tree_grid[x][j])
                if tree_grid[i][j] <= tree_grid[x][j]:
                    visible[1] = False
            for y in range(j):
                #print(tree_grid[i][y])
                if tree_grid[i][j] <= tree_grid[i][y]:
                    visible[2] = False
            for y in range(j+1, len(tree_grid[0])):
                #print(tree_grid[i][y])
                if tree_grid[i][j] <= tree_grid[i][y]:
                    visible[3] = False
            for dir in visible:
                if dir == True:
                    #print('tree', tree_grid[i][j])
                    visible_trees.append(tree_grid[i][j])  
                    break
            #print('\n')      
    
    print(len(visible_trees))
    print(2*(len(tree_grid)+len(tree_grid[0]))-4)

find_visible_trees('input2.txt')