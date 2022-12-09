def find_priority(i):

    if i.islower():
        priority = ord(i)-96
    if i.isupper():
        priority = ord(i)-38
    return priority

def day3a():   
    
    input = open('input.txt', 'r')
    input_lines = input.readlines()
    priorities = []
    for line in input_lines:
        comp1 = line[:len(line)//2]
        comp2 = line[len(line)//2:]
        for i in comp1:
            if i in comp2:
                priority = find_priority(i)
                priorities.append(priority)
                print(comp1, comp2, i, priority)
                break
    print(sum(priorities))



def day3b():
    input = open('input.txt', 'r')
    input_lines = input.readlines()
    priorities = []

    for i in range(0, len(input_lines), 3):
        g1 = input_lines[i]
        g2 = input_lines[i+1]
        g3 = input_lines[i+2]
        for obj in g1:
            if (obj in g2) and (obj in g3):
                priority = find_priority(obj)
                print(obj, priority)
                priorities.append(priority)
                break
    
    print(sum(priorities))

day3b()

'''
import string

up = string.ascii_letters
for i in up:
    print(i, find_priority(i))
'''