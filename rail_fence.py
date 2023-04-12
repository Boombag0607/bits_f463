def rail_char(square, ct):
    m = len(square)
    c = len(square[0])
    i = 0
    f = 0
    for j in range(c):
        square[i][j] = '$'
        if i == m - 1:
            f = 1
        elif i == 0:
            f = 0
        if f == 0:
            i += 1
        else:
            i -= 1

    k = 0
    for i in range(m):
        for j in range(c):
            if square[i][j] == '$':
                square[i][j] = ct[k]
                k += 1

    i = 0
    f = 0
    k = 0
    for j in range(c):
        ct = ct[:k] + square[i][j] + ct[k+1:]
        k += 1
        if i == m - 1:
            f = 1
        elif i == 0:
            f = 0
        if f == 0:
            i += 1
        else:
            i -= 1

    return ct


def rail_word(square, word):
    m = len(square)
    c = len(square[0])
    i = 0
    f = 0
    for j in range(c):
        square[i][j] = '$'
        if i == m - 1:
            f = 1
        elif i == 0:
            f = 0
        if f == 0:
            i += 1
        else:
            i -= 1

    k = 0
    for i in range(m):
        for j in range(c):
            if square[i][j] == '$':
                square[i][j] = word[k]
                k += 1

    i = 0
    f = 0
    k = 0
    for j in range(c):
        word[k] = square[i][j]
        k += 1
        if i == m - 1:
            f = 1
        elif i == 0:
            f = 0
        if f == 0:
            i += 1
        else:
            i -= 1

    return word


def remove(word, x, c, ct):
    l = len(x)
    i = 0
    while i < c:
        id = ct.find(x, i)
        s = ""
        if id == -1:
            s = ct[i:]
            i = c
        else:
            s = ct[i:id]
            i = id + l
        word.append(s)
    return word


if __name__ == "__main__":
    N, n, M, m = map(int, input().split())
    x, ct = input().split()
    c = len(ct)

    square = [[' ' for j in range(c)] for i in range(m)]
    for _ in range(M):
        ct = rail_char(square, ct)

    word = []
    word = remove(word, x, c, ct)
    w = len(word)

    square2 = [[' ' for j in range(w)] for i in range(n)]
    for _ in range(N):
        word = rail_word(square2, word)

    for i in range(w):
        print(word[i], end=" ")
