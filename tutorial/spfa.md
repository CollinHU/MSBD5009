### Idea

* optimize via introducing a queue to do some pruning.

* detecting negative cycle, see this [link](https://stackoverflow.com/questions/18007979/detecting-negative-cycles-using-spfa-algorithm).

* in parallel implementation, these two hash-set based queues `queue_cur`, `queue_next` can be replaced with bool array

### Code Gist

see [spfa_explicit_iteration_num.py](../python_playground/spfa_explicit_iteration_num.py)

```python
def sssp_spfa(src_vertex, matrix, n):
    dist = [inf] * n
    dist[src_vertex] = 0

    prev = [None] * n
    visit = [0] * n

    queue_cur = {src_vertex}
    # iteration num
    i = 0
    while len(queue_cur) != 0:
        # iterate through all edges to check relaxation
        # pruning here `queue_cur`, only expands changed source vertices
        queue_next = set()
        for u in queue_cur:
            # check if you visited the same node at least |V| times
            visit[u] += 1
            if visit[u] < n:
                for v in xrange(n):
                    # if edge exists
                    weight = matrix[get_edge_offset(u, v, n)]
                    if weight != inf:
                        if dist[u] + weight < dist[v]:
                            dist[v] = dist[u] + weight
                            prev[v] = {u}
                            queue_next.add(v)
                        if dist[u] + weight == dist[v]:
                            prev[v].add(u)
        print ' '.join(['after iter', str(i), ', dist array:', str(dist)]), 'cur queue:', queue_cur
        queue_cur = queue_next
        i += 1

    if len(queue_cur) == 0:
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
