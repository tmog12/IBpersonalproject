import random

result = None
with open ('list.txt', 'r') as fin:
    range (1)
    lines = fin.readlines()
    index = random.randint(0, len(lines)-1)
    result = lines[index]

    print(result)
