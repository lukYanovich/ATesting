import networkx as nx
import matplotlib.pyplot as plt
import scipy
import numpy

inf = 300


def correct_graph(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                A[i][j] = inf


def incorrect_graph(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] is inf:
                A[i][j] = 0


def create_matrix_from_file(filename):
    file = open("tests/" + filename + ".txt")
    A = []
    for line in file:
        arr = line.split()
        A.append(list(map(int, arr)))
    for i in range(len(A)):
        count = 0
        for j in range(len(A[0])):
            if A[i][j] != 0:
                count += 1
        if count < 2:
            raise Exception("нет цикла")
    global inf
    inf = max(max(A)) ** 4
    return A


def print_graph(A):
    # incorrect_graph(A)
    # has orientation?
    # G = nx.convert_matrix.from_numpy_matrix(numpy.matrix(A), create_using=nx.DiGraph)
    G = nx.convert_matrix.from_numpy_matrix(numpy.matrix(A))
    plt.figure(figsize=(5, 4), dpi=100)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color="red", node_size=500, with_labels=True, arrows=True, arrowsize=20)
    # weight of edges
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)
    plt.axis("off")
    plt.show()
    # correct_graph(A)


def remove_edge(matrix, first_node, second_node):
    matrix[first_node][second_node] = matrix[second_node][first_node] = inf


def add_edge(matrix, first_node, second_node, weight=1):
    matrix[first_node][second_node] = matrix[second_node][first_node] = weight


def remove_node(matrix, node):
    del matrix[node]
    for i in matrix:
        del i[node]


def add_node(matrix):
    for i in matrix:
        i.append(inf)
    line = [inf] * len(matrix[0])
    line[len(line) - 1] = 0
    matrix.append(line)
