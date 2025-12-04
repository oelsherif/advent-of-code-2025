import time
with open("inputs/04.txt", "r") as File:
    grid = [line[:-1] for line in File.readlines()]

n_rows, n_cols = len(grid), len(grid[0])

def isInGrid(x, y):
    '''check if position (x, y) is within grid'''
    if x < 0 or x >= n_cols or y < 0 or y >= n_rows:
        return False
    return True

def isPaper(x, y):
    return grid[y][x] == '@'

def getPaperNeighbors(x, y):
    '''generate list of paper neighbors'''
    neighbors = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            new_x, new_y = x + dx, y + dy
            if not isInGrid(new_x, new_y):
                continue
            if isPaper(new_x, new_y):
                neighbors.append((new_x, new_y))
    return neighbors

t0 = time.time()

paper_neighbors = {}
for x in range(n_cols):
    for y in range(n_rows):
        if isPaper(x, y):
            paper_neighbors[(x, y)] = getPaperNeighbors(x, y)

ans_p1 = sum(1 for neighbors in paper_neighbors.values() if len(neighbors) < 4)
t1 = time.time()

ans_p2 = 0
to_check = set(paper_neighbors.keys())
while to_check:
    pos = to_check.pop()
    neighbors = paper_neighbors[pos]
    if len(neighbors) >= 4:
        continue
    ans_p2 += 1
    to_check.update(neighbors)
    for neighbor in neighbors:
        paper_neighbors[neighbor].remove(pos)

t2 = time.time()

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Part 1 time: {t1 - t0:.3f}s")
print(f"Part 2 time: {t2 - t1:.3f}s")
