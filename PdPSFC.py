from codecs import charmap_decode
import tbl2dict

binPath = 'test.bin'

charTBLPath = 'Tetris Attack.tbl'
codeTBLPath = 'Tetris Attack [Control Codes].tbl'

# Load binary containing text script
with open(binPath, 'rb') as f:
    binScript = f.read()

# Load character table file
with open(charTBLPath, 'r') as f:
    charTBLFile = f.read()
charTBLDict = tbl2dict.convert(charTBLFile)

# Load control code table file
with open(codeTBLPath, 'r') as f:
    codeTBLFile = f.read()
codeTBLDict = tbl2dict.convert(codeTBLFile)

# Merge both dictionaries together
TBLDict = charTBLDict.copy()

#print(TBLDict == charTBLDict) --> True
#TBLDict['peepee'] = 'poopoo'
#print(TBLDict == charTBLDict) --> False

TBLDict.update(codeTBLDict)

# Profit
#print(charmap_decode(binScript, 'strict', charTBLDict))
#print(charmap_decode(binScript, 'strict', codeTBLDict))
print(charmap_decode(binScript, 'strict', TBLDict))
with open("butt.txt", "w") as f:
    f.write(charmap_decode(binScript, 'strict', TBLDict)[0])