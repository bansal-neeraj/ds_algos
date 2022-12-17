# route between nodes
from collections import deque

adjacency_dic = {
    0:[1],
    1:[2],
    2:[0,3],
    3:[2],
    4:[6],
    5:[4],
    6:[5]
}

visited_nodes = {}


def find_route(start,end):
    """ depth first traversal - Graph"""
    visited_nodes[start] = True
    if start == end:
        return True
    else:
        for i in adjacency_dic[start]:
            if i not in visited_nodes:
                found = find_route(i,end)
                if found:
                    return True
        return False


print(find_route(5,3))

visited_nodes_bfs = {}


def find_route_bfs(start,end):
    """ breadth first search - graph"""
    d = deque()
    d.append(start)
    while d:
        n = d.popleft()
        visited_nodes_bfs[n] = True
        if n == end:
            return True
        else:
            if end in adjacency_dic[n]:
                return True
            else:
                for i in adjacency_dic[n]:
                    if i not in visited_nodes_bfs:
                        d.append(i)

    return False


print('bfs '*50)
print(find_route_bfs(5,1))

