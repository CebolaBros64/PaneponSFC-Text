from codecs import charmap_decode
import tbl2dict

binPath = 'test.bin'

charTBLPath = 'Tetris Attack.tbl'
codeTBLPath = 'Tetris Attack [Control Codes].tbl'

def offset_encoding(_dict, n):
    offsetDict = _dict.copy()
    offset = n * 16
    for entry in _dict:
        #print(entry)
        offsetDict[entry-offset] = _dict[entry]
    
    print(_dict)
    print(offsetDict)
    #return offsetDict

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
TBLDict.update(codeTBLDict)

# Profit
#print(charmap_decode(binScript, 'strict', charTBLDict))
#print(charmap_decode(binScript, 'strict', codeTBLDict)) 
#print(charmap_decode(binScript, 'strict', TBLDict))
#with open("[butt].txt", "w") as f:
#    f.write(charmap_decode(binScript, 'strict', TBLDict)[0])

#i = 0
#_str = ''
#try:
#    while True:
#    if binScript[i]
#    
#        print(_str)
#        _str += TBLDict[binScript[i]]
#        i += 1
#except IndexError:
#    print("Reached end of file")
#    print(_str)
#   

offset_encoding(TBLDict, 1)