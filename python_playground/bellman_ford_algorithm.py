inf = 999999


def get_edge_list_tuple(file_path):
    with open(file_path) as ifs:
        return map(lambda my_line: map(int, my_line.strip().split()),
                   filter(lambda line: '#' not in line, ifs.readlines()))


def get_edge_offset(src_v, dst_v, n):
    return src_v * n + dst_v


def get_weight_matrix(file_path='toy_graph_edge_list_negative_weight.txt'):
    edge_list = get_edge_list_tuple(file_path)
    max_id = -1
    for src, dst, weight in edge_list:
        max_id = max(max_id, src, dst)
    n = max_id + 1

    # matrix: adjacency and weight, dist: distance from single source vertex
    matrix = [inf] * (n * n)

    for src, dst, weight in edge_list:
        matrix[get_edge_offset(src, dst, n)] = weight

    return matrix, n


# bellman-ford algorithm
def sssp_bellman_ford(src_vertex, matrix, n):
    dist = [inf] * n
    prev = [None] * n

    dist[src_vertex] = 0
    # iteration num
    for i in xrange(n - 1):
        is_change = False
        # iterate through all edges to check relaxation
        for u in xrange(n):
            for v in xrange(n):
                # if edge exists
                weight = matrix[get_edge_offset(u, v, n)]
                if weight != inf:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        is_change = True
                        prev[v] = {u}
                    if dist[u] + weight == dist[v]:
                        prev[v].add(u)
        print ' '.join(['after iter', str(i), ', dist array:', str(dist)])
        if not is_change:
            return dist, prev, False

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

    dist, prev, has_negative_cycle = sssp_bellman_ford(src_vertex, matrix, n)
    print 'shortest distance from src:', dist
    print 'vertex and its prev:', zip(range(n), prev)
    print 'has negative cycle:', has_negative_cycle


if __name__ == '__main__':
    demo(file_path='toy_graph_edge_list.txt')
    print ''.join(['---'] * 10)
    demo(file_path='toy_graph_edge_list_negative_weight.txt')
    print ''.join(['---'] * 10)
    demo(file_path='toy_graph_negative_cycle.txt')
