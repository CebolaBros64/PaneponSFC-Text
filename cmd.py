import re

test_cmd = """#GAME NAME:		Game Name Goes Here

#BLOCK NAME:		This is a text block
#TYPE:			NORMAL
#METHOD:		RAW
#SCRIPT START:		$B0B0
#SCRIPT STOP:		$BEEF
#TABLE:			SHIFT-JIS.tbl
#END BLOCK

#BLOCK NAME:		This is another text block
#TYPE:			NORMAL
#METHOD:		RAW
#SCRIPT START:		$DEAD
#SCRIPT STOP:		$FFFF
#TABLE:			SHIFT-JIS.tbl
#END BLOCK"""


def convert(cmd):
    lines = re.findall(r"#(.+)", cmd)

    _dict = {}
    block = {}

    for i, line in enumerate(lines):  # For each line in the command list...
        if ":" in line:  # ...check for a colon.
            # If a colon is found:
            command_regex = re.match(r"^(.*):\s*(.*)$", line)  # Split string and get rid of whitespace

            if command_regex.group(1) == "GAME NAME":
                _dict[command_regex.group(1)] = command_regex.group(2)
                _dict['BLOCKS'] = []

            else:
                if command_regex.group(2).startswith("$"):  # If a hex value is found within the string...
                    # ...convert it into a proper integer.
                    arg = int(command_regex.group(2)[1:], 16)

                else:  # Otherwise, keep it as is.
                    arg = command_regex.group(2)

                block[command_regex.group(1)] = arg

        else:  # If a colon is not found: ("#END BLOCK")
            _dict['BLOCKS'].append(block.copy())

    return _dict


if __name__ == "__main__":
    from pprint import pprint
    pprint(convert(test_cmd), sort_dicts=False)
