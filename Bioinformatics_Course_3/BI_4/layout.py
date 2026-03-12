from random import gauss
from generic_network import GenericNetwork
import math
import random

class Layout:
    def __init__(self, file_path):
        """
        :param file_path: path to a white-space-separated file that contains node interactions
        """
        # create a network from the given file
        self.network = GenericNetwork()
        self.network.read_from_tsv(file_path)
        # friction coefficient
        self.alpha = 0.03
        # random force interval
        self.interval = 0.3
        # initial square to distribute nodes
        self.size = 50

    def init_positions(self):
        """
        Initialise or reset the node positions, forces and charge.
        """
        for node in self.network.nodes.values():
            node.pos_x = random.uniform(0, self.size)
            node.pos_y = random.uniform(0, self.size)
            node.force_x = 0
            node.force_y = 0
            node.charge = random.uniform(0.1, 1)  # Set charge randomly (example range)

    def calculate_forces(self):
        """
        Calculate the force on each node during the current iteration.
        """
        for node_i in self.network.nodes.values():
            for node_j in self.network.nodes.values():
                if node_i != node_j:
                    # Calculate distance between nodes
                    dx = node_j.pos_x - node_i.pos_x
                    dy = node_j.pos_y - node_i.pos_y
                    distance = math.sqrt(dx**2 + dy**2)

                    # Coulomb repulsion force
                    coulomb_force = node_i.charge * node_j.charge / (distance ** 2)
                    node_i.force_x -= coulomb_force * dx / distance
                    node_i.force_y -= coulomb_force * dy / distance

                    # Hooke attraction force
                    hooke_force = distance * 0.1  # Adjust this constant for desired spring stiffness
                    node_i.force_x += hooke_force * dx / distance
                    node_i.force_y += hooke_force * dy / distance


    def add_random_force(self, temperature):
        """
        Add a random force within [- temperature * interval, temperature * interval] to each node.
        (There is nothing to do here for you.)
        :param temperature: temperature in the current iteration
        """
        for node in self.network.nodes.values():
            node.force_x += gauss(0.0, self.interval * temperature)
            node.force_y += gauss(0.0, self.interval * temperature)

    def displace_nodes(self):
        """
        Change the position of each node according to the force applied to it and reset the force on each node.
        """
        for node in self.network.nodes.values():
            node.pos_x += self.alpha * node.force_x
            node.pos_y += self.alpha * node.force_y
            node.force_x = 0
            node.force_y = 0


    def calculate_energy(self):
        """
        Calculate the total energy of the network in the current iteration.
        :return: total energy
        """
        total_energy = 0
        for node_i in self.network.nodes.values():
            for node_j in self.network.nodes.values():
                if node_i != node_j:
                    dx = node_j.pos_x - node_i.pos_x
                    dy = node_j.pos_y - node_i.pos_y
                    distance = math.sqrt(dx**2 + dy**2)
                    # Coulomb repulsion energy
                    coulomb_energy = node_i.charge * node_j.charge / distance
                    total_energy += coulomb_energy
                    # Hooke attraction energy
                    hooke_energy = 0.5 * distance ** 2  # Simplified form for demonstration
                    total_energy += hooke_energy
        return total_energy

    def layout(self, iterations):
        """
        Executes the force directed layout algorithm. (There is nothing to do here for you.)
        :param iterations: number of iterations to perform
        :return: list of total energies
        """
        # initialise or reset the positions and forces
        self.init_positions()
        energies = []

        for _ in range(iterations):
            self.calculate_forces()
            self.displace_nodes()
            energy = self.calculate_energy()
            energies.append(energy)

        return energies

    def simulated_annealing_layout(self, iterations):
        """
        Executes the force directed layout algorithm with simulated annealing.
        :param iterations: number of iterations to perform
        :return: list of total energies
        """
        self.init_positions()
        energies = []

        temperature = 1.0  # Initial temperature
        temperature_decay = 0.95  # Temperature decay rate

        temperature = 1.0  # Initial temperature
        temperature_decay = 0.95  # Temperature decay rate
        
        for i in range(iterations):
            # DECREASE THE TEMPERATURE IN EACH ITERATION. YOU CAN BE CREATIVE.
            temperature *= temperature_decay

            # there is nothing to do here for you
            self.calculate_forces()
            self.add_random_force(temperature)
            self.displace_nodes()
            energies.append(self.calculate_energy())

        return energies
