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
    
    #print(_dict)
    #print(offsetDict)
    return offsetDict
    
def dict_merge(a, b):
    '''Merges two dictionaries together'''
    finalDict = a.copy()
    finalDict.update(b)
    return finalDict

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

TBLDict = dict_merge(charTBLDict, codeTBLDict)

# Profit
#print(charmap_decode(binScript, 'strict', charTBLDict))
#print(charmap_decode(binScript, 'strict', codeTBLDict)) 
#print(charmap_decode(binScript, 'strict', TBLDict))

i = 0
_str = ''
tempTBLDict = TBLDict.copy()
try:
    while True:
        if binScript[i] == 0xC8: # 0xC8 = <table>;
            offsetTBLDict = offset_encoding(charTBLDict, binScript[i+1])
            tempTBLDict = dict_merge(offsetTBLDict, codeTBLDict)
    
        #print(_str)
        _str += tempTBLDict[binScript[i]]
        i += 1
except IndexError:
    print("Reached end of file")
    print(_str)
   
with open("[butt].txt", "w") as f:
    f.write(_str)
    
#offset_encoding(TBLDict, 1)