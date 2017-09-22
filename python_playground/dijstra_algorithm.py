import networkx as nx
from fibonacci_heap import FibonacciHeap
from bellman_ford_algorithm import *


# key is assigned dist[u], value is assigned u
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        # print 'lt', self.key, other.key
        return self.key < other.key

    def __gt__(self, other):
        # print 'gt', self.key, other.key
        return self.key > other.key

    def __str__(self):
        return 'dist[u],u:' + ','.join(map(str, [self.key, self.value]))


def sssp_dijstra_with_heap(src_vertex, matrix, n):
    dist = [inf] * n
    dist[src_vertex] = 0

    prev = [None] * n
    is_mark = [False] * n

    # for looking up nodes, used before `decrease_key`
    data_ref_arr = [None] * n
    fib_heap = FibonacciHeap()

    for v in xrange(n):
        if v != src_vertex:
            data_ref_arr[v] = fib_heap.insert(Data(inf, v))
        else:
            data_ref_arr[v] = fib_heap.insert(Data(0, v))

    print [str(x.data) for x in fib_heap.iterate(fib_heap.root_list)]
    # print str(fib_heap.find_min().data)

    while fib_heap.total_nodes > 0:
        # delete min
        data = fib_heap.extract_min().data
        assert isinstance(data, Data)
        u = data.value
        is_mark[u] = True
        print 'delete min:', str(data)
        for v in filter(lambda ele: not is_mark[ele], range(n)):
            weight = matrix[get_edge_offset(u, v, n)]
            if weight != inf:
                if dist[u] + weight < dist[v]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        prev[v] = {u}

                        # decrease key
                        fib_heap.decrease_key(data_ref_arr[v], Data(dist[v], v))
                    if dist[u] + weight == dist[v]:
                        prev[v].add(u)
    is_mark = [False] * n
    return dist, prev


def sssp_dijstra_without_heap(src_vertex, matrix, n):
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
    dist, prev = sssp_dijstra_without_heap(0, matrix, n)
    print 'shortest distance from src:', dist
    print 'vertex and its prev:', zip(range(n), prev)


def demo_with_heap():
    matrix, n = get_weight_matrix('toy_graph_edge_list.txt')
    dist, prev = sssp_dijstra_with_heap(0, matrix, n)
    print 'shortest distance from src:', dist
    print 'vertex and its prev:', zip(range(n), prev)


if __name__ == '__main__':
    demo_without_heap()
    print ''.join(['---'] * 10)
    demo_with_heap()
