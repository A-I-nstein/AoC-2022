# main function
def find_best_score(input_file):

    # read input from file
    with open(input_file, 'r') as input_buffer:
        input_lines = input_buffer.readlines()

    # program variables
    tree_grid = []
    best_score = 0

    # populating the grid
    for line in input_lines:
        tree_grid.append([int(char) for char in line if char.isnumeric()])

    # findind the trees that are visible
    for i in range(1, len(tree_grid)-1):
        for j in range(1, len(tree_grid[0])-1):

            score = 1
            
            temp_score = 0
            for x in range(i-1, -1, -1):
                if tree_grid[i][j] > tree_grid[x][j]:
                    temp_score += 1
                elif tree_grid[i][j] == tree_grid[x][j]:
                    temp_score += 1
                    break
                else:
                    temp_score += 1
                    break
            score *= temp_score
            
            temp_score = 0
            for x in range(i+1, len(tree_grid)):
                if tree_grid[i][j] > tree_grid[x][j]:
                    temp_score += 1
                elif tree_grid[i][j] == tree_grid[x][j]:
                    temp_score += 1
                    break
                else:
                    temp_score += 1
                    break
            score *= temp_score
            
            temp_score = 0  
            for y in range(j-1, -1, -1):
                if tree_grid[i][j] > tree_grid[i][y]:
                    temp_score += 1
                elif tree_grid[i][j] == tree_grid[i][y]:
                    temp_score += 1
                    break
                else:
                    temp_score += 1
                    break
            score *= temp_score
            
            temp_score = 0  
            for y in range(j+1, len(tree_grid[0])):
                if tree_grid[i][j] > tree_grid[i][y]:
                    temp_score += 1
                elif tree_grid[i][j] == tree_grid[i][y]:
                    temp_score += 1
                    break
                else:
                    temp_score += 1
                    break
            score *= temp_score
                    
            if score > best_score:
                best_score = score
    
    print(best_score)


find_best_score('input2.txt')