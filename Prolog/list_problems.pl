/*
 *    P01: Find the last element of a list
 */
my_last(X, [X]).
my_last(X, [_|T]) :- my_last(X, T).

/*
 *    P02: Find the last but one element of a list
 */
last_but_one(X, [X, _]).
last_but_one(X, [_|T]) :- last_but_one(X, T).

/*
 *    P03: Find the K'th element of a list
 */
element_at(X, [X|_], 1).
element_at(X, [_|T], K) :- 
    Y is K - 1, 
    element_at(X, T, Y).

/*
 *    P04: Find the number of elements of a list
 */
do_find_length(X, [], X).
do_find_length(X, [_|T], L) :- 
    Y is L + 1, 
    do_find_length(X, T, Y).
my_length(X, Y) :- do_find_length(X, Y, 0).

/*
 *    P05: Reverse a list
 */
do_reverse(X, [], X).
do_reverse(X, [H|T], L) :- do_reverse(X, T, [H|L]).
my_reverse(X, L) :- do_reverse(X, L, []).

/*
 *    P06: Find out whether a list is palindrome
 */
palin(L) :- 
    my_reverse(X, L), 
    X = L.

/*
 *    P07: Flatten a nested list structure
 */
my_flatten([], []).
my_flatten([[Y|Z]|W], X) :- 
    my_flatten([Y|Z], A), 
    my_flatten(W, B), 
    append(A, B, X).
my_flatten([H|T], X) :- 
    my_flatten(T, Y), 
    append([H], Y, X).
	
/*
 *    P08: Eliminate consecutive duplicates of list elements
 */
do_compress([], X, X).
do_compress([H1|T], ACC, X) :- 
    [H2|T1] = T,
    H1 = H2, 
    do_compress([H2|T1], ACC, X).
do_compress([H|T], ACC, X) :- 
    append(ACC, [H], Y), 
    do_compress(T, Y, X).
compress(L, X) :- do_compress(L, [], X).

/*
 *    P09: Pack consecutive duplicates of list elements into sublists
 */
do_build_list(0, _, X, X).
do_build_list(N, A, ACC, X) :- N1 is N-1, do_build_list(N1, A, [A|ACC], X).
build_list(N, A, X) :- do_build_list(N, A, [], X). 

do_pack([], X, _, X).
do_pack([H1|T1], ACC, N, X) :-
    [H2|_] = T1,
    H1 = H2,
    N1 is N + 1,    
    do_pack(T1, ACC, N1, X).
do_pack([H|T], ACC, N, X) :-
    N1 is N + 1,
    build_list(N1, H, L),
    append(ACC, [L], Y),
    do_pack(T, Y, 0, X).
pack(L, X) :- do_pack(L, [], 0, X).

/*
 *    P10: Run length-encoding of a list
 */
do_encode([], X, X).
do_encode([[H|T1]|T], ACC, X) :-
    my_length(LEN, [H|T1]),
    append(ACC, [[LEN, H]], Y),
    do_encode(T, Y, X).
encode(L, X) :- 
    pack(L, Y), 
    do_encode(Y, [], X).

/*
 *    P11: Modified run length-encoding of a list
 */
encoding_item([H], [H]).
encoding_item([H|T], X) :-
    my_length(LEN, [H|T]),
    X = [[LEN, H]].

do_encode_modified([], X, X).
do_encode_modified([[H|T1]|T], ACC, X) :-
    encoding_item([H|T1], ITEM),
    append(ACC, ITEM, Y),
    do_encode_modified(T, Y, X).
encode_modified(L, X) :- 
    pack(L, Y), 
    do_encode_modified(Y, [], X).

/*
 *    P12: Decode a length-encoded list
 */
do_decode([], X, X).
do_decode([[LEN, ITEM]|T], ACC, X) :- 
    build_list(LEN, ITEM, L),
    append(ACC, L, Y),
    do_decode(T, Y, X).
do_decode([H|T], ACC, X) :-
    append(ACC, [H], Y),
    do_decode(T, Y, X).
decode(L, X) :- do_decode(L, [], X).

/*
 *    P14: Duplicate the elements of a list
 */
do_duplicate([], X, X).
do_duplicate([H|T], ACC, X) :-
    append(ACC, [H, H], Y),
    do_duplicate(T, Y, X).
dupli(L, X) :- do_duplicate(L, [], X).

/*
 *    P22: Create a list containing all integers within a given range.
 */
do_range(A, A, L, L).
do_range(A, B, ACC, L) :- 
    append(ACC, [A], Y),
    A1 is A + 1,
    do_range(A1, B, Y, L).
range(A, B, L) :- B1 is B + 1, do_range(A, B1, [], L).

