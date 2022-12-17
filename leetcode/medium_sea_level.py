# leetcode Q 417
def find_path_altlantic(n, g, visited):
    if n not in visited:
        # print(n,end=',')
        r = n[0]
        c = n[1]
        if r == rows - 1 or c == cols - 1:
            return True
        visited.add(n)
        for j in g[n]:
            if j not in visited:
                find_path_altlantic(j, g, visited)


def find_path_pacific(n, g, visited):
    if n not in visited:
        # print(n,end=',')
        r = n[0]
        c = n[1]
        if r == 0 or c == 0:
            return True
        visited.add(n)
        for j in g[n]:
            if j not in visited:
                x = find_path_pacific(j, g, visited)
        return x

def find_neighbours(r, c):
    n_list = []
    ele = heights[r][c]
    if r - 1 != -1 and heights[r - 1][c] <= ele:
        n_list.append((r - 1, c))
    if r + 1 <= rows - 1 and heights[r + 1][c] <= ele:
        n_list.append((r + 1, c))
    if c - 1 != -1 and heights[r][c - 1] <= ele:
        n_list.append((r, c - 1))
    if c + 1 <= cols - 1 and heights[r][c + 1] <= ele:
        n_list.append((r, c + 1))

    return n_list


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]

rows = len(heights)
cols = len(heights[0])

my_dict = {}
for r in range(rows):
    for c in range(cols):
        if (r == 0 and c == cols - 1) or (r == rows - 1 and c == 0):
            continue
        else:
            my_dict[(r, c)] = find_neighbours(r, c)

for k, v in my_dict.items():
    print(k, v)

result = []
for k in my_dict.keys():
    visited = set()
    altantic = find_path_altlantic(k,my_dict,visited)
    # print(k,altantic,'atlantic')
    visited.clear()
    pacific = find_path_pacific(k,my_dict,visited)
    print(k,pacific,'pacific')
    if altantic and pacific:
        result.append(k)


print(result)
