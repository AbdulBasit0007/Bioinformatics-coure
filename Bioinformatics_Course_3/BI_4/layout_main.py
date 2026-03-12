from layout import Layout
from tools import plot_layout, plot_energies


file_paths = ['star.txt', 'star++.txt', 'dog.txt']

for file_path in file_paths:
    # Initialize Layout object
    layout = Layout(file_path)
    
    # Run basic layout algorithm
    basic_energies = layout.layout(1000)
    basic_final_energy = basic_energies[-1]
    print(f"Final energy for {file_path} (basic): {basic_final_energy}")

    # Plot layout for basic algorithm
    plot_layout(layout, f"Layout for {file_path} (Basic)")

    # Run simulated annealing layout algorithm
    annealing_energies = layout.simulated_annealing_layout(1000)
    annealing_final_energy = annealing_energies[-1]
    print(f"Final energy for {file_path} (simulated annealing): {annealing_final_energy}")

    # Plot layout for simulated annealing algorithm
    plot_layout(layout, f"Layout for {file_path} (Simulated Annealing)")

    # Choose one network (e.g., the first one) to compare energies per step
    if file_path == file_paths[0]:
        # Plot energies per step for basic layout algorithm
        plot_energies([basic_energies], ['Basic Layout'], 'Energies per Step (Basic)')

        # Plot energies per step for simulated annealing layout algorithm
        plot_energies([annealing_energies], ['Simulated Annealing Layout'], 'Energies per Step (Simulated Annealing)')