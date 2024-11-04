import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from src.core.cube import Cube
from src.core.algorithm import Algorithm
from src.algorithm.genetic_algorithm import GeneticAlgorithm
from src.algorithm.hill_climbing_sideways_move import HillClimbingSidewaysMove
from src.algorithm.simulated_annealing import SimulatedAnnealing
from src.algorithm.stochastic_hill_climbing import Stochastic

class MagicCubeVisualizer:
    def __init__(self, size):
        self.size = size
        self.magic_constant = size * (size ** 3 + 1) // 2  # Magic constant for n x n x n cube
        self.states = []  # List to store different states of the cube
        self.cube = None
        
        self.current_index = 0  # Track the current state index
        self.is_playing = False   # Track playback status

    def find_lines_equal_to_magic_constant(self):
        lines = []
        # Check rows and columns in each layer
        for z in range(self.size):
            for i in range(self.size):
                if np.sum(self.cube[i, :, z]) == self.magic_constant:
                    lines.append((i, 'row', z))
                if np.sum(self.cube[:, i, z]) == self.magic_constant:
                    lines.append((i, 'col', z))

        # Check diagonals in each layer
        for z in range(self.size):
            if np.sum(self.cube.diagonal(offset=0, axis1=0, axis2=1)[..., z]) == self.magic_constant:
                lines.append(('diag', 'main', z))
            if np.sum(np.fliplr(self.cube).diagonal(offset=0, axis1=0, axis2=1)[..., z]) == self.magic_constant:
                lines.append(('diag', 'anti', z))

        return lines

    def display_layers(self):
        fig, axes = plt.subplots(1, self.size, figsize=(4 * self.size - 1, 4))  # Create subplots

        for z in range(self.size):
            axes[z].imshow(self.cube[:, :, z], cmap='Blues', vmin=1, vmax=self.size**3)

            # Remove axis ticks and labels
            axes[z].set_xticks([]) 
            axes[z].set_yticks([])  

            # Add labels to the edges (vertices) of each cell in the layer
            for i in range(self.size):
                for j in range(self.size):
                    # Label the center of each cell
                    axes[z].text(j - 0.75, i - 0.75, str(self.cube[i, j, z]), 
                                ha='center', va='center', color='black', fontsize=12)

        plt.subplots_adjust(wspace=0.5)  # Adjust the width space as needed
        plt.tight_layout()

        # Create playback control buttons
        ax_play = plt.axes([0.1, 0.01, 0.1, 0.05])
        ax_pause = plt.axes([0.22, 0.01, 0.1, 0.05])
        ax_next = plt.axes([0.34, 0.01, 0.1, 0.05])
        ax_prev = plt.axes([0.46, 0.01, 0.1, 0.05])
        
        btn_play = Button(ax_play, 'Play')
        btn_pause = Button(ax_pause, 'Pause')
        btn_next = Button(ax_next, 'Next')
        btn_prev = Button(ax_prev, 'Previous')

        # Set button callbacks
        btn_play.on_clicked(self.playback)
        btn_pause.on_clicked(self.pause)
        btn_next.on_clicked(self.next_state)
        btn_prev.on_clicked(self.prev_state)

        plt.show()

    def playback(self, event):
        """Starts playback."""
        self.is_playing = True
        while self.is_playing and self.current_index < len(self.states)-1:
            self.cube = self.states[self.current_index]
            self.display_layers()  # Display the current state
            plt.pause(1)  # Wait for 1 second
            self.current_index += 1

    def pause(self, event):
        """Pauses playback."""
        self.is_playing = False

    def next_state(self, event):
        """Displays the next state."""
        if self.current_index < len(self.states) - 1:
            self.current_index += 1
            self.cube = self.states[self.current_index]
            self.display_layers()

    def prev_state(self, event):
        """Displays the previous state."""
        if self.current_index > 0:
            self.current_index -= 1
            self.cube = self.states[self.current_index]
            self.display_layers()

    def update_cube_state(self, new_state):
        self.cube = new_state
        self.states.append(self.cube)  # Store the new state

# Usage example
if __name__ == "__main__":
    # Initialize the magic cube
    magic_cube = Cube()
    magic_cube.display_cube()  # Display the initial cube state

    # Initialize the visualizer
    visualizer = MagicCubeVisualizer(magic_cube.get_size())

    # Example: Store the initial cube state in the visualizer
    visualizer.update_cube_state(magic_cube.get_cube())

    # Select an algorithm
    print("Pilihan Algoritma:")
    print("1. Hill Climbing with Sideways Move")
    print("2. Simulated Annealing")
    print("3. Genetic Algorithm")
    print("4. Stochastic Hill Climbing")
    
    no_algoritma = int(input("Pilihan algoritma: "))
    
    # Example algorithm selection (you'll need to define the algorithms)
    if no_algoritma == 1:
        maximum_sideways_move = int(input("Maximum Sideways Move: "))
        algorithm = HillClimbingSidewaysMove(maximum_sideways_move)
    elif no_algoritma == 2:
        algorithm = SimulatedAnnealing()
    elif no_algoritma == 3:
        population_size = int(input("Population Size: "))
        number_of_iterations = int(input("Maximum Number of Iterations: "))
        algorithm = GeneticAlgorithm(population_size, number_of_iterations)
    elif no_algoritma == 4:
        algorithm = Stochastic()
    else:
        print("Tidak diimplementasikan...")

    # Run the algorithm
    finished_algorithm = algorithm.solve()

    # Store each iteration's cube state in the visualizer
    for i in range(len(finished_algorithm.iterations)):
        new_state = np.array(finished_algorithm.iterations[i].get_cube())
        visualizer.update_cube_state(new_state)

    # Show the visualization
    visualizer.display_layers()

    print("Duration:",finished_algorithm.duration)
    print("Number of Iterations:", len(finished_algorithm.fitness_values)-1)
    print("Initial:",finished_algorithm.iterations[0].display_cube())
    print("Initial fitness:", finished_algorithm.iterations[0].evaluate_fitness())
    print("Final result:",finished_algorithm.iterations[len(finished_algorithm.iterations)-1].display_cube())
    print("Final fitness:",finished_algorithm.iterations[len(finished_algorithm.iterations)-1].evaluate_fitness())

