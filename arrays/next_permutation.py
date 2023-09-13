if __name__ == "__main__":
    ls = [2, 3, 1, 4]
    i = len(ls) - 2
    while i>=0:
        if ls[i] <= ls[i + 1]:
            break
        i-=1
    if i == -1:
        print(reversed(ls))
        exit(0)
    j = len(ls) - 1
    while j > i:
        if ls[j] > ls[i]:
            ls[j], ls[i] = ls[i], ls[j]
            break
        j-=1
    ls[i + 1:] = reversed(ls[i + 1:])
    print(ls)