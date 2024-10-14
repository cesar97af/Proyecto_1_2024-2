import math
import matplotlib.pyplot as plt
from kepler import Kepler  # Importa la clase Kepler

# Clase para visualización de la órbita
class Visualizacion:
    def __init__(self, planetas):
        # Convierte cada planeta del diccionario en un objeto Kepler
        self.planetas = planetas

    def graficar_orbitas(self):
        fig, ax = plt.subplots()
        for planeta in self.planetas:
            E0 = 0  # Valor inicial para E
            E_final, iterations = planeta.newton_raphson(E0)
            ax.plot([0, math.cos(E_final)], [0, math.sin(E_final)], label=f"Órbita de {planeta.nombre}")
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.set_title("Órbitas de los planetas")
        plt.show()
