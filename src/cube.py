import random

class Cube:
    SIZE = 5
    TOTAL_ELEMENTS = 125

    def __init__(self):
        self.__cube = self.initialize_cube()
    
    def initialize_cube(self):
        # Array of distinct values
        values = [i for i in range (1,Cube.TOTAL_ELEMENTS+1)]

        # Initialize 3D array with '0'
        cube = [[[0 for _ in range(Cube.SIZE)] for _ in range(Cube.SIZE)] for _ in range(Cube.SIZE)]

        # Assign random values into 3D array
        for layer in range (Cube.SIZE):
            for row in range (Cube.SIZE):
                for column in range (Cube.SIZE):
                    index = random.randint(0,len(values)-1)
                    cube[layer][row][column] = values.pop(index)
        
        return cube
    
    def display_cube(self):
        for i, face in enumerate(self.__cube):
            print(f"Layer {i+1}:")
            for row in face:
                print(row)
            print()

    def get_size(self):
        return Cube.SIZE
    
    def random_neighbor(self):
        # Randomly select two positions in the cube
        layer1, row1, col1 = random.randint(0, Cube.SIZE - 1), random.randint(0, Cube.SIZE - 1), random.randint(0, Cube.SIZE - 1)
        layer2, row2, col2 = random.randint(0, Cube.SIZE - 1), random.randint(0, Cube.SIZE - 1), random.randint(0, Cube.SIZE - 1)

        # Swap the values at the two positions
        self.__cube[layer1][row1][col1], self.__cube[layer2][row2][col2] = self.__cube[layer2][row2][col2], self.__cube[layer1][row1][col1]

# Contoh penggunaan
magic_cube = Cube()
magic_cube.display_cube()
magic_cube.random_neighbor()
magic_cube.display_cube()