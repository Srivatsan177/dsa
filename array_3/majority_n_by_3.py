if __name__ == "__main__":
    nums = [11, 33, 33, 11, 33, 11]
    el1, el2 = nums[0], nums[1]
    cnt1, cnt2 = 0, 0
    for num in nums:
        if cnt1 == 0 and el2 != num:
            cnt1 = 1
            el1 = num
        elif cnt2 == 0 and el1 != num:
            cnt2 = 1
            el1 =num
        elif el1 == num:
            cnt1 += 1
        elif el2 == num:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    cnt1, cnt2 = 0, 0
    for num in nums:
        if el1 == num:
            cnt1 += 1
        if el2 == num:
            cnt2 += 1
    print(el1, cnt1, el2, cnt2)
