from src.core.cube import Cube
from src.core.algorithm import Algorithm
from src.utils.cube_utility import CubeUtility

import time

class Stochastic(Algorithm):
    def __init__(self, maximum_move):
        super().__init__()
        self.maximum_iteration = maximum_move

    def initializeCube(self) -> Cube:
        return Cube()
    
    def randomCube(self):
        return self.cube.get_cube()
    
    def evaluateCube(self, cube):
        return cube.evaluate_fitness()
    
    def randomMove(self, cube):
        return CubeUtility().random_neighbor(cube)
    
    def solve(self) -> Algorithm:
        current_cube = self.initializeCube()
        current_fitness = self.evaluateCube(current_cube)
        start_time = time.time()

        self.iterations.append(current_cube)
        self.fitness_values.append(current_fitness)

        for _ in range (self.maximum_iteration):
            neighbor = self.randomMove(self.cube)
            neighbor_fitness = self.evaluateCube(neighbor)

            if neighbor_fitness > current_fitness:
                current_cube = neighbor
                current_fitness = neighbor_fitness
            
            self.iterations.append(current_cube)
            self.fitness_values.append(current_fitness)

        end_time = time.time()
        duration = end_time - start_time
        self.duration = duration

        return self

# # Contoh penggunaan
# sto = Stochastic(10)
# storesult = sto.solve()
# print("Final Cube:", storesult)
# print("Final Fitness:", storesult.cube.evaluate_fitness())
# print("Number of Iterations:",str(len(storesult.iterations)-1))
# print("Duration: ",storesult.duration)