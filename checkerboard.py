''' ANANYA GAUTAM
    2020AAPS2096H
    This file is for straddle checkerboard decryption (straddle.py)
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
            print(key_permutation)
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
                print(key_permutation)
            else:
                row.append('0')
        checkerboard[digits[j]] = row
    
    return checkerboard

print(generate_checkerboard("FKMCPDYEHBIGQROSAZLUTJNWVX", (3,7)))