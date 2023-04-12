''' ANANYA GAUTAM
    2020AAPS2096H
'''


def generate_checkerboard(key_permutation, digits):
    checkerboard = {0: []}
    row = []

    # make first row
    for i in range(10):
        checkerboard[0].append(i)
        if (i != digits[0] and i != digits[1]):
            row.append(key_permutation[0])
            key_permutation = key_permutation[1:]
            # print(key_permutation)
        else:
            row.append('0')

    checkerboard[1] = row
    # add digit rows
    for j in range(2):
        row = []
        for i in range(10):
            if (len(key_permutation) > 0):
                row.append(key_permutation[0])
                key_permutation = key_permutation[1:]
                # print(key_permutation)
            else:
                row.append('0')
        checkerboard[digits[j]] = row

    return checkerboard


def straddle_checkerboard_decrypt(key_permutation, digits, ciphertext):
    checkerboard = generate_checkerboard(key_permutation, digits)
    plaintext = ""
    ch_int = 0
    i = 0
    while i < len(ciphertext):
        ch_int = int(ciphertext[i])
        if (ch_int != digits[0] and ch_int != digits[1]):
            plaintext += checkerboard[1][ch_int]
        elif (ch_int == digits[0]):
            i += 1
            ch_int = int(ciphertext[i])
            plaintext += checkerboard[digits[0]][ch_int]

        elif (ch_int == digits[1]):
            i += 1
            ch_int = int(ciphertext[i])
            plaintext += checkerboard[digits[1]][ch_int]
        i += 1
    return plaintext


print(straddle_checkerboard_decrypt("FKMCPDYEHBIGQROSAZLUTJNWV",
      [3, 7], "690974672309938377275387070360723094383772709"))
