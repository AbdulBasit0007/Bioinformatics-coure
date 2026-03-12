# -*- coding: utf-8 -*-
# Assignment 6 - 6.2. Boolean Network

import numpy as np

# weights
activation_weight = 3
inhibition_weight = 4

# propagation matrix
def propagate(state):
    A, B, C, D, E, F = state

    # used chatGPT!! here I had some problem in if-else statement
    next_A = 1 if (activation_weight * (A + B + E) - inhibition_weight * C) > 0 else 0
    next_B = 1 if (activation_weight * A) > 0 else 0
    next_C = 1 if (activation_weight * E) > 0 else 0
    next_D = 1 if (activation_weight * E) > 0 else 0
    next_E = 1 if (activation_weight * (D + F)) > 0 else 0
    next_F = 1 if (activation_weight * A - inhibition_weight * F) > 0 else 0
    
    return [next_A, next_B, next_C, next_D, next_E, next_F]

def int_to_state(n):
    return [(n >> i) & 1 for i in range(6)]

def state_to_int(state):
    return sum([bit << i for i, bit in enumerate(state)])

# simulate network. Had some problems in while statement I used chatGPT here!!
def simulate(initial_state):
    state = initial_state
    states = []
    while state not in states:
        states.append(state)
        state = propagate(state)
    return states

# initial states
initial_states = [0, 1, 6, 15, 37, 52]

if __name__ == '__main__':
    for initial in initial_states:
        initial_state = int_to_state(initial)
        trajectory = simulate(initial_state)
        trajectory_int = [state_to_int(state) for state in trajectory]
        print(f"Initial state {initial}: Trajectory {trajectory_int}")

    all_trajectories = {}
    for initial in range(64):
        initial_state = int_to_state(initial)
        trajectory = simulate(initial_state)
        trajectory_int = [state_to_int(state) for state in trajectory]
        all_trajectories[initial] = trajectory_int

    attractors = {}
    for initial, trajectory in all_trajectories.items():
        attractor_start = trajectory.index(trajectory[-1])
        attractor = tuple(trajectory[attractor_start:])
        if attractor not in attractors:
            attractors[attractor] = []
        attractors[attractor].append(initial)

    for attractor, basin in attractors.items():
        print(f"Attractor {attractor}: Basin {basin} (Length {len(attractor)})")
        print(f"Coverage: {len(basin) / 64:.2%}")