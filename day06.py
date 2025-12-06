import time, math
t0 = time.time()
with open("inputs/06.txt", "r") as File:
    lines = [line[:-1] for line in File.readlines()]

op_line = lines[-1]
op_locs = [i for i, op in enumerate(op_line) if op != ' '] + [len(op_line) + 1]
spans = [(op_locs[i], op_locs[i+1] - 1) for i in range(len(op_locs)-1)]
number_grid = [[line[a:b] for a, b in spans] for line in lines[:-1]]
ops = op_line.split()
n = len(ops)
cols = [[row[i] for row in number_grid] for i in range(n)]

def get_nums_a(col):
    '''read the numbers in a column horizontally'''
    return [int(word) for word in col]

def get_nums_b(col):
    '''read the numbers in a column vertically'''
    n = len(col[0])
    return [int(''.join(row[i] for row in col)) for i in range(n)]

def eval(nums, op):
    if op == '+':
        return sum(nums)
    else:
        return math.prod(nums)
    
ans_p1 = sum(eval(get_nums_a(col), op) for col, op in zip(cols, ops))
ans_p2 = sum(eval(get_nums_b(col), op) for col, op in zip(cols, ops))

t1 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t1 - t0:.3f}s")
