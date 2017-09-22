# MSBD5009

MSBD5009 Tutorial Materials

## Guidance

* [set your environment](./guidance/set-env.md)
* [ssh-related](./guidance/ssh-related.md)

## Tutorial

All three assignments are about single source shortest path, where we have negative weights for edges,
and possibly negative cycles. Thus, dijstra algorithm can not be used due to negative cycle.

In order to speedup your algorithm based on bellman-ford algorithm, you need to further study shortest-path-faster-algorithm with pruning compared to bellman-ford algorithm.

* [dijstra algorithm](tutorial/dijstra.md), not used in our assignment
* [bellman-ford algorithm](tutorial/bellman-ford.md)
* [spfa](tutorial/spfa.md), i.e, Shortest-Path-Faster-Algorithm

You can also have a look at python demo codes. [bellman-ford algorithm](python_playground/bellman_ford_algorithm.py), [spfa](python_playground/shortest_path_fast_algorithm.py), [dijstra algorithm](python_playground/dijstra_algorithm.py).
