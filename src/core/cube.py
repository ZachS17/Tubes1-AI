import random

class Cube:
    def __init__(self, size):
        self.SIZE = size
        self.TOTAL_ELEMENTS = size ** 3
        self.MAGIC_CONSTANT = Cube.calculate_magic_constant(size)
        self.__cube = self.initialize_cube()
    
    def initialize_cube(self):
        # Array of distinct values
        values = [i for i in range (1,self.TOTAL_ELEMENTS+1)]

        # Initialize 3D array with '0'
        cube = [[[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)] for _ in range(self.SIZE)]

        # Assign random values into 3D array
        for layer in range (self.SIZE):
            for row in range (self.SIZE):
                for column in range (self.SIZE):
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
        return self.SIZE
    
    def get_total_elements(self):
        return self.TOTAL_ELEMENTS
    
    def get_magic_constant(self):
        return self.MAGIC_CONSTANT
    
    @staticmethod
    def calculate_magic_constant(size: int) -> int:
        # Formula for the magic constant of an n x n magic square/cube
        return size * (size**2 + 1) // 2

# Contoh penggunaan
magic_cube = Cube()
magic_cube.display_cube()