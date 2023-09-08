from itertools import combinations

total = 0

for i in range(1, 20):
    total += len(list(combinations(range(i + 4), 4)))

print(total)
