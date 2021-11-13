import re


def convert_list2dict(_list):
    """ method 2 from this page https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/ """
    it = iter(_list)
    res_dct = dict(zip(it, it))
    return res_dct


def convert(tbl):
    # input regex expression and table file in https://regex101.com/ for explanation
    tbl2list = re.findall(r"(.*)=(.*)", tbl)

    final_dict = {}

    for entry in tbl2list:
        # convert to dict
        entry2dict = convert_list2dict(entry)

        # check if it's a control code that uses arguments
        ctrlcode_regex = re.search(r"^\$(.*)", entry[0])

        if ctrlcode_regex is not None:
            ctrlarg_regex = re.findall(r"(.*),(\d$)", entry[1])[0]

            # Key manipulation
            # remove the '$' and transform hex in str to byte
            # the regex removes the '$', the bytes.fromhex takes the str containing the hex value and turns into a byte
            entry2dict[int(ctrlcode_regex[1], 16)] = entry2dict[entry[0]]
            entry2dict.pop(entry[0])

            # Value manipulation
            # remove the argmument number at the end (",1", ",2", etc)
            # print(ctrlarg_regex)
            entry2dict[int(ctrlcode_regex[1], 16)] = {
                'value': ctrlarg_regex[0],
                'args': int(ctrlarg_regex[1])
                                                      }

            # replace \\n by \n (not sure if this is the proper way to do it but hey, it works)
            entry2dict[int(ctrlcode_regex[1], 16)] = {
                'value': entry2dict[int(ctrlcode_regex[1], 16)]['value'].replace('\\n', '\n'),
                'args': int(ctrlarg_regex[1])
                                                      }
        else:
            entry2dict[int(entry[0], 16)] = entry2dict[entry[0]]  # same as before
            entry2dict.pop(entry[0])

            entry2dict[int(entry[0], 16)] = {'value': entry2dict[int(entry[0], 16)].replace('\\n', '\n')}

        # add entry to final dictionary
        final_dict.update(entry2dict)

    return final_dict


if __name__ == "__main__":
    with open('Panel de Pon [Control Codes].tbl', 'r', encoding='UTF-8') as f:
        codeTBLFile = f.read()
    codeTBLDict = convert(codeTBLFile)

    print(codeTBLDict)
