import numpy as np
import matplotlib.pyplot as plt

A = 5.0
B = 5.0
C = 5.0
D = 0.0

# rate constants
k1 = 0.1
k2 = 0.1
k3 = 0.1

# time parameters
t_final = 100.0
delta_t = 0.1
num_steps = int(t_final / delta_t)

# arrays to store concentrations over time
A_conc = np.zeros(num_steps)
B_conc = np.zeros(num_steps)
C_conc = np.zeros(num_steps)
D_conc = np.zeros(num_steps)
time = np.linspace(0, t_final, num_steps)

# Euler Forward Integrator
for i in range(num_steps):
    A_conc[i] = A
    B_conc[i] = B
    C_conc[i] = C
    D_conc[i] = D
    
    R1 = k1 * A * B
    R2 = k2 * C
    R3 = k3 * D * A
    
    dA_dt = -R1 + R2 - R3
    dB_dt = -R1 + R3
    dC_dt = R1 - R2
    dD_dt = R2 - R3
    
    A += dA_dt * delta_t
    B += dB_dt * delta_t
    C += dC_dt * delta_t
    D += dD_dt * delta_t

# plotting the results
plt.figure(figsize=(10, 6))
plt.plot(time, A_conc, label='[A]')
plt.plot(time, B_conc, label='[B]')
plt.plot(time, C_conc, label='[C]')
plt.plot(time, D_conc, label='[D]')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (µm⁻³)')
plt.legend()
plt.title('Concentration vs Time')
plt.grid(True)
plt.show()

# concentrations at t = 5.5 s
index_5_5s = int(5.5 / delta_t)
A_5_5s = A_conc[index_5_5s]
B_5_5s = B_conc[index_5_5s]
C_5_5s = C_conc[index_5_5s]
D_5_5s = D_conc[index_5_5s]

# A_5_5s, B_5_5s, C_5_5s, D_5_5s

print(f'Concentrations at t = 5.5 s:')
print(f'A: {A_5_5s:.4f} μm⁻³')
print(f'B: {B_5_5s:.4f} μm⁻³')
print(f'C: {C_5_5s:.4f} μm⁻³')
print(f'D: {D_5_5s:.4f} μm⁻³')
