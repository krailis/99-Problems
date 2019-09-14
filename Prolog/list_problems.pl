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
compress([], []).
compress([H1|T], X) :- 
    [H2|T1] = T,
    H1 = H2, 
    compress([H2|T1], X).
compress([H|T], [H|X]) :- compress(T, X).

/*
 *    P09: Pack consecutive duplicates of list elements into sublists
 */
build_list(0, _, []).
build_list(N, A, [A|X]) :- N1 is N - 1, build_list(N1, A, X). 

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
 *    P13: Run length-encoding of a list (direct solution)
 */
do_encode_direct([], X, _, X).
do_encode_direct([H1|T1], ACC, N, X) :-
    [H2|_] = T1,
    H1 = H2,
    N1 is N + 1,    
    do_encode_direct(T1, ACC, N1, X).
do_encode_direct([H|T], ACC, N, X) :-
    N1 is N + 1,
    N1 = 1,
    append(ACC, [H], Y),
    do_encode_direct(T, Y, 0, X).
do_encode_direct([H|T], ACC, N, X) :-
    N1 is N + 1,
    append(ACC, [[N1, H]], Y),
    do_encode_direct(T, Y, 0, X).
encode_direct(L, X) :- do_encode_direct(L, [], 0, X).

/*
 *    P14: Duplicate the elements of a list
 */
dupli([], []).
dupli([H|T], [H, H|X]) :- dupli(T, X).

/*
 *    P15: Duplicate the elements of a list a give number of times
 */
do_duplicate_n_times([], _, _, []).
do_duplicate_n_times([H|T], N, ACC, X) :-
    build_list(N, H, L),
    append(ACC, L, Y),
    do_duplicate_n_times(T, N, Y, X).
dupli_n_times(L, N, X) :- do_duplicate_n_times(L, N, [], X).

/*
 *    P16: Drop every N-th element from a list
 */
do_drop([], _, _, X, X).
do_drop([_|T], N, I, ACC, X) :-
    I1 is I + 1,
    I1 = N,
    do_drop(T, N, 0, ACC, X).
do_drop([H|T], N, I, ACC, X) :-
    I1 is I + 1,
    append(ACC, [H], Y),
    do_drop(T, N, I1, Y, X).
drop(L, N, X) :- do_drop(L, N, 0, [], X).

/*
 *    P17: Split a list into two parts. The length of the first part is given.
 */
do_split([], _, _, L1, L1, []).
do_split([H|L2], N, N, ACC, L1, L2) :- append(ACC, [H], L1).    
do_split([H|T], N, I, ACC, L1, L2) :-
    I1 is I + 1,
    append(ACC, [H], Y),
    do_split(T, N, I1, Y, L1, L2).
split(L, 0, [], L).
split(L, N, L1, L2) :- do_split(L, N, 1, [], L1, L2).

/*
 *    P18: Extract a slice from a list.
 */
do_slice([], _, _, _, X, X).
do_slice(_, _, K, K, X, X).
do_slice([_|T], I, K, J, ACC, X) :-
    J < I,
    J1 is J + 1,
    do_slice(T, I, K, J1, ACC, X).
do_slice([H|T], I, K, J, ACC, X) :-
    J1 is J + 1,
    append(ACC, [H], Y),
    do_slice(T, I, K, J1, Y, X).
slice(L, I, K, X) :- 
    I1 is I - 1, 
    do_slice(L, I1, K, 0, [], X).

/*
 *    P19: Rotate a list N places to the left.
 */
rotate([], _, []). 
rotate(L, 0, L).
rotate(L, N, X) :-
    N > 0,
    split(L, N, L1, L2),
    append(L2, L1, X).
rotate(L, N, X) :-
    length(L, LEN),
    N1 is LEN + N,
    split(L, N1, L1, L2),
    append(L2, L1, X).

/*
 *    P20: Remove the K'th element from a list.
 */
remove_at(X, L, N, R) :-
    N1 is N - 1,
    split(L, N1, L1, L2),
    [X|T] = L2,
    append(L1, T, R).

/*
 *    P21: Insert an element at a given position into a list.
 */
insert_at(ELEM, L, POS, X) :-
    N is POS - 1,
    split(L, N, L1, L2),
    append(L1, [ELEM|L2], X).

/*
 *    P22: Create a list containing all integers within a given range.
 */
range(A, A, [A]).
range(A, B, [A|L]) :- A1 is A + 1, range(A1, B, L).

/*
 *    P23: Extract given number of randomly selected items from a list.
 */
rnd_select(_, 0, []).
rnd_select(L, N, [I|X]) :-
    length(L, LEN),
    LEN1 is LEN + 1,
    random(1, LEN1, RAND),
    remove_at(I, L, RAND, R),
    N1 is N - 1,
    rnd_select(R, N1, X).

/*
 *    P24: Lotto: Draw N different random numbers from the set 1 ... M
 */
lotto(N, M, L) :-
    range(1, M, Y),
    rnd_select(Y, N, L).

/*
 *    P25: Generate a random permutation of the elements of a list.
 */
rnd_permu(L, X) :- 
    length(L, LEN), 
    rnd_select(L, LEN, X).

