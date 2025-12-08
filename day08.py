import time, bisect
t0 = time.time()
with open("inputs/08.txt", "r") as File:
    lines = [line[:-1] for line in File.readlines()]
n = 1000

points =  [tuple(int(num) for num in line.split(',')) for line in lines]
n_points = len(points)

def getD2(point1, point2):
    '''calculate square of the distance between two points'''
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

pairs, pair_distance = [], []
for i, point1 in enumerate(points):
    for j in range(i+1, n_points):
        point2 = points[j]
        dist2 = getD2(point1, point2)
        idx = bisect.bisect(pair_distance, dist2)
        pair_distance.insert(idx, dist2)
        pairs.insert(idx, (i,j))

### Part 1
key_id = 0
point_circuit = [None for _ in range(n_points)]
circuits = {}
for count in range(n):
    i, j = pairs[count]
    circuit_i, circuit_j = point_circuit[i], point_circuit[j]
    if circuit_i == None and circuit_j == None:
        point_circuit[i] = key_id
        point_circuit[j] = key_id
        circuits[key_id] = {i, j}
        key_id += 1
    elif circuit_j == None:
        point_circuit[j] = circuit_i
        circuits[circuit_i].add(j)
    elif circuit_i == None:
        point_circuit[i] = circuit_j
        circuits[circuit_j].add(i)
    elif circuit_i == circuit_j:
        continue
    else:
        junctions_j = circuits.pop(circuit_j)
        for junc in junctions_j:
            point_circuit[junc] = circuit_i
        circuits[circuit_i].update(junctions_j)

sizes = sorted([len(circuit) for circuit in circuits.values()], reverse=True)
ans_p1 = sizes[0] * sizes[1] * sizes[2]

### Part 2
key_id = 0
point_circuit = [None for _ in range(n_points)]
circuits = {}
for count in range(len(pairs)):
    i, j = pairs[count]
    circuit_i, circuit_j = point_circuit[i], point_circuit[j]
    if circuit_i == None and circuit_j == None:
        point_circuit[i] = key_id
        point_circuit[j] = key_id
        circuits[key_id] = {i, j}
        key_id += 1
    elif circuit_j == None:
        point_circuit[j] = circuit_i
        circuits[circuit_i].add(j)
    elif circuit_i == None:
        point_circuit[i] = circuit_j
        circuits[circuit_j].add(i)
    elif circuit_i == circuit_j:
        continue
    else:
        junctions_j = circuits.pop(circuit_j)
        for junc in junctions_j:
            point_circuit[junc] = circuit_i
        circuits[circuit_i].update(junctions_j)
    if len(next(iter(circuits.values()))) == n_points:
        break

x1, x2 = points[i][0], points[j][0]
ans_p2 = x1 * x2

t1 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t1 - t0:.3f}s")
