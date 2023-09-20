if __name__ == "__main__":
    ls = {3, 8, 4, 7, 6}
    max_cnt = 0
    for i in ls:
        cnt = 1
        num = i
        while num + 1 in ls:
            num += 1
            cnt += 1
        max_cnt = max(cnt, max_cnt)
    print(max_cnt)
