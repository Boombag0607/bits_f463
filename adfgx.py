'''ANANYA GAUTAM
    2020AAPS2096H
'''
# import math

def adfgx_encrypt(keyword, permutation, plain_text):
    adfgx = "ADFGX"

    poly_square = [list(permutation[i:i+5])
                   for i in range(0, len(permutation), 5)]

    col_key_map = {}
    for i in range(5):
        for j in range(5):
            col_key_map[poly_square[i][j]] = (i, j)

    codes = []
    for i in range(len(plain_text)):
        pos = col_key_map[plain_text[i]]
        codes.append(adfgx[pos[0]] + adfgx[pos[1]])

    code_list = ''.join(codes)

    dict = {}
    for i in range(len(keyword)):
        dict[i] = [keyword[i]]

    for i in range(len(code_list)):
        dict[i % len(keyword)].append(code_list[i])

    indices = [(keyword[i], i) for i in range(len(keyword))]
    indices = sorted(indices)

    ciphertext = ''
    for idx in indices:
        index = idx[1]
        for i in range(1, len(dict[index])):
            ciphertext += dict[index][i]

    return ciphertext

ciphertext = adfgx_encrypt("GERMAN", "PHQGMEAYNOFDXKRCVSZWBUTIL", "ATTACK")
print(ciphertext)
