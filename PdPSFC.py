from codecs import charmap_decode
import tbl2dict

binPath = 'test.bin'

charTBLPath = 'Tetris Attack.tbl'

# Load binary containing text script
with open(binPath, 'rb') as f:
    binScript = f.read()

# Load character table file
with open(charTBLPath, 'r', encoding='unicode_escape') as f:
    charTBLFile = f.read()

print(charmap_decode(binScript, 'strict', tbl2dict.convert(charTBLFile)))