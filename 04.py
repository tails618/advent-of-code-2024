# day 4
# input must NOT have a trailing newline

def search_for_word(x, y, dx, dy, word):
    for i in range(len(word)):
        x1, y1 = x + i * dx, y + i * dy
        if (not (0 <= x1 < len(rows[0]) and 0 <= y1 < len(rows))) or rows[y1][x1] != word[i]:
            return False
    return True

def search_for_word_cross(x, y):
    if x > 0 and x < len(rows[0]) - 1 and y > 0 and y < len(rows) - 1:
        if rows[y][x] == 'A':
            if rows[y-1][x-1] == 'M' and rows[y+1][x+1] == 'S':
                if (rows[y+1][x-1] == 'M' and rows[y-1][x+1] == 'S') or (rows[y+1][x-1] == 'S' and rows[y-1][x+1] == 'M'):
                    return True
            elif rows[y-1][x-1] == 'S' and rows[y+1][x+1] == 'M':
                if (rows[y+1][x-1] == 'M' and rows[y-1][x+1] == 'S') or (rows[y+1][x-1] == 'S' and rows[y-1][x+1] == 'M'):
                    return True
    return False


sum = 0
sum2 = 0
with open('04-data.txt', 'r') as f:
    grid: list[str] = f.readlines()
    rows: list[str] = [line.strip() for line in grid]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for row in range(len(rows)):
        for col in range(len(rows[0])):
            for dx, dy in directions:
                if search_for_word(col, row, dx, dy, 'XMAS'):
                    sum += 1
            if search_for_word_cross(col, row):
                sum2 += 1

print(sum)
print(sum2)