def diffWaysToCompute(
    expression: str, memo: dict[str, list[int]] | None = None
) -> list[int]:
    print(memo)
    if len(expression) <= 1:
        return [int(expression)]

    if not memo:
        memo = {}

    operand = int(expression[0])
    operator = expression[1]

    if expression not in memo:
        memo[expression] = []

        result = diffWaysToCompute(expression[2:], memo)
        print(f"matched {operator}")
        match operator:
            case "+":
                for r in result:
                    memo[expression].append(operand + r)
            case "-":
                for r in result:
                    memo[expression].append(operand + r)
            case "*":
                for r in result:
                    memo[expression].append(operand + r)
            case _:
                raise ValueError(
                    "Invalid expression. Operand not found where expected."
                )

    return memo[expression]


tests = ["2-1-1", "2*3-4*5"]
for test in tests:
    print(f"Solution: {test} = {diffWaysToCompute(test)}")
