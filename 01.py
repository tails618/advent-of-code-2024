# day 1

# puzzle 1

l = open('01-data.txt', 'r').read().split()
l1, l2 = sorted(l[0::2]), sorted(l[1::2])
res = sum(abs(int(a) - int(b)) for a, b in zip(l1, l2))
print(res)

# puzzle 2

res = sum(int(n) * l2.count(n) for n in l1)
print(res)