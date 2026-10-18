import pickle

with open("trie.pkl", "rb") as f:
    trie = pickle.load(f)

board = [input().lower() for i in range(5)]

words = set()

def dfs(i, j, node, word, used):
    if (i, j) in used:
        return
    node = node.get(board[i][j])
    if node is None:
        return
    word += board[i][j]
    if len(word) >= 4 and None in node:
        words.add(word)
    used.add((i, j))
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == dj == 0:
                continue
            if 0 <= i + di < 5 and 0 <= j + dj < 5:
                dfs(i + di, j + dj, node, word, used)
    used.remove((i, j))

for i in range(5):
    for j in range(5):
        dfs(i, j, trie, "", set())

for word in sorted(words, key=lambda x: -len(x)):
    print(word.upper())