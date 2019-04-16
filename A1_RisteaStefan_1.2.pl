% KB

translate(unu, one).
translate(doi, two).
translate(trei, three).
translate(patru, four).
translate(cinci, five).
translate(sase, six).
translate(sapte, seven).
translate(opt, eight).
translate(noua, nine).


% Predicate

% translate_list(+List_Ro : list, -List_Eng : list).
% Succeeds if List_Eng is the translated list of the elements in List_Ro.
% 
% @param List_Ro - The list of elements in Romanian.
% @param List_Eng - The list of elements translated in English from List_Ro (the result).
% 
% Example:
% ? - translate_list([unu, doi, trei], Result).
% [ Result = [one, two, three] ]
translate_list([],[]).
translate_list([H1|T1],[H2|T2]) :-
    translate(H1, H2),
    translate_list(T1, T2), !.

% Test for the solution to Problem_2:
% ? - translate_list([unu, doi, trei], Result).