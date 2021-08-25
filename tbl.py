import re

def list2dictConvert(_list):
    ''' method 2 from this page https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/ '''
    it = iter(_list)
    res_dct = dict(zip(it, it))
    return res_dct

def convert(tbl):
    # input regex expression and table file in https://regex101.com/ for explanation
    tbl2list = re.findall(r"(.*)=(.*)", tbl)

    finalDict = {}

    for entry in tbl2list:
        # convert to dict
        entry2dict = list2dictConvert(entry)
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
            # replace \\n by \n (pretty sure this is not good code practice but hey, it should work)
            entry2dict[int(entry[0], 16)] = entry2dict[int(entry[0], 16)].replace('\\n', '\n')
            #pass
        
        # add entry to final dictionary
        finalDict.update(entry2dict)
        
    #print(finalDict)
    return finalDict
