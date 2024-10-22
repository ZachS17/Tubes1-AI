import random
from ..core.cube import Cube

class CubeUtility:
    def random_neighbor(self):
        # Randomly select two positions in the cube
        layer1, row1, col1 = random.randint(0, self.get_size() - 1), random.randint(0, self.get_size() - 1), random.randint(0, self.get_size() - 1)
        layer2, row2, col2 = random.randint(0, self.get_size() - 1), random.randint(0, self.get_size() - 1), random.randint(0, self.get_size() - 1)

        # Swap the values at the two positions
        self.__cube[layer1][row1][col1], self.__cube[layer2][row2][col2] = self.__cube[layer2][row2][col2], self.__cube[layer1][row1][col1]
