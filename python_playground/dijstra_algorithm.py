import networkx as nx
import heapq

inf = 999999


def get_edge_list_tuple(file_path):
    with open(file_path) as ifs:
        return map(lambda my_line: map(int, my_line.strip().split()),
                   filter(lambda line: '#' not in line, ifs.readlines()))


def sssp_dijstra(src, graph):
    n = (max(toy_graph.nodes()) + 1)
    # step 1: init dist
    dist = [inf] * n
    dist[src] = 0

    # step 2: is_mark
    is_mark = [False] * n

if __name__ == '__main__':
    toy_graph = nx.DiGraph()
    toy_graph.add_weighted_edges_from(get_edge_list_tuple('toy_graph_edge_list.txt'))
    for src, dst in toy_graph.edges():
        print src, dst, toy_graph.edge[src][dst]['weight']

    lst = [3, 4, -1]
