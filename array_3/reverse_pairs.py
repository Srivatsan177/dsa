if __name__ == "__main__":
    arr = [1,3,2,3,1]


    def merge(arr, a, mid, c, n):
        left = a
        right = mid + 1
        temp = []
        while left <= mid and right <= n:
            if arr[left] < arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= n:
            temp.append(arr[right])
            right += 1
        for i in range(a, c + 1):
            arr[i] = temp[i - a]

    def count_pairs(arr, a, mid, b):
        right = mid + 1
        cnt = 0
        for i in range(a, mid + 1):
            while right <= b and arr[i] > 2 * arr[right]:
                right += 1
            cnt += (right - (mid + 1))
        return cnt


    def merge_sort(arr, a, b, n):
        cnt = 0
        if a >= b:
            return cnt
        mid = (a + b) // 2
        cnt += merge_sort(arr, a, mid, n)
        cnt += merge_sort(arr, mid + 1, b, n)
        # Count pairs before merge
        cnt += count_pairs(arr, a, mid, b)
        merge(arr, a, mid, b, n)
        return cnt


    print(merge_sort(arr, 0, len(arr) - 1, len(arr) - 1))
    print(arr)
