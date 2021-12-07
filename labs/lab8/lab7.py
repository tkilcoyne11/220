def encode(s, key):
    acc = ""
    for c in s:
        acc += chr((ord(c) - 97 + key) % 26 + 97)
    return acc


def encode_better(s, k):
    acc = ""
    for i in range(len(s)):
        c = ord(s[i])
        key = k[i]
        key = ord(key) - 97
        c = c + key
        new_c = chr(c)
        acc += new_c
    return acc
