# Practical 06 – Alpha Beta Pruning Algorithm

## Aim
To implement the Alpha-Beta Pruning algorithm for optimizing the Minimax search in game development.

---

## Objective
- To understand the concept of game tree search.
- To learn how Alpha-Beta pruning improves the Minimax algorithm.
- To reduce the number of nodes evaluated during game decision making.

---

## Theory

Alpha-Beta pruning is an optimization technique used in the **Minimax algorithm**.  
It reduces the number of nodes that need to be evaluated in a game tree.

It works by eliminating branches that cannot influence the final decision.

Two parameters are used:

- **Alpha (α)** → Best value that the maximizer currently can guarantee.
- **Beta (β)** → Best value that the minimizer currently can guarantee.

If at any point:
