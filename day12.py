import time
t0 = time.time()
with open("inputs/12.txt", "r") as File:
    lines = [line[:-1] for line in File.readlines()]

i, n = 0, len(lines)
shapes = []
dimensions, quantities = [], [] #dimensions and required quantities per shape of each region

while i < n:
    line = lines[i]
    if line[1] == ':':
        shapes.append(lines[i+1:i+4])
        i += 5
    else:
        before, after = line.split(':')
        dimensions.append(tuple(int(word) for word in before.split('x')))
        quantities.append([int(word) for word in after.split()])
        i += 1

shape_area = [sum(line.count('#') for line in shape) for shape in shapes]

ans = 0
for dimension, quantity in zip(dimensions, quantities):
    a = dimension[0] * dimension[1]
    b = sum(quantity[k]*shape_area[k] for k in range(len(quantity)))
    if a >= b:
        ans += 1

t1 = time.time()

print(f"Answer: {ans}")
print(f"Time: {t1 - t0:.3f}s")
