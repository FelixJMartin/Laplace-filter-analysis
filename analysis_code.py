# Imports --------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Optional dark style
plt.style.use('dark_background')

# Circuit parameters ---------------------------------------------------
R = 5e3       # Resistance 
C = 20e-9     # Capacitance
L = 50e-3     # Inductance 

# Transfer function H(s) = (C L R s^2 + R) / (C L R s^2 + L s + R) ----
myFilter = signal.TransferFunction([C * L * R, 0, R], [C * L * R, L, R])

#  Analytical step response --------------------------------------------
alpha = 1 / (2 * C * R)
beta = np.sqrt((1 / (C * L)) - (1 / (2 * C * R))**2)

# Time vector (0 to 2 ms)
t = np.linspace(0, 0.0020, 1000)

# Analytical solution for unit-step input
y_analytical = 1 - np.exp(-alpha * t) * (1 / (R * C * beta)) * np.sin(beta * t)

# Numerical step response (from transfer function) --------------------
t_numeric, y_numeric = signal.step(myFilter, T=t)

#  Plot: Analytical vs Numerical step responses ------------------------
plt.figure(figsize=(8, 5))
plt.plot(t_numeric, y_numeric, label='Numerical step response')
plt.plot(t, y_analytical, '--', label='Analytical step response')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response: analytical vs numerical')
plt.grid(True)
plt.legend()

# Square wave + Fourier series terms ----------------------------------
# Square wave parameters
T_0 = 0.0002                 # Period [s] 
omega_0 = 2 * np.pi / T_0    # Fundamental angular frequency

# Time axis for square wave demo (0 to 0.4 ms)
t_sq = np.linspace(0, 0.0004, 1000)

# Square wave in {0,1}, starting at 1 V
square_wave = 0.5 * (1 + np.sign(np.sin(omega_0 * t_sq)))

# Sum of first N nonzero sine terms (odd harmonics only)
N_terms = 5  # first 5 odd harmonics
terms = []
for k in range(N_terms):
    n = 2 * k + 1
    term = (2 / np.pi) * (1 / n) * np.sin(n * omega_0 * t_sq)
    terms.append(term)
sum_terms = np.sum(terms, axis=0)
x_fs = 0.5 + sum_terms  

# --- 7) Plot individual FS terms (optional) ---------------------------------
fig_terms, axes = plt.subplots(3, 2, figsize=(12, 9))
axes = axes.ravel()

axes[0].plot(t_sq, square_wave, label='Square wave (0–1 V)')
axes[0].set_title('Square wave signal')
axes[0].set_xlabel('Time [s]')
axes[0].set_ylabel('Amplitude [V]')
axes[0].grid(True)
axes[0].set_ylim(-0.2, 1.2)
axes[0].legend()

for k in range(N_terms):
    ax = axes[k + 1]
    ax.plot(t_sq, terms[k], label=f'Term {k+1} (n={2*k+1})')
    ax.set_title(f'Fourier term {k+1}')
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Amplitude [V]')
    ax.grid(True)
    ax.legend()

fig_terms.tight_layout()

# Plot FS sum vs square wave ------------------------------------------
plt.figure(figsize=(10, 5))
plt.plot(t_sq, square_wave, label='Square wave (0–1 V)')
plt.plot(t_sq, x_fs, '--', label=f'FS sum (first {N_terms} odd terms)')
plt.title(f'Fourier series approximation (first {N_terms} odd terms)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [V]')
plt.grid(True)
plt.ylim(-0.2, 1.2)
plt.legend()
plt.show()

