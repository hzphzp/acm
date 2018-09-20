'''
wrong!!! I shoud have known. There is only three parameter to describe the problem
I mean, if I use (x1, y1, x2, y2), then x2 and y2 is determined by x1 and y1, 
so it's redundant.
I am supposed to use (x, y, b), where x means the number of missionaries in one bank, and y
the cannibals, b indicates if there boat in this bank.
I will fix the code later if I am free

'''
import numpy as np


def legal(state: np.ndarray):
        if(state[0][0] > 0):
            if(state[0][0] < state[0][1]):
                return False
        if(state[1][0] > 0):
            if(state[1][0] < state[1][1]):
                return False
        if not np.all(state >= 0):
            return False
        return True


class Move:
    # this is the basic class of the sets of moving funcions
    __moving_type = [[[-1, 0], [1, 0]], [[0, -1], [0, 1]], [[-2, 0], [2, 0]], [[0, -2], [0, 2]], [[-1, -1], [1, 1]]]

    def left(self, state: np.ndarray):
        next_state = []
        for moving in self.__moving_type:
            result = state + np.array(moving)
            if legal(result):
                next_state.append(result)
        return next_state

    def right(self, state: np.ndarray):
        next_state = []
        for moving in self.__moving_type:
            result = state - np.array(moving)
            if legal(result):
                next_state.append(result)
        return next_state


class Solution:
    missionaries_number = 0
    cannibals_number = 0
    states = []
    left_next_states = []
    right_next_states = []
    move = Move()

    def __init__(self, init_state: np.ndarray):
        self.missionaries_number = init_state[0][0] + init_state[1][0]
        self.cannibals_number = init_state[0][1] + init_state[1][1]
        for i in range(self.missionaries_number):
            for j in range(self.cannibals_number):
                toadd = np.array([[i, j], [self.missionaries_number - i, self.cannibals_number - j]])

                if legal(toadd):
                    self.states.append(toadd)
                    self.left_next_states.append(self.move.left(toadd))
                    self.right_next_states.append(self.move.right(toadd))

    def find_path(self, init_state, goal_state):
        step = 0
        current_state = init_state
        path = []
        while not np.all(current_state == goal_state):
            path.append(current_state)






if __name__ == "__main__":
    init_state = [[3, 3], [0, 0]]
    goal_state = [[0, 0], [3, 3]]
    init_state = np.array(init_state)
    goal_state = np.array(goal_state)
    solution = Solution(init_state)
    print(solution.states)
    print(solution.left_next_states)
    print(solution.right_next_states)