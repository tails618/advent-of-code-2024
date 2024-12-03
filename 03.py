# day 3

memory: str = open('03-data.txt', 'r').read()

sum_pt1: int = 0
sum_pt2: int = 0
do: bool = True

while(len(memory) >= 8):
    if memory.startswith('do()'):
        do = True
        memory = memory[4:]
    elif memory.startswith("don't()"):
        do = False
        memory = memory[7:]
    elif memory.startswith('mul('):
        comma = memory.find(',')
        closing = memory.find(')')
        n1 = memory[4:comma]
        n2 = memory[comma + 1:closing]
        if n1.isdigit() and n2.isdigit():
            sum_pt1 += int(n1) * int(n2)
            if do:
                sum_pt2 += int(n1) * int(n2)
            memory = memory[closing:]
        else:
            memory = memory[4:]
    else:
        memory = memory[1:]

print(sum_pt1)
print(sum_pt2)