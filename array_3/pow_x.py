if __name__ == "__main__":
    # Binary exponentiation
    num = 8
    k = 3
    ans = 1
    while k != 0:
        if k % 2 == 0:
            num = num * num
            k /= 2
        else:
            ans = ans * num
            k -= 1
    print(ans)
