if __name__ == "__main__":
    def merge(ls, left, mid, right):
        temp = []
        x, y = left, mid + 1
        cnt = 0
        while x <= mid and y <= right:
            if ls[x] <= ls[y]:
                temp.append(ls[x])
                x += 1
            else:
                temp.append(ls[y])
                cnt += (mid - x) + 1
                y += 1
        while x <= mid:
            temp.append(ls[x])
            x += 1
        while y <= right:
            temp.append(ls[y])
            y += 1
        for i in range(left, right + 1):
            ls[i] = temp[i - left]
        return cnt


    def merge_sort(ls, left, right):
        cnt = 0
        if left >= right:
            return cnt
        mid = (left + right) // 2
        cnt += merge_sort(ls, left, mid)
        cnt += merge_sort(ls, mid + 1, right)
        cnt += merge(ls, left, mid, right)
        return cnt


    ls = [5, 3, 2, 1, 4]
    inv = merge_sort(ls, 0, len(ls) - 1)
    print(inv)
