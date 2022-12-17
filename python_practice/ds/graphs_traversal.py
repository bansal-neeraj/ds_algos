# graphs traversal , depth first and breadth first

#TODO BFS

def dfs(n,g,visited):
    if n not in visited:
        print(n,end=',')
        visited.add(n)
        for j in g[n]:
            if j not in visited:
                dfs(j,g,visited)


def main():
    g = {
        0:[1,4,5],
        1:[3,4],
        2:[1],
        3:[2,4],
        4:[],
        5:[],
    }

    visited = set()
    for k in g.keys():
        dfs(k,g,visited)


if __name__ == '__main__':
    main()


