def removeOuterParentheses(s: str) -> str:
    s_list = list(s)
    counter = 0

    for i in range(len(s_list)):
        if s_list[i] == "(":
            counter += 1
            prep_delete = counter == 1
        else:
            counter -= 1
            prep_delete = counter == 0

        if prep_delete:
            s_list[i] = ""

    return "".join(s_list)


tests = ["(())()()", "((()))(())", "()()()"]
for test in tests:
    print(f"'{test}' -> '{removeOuterParentheses(test)}'")
