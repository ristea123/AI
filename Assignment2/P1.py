from search import Problem

size1 = 4
size2 = 3

class P1(Problem):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        self.visited_states = []
        Problem.__init__(self, self.initial, self.goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        return action

    def actions(self, current_state):
        actions = []
        self.visited_states.append(current_state)
        new_state = ( size1, current_state[1] )
        if current_state[0] != size1:
            actions.append(new_state)

        new_state = ( current_state[0], size2 )
        if current_state[1] != size2:
            actions.append(new_state)

        new_state = ( 0, current_state[1] )
        if current_state[0] != 0:
            actions.append(new_state)

        new_state = ( current_state[0], 0 )
        if current_state[1] != 0:
            actions.append(new_state)

        if current_state[0] + current_state[1] <= size1:
            new_state = ( current_state[0] + current_state[1], 0 )
        else:
            new_state = ( size2, current_state[1] - ( size2 - current_state[0] ) )
        if current_state[0] != size1:
            actions.append( new_state )

        if current_state[0] + current_state[1] <= size2:
            new_state = ( 0, current_state[0] + current_state[1] )
        else:
            new_state = ( current_state[0] - ( size2 - current_state[1] ), size2 )
        if current_state[1] != size2:
            actions.append( new_state )
        
        return actions
