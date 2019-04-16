% Predicate

% insert_at_nth_poz(+Initial_List : list, +Atom_to_Insert : atom, +Position : atom, -Resulting_List : list).
% Succeeds if Resulting_List is the list containing the elements of Initial_List
% 		and the element Atom_to_Insert, inserted at the position Position in Initial_list.
% 
% @param Initial_List - The initial list.
% @param Atom_to_Insert - The atom to be inserted.
% @param Position - The position where the Atom_to_Insert will be inserted in Initial_list.
% @param Resulting_List - The generated list after the inserion (the result).
% 
% Example:
% ? - insert_at_nth_poz([1,2,3,4], x, 2, Result).
% [ R = [1, x, 2, 3, 4] ]
insert_at_nth_poz(List, A, 1, [A|List]).
insert_at_nth_poz([H|T1], A, B, [H|T2]) :-
    C is B-1,
    insert_at_nth_poz(T1, A, C, T2), !.

% Test for the solution to Problem_4:
% ? - insert_at_nth_poz([1,2,3,4], x, 2, Result).