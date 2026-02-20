def string(a: list[int], b: int):
    c = 0
    d = len(a) - 1

    count = 0

    while c <= d:
        count += 1
        e = (c + d) // 2
        print(count, e)

        if a[e] == b:
            return e
        elif a[e] > b:
            d = e - 1
        else:
            c = e + 1

    return -1


print(string([1, 2, 3, 4, 7, 8, 10, 12], 7))
