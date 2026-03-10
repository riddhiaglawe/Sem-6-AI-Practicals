# Practical 07 – Prolog Family Relationship

## Aim
To write a Prolog program to demonstrate family relationships.

## Objective
- Represent knowledge using facts
- Define relationships using rules
- Understand unification and backtracking
- Model family relations like parent, sibling, and grandparent

## Theory
Prolog (Programming in Logic) is a logic-based programming language used in Artificial Intelligence.  
A Prolog program consists of **facts, rules, and queries**. It uses **unification and backtracking** to find answers to logical queries.

## Example

Facts:
parent(john, mary).
male(john).
female(mary).

Rule:
father(X,Y) :- parent(X,Y), male(X).

Query:
?- father(X, mary).

Output:
X = john

## Algorithm
1. Define family members using male and female facts.
2. Define parent relationships.
3. Create rules for father, mother, sibling, and grandparent.
4. Load the program in Prolog.
5. Execute queries to find relationships.

## Conclusion
This practical demonstrates how Prolog represents knowledge using logical rules and facts to determine family relationships.