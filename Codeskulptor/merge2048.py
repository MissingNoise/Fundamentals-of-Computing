"""
Merge function for 2048 game.
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # Removes and adds zeros in new_list from list
    count = line.count(0)
    new_line = filter(lambda a: a != 0, line)
    for number in range(count):
        new_line.append(0)
    # iterates through new_line and merges pairs
    for number in range(len(line)-1):
        print number
        print new_line
        if new_line[number] is 0:
            continue
        if new_line[number] == new_line[number + 1]:
            new_line.pop(number + 1)
            new_line[number] = new_line[number] * 2
            new_line.append(0)
    return new_line