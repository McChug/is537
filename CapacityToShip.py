from functools import reduce


def shipWithinDays(weights: list[int], days: int) -> int:
    def isPossible(capacity: int):
        accumulator = 0
        day = 1
        i = 0
        while i < len(weights):
            accumulator += weights[i]
            if accumulator > capacity:
                accumulator = 0
                day += 1
            else:
                i += 1

            if day > days:
                return False

        return True

    bottom = max(weights)
    capacity = reduce(lambda x, y: x + y, weights)

    while bottom < capacity:
        mid = (capacity + bottom) // 2
        if isPossible(mid):
            capacity = mid
        else:
            bottom = mid + 1

    return capacity


tests = [
    {"weights": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "days": 5, "expected": 15},
    {"weights": [3, 2, 2, 4, 1, 4], "days": 3, "expected": 6},
    {"weights": [1, 2, 3, 1, 1], "days": 4, "expected": 3},
]

for i, test in enumerate(tests, 1):
    result = shipWithinDays(test["weights"], test["days"])
    status = "PASS" if result == test["expected"] else "FAIL"
    print(
        f"Test {i}: [{status}] weights={test['weights']}, days={test['days']}\n=> {result} (expected {test['expected']})"
    )
