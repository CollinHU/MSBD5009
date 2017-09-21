from bellman_ford_algorithm import *


def sssp_spfa(src_vertex, matrix, n):
    dist = [inf] * n
    dist[src_vertex] = 0

    prev = [None] * n
    visit = [0] * n

    check_vertex_lst = []
    queue = [src_vertex]
    while len(queue) > 0:
        u = queue.pop(0)
        visit[u] += 1
        check_vertex_lst.append(u)

        # check if you visited the same node at least |V| times
        if visit[u] < n:
            # iterate through all edges to check relaxation
            for v in xrange(n):
                # if edge exists
                weight = matrix[get_edge_offset(u, v, n)]
                if weight != inf:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        prev[v] = {u}
                        queue.append(v)
                        if visit[v] >= n:
                            return dist, prev, True
                    if dist[u] + weight == dist[v]:
                        prev[v].add(u)

    print 'checked vertex list:', check_vertex_lst
    # if relaxation happens then there must be a negative-cycle
    for u in xrange(n):
        for v in xrange(n):
            # if edge exists
            weight = matrix[get_edge_offset(u, v, n)]
            if weight != inf:
                if dist[u] + weight < dist[v]:
                    print 'has negative cycle'
                    return dist, prev, True
    return dist, prev, False


def demo(file_path, src_vertex=0):
    matrix, n = get_weight_matrix(file_path)

    dist, prev, has_negative_cycle = sssp_spfa(src_vertex, matrix, n)
    print 'shortest distance from src:', dist
    print 'vertex and its prev:', zip(range(n), prev)
    print 'has negative cycle:', has_negative_cycle


if __name__ == '__main__':
    demo(file_path='toy_graph_edge_list_negative_weight.txt')
    print ''.join(['---'] * 10)
    demo(file_path='toy_graph_negative_cycle.txt')
