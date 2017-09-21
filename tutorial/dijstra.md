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
