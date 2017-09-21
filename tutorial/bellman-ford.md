### Idea

* first step: do iterative computations
  * outer loop `n-1` times, proof to be correct sssp by bellman and ford
  * inner loop all edges and do relaxation if possible, in your assignment, you do not need to record `prev`

* second step: check if negative cycle exists, iff exist `u` where relaxation happens for `v`, i.e, `dist[u] + weight < dist[v]:`

### Attention

our graph is directed, (u,v) weight differs from (v,u).

be careful with `get_edge_offset(u, v, n)`， our matrix is represented in 1d array.

### Code Gist

see [bellman_ford_algorithm.py](../python_playground/bellman_ford_algorithm.py)

```python
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
```
