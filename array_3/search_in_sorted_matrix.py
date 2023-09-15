if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    num_to_search = 16
    row_start, row_end = 0, len(matrix) - 1
    ind = -1, -1
    while row_start <= row_end:
        mid = (row_start + row_end) // 2
        if matrix[mid][0] > num_to_search:
            row_end = mid - 1
        elif matrix[mid][0] < num_to_search:
            row_start = mid + 1
        else:
            ind = mid, 0
            break
    print(row_start, row_end)
    row_to_search = min(row_start, row_end)
    col_start, col_end = 0, len(matrix[0])
    if row_to_search == len(matrix):
        exit()
    while col_start <= col_end:
        print(col_start, col_end)
        mid = (col_start + col_end) // 2
        if matrix[row_to_search][mid] > num_to_search:
            col_end = mid - 1
        elif matrix[row_to_search][mid] < num_to_search:
            col_start = mid + 1
        else:
            ind = row_to_search, mid
            break
    print(ind)