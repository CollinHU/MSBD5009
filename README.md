# MSBD5009

MSBD5009 Tutorial Materials

## Guidance

* [set your environment](./guidance/set-env.md)
* [ssh-related](./guidance/ssh-related.md)

## Tutorial

### Input

We use directed, weighted graph in adjacency matrix as our input.

Adjacency matrix is in 1D array, where offset of an edge should be computed by `u * n + v`. Here, `u` is a source vertex and `v` is a destination vertex, `n` is the total vertex number.

### Algorithm(SSSP)

All three assignments are about single source shortest path(sssp), where we have negative weights for edges,
and possibly negative cycles. Thus, dijstra algorithm can not be used due to negative weight.

In order to speedup your algorithm based on bellman-ford algorithm, you need to further study shortest-path-faster-algorithm with pruning compared to bellman-ford algorithm.

* [dijstra algorithm](tutorial/dijstra.md), not used in our assignments
* [bellman-ford algorithm](tutorial/bellman-ford.md), used in our assignments
* [spfa](tutorial/spfa.md), i.e, Shortest-Path-Faster-Algorithm, bellman-ford with more pruning, two-queue-based iterative design

You can have a look at python demo codes for better understanding.

algorithm | link
--- | ---
bellman-ford algorithm | [bellman-ford algorithm](python_playground/bellman_ford_algorithm.py)
spfa: bellman-ford with pruning | [spfa-with-two-queues](python_playground/spfa_explicit_iteration_num.py)
dijstra with heap and w/o heap| [dijstra algorithm](python_playground/dijstra_algorithm.py)
