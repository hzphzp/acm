'''
wrong!!! I shoud have known. There is only three parameter to describe the problem
I mean, if I use (x1, y1, x2, y2), then x2 and y2 is determined by x1 and y1, 
so it's redundant.
I am supposed to use (x, y, b), where x means the number of missionaries in one bank, and y
the cannibals, b indicates if there boat in this bank, 1 denote that there is a boat, -1 denote the opposite.
I will fix the code later if I am free

'''


def legal(state: list, init_state: list):
        if(state[0] > 0):
            if(state[0] < state[1]):
                return False
        if(state[0] < 3):
            if(state[0] > state[1]):
                return False
        if not 0 <= state[0] <= init_state[0]:
            return False
        if not 0 <= state[1] <= init_state[1]:
            return False
        if state[2] != -1 and state[2] != 1:
            return False
        return True


class Move:
    # this is the basic class of the sets of moving funcions
    __moving_type = [[-1, 0], [0, -1], [-2, 0], [0, -2], [-1, -1]]

    def __init__(self, init_state: list):
        self.init_state = init_state

    def move(self, state: list):
        next_state = []
        for x, y in self.__moving_type:
            result = state.copy()
            result[0] += result[2] * x
            result[1] += result[2] * y
            result[2] = result[2] * (-1)
            if legal(result, self.init_state):
                next_state.append(result)
        return next_state

    def __call__(self, state: list):
        return self.move(state)


class Solution:
    def __init__(self, init_state: list):
        if init_state[2] == -1:
            print("this initial state is not legal, there should be a boat in the initial time")
            return None
        self.init_state = init_state
        self.missionaries_number = init_state[0]
        self.cannibals_number = init_state[1]
        self.move = Move(init_state)
        self.states = []
        self.next_states = []
        for x in range(self.missionaries_number + 1):
            for y in range(self.cannibals_number + 1):
                for b in (-1, 1):
                    '''
                        toadd = [x, y, b]
                        if legal(toadd, init_state):
                        self.states.append(toadd)
                        self.next_states.append(self.move(toadd))
                    '''
                    if legal([x, y, b], init_state):
                        self.states.append([x, y, b])
                        self.next_states.append(self.move([x, y, b]))

    def find_path(self, goal_state: list):
        # Breadth-First-Search
        visited = [0 for x in self.states]
        to_visit = []
        its_father = [-1 for x in self.states]
        to_visit.append(self.init_state)
        path = []
        while not len(to_visit) == 0:
            current_state = to_visit.pop(0)
            for child in self.next_states[self.states.index(current_state)]:
                if visited[self.states.index(child)] == 1:
                    continue
                if child == goal_state:
                    print("I find the best solution")
                    path.append(goal_state)
                    path.append(current_state)
                    father = its_father[self.states.index(current_state)]
                    while father != self.init_state:
                        path.append(father)
                        father = its_father[self.states.index(father)]
                    path.append(self.init_state)
                    return list(reversed(path))
                visited[self.states.index(child)] = 1
                to_visit.append(child)
                its_father[self.states.index(child)] = current_state


if __name__ == "__main__":
    init_state = [3, 3, 1]
    goal_state = [0, 0, -1]
    solution = Solution(init_state)
    print(solution.find_path(goal_state))