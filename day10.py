import time, bisect
from collections import defaultdict
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

def getFewestPresses(diagram, schematics):
    n = len(diagram)
    target = diagramToInt(diagram)
    given_nums = {schematicToInt(schematic, n) for schematic in schematics}
    curr_nums = {0}
    #seen_nums = given_nums.copy()
    presses = 0
    while True:
        if target in curr_nums:
            return presses
        curr_nums = {num1 ^ num2 for num1 in curr_nums for num2 in given_nums}
        presses += 1

# for diagram, schematics, reqs in zip(diagrams, button_schematics, joltage_requirements):
#     print(diagram, schematics, reqs)
#     print(getFewestPresses(diagram, schematics))

ans_p1 = sum(getFewestPresses(diagram, schematics) for diagram, schematics in zip(diagrams, button_schematics))
#ans_p2 = 0

t1 = time.time()
print(f"Part 1 answer: {ans_p1}")
#print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t1 - t0:.3f}s")
