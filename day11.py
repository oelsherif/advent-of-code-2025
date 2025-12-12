import time, numpy as np
t0 = time.time()
with open("inputs/11.txt", "r") as File:
    lines = [line[:-1] for line in File.readlines()]

outputs = {}
for line in lines:
    before, after = line.split(":")
    outputs[before] = after.split()

def count_paths(start: str, ends: list[str], memory):
    past_ans = memory.get(start)
    if past_ans is not None:
        return past_ans
    if start in ends:
        ans = np.zeros(len(ends), dtype = np.int64)
        idx = ends.index(start)
        ans[idx] = 1
        return ans
    conns = outputs[start]
    ans = sum(count_paths(conn, ends, memory) for conn in conns)
    memory[start] = ans
    return ans
    
def paths_from_to(start: str, ends: list[str]):
    '''setting up memoization'''
    memory = {}
    return count_paths(start, ends, memory)

ans_p1 = paths_from_to('you', ['out'])[0]

svr_to_dac, svr_to_fft, svr_to_out = paths_from_to('svr', ['dac', 'fft', 'out'])
dac_to_fft, dac_to_out = paths_from_to('dac', ['fft', 'out'])
fft_to_dac, fft_to_out = paths_from_to('fft', ['dac', 'out'])

ans_p2 = svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out

t1 = time.time()

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t1 - t0:.3f}s")
