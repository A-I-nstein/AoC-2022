from collections import Counter

def find_dup(text):
    wc = Counter(text)
    for letter, count in wc.items():
        if (count>1):
            return False
    return True

def day6(input):

    # read input
    input = open(input, 'r')
    input_lines = input.readlines()

    for line in input_lines:
        for i in range(13, len(line)):
            text = line[i-13:i+1]
            state = find_dup(text)
            if state == True:
                print(i+1)
                break

day6('input2.txt')