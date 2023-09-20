if __name__ == "__main__":
    n, m = 2, 3
    ls = [[0 for i in range(m)] for j in range(n)]
    ls[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            ls[i][j] = ls[i - 1][j] + ls[i][j - 1]
    print(ls[-1][-1])
