Assignment 1. Prolog
Exercises:

1. Given the following knowledge base:
direct_train(craiova, bucharest).
direct_train(sibiu, craiova).
direct_train(deva, sibiu).
direct_train(brasov, deva).
direct_train(pitesti, brasov).
direct_train(ploiesti, pitesti).
direct_train(constanta, ploiesti).

This KB contains facts about direct train route between two cities. Journeys between unlinked
cities are possible by chaining together direct train routes. Write a recursive predicate that tells
if a journey is possible between two cities.

Example:
A query of your predicate should return „true” for (constanta, craiova).

2. Suppose we are given a KB with the following facts:

translate(unu, one).
translate(doi, two).
translate(trei, three).
translate(patru, four).
translate(cinci, five).
translate(sase, six).
translate(sapte, seven).
translate(opt, eight).
translate(noua, nine).

Write a predicate which translate a list of Romanian number words to the corresponding list of
English number words.

Example:
For this list: [unu, doi, trei, cinci] you have to obtain [one, two, three, five].

3. Given a number N write a predicate that duplicates each element of a given list N times.
Example:
[1, 2, 3] duplicate 3 times each element will result in [1, 1, 1, 2, 2, 2, 3, 3, 3]

4. Write a predicate that Insert an element at a given position into a list.
Example:
Initial list: [1, 2, 3]. Element to insert: x. Position where to insert: 2. Resulting list: [1, x,
2, 3]

5. Build a predicate that will generate a list with all consecutive integers within a given range.
Example:
Range: 5 -> 9. Resulting list: [5, 6, 7, 8, 9]

Instructions:

Each predicate should be well commented. For details have a look here:
http://people.cs.vt.edu/~ryder/5314/Projects/Prolog/SEdwardsPrologComments.pdf

You have to provide a document containing description for each solution
