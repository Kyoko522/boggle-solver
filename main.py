def is_valid(board, word, row, col, visited):
    if 0 <= row < len(board) and 0 <= col < len(board[0]) and not visited[row][col] and board[row][col] == word[0]:
        return True
    return False

def dfs(board, word, row, col, index, visited, path):
    if index == len(word):
        return path

    if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or visited[row][col] or board[row][col] != word[index]:
        return None

    visited[row][col] = True
    path.append((row + 1, col + 1))  # Adjust to 1-based indexing

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        result = dfs(board, word, row + dr, col + dc, index + 1, visited, path)
        if result is not None:
            return result

    visited[row][col] = False
    path.pop()
    return None

def check_word(board, word):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            path = dfs(board, word, row, col, 0, visited, [])
            if path:
                return path
    return None

def check(board, words):
    found_words = {}
    for word in words:
        path = check_word(board, word)
        if path:
            found_words[word] = path
    return found_words

if __name__ == '__main__':
    board = [
        ["a", "q", "o", "a", "u", "s", "i", "e", "a", "r", "t", "u", "e", "l", "r", "o"],
        ["l", "n", "u", "c", "r", "s", "u", "r", "s", "d", "i", "r", "z", "t", "o", "m"],
        ["q", "c", "a", "c", "l", "o", "d", "q", "t", "y", "i", "y", "c", "r", "a", "v"],
        ["d", "e", "s", "m", "p", "a", "n", "t", "s", "e", "m", "t", "d", "e", "s", "t"],
        ["i", "t", "q", "e", "e", "t", "r", "o", "a", "b", "n", "o", "a", "h", "n", "a"],
        ["d", "n", "e", "c", "r", "p", "o", "l", "v", "n", "e", "z", "s", "m", "i", "m"],
        ["p", "l", "o", "r", "s", "s", "i", "s", "t", "t", "u", "g", "c", "t", "o", "g"],
        ["b", "a", "l", "v", "r", "i", "d", "n", "m", "o", "l", "s", "b", "a", "n", "v"],
        ["o", "j", "n", "a", "o", "y", "l", "o", "i", "f", "g", "a", "e", "s", "z", "a"],
        ["n", "m", "e", "l", "l", "s", "e", "n", "n", "p", "i", "r", "m", "c", "i", "n"],
        ["l", "s", "a", "l", "n", "m", "u", "c", "r", "l", "a", "r", "m", "b", "a", "m"],
        ["p", "e", "m", "h", "z", "a", "r", "n", "y", "e", "c", "l", "p", "e", "s", "r"],
        ["i", "s", "n", "o", "u", "s", "t", "a", "o", "s", "c", "e", "i", "c", "i", "o"],
        ["r", "d", "e", "a", "s", "d", "o", "l", "d", "l", "e", "s", "r", "l", "o", "m"],
        ["p", "g", "u", "r", "l", "v", "o", "c", "l", "s", "e", "r", "b", "m", "e", "m"],
        ["s", "i", "a", "s", "n", "a", "p", "r", "m", "u", "r", "h", "t", "o", "s", "c"]
    ]

    words = []
    with open("word_list_3000.txt", "r") as file:
        for line in file:
            words.append(line.strip())

    found_words = check(board, words)

    for word, path in found_words.items():
        print(f"Word: {word}")
        for point in path:
            print(f"    Point: {point}")
        print()  # Add an empty line for better separation between words