from search import Problem
from math import sqrt

class P2(Problem):

    def __init__(self, initial, goal=( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0 ) ):
        self.goal = goal
        Problem.__init__(self, initial, goal)

    def find_blank_square(self, state):
        return state.index(0)

    def actions(self, state):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 4 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 4:
            possible_actions.remove('UP')
        if index_blank_square % 4 == 3:
            possible_actions.remove('RIGHT')
        if index_blank_square > 11:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -4, 'DOWN': 4, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal

    def check_solvability(self, state):
        inversion = 0
        for i in range(len(state)):
            for j in range(i, len(state)):
                if state[i] > state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

class FifteenPuzzleMiss(P2):
    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """
        return sum(s != g for (s, g) in zip(node.state, self.goal))


# Manhattan method
class FifteenPuzzleMht(P2):
    def h(self, node):
        """ implement Manhattan distance. Hint! Look at
        Missplaced Tiles heuristic function above """
        dist = 0
        for state, goal in zip(node.state, self.goal):
            statePozX = state / 4;
            statePozY = state % 4;
            goalPozX = goal / 4;
            goalPozY = goal % 4;
            dist += abs(statePozX - goalPozX) + abs(statePozY - goalPozY)
        return dist

class FifteenPuzzleR_C(P2):
    def h(self, node):
        dist = 0
        for state, goal in zip(node.state, self.goal):
            statePozX = state / 4;
            statePozY = state % 4;
            goalPozX = goal / 4;
            goalPozY = goal % 4;
            dist += ((statePozX != goalPozX) + (statePozY != goalPozY))

        return dist

# Euclidean distance
class FifteenPuzzleEucl(P2):
    def h( self, node):
        dist = 0
        for state, goal in zip(node.state, self.goal):
            statePozX = state / 4;
            statePozY = state % 4;
            goalPozX = goal / 4;
            goalPozY = goal % 4;
            dist += sqrt( pow(statePozX - goalPozX, 2) + pow(statePozY - goalPozY, 2) )

        return dist


   
