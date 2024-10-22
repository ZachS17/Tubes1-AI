from ..core.cube import Cube

# Base Class for Magic Cube Solvers
class Algorithm:
    def __init__(self):
        self.cube = Cube()
    
    def solve(self):
        """
        Template method to be implemented by each specific algorithm.
        Should contain the logic for solving the magic cube.
        """
        raise NotImplementedError("The solve method must be implemented by subclasses.")

    def evaluate(self):
        """
        Optional common method to evaluate the quality of the solution.
        Can be used by all algorithms, or overridden by specific algorithms.
        """
        pass
