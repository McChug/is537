def diffWaysToCompute(
    expression: str, memo: dict[str, list[int]] | None = None
) -> list[int]:
    if expression not in memo:
        memo[expression] = []

    return memo[expression]


tests = ["2-1-1", "2*3-4*5"]
for test in tests:
    print(f"Solution: {test} = {diffWaysToCompute(test)}")
