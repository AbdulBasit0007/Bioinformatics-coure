from bioGRID import BioGRIDReader
from network_scale_free import ScaleFreeNetwork
from tools import plot_distribution_comparison, scale_free_distribution, cumulative, KS_dist
from network_random import RandomNetwork



def exercise_1b():
    # Create scale-free networks
    n_nodes_1 = 10000
    n_nodes_2 = 100000
    m_edges = 2

    scale_free_net_1 = ScaleFreeNetwork(n_nodes=n_nodes_1, n_edges_per_iteration=m_edges)
    scale_free_net_2 = ScaleFreeNetwork(n_nodes=n_nodes_2, n_edges_per_iteration=m_edges)

    # Compute degree distributions for scale-free networks
    degree_distribution_1 = scale_free_net_1.degree_histogram()
    degree_distribution_2 = scale_free_net_2.degree_histogram()

    # Plot degree distributions for scale-free networks
    plot_distribution_comparison(
        histograms=[degree_distribution_1, degree_distribution_2],
        legend=[f"n = {n_nodes_1}, m = {m_edges}", f"n = {n_nodes_2}, m = {m_edges}"],
        title="Degree Distribution of Scale-Free Networks",
        log=True
    )

    # Create a random network
    random_net = RandomNetwork(n_nodes=10000, n_edges=20000)

    # Compute degree distribution for the random network
    random_degree_distribution = random_net.degree_histogram()

    # Plot degree distributions for scale-free and random networks together
    plot_distribution_comparison(
        histograms=[degree_distribution_1, random_degree_distribution],
        legend=[f"Scale-Free (n = {n_nodes_1}, m = {m_edges})", f"Random (n = 10000, m = 20000)"],
        title="Degree Distribution Comparison",
        log=True
    )


def exercise_1c():
    # Create a random network with n = 10,000 nodes and m = 20,000 edges
    random_net = RandomNetwork(n_nodes=10000, n_edges=20000)

    # Compute degree distribution for the random network
    random_degree_distribution = random_net.degree_histogram()

    # Compute the theoretical power-law distribution
    max_degree = max(random_degree_distribution)
    gamma = 2.5  # Choose an appropriate value for gamma
    theoretical_distribution = scale_free_distribution(max_degree, gamma)

    # Compute the cumulative distributions
    random_cumulative_distribution = cumulative(random_degree_distribution)
    theoretical_cumulative_distribution = cumulative(theoretical_distribution)

    # Compute the Kolmogorov–Smirnov distance
    ks_distance = KS_dist(random_cumulative_distribution, theoretical_cumulative_distribution)

    print("Kolmogorov–Smirnov distance between random network degree distribution and theoretical power law distribution:", ks_distance)

    # Plot the degree distribution of the random network and the theoretical power law distribution
    plot_distribution_comparison(
        histograms=[random_degree_distribution, theoretical_distribution],
        legend=["Random Network", "Theoretical Power Law Distribution"],
        title="Degree Distribution Comparison",
        log=True
    )


def exercise_2b(bio_grid: BioGRIDReader):
    # TODO
    pass


def exercise_2c(bio_grid: BioGRIDReader):
    # TODO
    pass


# main guard: this makes sure that the following is only executed when this file is called as a script directly
# that way, this file could be imported in other files to use the above functions without the processing below
# taking place every time
if __name__ == '__main__':
    print('# Exercise 1')
    exercise_1b()
    exercise_1c()

    print('# Exercise 2')
    # read the BioGRID database here so that it only has to be done once
    bio_grid_reader = BioGRIDReader('BIOGRID-ALL-4.4.232.tsv')

    exercise_2b(bio_grid_reader)
    exercise_2c(bio_grid_reader)


