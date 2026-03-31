def searchMatrix(self, matrix, target):
    m = len(matrix) - 1
    n = len(matrix[0]) - 1

    bottom = 0
    top = m

    while bottom < top:
        mid = (bottom + top) // 2
        print(bottom, top, mid)

        if matrix[mid][0] == target or matrix[mid][n] == target:
            return True
        elif matrix[mid][0] > target:
            top = mid - 1
        elif matrix[mid][n] < target:
            bottom = mid + 1
        else:
            bottom = mid
            break

    row = matrix[bottom]
    print(row)
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid)

        if row[mid] == target:
            return True
        elif row[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False
        