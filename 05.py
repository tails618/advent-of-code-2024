# day 5
# input MUST have a trailing newline

def check_validity(update: list[int]) -> bool:
    for page1loc in range(len(update)):
        for page2loc in range(page1loc + 1, len(update)):
            if update[page1loc] in rules_list[update[page2loc]]:
                return False
    return True

def fix(update: list[int]) -> list[int]:
    for page1loc in range(len(update)):
        for page2loc in range(page1loc + 1, len(update)):
            if update[page1loc] in rules_list[update[page2loc]]:
                update[page1loc], update[page2loc] = update[page2loc], update[page1loc]
    return update

with open('05-data.txt') as f:
    lines: list[str] = f.readlines()
    split: int = lines.index('\n')
    rules: list[str] = lines[:split]
    updates: list[str] = lines[split + 1:]

    rules_list: list[list[int]] = [[] for i in range(99)]
    for rule in rules:
        rule1 = int(rule[:2])
        rule2 = int(rule[3:])
        rules_list[rule1] += [rule2]

    sum_pt1 = 0
    sum_pt2 = 0

    for update in updates:
        update = update[:-1].split(',')
        update_formatted: list[int] = list(map(int, update))
        valid = True
        if check_validity(update_formatted):
            sum_pt1 += update_formatted[int(len(update_formatted) / 2)]
        else:
            fixed_update = fix(update_formatted)
            sum_pt2 += fixed_update[int(len(fixed_update) / 2)]

    print(sum_pt1)
    print(sum_pt2)
