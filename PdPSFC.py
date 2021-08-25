import tbl

binPath = 'test.bin'
charTBLPath = 'Tetris Attack.tbl'
codeTBLPath = 'Tetris Attack [Control Codes].tbl'


def offset_encoding(_dict, n):
    """Offsets the keys of a dictionary by (entry-(n*16))"""
    offset_dict = _dict.copy()
    offset = n * 16
    for entry in _dict:
        offset_dict[entry - offset] = _dict[entry]

    return offset_dict


def dict_merge(a, b):
    """Merges two dictionaries together"""
    final_dict = a.copy()
    final_dict.update(b)
    return final_dict


def decode_binary(_bin):
    """Handles decoding of the binary into text"""
    i = 0
    _str = ''
    temp_tbl_dict = TBLDict.copy()
    try:
        while True:
            if _bin[i] == 0xC8:  # 0xC8 = <table>;
                offset_tbl_dict = offset_encoding(charTBLDict, _bin[i + 1])
                temp_tbl_dict = dict_merge(offset_tbl_dict, codeTBLDict)

            # print(_str)
            _str += temp_tbl_dict[_bin[i]]
            i += 1
    except IndexError:
        # print("Reached end of file")
        return _str


if __name__ == "__main__":
    # Load binary containing text script
    with open(binPath, 'rb') as f:
        binScript = f.read()

    # Load character table file
    with open(charTBLPath, 'r', encoding='UTF-8') as f:
        charTBLFile = f.read()
    charTBLDict = tbl.convert(charTBLFile)

    # Load control code table file
    with open(codeTBLPath, 'r') as f:
        codeTBLFile = f.read()
    codeTBLDict = tbl.convert(codeTBLFile)

    TBLDict = dict_merge(charTBLDict, codeTBLDict)

    # Profit
    with open("[butt].txt", "w", encoding='UTF-8') as f:
        f.write(decode_binary(binScript))
