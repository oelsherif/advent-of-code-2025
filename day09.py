import time, bisect
from collections import defaultdict
t0 = time.time()
with open("inputs/09.txt", "r") as File:
    points = [tuple(int(word) for word in line.split(',')) for line in File.readlines()]

def getArea(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x2-x1)+1) * (abs(y2-y1)+1)

n = len(points)

ans_p1, ans_p2 = 0, 0
for i, p1 in enumerate(points[:n-1]):
    for j in range(i+2, n):
        p2 = points[j]
        area = getArea(p1, p2)
        if area > ans_p1:
            ans_p1 = area

t1 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Time: {t1 - t0:.3f}s")
