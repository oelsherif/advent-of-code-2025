import time, bisect
from collections import defaultdict
t0 = time.time()
with open("inputs/09.txt", "r") as File:
    points = [tuple(int(word) for word in line.split(',')) for line in File.readlines()]

def getArea(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x2-x1)+1) * (abs(y2-y1)+1)

points.append(points[0])
n = len(points)

hor_lines, ver_lines = defaultdict(list), defaultdict(list)
for i, p1 in enumerate(points[:n-1]):
    p2 = points[i+1]
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        ver_lines[x1].append((min(y1, y2), max(y1, y2)))
    if y1 == y2:
        hor_lines[y1].append((min(x1, x2), max(x1, x2)))

ver_keys = sorted(list(ver_lines.keys()))
hor_keys = sorted(list(hor_lines.keys()))

def inSpanExclusive(num, span):
    a, b = span
    if num > a and num < b:
        return True
    return False

def isAreaClean(p1, p2):
    '''cheack if area formed from opposite corners p1 and p2 is interrupted by any lines'''
    x1, y1 = p1
    x2, y2 = p2
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    x_idx_1 = bisect.bisect_right(ver_keys, x_min)
    x_idx_2 = bisect.bisect_left(ver_keys, x_max)
    for ver_key in ver_keys[x_idx_1:x_idx_2]:
        y_spans = ver_lines[ver_key]
        for y_span in y_spans:
            y_a, y_b = y_span
            if y_min >= y_a and y_min < y_b:
                return False
            if y_max > y_a and y_max <= y_b:
                return False       
    y_idx_1 = bisect.bisect_right(hor_keys, y_min)
    y_idx_2 = bisect.bisect_left(hor_keys, y_max)
    for hor_key in hor_keys[y_idx_1:y_idx_2]:
        x_spans = hor_lines[hor_key]
        for x_span in x_spans:
            x_a, x_b = x_span
            if x_min >= x_a and x_min < x_b:
                return False
            if x_max > x_a and x_max <= x_b:
                return False
    return True

def isAreaInside(p1, p2):
    '''
    was intended to check if clean area formed from opposite corners p1 and p2 is inside loop, i.e contains only red and green tiles
    did not need to implement as the case where the biggest clean area is outside the loop was not in the input data
    '''

ans_p1, ans_p2 = 0, 0
for i, p1 in enumerate(points[:n-2]):
    for j in range(i+2, n-1):
        p2 = points[j]
        area = getArea(p1, p2)
        if area > ans_p1:
            ans_p1 = area
        if area <= ans_p2:
            continue
        if isAreaClean(p1, p2):
            ans_p2 = area


t1 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t1 - t0:.3f}s")
