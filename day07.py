import time
from collections import defaultdict
t0 = time.time()
with open("inputs/07.txt", "r") as File:
    grid = [line[:-1] for line in File.readlines()]

beams_per_loc = {grid[0].find('S'): 1}
ans_p1, ans_p2 = 0, 1
for row in grid[1:]:
    new_beams_per_loc = defaultdict(int)
    for loc, num in beams_per_loc.items():
        if row[loc] == '^':
            ans_p1 += 1
            ans_p2 += num
            new_beams_per_loc[loc-1] += num
            new_beams_per_loc[loc+1] += num
        else:
            new_beams_per_loc[loc] += num
    beams_per_loc = new_beams_per_loc.copy()

#ans_p2 = sum(beams_per_loc.values())
t1 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t1 - t0:.3f}s")
