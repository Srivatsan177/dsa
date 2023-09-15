import math

if __name__ == "__main__":
    # Gap method optimal
    def swap(arr1, arr2, ind1, ind2):
        if arr1[ind1] > arr2[ind2]:
            arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]
    def sorted_arrays(arr1, arr2):
        n = len(arr1) + len(arr2)
        gap = (n // 2) + n % 2
        while gap > 0:
            left = 0
            right = left + gap
            while right < n:
                if left < len(arr1) and right >= len(arr1):
                    swap(arr1, arr2, left, right - len(arr1))

                elif left >= len(arr1):
                    swap(arr2, arr2, left - len(arr1), right - len(arr1))
                else:
                    swap(arr1, arr1, left, right)
                left += 1
                right += 1
            if gap == 1:
                break
            gap = (gap // 2) + gap % 2


    ls1, ls2 = [1, 4, 8, 10], [2, 3, 9]
    # print(sorted_arrays(ls1, ls2))
    sorted_arrays(ls1, ls2)
    print(ls1, ls2)
