from codecs import charmap_decode
import tbl2dict

with open("test.bin", 'rb') as f:
    test = f.read()

filepath = 'Tetris Attack.tbl'

# Driver Code
with open(filepath, 'r', encoding='unicode_escape') as f:
    tblFile = f.read()

print(charmap_decode(test, 'strict', tbl2dict.convert(tblFile)))