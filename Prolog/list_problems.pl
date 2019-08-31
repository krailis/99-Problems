my_last(X, [X]).
my_last(X, [_|T]) :- my_last(X, T).

last_but_one(X, [X, _]).
last_but_one(X, [_|T]) :- last_but_one(X, T).

element_at(X, [X|_], 1).
element_at(X, [_|T], K) :- 
	Y is K - 1, 
	element_at(X, T, Y).

do_find_length(X, [], X).
do_find_length(X, [_|T], L) :- 
	Y is L + 1, 
	do_find_length(X, T, Y).
my_length(X, Y) :- do_find_length(X, Y, 0).

do_reverse(X, [], X).
do_reverse(X, [H|T], L) :- do_reverse(X, T, [H|L]).
my_reverse(X, L) :- do_reverse(X, L, []).

palin(L) :- 
	my_reverse(X, L), 
	X = L.

my_flatten([], []).
my_flatten([[Y|Z]|W], X) :- 
	my_flatten([Y|Z], A), 
	my_flatten(W, B), 
	append(A, B, X).
my_flatten([H|T], X) :- 
	my_flatten(T, Y), 
	append([H], Y, X).
	
do_compress([], X, X).
do_compress([H1|T], ACC, X) :- 
	[H2|T1] = T,
	H1 = H2, 
	do_compress([H2|T1], ACC, X).
do_compress([H|T], ACC, X) :- 
	append(ACC, [H], Y), 
	do_compress(T, Y, X).
compress(L, X) :- do_compress(L, [], X).

