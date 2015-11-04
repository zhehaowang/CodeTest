/**
 * Check if a certain element is in the given list
 * @param list
 * @param element
 * @param true | false
 */
has_element([], _, false).
has_element([H|_], H, true).
has_element([H|T], X, Y) :- H \= X, has_element(T, X, Y).

/**
 * Append a list to a given list
 * @param list1
 * @param list2
 * @param list1 + list2
 */
append_list([], X, X).
append_list([H|T], X, [H|TX]) :- append_list(T, X, TX).

/**
 * Check if numbers in a list are unique
 * @param test_list
 * @param helper_list, should use []
 * @param true | false
 */
is_distinct([], _, true).
is_distinct([H|T], Y, false) :- has_element(Y, H, true).
is_distinct([H|T], Y, X) :- has_element(Y, H, false), append_list(Y, [H], YH), is_distinct(T, YH, X).

/**
 * Get the i-th element from the list
 * @param list
 * @param index
 * @param [element]
 */
get_n([], I, []).
get_n([H|_], 0, [H]).
get_n([H|T], I, X) :- I \= 0, N is I - 1, get_n(T, N, X).

/**
 * Extract a column from a given matrix
 * Note: This logic is kind of weird: 
 *  we get the i-th element [E] of the current row H, try to get the i-th 
 *  element of the next row with some list Y, and make sure Y + E gives 
 *  our given extracted array X; since we know E is an array with one or 
 *  zero element, we can append list Y to it
 * @param list of lists
 * @param column number
 * @param resulting list
 */
extract_column([], I, []).
extract_column([H|T], I, X) :- get_n(H, I, E), extract_column(T, I, Y), append_list(E, Y, X).

/**
 * This can only tell if a given thing meets sudoku constraints, but cannot find sudoku based on given numbers
 */
sudoku(0, []).
sudoku(N, [H|T]) :- is_distinct(H, [], true), N1 is N - 1, extract_column([H|T], N1, Y), is_distinct(Y, [], true), sudoku(N1, T).

