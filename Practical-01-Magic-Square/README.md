# Practical 01 – Magic Square Generation (Python)

## Aim
To implement a Python program to generate a Magic Square of given odd dimension using Google Colab or VS Code.

## Objective
- To understand the concept of Magic Square.
- To apply problem-solving techniques.
- To revise Python fundamentals.

## Theory
A Magic Square of order n is a square matrix of size n × n where the sum of numbers in each row, column, and diagonal is equal.

Magic Constant:
M = n(n² + 1) / 2

This implementation works only for odd numbers.

## Algorithm
1. Initialize an empty n×n matrix.
2. Place number 1 in middle of first row.
3. Follow wrap-around conditions.
4. Apply conflict resolution rule when cell is occupied.
5. Repeat until n² numbers are placed.

## Technology Used
- Python
- VS Code / Google Colab

## Output
The program generates a valid Magic Square and displays the magic constant.

## Conclusion
The program successfully generates a Magic Square for odd dimensions and verifies the constant sum property.
