import random
from ..core.cube import Cube

class CubeUtility:
    def random_neighbor(self, cube : Cube):
        # Randomly select two positions in the cube
        layer1, row1, col1 = random.randint(0, cube.get_size() - 1), random.randint(0, cube.get_size() - 1), random.randint(0, cube.get_size() - 1)
        layer2, row2, col2 = random.randint(0, cube.get_size() - 1), random.randint(0, cube.get_size() - 1), random.randint(0, cube.get_size() - 1)

        # Swap the values at the two positions
        cube.get_cube()[layer1][row1][col1], cube.get_cube()[layer2][row2][col2] = cube.get_cube()[layer2][row2][col2], cube.get_cube()[layer1][row1][col1]

        return cube

    def find_greatest_value_neighbor(self, cube : Cube):
        # Original fitness
        original_fitness = cube.evaluate_fitness()
        best_fitness = original_fitness
        best_cube = [layer[:] for layer in cube.get_cube()]

        # All possible pair of elements
        for layer1 in range(cube.size):
            for row1 in range(cube.size):
                for col1 in range(cube.size):
                    for layer2 in range(cube.size):
                        for row2 in range(cube.size):
                            for col2 in range(cube.size):
                                # Which are not the same
                                if (layer1, row1, col1) < (layer2, row2, col2):  # Only unique pairs

                                    # Swap the elements
                                    cube.get_cube()[layer1][row1][col1], cube.get_cube()[layer2][row2][col2] = \
                                        cube.get_cube()[layer2][row2][col2], cube.get_cube()[layer1][row1][col1]

                                    # Calculate fitness for this neighbor
                                    new_fitness = cube.evaluate_fitness()

                                    # Update values if better
                                    if new_fitness > best_fitness:
                                        best_fitness = new_fitness
                                        best_cube = [layer[:] for layer in cube.get_cube()]

                                    # Revert swap to restore for next iteration
                                    cube.get_cube()[layer1][row1][col1], cube.get_cube()[layer2][row2][col2] = \
                                        cube.get_cube()[layer2][row2][col2], cube.get_cube()[layer1][row1][col1]

        # Best possible neighbor cube
        cube.__cube = best_cube

        return cube
