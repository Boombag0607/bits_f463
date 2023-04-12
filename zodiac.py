''' ANANYA GAUTAM
    2020AAPS2096H'''

import math

def zodiac_decrypt(key, cipher_text):
    # calculate number of rows
    n_rows = math.ceil(len(cipher_text) / key)
    plain_text = ""
    idx = 0
    # add_idx = 0
    matrix = [['z' for j in range(key)] for i in range(n_rows)]
    print(matrix)
    
    for i in range(len(cipher_text)):
        print(cipher_text[i], )
        if ((i)%n_rows):
            idx = (idx + 2)%key
        else:
            idx = matrix[0].index('z')
        matrix[i % n_rows][idx] = cipher_text[i]
        

    print(matrix)
    print(cipher_text)
    # plain_text = ''.join([''.join(row) for row in matrix])
    for row in matrix:
        for ch in row:
            if ch != 'z':
                plain_text += ch
    return plain_text


print(zodiac_decrypt(3, "WBDAEYTRO"))