% Predicate

% concatenate(+First_List : list, +Second_List : list, -Concatenated_List : list).
% Succeeds if Concatenated_List is the concatenation of First_List and Second_List.
% 
% @param First_List - The first list to be concatenated.
% @param Second_List - The second list, that is to be concatenated after Fists_List.
% @param Concatenated_List - The list containing the concatenation of First_List and Second_List (the result).
% 
% Example:
% ? - concatenate([1,2,3], [4,5,6], Result).
% [ Result = [1, 2, 3, 4, 5, 6] ]
concatenate([], A, A).
concatenate([H|T1], A, [H|T2]):-
    concatenate(T1, A, T2), !.


% multiply_element(+Element_to_Multiply : list, -Times_to_Multiply : atom, -Generated_List : list).
% Succeeds if Generated_List contains Element_to_Multiply multiplied Times_to_Multiply times.
% 
% @param Element_to_Multiply - The list of a single atom to be multiply Times_to_Multiply times.
% @param Times_to_Multiply - The number of times to multply the Element_to_Multiply.
% @param Generated_List - The generated after the multiplication of Element_to_Multiply.
% 
% Example:
% ? - multiply_element([1], 5, Result).
% [ Result = [1, 1, 1, 1, 1] ]
multiply_element(_,0,[]).
multiply_element([H], A, [H|T]):-
    B is A-1,
    multiply_element([H], B, T), !.


% duplicate(+Initial_List : list, +Times_to_Duplicate : atom, -Generated_List: list).
% Succeeds if Generated_List contains the elements from Initial_List duplicated Times_to_Duplicate times.
% 
% @param Initial_List - The list of elements to be duplicated Times_to_Duplicate times.
% @param Times_to_Duplicate - The number of times to duplicate each element from Initial_List.
% @param Generated_List - The list generated after the duplication of each element from Initial_List.
% 
% Example:
% ? - duplicate([1,2,3], 3, Result).
% [ Result = [1, 1, 1, 2, 2, 2, 3, 3, 3] ]
duplicate([], _, []).
duplicate([H|T], A, R):-
    multiply_element([H],A,B),
    duplicate(T,A,C),
    concatenate(B,C,R), !.

% Test for the solution to Problem_3:
% ? - duplicate([1,2,3], 3, Result).