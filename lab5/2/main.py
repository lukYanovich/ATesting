import sys
import random
from graph import *


def get_way(matrix):
    way = [i for i in range(len(matrix))]
    random.shuffle(way)
    return way


def get_weights(way, matrix):
    return [matrix[way[i]][way[i + 1]] for i in range(len(way) - 1)]


def print_way(way, matrix, _end="\n"):
    weights = get_weights(way, matrix)
    print(way)
    print([sum(weights), weights], end=_end)


def swap_pair(way, A):
    if len(way) > 2:
        for i in range(len(way) - 1):
            a = way[i]
            b = way[i + 1]
            way1 = way.copy()
            del way1[i + 1]
            del way1[i]
            for j in range(i, len(way1) - 1):
                c = way1[j]
                d = way1[j + 1]
                if A[a][b] + A[c][d] > A[a][d] + A[c][b]:
                    pos1 = way.index(b)
                    pos2 = way.index(d)
                    way[pos1], way[pos2] = way[pos2], way[pos1]
                    return True
    return False


def find_best_way(way, A):
    print("source way:")
    print_way(way, A)
    print("start improving:")
    res = swap_pair(way, A)
    count = 0
    while res:
        count += 1
        print_way(way, A)
        res = swap_pair(way, A)
        if count > 20:
            break
    print("record:")
    print_way(way, A, _end="\n\n")
    return way


def finding(A):
    ways = []
    for i in range(5):
        better_way = find_best_way(get_way(A), A)
        ways.append(better_way)
    ways = [(sum(get_weights(i, A)), i) for i in ways]
    print(ways)
    print("final: ", sorted(ways, key=lambda x: x[0])[0])


if __name__ == "__main__":
    A = create_matrix_from_file("1")
    print_graph(A)
    finding(A)

    while True:
        line = input("\nenter command: ")
        if line == "exit":
            sys.exit()
        input_line = line.split()
        if len(input_line) >= 3:
            if input_line[0] == "a":
                add_edge(A, int(input_line[1]), int(input_line[2]), int(input_line[3]))
            elif input_line[0] == "d":
                remove_edge(A, int(input_line[1]), int(input_line[2]))
        elif len(input_line) == 2 and input_line[0] == "d":
            remove_node(A, int(input_line[1]))
        elif len(input_line) == 1 and input_line[0] == "a":
            add_node(A)
        print_graph(A)
        finding(A)
