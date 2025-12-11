import time, pulp, numpy as np
t0 = time.time()
with open("inputs/10.txt", "r") as File:
    lines = [line[:-1] for line in File.readlines()]

diagrams, button_schematics, joltage_requirements = [], [], []
for line in lines:
    words = line.split()
    diagrams.append(words[0][1:-1])
    schematics = []
    for word in words[1:-1]:
        schematics.append([int(s) for s in word[1:-1].split(',')])
    button_schematics.append(schematics)
    joltage_requirements.append([int(s) for s in words[-1][1:-1].split(',')])

def diagramToInt(s):
    s = s.replace('.', '0').replace('#', '1')
    return int(s, 2)

def schematicToInt(arr, n):
    val = 0
    for num in arr:
        val += 2**(n-1-num)
    return val

def getFewestPressesA(diagram, schematics):
    '''get fewest presses need for part A, to get the lights to match the target diagram'''
    n = len(diagram)
    target = diagramToInt(diagram)
    given_nums = {schematicToInt(schematic, n) for schematic in schematics}
    curr_nums = {0}
    seen_nums = {0}
    presses = 0
    while True:
        if target in curr_nums:
            return presses
        curr_nums = {num1 ^ num2 for num1 in curr_nums for num2 in given_nums}
        curr_nums -= seen_nums
        seen_nums |= curr_nums
        presses += 1

def schematicsToBinList(schematic, n):
    '''return a list of zeroes and ones corresponding to the schematic, which would be our increments'''
    inc = [0]*n
    for num in schematic:
        inc[num] += 1
    return inc

def getFewestPressesB(schematics, reqs):
    '''
    get fewest presses needed for part B, to get the joltage to match target joltage
    solving system of equation using pulp to gurantee integer non-negative answers
    '''
    n = len(reqs)
    target = np.array(reqs)
    incs = np.array([schematicsToBinList(schematic, n) for schematic in schematics])
    M = incs.T

    a, b = M.shape
    prob = pulp.LpProblem("SolveSystem", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(b)]
    prob += pulp.lpSum(x)
    for i in range(a):
        prob += pulp.lpSum(M[i, j] * x[j] for j in range(b)) == target[i]
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    sol = [v.value() for v in x]

    return round(sum(sol))

ans_p1 = sum(getFewestPressesA(diagram, schematics) for diagram, schematics in zip(diagrams, button_schematics))
ans_p2 = sum(getFewestPressesB(schematics, reqs) for schematics, reqs in zip(button_schematics, joltage_requirements))

t1 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t1 - t0:.3f}s")
