def getRow(rowIndex: int) -> list[int]:
    my_dict = {}
    cols = rowIndex + 1
    new_row = []
    for c in range(1, cols - 1):
        new_row.append(getnum(rowIndex - 1, c - 1,my_dict) + getnum(rowIndex - 1, c,my_dict))

    return [1] + new_row + [1]


def getnum(r, c,my_dict):
    if r == 0 or c == 0 or r == c:
        return 1
    else:
        if (r - 1, c - 1) not in my_dict:
            my_dict[(r - 1, c - 1)] = getnum(r - 1, c - 1,my_dict)
        if (r - 1, c) not in my_dict:
            my_dict[(r - 1, c)] = getnum(r - 1, c,my_dict)
        return my_dict[(r - 1, c - 1)] + my_dict[(r - 1, c)]


print(getRow(6))