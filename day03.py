import time
with open("inputs/03.txt", "r") as File:
    banks = [line[:-1] for line in File.readlines()]

def getMaxJoltage(bank, k):
    '''find highest joltage of length k'''
    n = len(bank)
    s = ''
    i_left = 0
    for i_right in range(n-k+1, n+1):
        target = bank[i_left:i_right]
        char = max(target)
        s += char
        i_left += target.find(char) + 1
    return int(s)

t0 = time.time()
ans_p1 = sum(getMaxJoltage(bank, 2) for bank in banks)
t1 = time.time()
ans_p2 = sum(getMaxJoltage(bank, 12) for bank in banks)
t2 = time.time()

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Part 1 time: {t1 - t0:.3f}s")
print(f"Part 2 time: {t2 - t1:.3f}s")
