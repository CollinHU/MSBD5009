import networkx as nx
from fibonacci_heap import FibonacciHeap
from bellman_ford_algorithm import *


# def sssp_dijstra_with_heap(src):
#     n = (max(toy_graph.nodes()) + 1)
#     # step 1: init dist
#     dist = [inf] * n
#     dist[src] = 0
#
#     # step 2: is_mark
#     is_mark = [False] * n


def sssp_dijstra_without_heap_for_dense_graph(src_vertex, matrix, n):
    dist = [inf] * n
    dist[src_vertex] = 0

    prev = [None] * n
    is_mark = [False] * n

    def is_empty():
        for is_mark_flag in is_mark:
            if not is_mark_flag:
                return False
        return True

    # find min and delete
    def delete_min():
        min_dist = inf
        min_v = -1
        for u in filter(lambda ele: not is_mark[ele], range(n)):
            if dist[u] < min_dist:
                min_v = u
        return min_v

    while not is_empty():
        u = delete_min()
        is_mark[u] = True
        for v in filter(lambda ele: not is_mark[ele], range(n)):
            weight = matrix[get_edge_offset(u, v, n)]
            if weight != inf:
                if dist[u] + weight < dist[v]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        prev[v] = {u}
                    if dist[u] + weight == dist[v]:
                        prev[v].add(u)
    return dist, prev


def demo_without_heap():
    matrix, n = get_weight_matrix('toy_graph_edge_list.txt')
    dist, prev = sssp_dijstra_without_heap_for_dense_graph(0, matrix, n)
    print 'shortest distance from src:', dist
    print 'vertex and its prev:', zip(range(n), prev)


if __name__ == '__main__':
    demo_without_heap()
