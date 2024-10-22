from ...src.core.cube import Cube
from ...src.core.algorithm import Algorithm

import random
from typing import Tuple

class GeneticAlgorithm(Algorithm):
    def __init__(self, population_size : int):
        self.__population_size = population_size
        self.__population = self.initialize_population(population_size)
    
    # Initialize random cubes
    def initialize_population(self):
        return self.sort_fitness_value([Cube() for _ in range(Cube.SIZE)])
    
    # Crossover by random point
    def crossover(self, parent1 : Cube, parent2 : Cube):
        # Get the random crossover point
        crossover_point = self.get_random_point_indexes()

        layer = crossover_point[0]
        row = crossover_point[1]
        column = crossover_point[2]

        # Crossover process
        
        # Swap values for the specific layer
        for j in range (row, Cube.SIZE):
            for k in range (column, Cube.SIZE):
                parent1[layer][j][k], parent2[layer][j][k] = parent2[layer][j][j], parent1[layer][j][k]

        # Continue swap for next layers
        for i in range (layer+1, Cube.SIZE):
            for j in range (Cube.SIZE-1):
                for k in range (Cube.SIZE-1):
                    parent1[i][j][k], parent2[i][j][k] = parent2[i][j][j], parent1[i][j][k]
    
    def mutate(self, individual):
        # # Option1
        # Changes cells with any random number (most likely leads to duplicate numbers)
        # # Get the random crossover point
        # mutation_point = self.get_random_point_indexes()

        # layer = mutation_point[0]
        # row = mutation_point[1]
        # column = mutation_point[2]
        
        # # Mutate with random number
        # individual[layer][row][column] = random.randint(1,self.__cube.get_total_elements)

        # Option 2 (more logical)
        # # Swap values randomly hence no duplicates (heuristic, is it okay ??)

        # Try 3 swap for more variations
        for i in range (3):
            mutation_point1 = self.get_random_point_indexes()

            layer1 = mutation_point1[0]
            row1 = mutation_point1[1]
            column1 = mutation_point1[2]

            mutation_point2 = self.get_random_point_indexes()

            layer2 = mutation_point2[0]
            row2 = mutation_point2[1]
            column2 = mutation_point2[2]

            individual[layer1][row1][column1], individual[layer2][row2][column2] = individual[layer2][row2][column2], individual[layer1][row1][column1]

    def get_random_point_indexes(self) -> Tuple[int,int,int]:
        random_point = random.randint(0, Cube.SIZE-1)

        # Convert mutation point into indexes
        layer = random_point // (Cube.SIZE ** 2)
        row = (random_point % Cube.SIZE) // (Cube.SIZE)
        column = (random_point % Cube.SIZE) % Cube.SIZE

        return (layer, row, column)
    
    def selection_wheel(self):
        fitness_value_array = []
        for i in range (self.__population_size):
            fitness_value_array.append(self.__population[i].evaluate_fitness())

        new_population = []

        for j in range (self.__population_size):

            # Total fitness
            total_fitness = sum(fitness_value_array)

            # Probabilities
            probabilities = [f / total_fitness for f in fitness_value_array]

            # Cumulative
            cumulative_probabilities = []
            cumulative_sum = 0
            for p in probabilities:
                cumulative_sum += p
                cumulative_probabilities.append(cumulative_sum)

            # Random number between 0 and 1
            random_number = random.random()

            # Find the index corresponding to the number
            selected_index = None
            for index, cumulative in enumerate(cumulative_probabilities):
                if random_number <= cumulative:
                    selected_index = index
                    break

            new_population.append(self.__population[selected_index])
        
        self.__population = new_population

    def sort_fitness_value(self):
        temp_population = sorted(self.__population, key=self.__population[0].evaluate_fitness())

    # Core loop for running genetic algorithm
    def solve(self, population_size, num_iteration):
        # Calculate number of crossover process
        num_crossover = population_size // 2
        # Iteration
        for i in range (num_iteration):
            # Even or odd (elitism)
            for j in range (0, num_crossover, 2):
                self.crossover(self.__population[j],self.__population[j+1])
            # Mutation
            for k in range (population_size):
                # Mutation rate 10%
                mutation_number = random.randint(1,10)
                # 10% chance
                if (mutation_number == 1):
                    self.mutate(self.__population[k])
            # Selecting successors
            self.selection_wheel()
            # Ordering (highest value -> elite, unchanged)
            self.sort_fitness_value()

# Contoh penggunaan
ga = GeneticAlgorithm(population_size=10)
ga.solve(population_size=10, num_iteration=100)