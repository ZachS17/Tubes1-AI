'''
Objective : Menyelesaikan permasalahan Magic Cube
Tasks:
1. State awal dan akhir dari kubus
2. Nilai objective function akhir yang dicapai
3. Plot nilai objective function terhadap banyak iterasi yang telah dilewati
4. Durasi proses pencarian
5. Banyak iterasi hingga proses pencarian berhenti
Note: Tambahkan parameter maximum sideways move, dimana ketika banyak sideways move yang dilakukan sudah mencapai maksimum, pencarian dihentikan
'''

from ...src.core.cube import Cube
from ...src.core.algorithm import Algorithm
from ...src.utils.cube_utility import CubeUtility

import time
import random
import numpy as np
import matplotlib.pyplot as plt

class HillClimbingSidewaysMove(Algorithm):
    def __init__(self, cube):
        super().__init__()
        self.cube = cube
        self.iterations = []
        self.fitness_values = []
        self.maximum_sideways_move = 100

    def initializeCube(self) -> Cube:
        return Cube()
    
    def randomCube(self):
        return self.cube.get_cube()

    def randomFloat(self) -> float:
        return random.uniform(0, 1)
    
    def evaluateCube(self, cube):
        return cube.evaluate_fitness()
    
    def randomMove(self, cube):
        return CubeUtility().random_neighbor(cube)
    
    def solve(self) -> Cube:
        current_cube = self.initializeCube()
        current_fitnes = self.evaluateCube(current_cube)
        start_time = time.time()

        iteration = 0
        sideways_move = 0

        while True:
            neighbor = self.randomMove(current_cube)
            neighbor_fitness = self.evaluateCube(neighbor)

            if neighbor_fitness > current_fitness:
                current_cube = neighbor
                current_fitnes = neighbor_fitness
                sideways_move = 0
            else:
                sideways_move += 1
            
            if sideways_move == self.maximum_sideways_move:
                break
            
            iteration += 1
            
            self.iterations.append(iteration)
            self.fitness_values.append(current_fitness)

            end_time = time.time()
            duration = end_time - start_time

            if duration > 1000:
                print(f"Objective Value: {current_fitness}")
                print(f"Duration: {duration} seconds")
                print(f"Iterations: {iteration}")
                break

        print(f"Final Objective Value: {current_fitness}")
        print(f"Duration: {duration} seconds")
        print(f"Iterations: {iteration}")

        self.plotResults()

        return current_cube

    def plotResults(self):
        # Plot objective function values
        plt.figure(figsize=(12, 6))
        plt.plot(self.iterations, self.fitness_values, label='Objective Function')
        plt.xlabel('Iteration')
        plt.ylabel('Objective Function Value')
        plt.title('Objective Function Value over Iterations')
        plt.legend()
        plt.show()
