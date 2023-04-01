from collections import defaultdict
from functools import wraps
from itertools import combinations, product
import os
import shutil
import time


PROB1 = {0: 0.001, 1: 0.003, 2: 0.006, 3: 0.01, 4: 0.015, 5: 0.021, 6: 0.029,
         7: 0.036, 8: 0.045, 9: 0.055, 10: 0.063, 11: 0.069, 12: 0.073, 13: 0.075}
PROB2 = {27 - k: PROB1[k] for k in PROB1}
# PROB1 = {0: 0.001, 1: 0.003, 2: 0.006}
# PROB2 = {5 - k: PROB1[k] for k in PROB1}


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(
            f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


def gen_prob_mem(prob):
    mem = {"": 0}
    for l in range(1, len(prob)+1):
        combs = combinations(prob.keys(), l)
        for comb in combs:
            prev_str = ",".join(map(str, comb[:-1]))
            s = mem[prev_str] + prob[comb[-1]]
            if prev_str:
                prev_str = prev_str + ","
            comb_str = prev_str + str(comb[-1])
            mem[comb_str] = s
    del mem[""]
    return mem


def group(m):
    sum_group = defaultdict(list)
    for k in m:
        sum_group[round(m[k], 3)].append(k)
    return sum_group

@timeit
def group_prod_and_write(g1, g2, ks, res_dir):
    p_g = defaultdict(list)
    for ak, bk in ks:
        for a, b in product(g1[ak], g2[bk]):
            comb_str = f"{a},{b}"
            s = round(ak + bk, 3)
            p_g[s].append(comb_str)
    for k in p_g:
        write(p_g[k], os.path.join(res_dir, f"{k}.txt"))
    


CNT = 0
def write(res, fname):
    global CNT
    # print(f"write {len(res)} {fname}")
    with open(fname, 'a') as f:
        CNT += len(res)
        f.writelines(line + '\n' for line in res)


if __name__ == '__main__':
    res_dir = './data'
    shutil.rmtree(res_dir)
    os.mkdir(res_dir)

    mem1 = gen_prob_mem(PROB1)
    mem2 = gen_prob_mem(PROB2)
    g1 = group(mem1)
    g2 = group(mem2)
    for k in g1:
        write(g1[k], os.path.join(res_dir, f"{k}.txt"))
    for k in g2:
        write(g2[k], os.path.join(res_dir, f"{k}.txt"))

    prod_k = [(ak, bk) for ak, bk in product(g1, g2)]
    batch_size = 5000
    for i in range((len(prod_k)+batch_size-1)//batch_size):
            print("batch " ,i)
            group_prod_and_write(g1, g2, prod_k[i*batch_size:i*batch_size+batch_size], res_dir)
    print(f"total lines {CNT}")