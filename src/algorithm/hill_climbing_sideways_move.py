from src.core.cube import Cube
from src.core.algorithm import Algorithm
from src.utils.cube_utility import CubeUtility

import time

class HillClimbingSidewaysMove(Algorithm):
    def __init__(self, maximum_move):
        super().__init__()
        self.maximum_sideways_move = maximum_move

    def initializeCube(self) -> Cube:
        return Cube()
    
    def randomCube(self):
        return self.cube.get_cube()
    
    def evaluateCube(self, cube):
        return cube.evaluate_fitness()
    
    def bestNeighbor(self, cube):
        return CubeUtility().find_greatest_value_neighbor(cube)
    
    def solve(self) -> Algorithm:
        current_cube = self.initializeCube()
        current_fitness = self.evaluateCube(current_cube)
        start_time = time.time()

        sideways_move = 0

        self.iterations.append(current_cube)
        self.fitness_values.append(current_fitness)

        while True:
            neighbor = self.bestNeighbor(self.cube)
            neighbor_fitness = self.evaluateCube(neighbor)

            if neighbor_fitness > current_fitness:
                current_cube = neighbor
                current_fitness = neighbor_fitness
                sideways_move = 0
            elif neighbor_fitness == current_fitness:
                current_cube = neighbor
                current_fitness = neighbor_fitness
                sideways_move += 1
            
            self.iterations.append(current_cube)
            self.fitness_values.append(current_fitness)

            if sideways_move == self.maximum_sideways_move:
                end_time = time.time()
                duration = end_time - start_time
                self.duration = duration
                break

        return self

# # Contoh penggunaan
# hcsm = HillClimbingSidewaysMove(10)
# hcsmresult = hcsm.solve()
# print("Final Cube:", hcsmresult)
# print("Final Fitness:", hcsmresult.cube.evaluate_fitness())
# print("Number of Iterations:",str(len(hcsmresult.iterations)-1))
# print("Duration: ",str(hcsmresult.duration))