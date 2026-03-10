% -------- PARENT FACTS (ALL TOGETHER) --------

parent(vithobaji, vyankatrao).
parent(parawati, vyankatrao).

parent(vyankatrao, vijay).
parent(vatsala, vijay).

parent(vijay, mandar).
parent(manjusha, mandar).

parent(vijay, riddhi).
parent(manjusha, riddhi).

% -------- MALE FACTS (ALL TOGETHER) --------

male(vithobaji).
male(vyankatrao).
male(vijay).
male(mandar).

% -------- FEMALE FACTS (ALL TOGETHER) --------

female(parawati).
female(vatsala).
female(manjusha).
female(riddhi).

% -------- MARRIAGE FACTS (GROUPED) --------

husband(vithobaji, parawati).
husband(vyankatrao, vatsala).
husband(vijay, manjusha).

wife(parawati, vithobaji).
wife(vatsala, vyankatrao).
wife(manjusha, vijay).

% -------- RULES --------

father(X, Y) :-
parent(X, Y),
male(X).

mother(X, Y) :-
parent(X, Y),
female(X).

child(X, Y) :-
parent(Y, X).

son(X, Y) :-
child(X, Y),
male(X).

daughter(X, Y) :-
child(X, Y),
female(X).

sibling(X, Y) :-
parent(Z, X),

parent(Z, Y),
X \= Y.

grandparent(X, Y) :-
parent(X, Z),
parent(Z, Y).

great_grandparent(X, Y) :-
parent(X, A),
parent(A, B),
parent(B, Y).

grandfather(X, Y) :-
grandparent(X, Y),
male(X).

grandmother(X, Y) :-
grandparent(X, Y),
female(X).

ancestor(X, Y) :-
parent(X, Y).
ancestor(X, Y) :-

parent(X, Z),
ancestor(Z, Y).
