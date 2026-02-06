def groupAnagrams(strs: list[str]):
    result: list[list[str]] = []

    current_index = 0
    addresses: dict[str, int] = {}

    for word in strs:
        ordered = "".join(sorted(word))

        if ordered in addresses:
            result[addresses[ordered]].append(word)
        else:
            result.append([word])
            addresses[ordered] = current_index
            current_index += 1

    return result


tests = [["ball", "labs", "slab"], ["rat", "cat", "tar", "anagram", "nagaram"]]
for test in tests:
    print(f"input: {test}\n output: {groupAnagrams(test)}")
