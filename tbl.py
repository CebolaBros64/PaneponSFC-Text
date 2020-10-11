import re
from codecs import charmap_decode

with open("test.bin", 'rb') as f:
    test = f.read()

filepath = 'Tetris Attack.tbl'

def Convert(a):
    ''' method 2 from this page https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/ '''
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

# Driver Code
with open(filepath, 'r', encoding='unicode_escape') as f:
    tblFile = f.read()

tbl2list = re.findall(r"(.*)=(.*)", tblFile) # input regex expression and table file in https://regex101.com/ for explanation

#print(tbl2list)
#print(tbl2list[0][0])

list2dict = {}

for entry in tbl2list:
    # convert to dict
    entry2dict = Convert(entry)
    #print(entry2dict)
    
    # check if it's a control code with arguments
    #print(re.search(r"^\$(.*)", entry[0]))
    ctrlcodeRegex = re.search(r"^\$(.*)", entry[0])
    
    if ctrlcodeRegex != None:
        # Key manipulation
        # remove the '$' and transform hex in str to byte
        #print(ctrlcodeRegex[1])
        #print(entry[0])
        #print(entry2dict[entry[0]])
        entry2dict[int(ctrlcodeRegex[1], 16)] = entry2dict[entry[0]] # the regex removes the '$', the bytes.fromhex takes the str containing the hex value and turns into a byte
        entry2dict.pop(entry[0])
       
        #print(entry[0])
       
        # Value manipulation
        # this would be used to remove the argmument number at the end (",1", ",2", etc), but there's no need to right now
        #print(re.findall(r"(.*),(\d$)", entry[1]))
        #print(ctrlcodeRegex)
        # replace \\n by \n (pretty sure this is not good code practice but hey, it should work)
        entry2dict[int(ctrlcodeRegex[1], 16)] = entry2dict[int(ctrlcodeRegex[1], 16)].replace('\\n', '\n')
        #pass
    else:
        #print(entry[0])
        #entry2dict[bytes.fromhex(entry[0])] = entry2dict[entry[0]] # same as before
        entry2dict[int(entry[0], 16)] = entry2dict[entry[0]] # same as before
        entry2dict.pop(entry[0])
        #pass
    
    # add entry to final dictionary
    list2dict.update(entry2dict)
    
#print(list2dict)
#print(test[0])
#print(test[0] == 0xf5) --> true
#print(test[0] == '0xf5') --> false
#list2dict = {
#    0xf5 : 'clear'
#}
print(charmap_decode(test, 'strict', list2dict))