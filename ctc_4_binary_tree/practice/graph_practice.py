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

# input_graph = adjacency_dic
input_graph = graph_adjancency

visited = []

def visit_nodes(k):
    if k not in visited:
        visited.append(k)
        for n in input_graph[k]:
            visit_nodes(n)


for i in input_graph.keys():
    visit_nodes(i)

print(visited)

# [1, 2, 4, 6, 7, 3, 5]



