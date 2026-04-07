def exist(board, word):
    m = len(board)
    n = len(board[0])

    def wordSearch(i, j, depth, current_path=None):
        if current_path == None:
            current_path = set()

        if board[i][j] != word[depth]:
            return False

        if depth >= len(word) - 1:
            return True

        current_path.add((i, j))

        adjacents = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        valid_adjacents = [(y, x) for (y, x) in adjacents if 0 <= y and y < m and 0 <= x and x < n]
        for y, x in valid_adjacents:
            if (y, x) not in current_path:
                if wordSearch(y, x, depth + 1, current_path):
                    return True

        current_path.remove((i, j))

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if wordSearch(i, j, 0):
                    return True
    
    return False

test_board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
test_word = "ABCESEEEFS"
print(exist(test_board, test_word))