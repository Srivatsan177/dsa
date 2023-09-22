import collections
if __name__ == "__main__":
    ls = [4, 2, 2, 6, 4]
    k = 6
    xi = 0
    xor_index = collections.defaultdict(int)
    xor_index[xi] = 1
    cnt = 0
    for idx, num in enumerate(ls):
        xi ^= num
        x = xi ^ k
        cnt += xor_index[x]
        xor_index[xi] += 1
    print(cnt)