import tbl
from pprint import pprint


def print_tbl(_dict):
    """Takes a Python dictionary and prints it as a Thingy table file"""
    for i in _dict:
        print(f"{i:0{2}x}={_dict[i]['value']}")  # https://stackoverflow.com/a/12638477


def pdp_workaround(og_dict, revert=False):
    """Panel de Pon has some weird behavior in how the tables are offset.

    In some occasions, the <table> control code may offset the charset by (argument * 8) instead of the expected
    (argument * 16). I have yet to understand why this happens.

    This function offsets characters in the table in a way that works around this quirk. It can also do the reverse of
    said operation."""

    new_dict = dict()
    offset_value = 0

    for index in og_dict:

        if index % 16 == 0 and index != 0:  # If entry index diviseable by 16 and not zero
            offset_value += 16

        if revert:
            new_dict[index - offset_value] = og_dict[index]
        else:
            new_dict[index + offset_value] = og_dict[index]

    return new_dict


if __name__ == "__main__":
    with open('Panel de Pon.tbl', 'r', encoding='UTF-8') as f:
        codeTBLFile = f.read()
    codeTBLDict = tbl.convert(codeTBLFile)

    fixed_table = pdp_workaround(codeTBLDict, revert=True)

    # pprint(codeTBLDict)
    # pprint(fixed_table)

    print_tbl(fixed_table)

