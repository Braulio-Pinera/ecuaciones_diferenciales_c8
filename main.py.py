import numpy as np
import matplotlib.pyplot as plt

# Ecuación diferencial: dy/dt = y
def f(t, y):
    return y

# Parámetros
t0 = 0
tf = 1
h = 0.2

# Número de pasos
n_steps = int((tf - t0) / h)

# Vectores
t = np.zeros(n_steps + 1)
y_euler = np.zeros(n_steps + 1)
y_exacta = np.zeros(n_steps + 1)

# Condición inicial
t[0] = t0
y_euler[0] = 1

# Solución exacta
y_exacta[0] = 1

# Método de Euler
for i in range(n_steps):
    t[i+1] = t[i] + h
    y_euler[i+1] = y_euler[i] + h * f(t[i], y_euler[i])
    y_exacta[i+1] = np.exp(t[i+1])

# Mostrar resultados numéricos
print("t\tEuler\t\tExacta")
for i in range(n_steps + 1):
    print(f"{t[i]:.1f}\t{y_euler[i]:.5f}\t{y_exacta[i]:.5f}")

# Gráfica
plt.plot(t, y_euler, 'o--', label='Euler')
plt.plot(t, y_exacta, label='Solución exacta')
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Método de Euler vs Solución Exacta")
plt.legend()
plt.grid()
plt.show()