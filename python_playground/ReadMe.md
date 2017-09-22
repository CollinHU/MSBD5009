## Three Toy Graphs

no negative weight

```
# src dst weight
0 1 10
0 5 8
1 3 2
2 1 1
3 2 2
4 3 1
4 1 4
5 4 1
```

no negative cycle

```
# src dst weight
0 1 10
0 5 8
1 3 2
2 1 1
3 2 2
4 3 1
4 1 4
5 4 1

```

negative cycle

```
# src dst weight
0 1 10
1 2 2
2 3 -1
3 1 -3
```

## Runtime Results

### Bellman-Ford

```
after iter 0 , dist array: [0, 10, 14, 12, 9, 8]
after iter 1 , dist array: [0, 10, 14, 10, 9, 8]
after iter 2 , dist array: [0, 10, 12, 10, 9, 8]
after iter 3 , dist array: [0, 10, 12, 10, 9, 8]
shortest distance from src: [0, 10, 12, 10, 9, 8]
vertex and its prev: [(0, None), (1, set([0])), (2, set([3])), (3, set([4])), (4, set([5])), (5, set([0]))]
has negative cycle: False
------------------------------
after iter 0 , dist array: [0, 10, 10, 12, 9, 8]
after iter 1 , dist array: [0, 5, 10, 8, 9, 8]
after iter 2 , dist array: [0, 5, 5, 7, 9, 8]
after iter 3 , dist array: [0, 5, 5, 7, 9, 8]
shortest distance from src: [0, 5, 5, 7, 9, 8]
vertex and its prev: [(0, None), (1, set([4])), (2, set([3])), (3, set([1])), (4, set([5])), (5, set([0]))]
has negative cycle: False
------------------------------
after iter 0 , dist array: [0, 8, 12, 11]
after iter 1 , dist array: [0, 6, 10, 9]
after iter 2 , dist array: [0, 4, 8, 7]
has negative cycle
shortest distance from src: [0, 4, 8, 7]
vertex and its prev: [(0, None), (1, set([3])), (2, set([1])), (3, set([2]))]
has negative cycle: True
```

### SPFA

```
checked vertex list: [0, 1, 5, 3, 4, 2, 3, 2]
shortest distance from src: [0, 10, 12, 10, 9, 8]
vertex and its prev: [(0, None), (1, set([0])), (2, set([3])), (3, set([4])), (4, set([5])), (5, set([0]))]
has negative cycle: False
------------------------------
checked vertex list: [0, 1, 5, 3, 4, 2, 1, 3, 3, 2]
shortest distance from src: [0, 5, 5, 7, 9, 8]
vertex and its prev: [(0, None), (1, set([4])), (2, set([3])), (3, set([1])), (4, set([5])), (5, set([0]))]
has negative cycle: False
------------------------------
checked vertex list: [0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
has negative cycle
shortest distance from src: [0, 4, 8, 7]
vertex and its prev: [(0, None), (1, set([3])), (2, set([1])), (3, set([2]))]
has negative cycle: True
```

### SPFA Explicit Iteration

```
after iter 0 , dist array: [0, 10, 999999, 999999, 999999, 8]
after iter 1 , dist array: [0, 10, 999999, 12, 9, 8]
after iter 2 , dist array: [0, 10, 14, 10, 9, 8]
after iter 3 , dist array: [0, 10, 12, 10, 9, 8]
after iter 4 , dist array: [0, 10, 12, 10, 9, 8]
shortest distance from src: [0, 10, 12, 10, 9, 8]
vertex and its prev: [(0, None), (1, set([0])), (2, set([3])), (3, set([4])), (4, set([5])), (5, set([0]))]
has negative cycle: False
------------------------------
after iter 0 , dist array: [0, 10, 999999, 999999, 999999, 8]
after iter 1 , dist array: [0, 10, 999999, 12, 9, 8]
after iter 2 , dist array: [0, 5, 10, 8, 9, 8]
after iter 3 , dist array: [0, 5, 5, 7, 9, 8]
after iter 4 , dist array: [0, 5, 5, 7, 9, 8]
shortest distance from src: [0, 5, 5, 7, 9, 8]
vertex and its prev: [(0, None), (1, set([4])), (2, set([3])), (3, set([1])), (4, set([5])), (5, set([0]))]
has negative cycle: False
------------------------------
after iter 0 , dist array: [0, 10, 999999, 999999]
after iter 1 , dist array: [0, 10, 12, 999999]
after iter 2 , dist array: [0, 10, 12, 11]
has negative cycle
shortest distance from src: [0, 10, 12, 11]
vertex and its prev: [(0, None), (1, set([0])), (2, set([1])), (3, set([2]))]
has negative cycle: True
```

### Dijstra

```
shortest distance from src: [0, 10, 12, 10, 9, 8]
vertex and its prev: [(0, None), (1, set([0])), (2, set([3])), (3, set([4])), (4, set([5])), (5, set([0]))]
------------------------------
['dist[u],u:0,0', 'dist[u],u:999999,5', 'dist[u],u:999999,4', 'dist[u],u:999999,3', 'dist[u],u:999999,2', 'dist[u],u:999999,1']
delete min: dist[u],u:0,0
delete min: dist[u],u:8,5
delete min: dist[u],u:9,4
delete min: dist[u],u:10,1
delete min: dist[u],u:10,3
delete min: dist[u],u:12,2
shortest distance from src: [0, 10, 12, 10, 9, 8]
vertex and its prev: [(0, None), (1, set([0])), (2, set([3])), (3, set([4])), (4, set([5])), (5, set([0]))]
```