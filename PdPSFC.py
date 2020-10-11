from codecs import charmap_decode
import tbl2dict

binPath = 'test.bin'

# Load binary containing text script
with open(binPath, 'rb') as f:
    binScript = f.read()

filepath = 'Tetris Attack.tbl'

# Driver Code
with open(filepath, 'r', encoding='unicode_escape') as f:
    tblFile = f.read()

print(charmap_decode(binScript, 'strict', tbl2dict.convert(tblFile)))