import networkx as nx
from fibonacci_heap import FibonacciHeap
from bellman_ford_algorithm import *

#
# def sssp_dijstra_with_heap(src):
#     n = (max(toy_graph.nodes()) + 1)
#     # step 1: init dist
#     dist = [inf] * n
#     dist[src] = 0
#
#     # step 2: is_mark
#     is_mark = [False] * n


# def sssp_dijstra_without_heap_for_dense_graph(src, matrix, n):


if __name__ == '__main__':
    toy_graph = nx.DiGraph()
    toy_graph.add_weighted_edges_from(get_edge_list_tuple('toy_graph_edge_list.txt'))
    for src, dst in toy_graph.edges():
        print src, dst, toy_graph.edge[src][dst]['weight']

    lst = [3, 4, -1]

