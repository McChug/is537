def factorial(n: int):
    if n <= 1:
        return 1
    result = n * factorial(n - 1)
    return result

    # result = 1
    # for i in range(1, n + 1):
    #     result = result * i

    # return result


print(factorial(5))
