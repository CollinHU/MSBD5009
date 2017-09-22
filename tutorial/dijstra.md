### main steps

* initialize single source vertex `S`, `dist[S] = 0`. for all other vertices `u`, `dist[u] = inf`
* initialize a heap, which supports `Insert`, `DeleteMin`, `DecreaseKey` operation, for all vertices `u` insert `u` and the heap maintains `DeleteMin` by checking `dist[u]`
* initialize a vertex property array, `is_mark`, where `is_mark[u] == true` represents the shorted path weight sum from source vertex to `u` is already known
* begins computation proposed by Dijstra

### Dijstra computation

* do as follows until heap is empty
  * `DeleteMin`, suppose you get `v`, `is_mark[v] = true`
  * `filter` all destination vertices of `v` by `is_mark[neighbor_of_v] == false`
  * `for each` vertex `w` in filtered list, do relaxation, i.e, check `dist[v] + weight between v and w < dist[w]`, if true update `dist[w]` and `DecreaseKey`, otherwise not.

### Code Gist

without heap

```python
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
```

with heap

```python
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
```
