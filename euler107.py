
MAX_EDGE = 2**32

def mst_weight(adj_matrix):
    num_nodes, tree_nodes, tree_weight = len(adj_matrix), [0], 0
    while len(tree_nodes) < num_nodes:
        source, dest, weight = min_edge(adj_matrix, tree_nodes)
        #print '(', source, dest, ') : ', weight, tree_nodes
        tree_nodes.append(dest)
        tree_weight += weight
        for i in xrange(num_nodes): adj_matrix[i][dest] = MAX_EDGE
    return tree_weight

def min_edge(adj_matrix, tree_nodes):
    dim, source, dest, min_weight = len(adj_matrix), -1, -1, MAX_EDGE
    for node in tree_nodes:
        def cost(x):
            if x in tree_nodes: return MAX_EDGE
            return adj_matrix[node][x]
        min_node = sorted(range(dim), key=cost)[0]
        edge_weight = cost(min_node)
        if edge_weight < min_weight:
            source, dest, min_weight = node, min_node, edge_weight
    return source, dest, min_weight

def graph_weight(adj_matrix):
    weight = 0
    for row in adj_matrix:
        for elem in row:
            if elem != MAX_EDGE:
                weight += elem
    return weight / 2

def read_edge(s):
    if s == '-':
        return MAX_EDGE
    return int(s)

with open('euler107_input.txt') as f:
    pe107 = [map(read_edge, line.strip().split(',')) for line in f.readlines()]

def euler107(adj_matrix=pe107):
    """http://projecteuler.net/index.php?section=problems&id=107

    Using network.txt (right click and 'Save Link/Target As...'), a 6K text
    file containing a network with forty vertices, and given in matrix form,
    find the maximum saving which can be achieved by removing redundant edges
    whilst ensuring that the network remains connected."""
    return graph_weight(adj_matrix) - mst_weight(adj_matrix)
