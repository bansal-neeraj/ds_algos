# GRAPH DFS

adjacency_dic = {
    0:[1,4,5],
    1:[3,4],
    2:[],
    3:[2,4],
    4:[],
    5:[],

}

graph_adjancency = {
    1:[2],
    2:[1,4,7],
    3:[5],
    4:[2,6],
    5:[3],
    6:[4,7],
    7:[2,6]
}


already_visited = []

# graph depth first traversal - working


def main(g):
    for key in g.keys():
        visit_node(key,g)


def visit_node(k,graph):
    if k not in already_visited:
        already_visited.append(k)
        for adj_node in graph[k]:
            visit_node(adj_node,graph)


if __name__ == '__main__':
    # main(adjacency_dic)
    main(graph_adjancency)
    print(already_visited)

