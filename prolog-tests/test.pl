test1(test).

myappend([], L2, L2).
myappend([H|T], L3, [H|Z]) :- myappend(T, L3, Z).

myreverse([], []).
myreverse([H|T], Y) :- myreverse(T, X), myappend(X, [H], Y).

myreverse2([], []).
myreverse2([H|T], Y) :- myappend(T, [H], X), myreverse2(T, X).

/**
 * 99 Problems in Prolog for practice
 * http://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/
 */

last_element([], none).
last_element([H], H).	
last_element([H|T], X) :- last_element(T, X).

my_last(X,[X]).
my_last(X,[_|L]) :- my_last(X,L).