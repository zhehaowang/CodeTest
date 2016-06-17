test1(test).

myappend([], L2, L2).
myappend([H|T], L3, [H|Z]) :- myappend(T, L3, Z).

myreverse([], []).
myreverse([H|T], Y) :- myreverse(T, X), myappend(X, [H], Y).

myreverse2([], []).
myreverse2([H|T], Y) :- myappend(T, [H], X), myreverse2(T, X).

/**
 * This groups the given array by 3 elements, for example, [1, 2, 3, 4, 5, 6] gives [[1, 2, 3], [4, 5, 6]]
 */
split3([X,Y,Z|L],[[X,Y,Z]|R]) :- split3(L,R).
split3([],[]).

/**
 * 99 Problems in Prolog for practice
 * http://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/
 */

last_element([], none).
last_element([H], H).	
last_element([H|T], X) :- last_element(T, X).

my_last(X,[X]).
my_last(X,[_|L]) :- my_last(X,L).

