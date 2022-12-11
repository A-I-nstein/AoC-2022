def day4a():   
    input = open('input.txt', 'r')
    input_lines = input.readlines()
    conflictin_pairs = []
    for line in input_lines:
        p1 = line.split(',')[0]
        p2 = line.split(',')[1]
        if (int(p1.split('-')[0]) >= int(p2.split('-')[0]) and int(p1.split('-')[1]) <= int(p2.split('-')[1])):
            conflictin_pairs.append(line)
        elif (int(p2.split('-')[0]) >= int(p1.split('-')[0]) and int(p2.split('-')[1]) <= int(p1.split('-')[1])):
            conflictin_pairs.append(line)
    print(len(conflictin_pairs))

def day4b():   
    input = open('input.txt', 'r')
    input_lines = input.readlines()
    conflictin_pairs = []
    for line in input_lines:
        p1 = line.split(',')[0]
        p2 = line.split(',')[1]
        p1_list = [i for i in range(int(p1.split('-')[0]), int(p1.split('-')[1])+1)]
        p2_list = [i for i in range(int(p2.split('-')[0]), int(p2.split('-')[1])+1)]
        #print(p1_list, p2_list)
        for n in p1_list:
            if n in p2_list:
                conflictin_pairs.append(line)
                break
    print(len(conflictin_pairs))
    #print(conflictin_pairs)


day4b()