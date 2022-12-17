"""
queens attack - backtracking
"""

grid_size = 4


def total_queens(r,n,under_attack,count):
    if r >= n:
        return count + 1
    else:
        for col in range(n):
            if (r, col) not in under_attack:
                attack_locs = calculate_attack(r, col,n)
                count = total_queens(r+1,n,under_attack + attack_locs,count)

    return count


def calculate_attack(r,c,n):
    col_attack = []
    start_row = r
    start_col = c
    while start_row + 1 < n:
        col_attack.append((start_row+1,start_col))
        start_row += 1

    right_diagonal = []
    start_row = r
    start_col = c
    while start_row+1 < n and start_col + 1 < n:
        right_diagonal.append((start_row+1,start_col+1))
        start_row += 1
        start_col += 1

    left_diagonal = []
    start_row = r
    start_col = c
    while start_row + 1 < n and start_col - 1 > -1:
        left_diagonal.append((start_row+1, start_col - 1))
        start_row += 1
        start_col -= 1

    return col_attack + right_diagonal + left_diagonal


x = total_queens(0,grid_size,[],0)
print(x)

