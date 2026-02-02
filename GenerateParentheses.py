def generateParentheses(n: int):
    solutions: list[str] = []

    for i in range(2 ** (n * 2 - 1)):
        solution = "("
        open = 1
        close = 0

        while close <= open and open <= n:
            if len(solution) == n * 2:
                solutions.append(solution)
                break

            if i % 2 == 0:
                solution += ")"
                close += 1
            else:
                solution += "("
                open += 1

            i = i // 2

    return solutions


for test in range(1, 9):
    result = generateParentheses(test)
    print(f"n({test}): {len(result)} {result}")


# def convertBase10ToBase2(n: int):
#     base2 = ""
#     while n > 0:
#         if n % 2 == 1:
#             base2 = "1" + base2
#         else:
#             base2 = "0" + base2

#         n = n // 2

#     return base2


# for test in range(0, 9):
#     print(f"b({test}): {convertBase10ToBase2(test)}")
