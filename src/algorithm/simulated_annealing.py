# Import dependencies library from source
from src.core.cube import Cube
from src.core.algorithm import Algorithm
from src.utils.cube_utility import CubeUtility

# Import other libraries
import time
import random
import numpy as np

class SimulatedAnnealing(Algorithm):
    def __init__(self):
        # Referring to the parent class
        super().__init__()
        self.delta = 0
        self.temperatures = []
        self.local_optima_stuck_count = 0
        self.stuck_threshold = 100
        self.max_iterations = 1000  # Maximum number of iterations

    # Initialize cubes
    def initializeCube(self) -> Cube:
        return Cube()

    # Get random cube
    def randomCube(self):
        return self.cube.get_cube()

    # Get random float between 0 and 1
    def randomFloat(self) -> float:
        return random.uniform(0, 1)

    # Mapping each iteration into temperature
    def schedule(self, iteration) -> float:
        return max(0.01, np.exp(-0.001 * iteration))

    # Generate random float between 0 and 1
    def randomProbability(self) -> float:
        return random.uniform(0, 1)

    # Evaluate cube fitness value
    def evaluateCube(self, cube):
        return cube.evaluate_fitness()

    # Randomize cube for create neighbor
    def randomMove(self, cube):
        return CubeUtility().random_neighbor(cube)

    # Acceptance probability
    def AcceptanceProbability(self, delta, temperature) -> float:
        return np.exp(-delta / temperature)

    # Core loop for running simulated annealing
    def solve(self) -> Algorithm:
        current_cube = self.initializeCube()
        current_fitness = self.evaluateCube(current_cube)
        start_time = time.time()

        iteration = 0
        temperature = self.schedule(iteration)
        no_improvement_steps = 0

        self.iterations.append(current_cube)
        self.fitness_values.append(current_fitness)

        while iteration < self.max_iterations and temperature > 0.01:
            neighbor = self.randomMove(current_cube)
            neighbor_fitness = self.evaluateCube(neighbor)
            delta = neighbor_fitness - current_fitness

            if delta > 0:
                # Accept the new neighbor if it's better
                current_cube, current_fitness = neighbor, neighbor_fitness
                no_improvement_steps = 0
            else:
                # Accept with probability if it's worse
                if self.randomProbability() < self.AcceptanceProbability(delta, temperature):
                    current_cube, current_fitness = neighbor, neighbor_fitness
                    no_improvement_steps = 0
                else:
                    no_improvement_steps += 1

            # Check for local optimum
            if no_improvement_steps >= self.stuck_threshold:
                self.local_optima_stuck_count += 1
                no_improvement_steps = 0  # Reset counter after counting

            # Update temperature and log values
            iteration += 1
            temperature = self.schedule(iteration)

            self.iterations.append(current_cube)
            self.fitness_values.append(current_fitness)
            self.temperatures.append(temperature)

        # Duration
        self.duration = time.time() - start_time

        print("Local Optimum Stuck:",self.local_optima_stuck_count)

        return self

# # Contoh penggunaan
# sa = SimulatedAnnealing()
# saresult = sa.solve()
# print("Final Cube:", saresult)
# print("Final Fitness:", saresult.cube.evaluate_fitness())
# print("Number of Iterations:", len(saresult.fitness_values)-1)
# print("Local Optima Stuck Count:", sa.local_optima_stuck_count)
# print("Duration:", sa.duration)
