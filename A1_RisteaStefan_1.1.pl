% KB

direct_train(craiova, bucharest).
direct_train(sibiu, craiova).
direct_train(deva, sibiu).
direct_train(brasov, deva).
direct_train(pitesti, brasov).
direct_train(ploiesti, pitesti).
direct_train(constanta, ploiesti).
direct_train(cluj, arad).


% Predicates

% train_chain_route(+First_City : atom, +Second_City : atom).
% Succeeds if First_City is connected to Second_city in an chain_route manner.
% 
% @param First_City - The starting city.
% @param Second_City - The destination city.
% 
% Example:
% ? - train_chain_route(craiova, constanta).
% [false]
train_chain_route(A, B) :- 
    direct_train(A, B).
train_chain_route(A, B) :- 
    direct_train(A, X),
    train_chain_route(X, B), !.