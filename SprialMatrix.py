def spiralOrder(matrix):
    result = []

    m = len(matrix)
    n = len(matrix[0])

    offset = {"top": 0, "right": 0, "bottom": 0, "left": 0}
    
    while True:
        for i in range(offset["left"], n - offset["right"]):
            result.append(matrix[0 + offset["top"]][i])
        offset["top"] += 1

        if offset["top"] + offset["bottom"] == m:
            break

        for i in range(offset["top"], m - offset["bottom"]):
            result.append(matrix[i][n - offset["right"] - 1])
        offset["right"] += 1

        if offset["right"] + offset["left"] == n:
            break

        for i in range(n - offset["right"] - 1, offset["left"] - 1, -1):
            result.append(matrix[m - offset["bottom"] - 1][i])
        offset["bottom"] += 1

        if offset["top"] + offset["bottom"] == m:
            break

        for i in range(m - offset["bottom"] - 1, offset["top"] - 1, -1):
            result.append(matrix[i][0 + offset["left"]])
        offset["left"] += 1

        if offset["right"] + offset["left"] == n:
            break

    return result
