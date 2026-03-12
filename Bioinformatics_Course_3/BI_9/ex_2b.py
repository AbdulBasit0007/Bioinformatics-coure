import numpy as np
import matplotlib.pyplot as plt

def gillespie_algorithm(volume, A_init, B_init, C_init, D_init, k1, k2, t_final):
    # initial concentrations
    A = A_init * volume
    B = B_init * volume
    C = C_init * volume
    D = D_init * volume

    # time variables
    t = 0
    time = [t]

    # concentration records
    A_conc = [A / volume]
    B_conc = [B / volume]
    C_conc = [C / volume]
    D_conc = [D / volume]

    while t < t_final:
        a1 = k1 * A * B
        a2 = k2 * C
        a0 = a1 + a2
        
        if a0 == 0:
            break
        
        r1 = np.random.random()
        r2 = np.random.random()

        # determine time to next reaction
        tau = (1.0 / a0) * np.log(1.0 / r1)
        t += tau
        
        # determine which reaction occurs
        if r2 < a1 / a0:
            # reaction 1: A + B -> C
            A -= 1
            B -= 1
            C += 1
        else:
            # reaction 2: C -> B + D
            C -= 1
            B += 1
            D += 1

        # record concentrations
        time.append(t)
        A_conc.append(A / volume)
        B_conc.append(B / volume)
        C_conc.append(C / volume)
        D_conc.append(D / volume)
    
    return time, A_conc, B_conc, C_conc, D_conc

# simulation parameters
A_init = 10  # µm^-3
B_init = 6   # µm^-3
C_init = 0   # µm^-3
D_init = 0   # µm^-3
k1 = 2e-3    # µm^-3 s^-1
k2 = 5e-2    # µm^-3 s^-1
t_final = 100  # seconds

# run simulation for 5 µm^3
volume_5 = 5  # µm^3
time_5, A_5, B_5, C_5, D_5 = gillespie_algorithm(volume_5, A_init, B_init, C_init, D_init, k1, k2, t_final)

# run simulation for 13 µm^3
volume_13 = 13  # µm^3
time_13, A_13, B_13, C_13, D_13 = gillespie_algorithm(volume_13, A_init, B_init, C_init, D_init, k1, k2, t_final)

# plotting the results for 5 µm^3
plt.figure(figsize=(12, 6))
plt.plot(time_5, A_5, label='[A]', color='blue')
plt.plot(time_5, B_5, label='[B]', color='green')
plt.plot(time_5, C_5, label='[C]', color='red')
plt.plot(time_5, D_5, label='[D]', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (µm⁻³)')
plt.legend()
plt.title('Concentration vs Time for Volume 5 µm³')
plt.grid(True)
plt.show()

# plotting the results for 13 µm^3
plt.figure(figsize=(12, 6))
plt.plot(time_13, A_13, label='[A]', color='blue')
plt.plot(time_13, B_13, label='[B]', color='green')
plt.plot(time_13, C_13, label='[C]', color='red')
plt.plot(time_13, D_13, label='[D]', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (µm⁻³)')
plt.legend()
plt.title('Concentration vs Time for Volume 13 µm³')
plt.grid(True)
plt.show()

