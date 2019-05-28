from search import *
from P1 import P1
from P2 import *
import time

def main():

    print("P1 results ")
    problem_P1 = P1((0,0), (2,0))
    start1 = time.time()
    path1 = breadth_first_graph_search(problem_P1).solution()
    end1 = time.time()

    print(path1, ' ', end1 - start1)

    start2 = time.time()
    path2 = depth_first_graph_search(problem_P1).solution()
    end2 = time.time()

    print(path2, ' ', end2 - start2, '\n')

    print("P2 results ")

    P2Eucl = FifteenPuzzleEucl((1, 2, 4, 0, 5, 6, 3, 7, 10, 11, 12, 8, 9, 13, 14, 15), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))

    start3 = time.time()
    path3 = astar_search(P2Eucl).solution()
    end3 = time.time()
    print(path3, ' ', end3 - start3)

    P2R_C = FifteenPuzzleR_C((1, 2, 4, 0, 5, 6, 3, 7, 10, 11, 12, 8, 9, 13, 14, 15), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))

    start4 = time.time()
    path4 = astar_search(P2R_C).solution()
    end4 = time.time()
    print(path4, ' ', end4 - start4)

    P2Mht = FifteenPuzzleMht((1, 2, 4, 0, 5, 6, 3, 7, 10, 11, 12, 8, 9, 13, 14, 15), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))

    start5 = time.time()
    path5 = astar_search(P2Mht).solution()
    end5 = time.time()
    print(path5, ' ', end5 - start5)

    P2Miss = FifteenPuzzleMiss((1, 2, 4, 0, 5, 6, 3, 7, 10, 11, 12, 8, 9, 13, 14, 15), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))

    start6 = time.time()
    path6 = astar_search(P2Miss).solution()
    end6 = time.time()
    print(path6, ' ', end6 - start6, '\n')

    """ Compare searchers """
    compare_searchers(problems  = [P2Eucl, P2R_C, P2Mht,P2Miss],
                      header    = ['Searcher', 'A* h1(n)', 'A* h2(n)', 'A* h3(n)', 'A* h4(n)' ], 
                      searchers = [ astar_search ] )
   

if __name__ == "__main__":
    main()

