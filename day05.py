import time
with open("inputs/05.txt", "r") as File:
    lines = File.readlines()

i_break = lines.index('\n') #find the index of the linebreak
spans = [tuple(int(word) for word in line.split('-')) for line in lines[:i_break]]
nums = [int(line) for line in lines[i_break+1:] ]

def isInSpan(num, span):
    a, b = span
    return True if (num >= a and num <= b) else False

def doOverlap(span1, span2):
    a1, b1 = span1
    a2, b2 = span2
    return False if (a1 > b2 or b1 < a2) else True

def merge(span1, span2):
    a1, b1 = span1
    a2, b2 = span2
    return (min(a1, a2), max(b1, b2))

def getLength(span):
    a, b = span
    return b - a + 1

def combineSpans(old_spans):
    '''return a list of spans handling all the overlaps'''
    new_spans = []
    while old_spans:
        span1 = old_spans.pop()
        for span2 in new_spans:
            if doOverlap(span1, span2):
                new_spans.remove(span2)
                old_spans.append(merge(span1, span2))
                break
        else:
            new_spans.append(span1)
    return new_spans

spans = combineSpans(spans)

t0 = time.time()
ans_p1 = 0
for num in nums:
    for span in spans:
        if isInSpan(num, span):
            ans_p1 += 1
            break
t1 = time.time()

ans_p2 = (sum(getLength(span) for span in spans))
t2 = time.time()

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Part 1 time: {t1 - t0:.3f}s")
print(f"Part 2 time: {t2 - t1:.3f}s")
