import tbl
import cmd
import argparse

progName = 'PaneponSFC-Text'
progDesc = 'Text editing utilities for the SNES Panel de Pon games.'


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


def decode_binary(_bin, TBLShftCtrl, ctrlTBLDict):
    """Handles decoding of the binary into text"""
    argcount = 0
    i = 0
    _str = ''
    temp_tbl_dict = TBLDict.copy()
    try:
        while True:
            if _bin[i] in ctrlTBLDict:

                if _bin[i] == TBLShftCtrl:  # 0xC8 = <table>;
                    offset_tbl_dict = offset_encoding(charTBLDict, _bin[i + 1])
                    temp_tbl_dict = dict_merge(offset_tbl_dict, codeTBLDict)

            # print(_str)

            if argcount > 0:
                _str += f"<{_bin[i]:02x}>"
                argcount -= 1
            else:
                _str += temp_tbl_dict[_bin[i]]['value']

                if _bin[i] in temp_tbl_dict and 'args' in temp_tbl_dict[_bin[i]]:
                    argcount = temp_tbl_dict[_bin[i]]['args']

            i += 1
    except IndexError:
        # print("Reached end of file")
        return _str


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=progName, description=progDesc)
    parser.add_argument('bin',
                        metavar='rom',
                        nargs=1,
                        help='SNES Game ROM')
    parser.add_argument('cmd',
                        metavar='commands',
                        nargs=1,
                        help='Commands file')
    parser.add_argument('tbl',
                        metavar='char_tbl',
                        nargs=1,
                        help='Character table')
    parser.add_argument('tblc',
                        metavar='code_tbl',
                        nargs=1,
                        help='Control code table')

    args = parser.parse_args()

    # Load commands file
    with open(args.cmd[0], 'r') as f:
        commands = cmd.convert(f.read())

    # Load binary containing text script
    with open(args.bin[0], 'rb') as f:
        binScript = f.read()

    # Load character table file
    with open(args.tbl[0], 'r', encoding='UTF-8') as f:
        charTBLFile = f.read()
    charTBLDict = tbl.convert(charTBLFile)

    # Load control code table file
    with open(args.tblc[0], 'r', encoding='UTF-8') as f:
        codeTBLFile = f.read()
    codeTBLDict = tbl.convert(codeTBLFile)

    TBLDict = dict_merge(charTBLDict, codeTBLDict)

    # Find <table> in the control code table file and assign
    # it to variable tblCtrl
    # https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
    TBLCtrl = list(codeTBLDict.keys())[list(codeTBLDict.values()).index({'value':'<table>', 'args': 1})]

    # Profit
    with open("[butt].txt", "w", encoding='UTF-8') as f:
        for block in commands['BLOCKS']:
            # print(block)
            f.write(f'### {block["BLOCK NAME"]} ###\n')
            stOffset = block['SCRIPT START']
            edOffset = block['SCRIPT STOP']

            f.write(decode_binary(binScript[stOffset:edOffset], TBLCtrl, codeTBLDict))
