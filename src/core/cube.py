import random
from collections import Counter

class Cube:
    SIZE = 5

    def __init__(self):
        self.size = Cube.SIZE
        self.total_elements = Cube.SIZE ** 3
        self.magic_constant = Cube.calculate_magic_constant(Cube.SIZE)
        self.__cube = self.initialize_cube()
    
    def initialize_cube(self):
        # Array of distinct values
        values = [i for i in range (1,self.total_elements+1)]

        # Initialize 3D array with '0'
        cube = [[[0 for _ in range(self.size)] for _ in range(self.size)] for _ in range(self.size)]

        # Assign random values into 3D array
        for layer in range (self.size):
            for row in range (self.size):
                for column in range (self.size):
                    index = random.randint(0,len(values)-1)
                    cube[layer][row][column] = values.pop(index)
        
        return cube
    
    def display_cube(self):
        for i, face in enumerate(self.__cube):
            print(f"Layer {i+1}:")
            for row in face:
                print(row)
            print()

    def get_cube(self):
        return self.__cube

    def get_size(self):
        return self.size
    
    def get_total_elements(self):
        return self.total_elements
    
    def get_magic_constant(self):
        return self.magic_constant
    
    def check_duplicates(self):
        # Flatten the 3D cube into a 1D list
        flattened_cube = [self.__cube[layer][row][col] 
                          for layer in range(Cube.SIZE) 
                          for row in range(Cube.SIZE) 
                          for col in range(Cube.SIZE)]
        
        # Use Counter to count the occurrences of each element
        counts = Counter(flattened_cube)
        
        # Prepare the result to show elements with duplicates
        duplicates_info = {value: count for value, count in counts.items() if count > 1}
        
        # Display the results
        if duplicates_info:
            print("Duplicates found:")
            for value, count in duplicates_info.items():
                print(f"Element {value} appears {count} times.")
            print(f"Total elements with duplicates: {len(duplicates_info)}")
        else:
            print("No duplicates, the cube is valid.")

        return duplicates_info
    
    @staticmethod
    def calculate_magic_constant(size: int = 5) -> int:
        # Formula for the magic constant of an n x n magic cube
        return size * (size**3 + 1) // 2

    def sum_column(self, i : int, k : int) -> int:
        total = 0
        for j in range (self.size):
            total += self.__cube[i][j][k]
        return total

    def sum_row(self, i : int, j : int) -> int:
        total = 0
        for k in range (self.size):
            total += self.__cube[i][j][k]
        return total
    
    def sum_layer(self, j : int, k : int) -> int:
        total = 0
        for i in range (self.size):
            total += self.__cube[i][j][k]
        return total

    def sum_diagonal_plane_layer(self, i : int) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[i][m][m]
        return total
    
    def sum_diagonal_plane_layer_reverse(self, i : int) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[i][self.size-1-m][m]
        return total
    
    def sum_diagonal_plane_row(self, j : int) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[m][j][m]
        return total
    
    def sum_diagonal_plane_row_reverse(self, j : int) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[self.size-1-m][j][m]
        return total
    
    def sum_diagonal_plane_column(self, k : int) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[m][m][k]
        return total
    
    def sum_diagonal_plane_column_reverse(self, k : int) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[self.size-1-m][m][k]
        return total
    
    def sum_diagonal_plane_reverse(self, i : int) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[i][m][self.size-1-m]
        return total

    def sum_diagonal_space_one(self) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[m][m][m]
        return total
    
    def sum_diagonal_space_two(self) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[self.size-1-m][self.size-1-m][m]
        return total
    
    def sum_diagonal_space_three(self) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[self.size-1-m][m][m]
        return total
    
    def sum_diagonal_space_four(self) -> int:
        total = 0
        for m in range (self.size):
            total += self.__cube[m][self.size-1-m][m]
        return total
    
    # Number of lines that equals magic_constant
    def evaluate_fitness(self) -> int:
        # Fitness value
        fitness_value = 0

        # Check sum of layers, rows, and columns
        for i in range(self.size):
            for j in range(self.size):
                if self.sum_layer(j, i) == self.magic_constant:
                    fitness_value += 1
                if self.sum_row(i, j) == self.magic_constant:
                    fitness_value += 1
                if self.sum_column(i, j) == self.magic_constant:
                    fitness_value += 1

            # Check plane diagonals within the same layer
            if self.sum_diagonal_plane_layer(i) == self.magic_constant:
                fitness_value += 1
            if self.sum_diagonal_plane_layer_reverse(i) == self.magic_constant:
                fitness_value += 1

        # Check diagonal planes within the same row
        for j in range(self.size):
            if self.sum_diagonal_plane_row(j) == self.magic_constant:
                fitness_value += 1
            if self.sum_diagonal_plane_row_reverse(j) == self.magic_constant:
                fitness_value += 1

        # Check diagonal planes within the same column
        for k in range(self.size):
            if self.sum_diagonal_plane_column(k) == self.magic_constant:
                fitness_value += 1
            if self.sum_diagonal_plane_column_reverse(k) == self.magic_constant:
                fitness_value += 1

        # Diagonal space
        if (self.sum_diagonal_space_one() == self.magic_constant):
            fitness_value += 1
        if (self.sum_diagonal_space_two() == self.magic_constant):
            fitness_value += 1
        if (self.sum_diagonal_space_three() == self.magic_constant):
            fitness_value += 1
        if (self.sum_diagonal_space_four() == self.magic_constant):
            fitness_value += 1

        return fitness_value

# Contoh penggunaan
magic_cube = Cube()
magic_cube.display_cube()
print(magic_cube.get_magic_constant())
print(magic_cube.evaluate_fitness())