import numpy as np
import matplotlib.pyplot as plt

G = 6.674 * 10**(-11)  # Constante gravitacional en m^3/kg/s^2
M_kg = 1.989 * 10**30  # Masa del Sol en kilogramos

# Clase para graficar la órbita y calcular la velocidad orbital
class GraficaOrbital:
    def __init__(self, a, e, r_valores, v_valores, planeta):
        self.a = a
        self.e = e
        self.r_valores = r_valores
        self.v_valores = v_valores
        self.planeta = planeta

    def velocidad_orbital(self):
        r_km = self.r_valores[-1]
        v_km_s = np.sqrt(2 * G * M_kg / (r_km * 1000))
        print(f"La velocidad orbital en la posición actual es {v_km_s:.2f} km/s.")
    
    def graficar_orbita(self):
        theta_vals = np.linspace(0, 2 * np.pi, 1000)
        r_vals = self.a * (1 - self.e**2) / (1 + self.e * np.cos(theta_vals))
        x_vals = r_vals * np.cos(theta_vals)
        y_vals = r_vals * np.sin(theta_vals)

        # Graficar la órbita
        plt.figure(figsize=(15, 9))
        plt.plot(x_vals, y_vals, label="Órbita elíptica")
        plt.scatter(0, 0, color='yellow', marker='o', s=900, label="Sol")
        plt.scatter(r_vals[0] * np.cos(self.v_valores[-1]), r_vals[0] * np.sin(self.v_valores[-1]),
                    color='blue', marker='o', s=100, label="Planeta (posición actual)")
        plt.xlabel("Distancia (km)")
        plt.ylabel("Distancia (km)")
        plt.title(f"Órbita elíptica del planeta {self.planeta.capitalize()} alrededor del Sol")
        plt.legend()
        plt.grid(True)
        plt.axis("equal")
        plt.show()