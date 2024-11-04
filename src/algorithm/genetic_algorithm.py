from src.core.cube import Cube
from src.core.algorithm import Algorithm

import time
import random
from typing import Tuple

class GeneticAlgorithm(Algorithm):
    def __init__(self, population_size : int, number_of_iteration):
        super().__init__()
        self.__population_size = population_size
        self.initialize_population()
        self.__num_iteration = number_of_iteration
    
    # Initialize random cubes
    def initialize_population(self):
        self.__population = [Cube() for _ in range(self.__population_size)]
        self.sort_fitness_value()
    
    # Crossover by random point
    def crossover(self, parent1 : Cube, parent2 : Cube):

        # Get a random layer index to swap from
        layer_to_swap = random.randint(0, Cube.SIZE - 1)
        
        # Swap entire layers between parents
        for row in range(Cube.SIZE):
            for col in range(Cube.SIZE):
                # Swap the elements at the same position in the chosen layer
                parent1.get_cube()[layer_to_swap][row][col], parent2.get_cube()[layer_to_swap][row][col] = \
                    parent2.get_cube()[layer_to_swap][row][col], parent1.get_cube()[layer_to_swap][row][col]
    
    def mutate(self, individual : Cube, ):
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
        for _ in range(3):
            mutation_point1 = self.get_random_point_indexes()
            mutation_point2 = self.get_random_point_indexes()

            # Swap only if they are not the same
            if mutation_point1 != mutation_point2:
                layer1, row1, col1 = mutation_point1
                layer2, row2, col2 = mutation_point2

                # Swap two random positions within the cube
                individual.get_cube()[layer1][row1][col1], individual.get_cube()[layer2][row2][col2] = \
                    individual.get_cube()[layer2][row2][col2], individual.get_cube()[layer1][row1][col1]
                
    def print_point_indexes(point : Tuple[int,int,int]):
        print("(" + str(point[0]) + "," + str(point[1]) + "," + str(point[2]) + ")")

    def get_random_point_indexes(self) -> Tuple[int,int,int]:
        random_point = random.randint(0, self.__population[0].get_total_elements()-1)

        # Convert mutation point into indexes
        layer = random_point // (Cube.SIZE ** 2)
        row = (random_point % (Cube.SIZE ** 2)) // (Cube.SIZE)
        column = (random_point % Cube.SIZE) % Cube.SIZE

        return (layer, row, column)
    
    def selection_wheel(self):
        fitness_value_array = []
        for i in range (self.__population_size):
            fitness_value_array.append(self.__population[i].evaluate_fitness())

        new_population = []

        for _ in range (self.__population_size):

            # Total fitness
            total_fitness = sum(fitness_value_array)

            # Handle case when total_fitness is 0
            if total_fitness == 0:
                # Assign equal probabilities if total_fitness is 0
                probabilities = [1 / self.__population_size] * self.__population_size
            else:
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
        temp_population = sorted(self.__population, key=lambda individual: individual.evaluate_fitness())
        self.__population = temp_population

    def print_fitness_values(self):
        for i in range (self.__population_size):
            print("Fitness Cube ke-" + str(i) + ": " + str(self.__population[i].evaluate_fitness()) + "\n")

    # Core loop for running genetic algorithm
    def solve(self):
        current_cube = self.__population[self.__population_size-1]
        current_fitness = current_cube.evaluate_fitness()
        self.iterations.append(current_cube)
        self.fitness_values.append(current_fitness)
        start_time = time.time()
        # Calculate number of crossover process
        num_crossover = self.__population_size // 2
        # Iteration
        for _ in range (self.__num_iteration):
            # Even or odd (elitism)
            for j in range (0, num_crossover, 2):
                self.crossover(self.__population[j],self.__population[j+1])

            # Mutation
            for k in range (self.__population_size):
                # Mutation rate 10%
                mutation_number = random.randint(1,10)
                # 10% chance
                if (mutation_number == 1):
                    self.mutate(self.__population[k])
            # Selecting successors
            self.selection_wheel()
            # Ordering (highest value -> elite, unchanged)
            self.sort_fitness_value()

            current_cube = self.__population[self.__population_size-1]
            current_fitness = current_cube.evaluate_fitness()
            self.iterations.append(current_cube)
            self.fitness_values.append(current_fitness)

        end_time = time.time()
        duration = end_time - start_time
        self.duration = duration

        return self

# # Contoh penggunaan
# ga = GeneticAlgorithm(population_size=10, number_of_iteration=10)
# garesult = ga.solve()
# print("Final Cube:", garesult)
# print("Final Fitness:", garesult.cube.evaluate_fitness())
# print("Number of Iterations:",str(len(garesult.iterations)-1))
# print("Duration: ",garesult.duration)