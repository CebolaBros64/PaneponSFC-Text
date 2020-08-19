file = '!Tabela de Caracteres - Tetris Attack.tbl'

test = "0H0ò+(5(ò72ò6+2:ò<28ý+2:ò72ò3/$<ò7+,6ò*$0(Gý"

def altElement(a):
    return a[::2]

with open(file, 'r') as f:
    tblDict = f.read().replace('=', '\n').split('\n')
    x = iter(tblDict)
    for keyname in altElement(tblDict):
        tblDict[bytes.fromhex(keyname)] = tblDict.pop(keyname)
    b = dict(zip(x, x))

print(test)
print(b)
print(test.translate(b))