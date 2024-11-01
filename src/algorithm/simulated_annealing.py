from ...src.core.cube import Cube
from ...src.core.algorithm import Algorithm
from ...src.utils.cube_utility import CubeUtility

import time
import random
import numpy as np
import matplotlib.pyplot as plt

class SimulatedAnnealing(Algorithm):
    def __init__(self, cube):
        super().__init__()
        self.cube = cube
        self.delta = 0
        self.iterations = []
        self.fitness_values = []
        self.temperatures = []
        self.local_optima_stuck_count = 0
        self.stuck_threshold = 100

    def initializeCube(self) -> Cube:
        return Cube()

    def randomCube(self):
        return self.cube.get_cube()

    def randomFloat(self)-> float:
        return random.uniform(0,1)

    def schedule(self, iteration)-> float:
        return max(0.01, np.exp(-0.001 * iteration))

    def randomProbability(self)-> float:
        return random.uniform(0,1)

    def evaluateCube(self, cube):
        return cube.evaluate_fitness()

    def randomMove(self, cube):
        return CubeUtility().random_neighbor(cube)

    def AcceptanceProbability(self, delta, temperature) -> float:
        return np.exp(-delta/temperature)

    def solve(self) -> Cube:
        current_cube = self.initializeCube()
        current_fitness = self.evaluateCube(current_cube)
        start_time = time.time()

        iteration = 0
        temperature = self.schedule(iteration)
        no_improvement_steps = 0

        while True:
            if temperature == 0:
                return current_cube

            neighbor = self.randomMove(current_cube)
            neighbor_fitness = self.evaluateCube(neighbor)
            delta = neighbor_fitness - current_fitness

            if delta > 0:
                current_cube, current_fitness = neighbor, neighbor_fitness
                no_improvement_steps = 0
            else:
                if self.randomProbability() < self.AcceptanceProbability(delta, temperature):
                    current_cube, current_fitness = neighbor, neighbor_fitness
                    no_improvement_steps = 0
                else:
                    current_cube, current_fitness = current_cube, current_fitnes
                    no_improvement_steps += 1

            if no_improvement_steps >= self.stuck_threshold:
                self.local_optima_stuck_count += 1
                no_improvement_steps = 0

            self.iterations.append(iteration)
            self.fitness_values.append(current_fitness)
            self.temperatures.append(temperature)

            iteration += 1
            temperature = self.schedule(iteration)

            end_time = time.time()
            duration = end_time - start_time

            if duration > 1000:
                print(f"Objective Value: {current_fitness}")
                print(f"Duration: {duration} seconds")
                break

        print(f"Final Objective Value: {current_fitness}")
        print(f"Duration: {duration} seconds")

        self.plotResults()

        return current_cube

    def plot_results(self):
        # Plot objective function values
        plt.figure(figsize=(12, 6))
        plt.plot(self.iterations, self.fitness_values, label='Objective Function')
        plt.xlabel('Iteration')
        plt.ylabel('Objective Function Value')
        plt.title('Objective Function Value over Iterations')
        plt.legend()
        plt.show()

        # Plot temperature schedule
        plt.figure(figsize=(12, 6))
        plt.plot(self.iterations, self.temperatures, label='Temperature', color='orange')
        plt.xlabel('Iteration')
        plt.ylabel('Temperature')
        plt.title('Temperature over Iterations')
        plt.legend()
        plt.show()