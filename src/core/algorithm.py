from ..core.cube import Cube

# Base Class for Magic Cube Solvers
class Algorithm:
    def __init__(self):
        self.cube = Cube()
        self.iterations = []
        self.fitness_values = []
        self.duration = None
    
    def solve(self):
        """
        Template method to be implemented by each specific algorithm.
        Should contain the logic for solving the magic cube.
        Returns the class itself to be taken its values for visualizing
        """
        raise NotImplementedError("The solve method must be implemented by subclasses.")
