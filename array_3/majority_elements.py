if __name__ == "__main__":
    # Moore voting
    nums = [4, 4, 2, 4, 3, 4, 4, 3, 2, 4]
    cnt, curr_element = 0, nums[0]
    for num in nums:
        if cnt == 0:
            curr_element = num
            cnt = 1
        elif curr_element == num:
            cnt += 1
        else:
            cnt -= 1
    cnt = 0
    for num in nums:
        if num == curr_element:
            cnt += 1
    print(cnt >= len(nums) // 2, curr_element)
