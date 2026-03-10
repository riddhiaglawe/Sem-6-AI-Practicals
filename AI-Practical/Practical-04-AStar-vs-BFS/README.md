# Practical 04 – A* Algorithm and BFS Comparison

## Aim
To implement A* algorithm to find shortest path and compare its performance with BFS.

## Objective
- To understand heuristic search.
- To implement A* algorithm.
- To compare time efficiency with BFS.

## Concepts Used
- g(n): Cost from start node
- h(n): Heuristic estimate
- f(n) = g(n) + h(n)
- OPEN and CLOSE lists

## Algorithm Steps
1. Add start node to OPEN list.
2. Select node with lowest f(n).
3. Expand node and calculate costs.
4. Move evaluated node to CLOSE.
5. Repeat until goal is reached.

## Advantages of A*
- Optimal
- Complete
- Efficient with good heuristic

## Conclusion
A* algorithm provides optimal shortest path and performs better than BFS when heuristic is accurate.
