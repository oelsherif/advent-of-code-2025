import time
with open("inputs/02.txt", "r") as File:
    spans = [tuple(code.split('-')) for code in File.readline()[:-1].split(',')]

def getLimits(span, k):
    '''return lowest and highest number where, if repeated k times, forms an invalid ID'''
    a, b = span
    n_a, n_b = len(a), len(b)
    if n_a % k:
        lim_1 = '1' + '0' * (n_a//k)
    else:
        first_part_a = a[:n_a//k]
        if int(first_part_a * k) >= int(a):
            lim_1 = first_part_a
        else:
            lim_1 = str(int(first_part_a) + 1)

    if n_b % k:
        lim_2 = '9' * (n_b//k)
    else:
        first_part_b = b[:n_b//k]
        if int(first_part_b * k) <= int(b):
            lim_2 = first_part_b
        else:
            lim_2 = str(int(first_part_b) - 1)
    return (int(lim_1), int(lim_2))

def getInvalidIDs(span, k):
    '''return all invalid IDs in span with k repititions'''
    low, high = getLimits(span, k)
    return [int(str(num) * k) for num in range(low, high+1)]

def getSum(span, n = None):
    '''return the sum of all the total invalid IDs'''
    if n is None:
        n = len(span[1])
    invalid_IDs = set()
    for k in range(2, n+1):
        invalid_IDs.update(getInvalidIDs(span, k))
    return sum(invalid_IDs)

t0 = time.time()
ans_p1 = sum(getSum(span, 2) for span in spans)
t1 = time.time()
ans_p2 = sum(getSum(span) for span in spans)
t2 = time.time()

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Part 1 time: {t1 - t0:.3f}s")
print(f"Part 2 time: {t2 - t1:.3f}s")
