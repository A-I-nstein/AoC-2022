# main function

def find_elf():
    
    elf_calories = []
    temp_calories = 0
    input = open('input.txt', 'r')
    input_lines = input.readlines()
    
    #print(repr(input_lines))
    
    for line in input_lines:
        if line == '\n':
            elf_calories.append(temp_calories)
            temp_calories = 0
        else:
            temp_calories = temp_calories + int(line)

    elf_calories.sort(reverse=True)
    print(elf_calories[0]+elf_calories[1]+elf_calories[2])

find_elf()