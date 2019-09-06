import numpy as np 
import sys
import math


class Solver:
        def __init__(self):
                self.symmetric_boats = 1 # should the # of boats be always even?

        def find_solution(self, C1, C2, C, V1, V2, V):
                boat2_only = math.ceil(C / C2) # boat2 is the preferred tool
                if self.symmetric_boats:
                        if boat2_only % 2:
                                boat2_only += 1
                if boat2_only * V2 <= V:
                        print(str(0) + ', ' + str(boat2_only))
                        return 
                # check if a feasible solution is possible
                if V1 < V2 or (C1 / V1) > (C2 / V2):
                        boat1_only = math.ceil(C / C1)
                        if self.symmetric_boats:
                                if boat1_only % 2:
                                        boat1_only += 1
                        if boat1_only * V1 > V:
                                print('No feasible solution.')
                                return
                # Need to solve with constraint programming, find gradient and then optimize
                x = np.linalg.solve(np.array([[C1, V1], [C2, V2]]), np.array([C, V]))
                x2 = math.floor(x[1])
                if self.symmetric_boats:
                        if x2 % 2:
                                x2 -= 1
                x1 = math.ceil((C - x2 * C2) / C1)
                assert V1* x1 + V2*x2 <= V
                print(str(x1) + ', ' + str(x2))


if __name__ == '__main__':
        s = Solver()
        for C1 in range(1, 5):
                for C2 in range(15, 25):
                        for V1 in np.arange(0.05, 0.10, 0.01):
                                for V2 in np.arange(1.5, 3.5, 0.5):
                                        s.find_solution(C1, C2, int(sys.argv[1]), V1, V2, int(sys.argv[2]))
