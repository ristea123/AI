% Predicate
% range(+Starting_Number : atom, +Ending_Number : atom, -Generated_List : list).
% Succeeds if Generated_list is the list containing the numbers from
% 		Starting_Number to Enging_Number in order.
% 
% @param Starting_Number - The starting of the interval generated in the list.
% @param Starting_Number - The ending of the interval generated in the list.
% @param Generated_list - The list containing the numbers in the interval (the result).
% 
% Example:
% ? - range(3, 8, Result).
% [ R = [3, 4, 5, 6, 7, 8] ]
range(A, B, []):-
    A is B+1, !.
range(A, B, [H|T]):-
    H is A,
    C is A+1,
    range(C, B, T).

% Test for the solution to Problem_5:
% ? - range(3, 8, Result).