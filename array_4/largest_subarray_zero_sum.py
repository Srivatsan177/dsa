if __name__ == "__main__":
    ls = [9, -3, 3, -1, 6, -5]
    sum_index = {}
    max_index = 0
    su = 0
    for idx, num in enumerate(ls):
        su += num
        if su == 0:
            max_index = idx + 1
        else:
            if su in sum_index:
                max_index = max(max_index, idx - sum_index[su])
            else:
                sum_index[su] = idx

    print(max_index)
