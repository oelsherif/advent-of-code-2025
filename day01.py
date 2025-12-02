import time
with open("inputs/01.txt", "r") as File:
    codes = [(line[0], int(line[1:])) for line in File.readlines()]

def countZeroes(dir, curr, new) -> int:
    '''counts the zeroes you pass or stop at in going from curr to new'''
    ans = abs(new//100 - curr//100)
    if dir == 'L':
        if new % 100 == 0:
            ans += 1
        if curr % 100 == 0:
            ans -= 1
    return ans

t0 = time.time()
ans_p1, ans_p2 = 0, 0
current = 50
for dir, num in codes:
    if dir == 'L':
        new = current - num
    else:
        new = current + num
    if new % 100 == 0:
        ans_p1 += 1
    ans_p2 += countZeroes(dir, current, new)
    current = new
t1 = time.time()

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t1 - t0:.3f}s")
