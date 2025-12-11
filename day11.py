import time
from collections import defaultdict
t0 = time.time()
with open("inputs/11.txt", "r") as File:
    lines = [line[:-1] for line in File.readlines()]

outputs = {}
for line in lines:
    before, after = line.split(":")
    outputs[before] = after.split()

start = 'you'
current = ['you']
ans_p1 = 0
while current:
    new = []
    for dev1 in current:
        conns = outputs[dev1]
        for conn in conns:
            if conn == 'out':
                ans_p1 += 1
            else:
                new.append(conn)
    current = new.copy()

t1 = time.time()
print(f"Part 1 answer: {ans_p1}")
#print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t1 - t0:.3f}s")
