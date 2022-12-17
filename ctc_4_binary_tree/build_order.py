# ctci 4.7 solution

graph3 ={
    'a':['d'],
    'b':['d'],
    'c':[],
    'd':['c'],
    'e':[],
    'f':['b','a']
}

graph_ctci ={
    'b':['a','e','h'],
    'd':['g'],
    'c':['a'],
    'f':['c','a','b'],
    'a':['e'],
    'e':[],
    'h':[],
    'g':[]
}

visited_nodes_ctci = []
build_order = []


def visit_node_ctci(k):
    if k not in visited_nodes_ctci:
        visited_nodes_ctci.append(k)
        for adj_node in graph3[k]:
            visit_node_ctci(adj_node)
        build_order.insert(0,k)


for key in graph3.keys():
    visit_node_ctci(key)

print(build_order)



