# main function

def find_total_score():   
    
    input = open('input.txt', 'r')
    input_lines = input.readlines()
    total_score = 0
    for i in input_lines:
        win_or_lose = 0
        symbol_point = 0
        if i[0] == 'A':
            if i[2] == 'Y':
                print(i[0], i[2])
                win_or_lose = 3
                symbol_point = 1
            elif i[2] == 'X':
                print(i[0], i[2])
                win_or_lose = 0
                symbol_point = 3
            else:
                print(i[0], i[2])
                win_or_lose = 6
                symbol_point = 2
        elif i[0] == 'B':
            if i[2] == 'Z':
                print(i[0], i[2])
                win_or_lose = 6
                symbol_point = 3
            elif i[2] == 'Y':
                print(i[0], i[2])
                win_or_lose = 3
                symbol_point = 2
            else:
                print(i[0], i[2])
                win_or_lose = 0
                symbol_point = 1
        elif i[0] == 'C':
            if i[2] == 'X':
                print(i[0], i[2])
                win_or_lose = 0
                symbol_point = 2
            elif i[2] == 'Z':
                print(i[0], i[2])
                win_or_lose = 6
                symbol_point = 1
            else:
                print(i[0], i[2])
                win_or_lose = 3
                symbol_point = 3
        print(win_or_lose + symbol_point)
        total_score = total_score + (win_or_lose + symbol_point)
    print(total_score)


find_total_score()