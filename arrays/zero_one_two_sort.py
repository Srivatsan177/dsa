if __name__ == "__main__":
    ls = [2, 0, 2, 1, 1, 0]
    zero_ind = 0
    two_ind = len(ls) - 1
    while True:
        if ls[zero_ind] == 0:
            zero_ind += 1
        else:
            break
    while True:
        if ls[two_ind] == 2:
            two_ind -= 1
        else:
            break
    ind = zero_ind + 1
    while ind < two_ind:
        if ls[ind] == 0:
            ls[ind], ls[zero_ind] = ls[zero_ind], ls[ind]
            zero_ind += 1
            while ls[zero_ind] == 0: zero_ind += 1
            ind = zero_ind
            continue
        if ls[ind] == 2:
            ls[ind], ls[two_ind] = ls[two_ind], ls[ind]
            two_ind -= 1
            while ls[two_ind] == 2: two_ind -=1
            continue
        ind += 1
    print(ls)
