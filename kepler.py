import math
from cuerpo_celeste import CuerpoCeleste  

class Kepler(CuerpoCeleste):
    def __init__(self, nombre, excentricidad, anomalia_media):
        super().__init__(nombre, excentricidad, anomalia_media)

    # Función que representa la ecuación de Kepler
    def funcion(self, E):
        return E - self.e * math.sin(E) - self.M

    # Derivada de la ecuación de Kepler
    def derivada(self, E):
        return 1 - self.e * math.cos(E)

    # Método de Newton-Raphson para encontrar la solución de la ecuación de Kepler
    def newton_raphson(self, E0, epsilon=1e-6, max_iter=100):
        E = E0
        E_valores = [E]  # Inicializa la lista de valores de E
        for i in range(max_iter):
            f = self.funcion(E)
            df = self.derivada(E)
            E_new = E - f / df
            error = abs((E_new - E) / E_new)
            E_valores.append(E_new)  # Añade el nuevo valor de E a la lista
            if error < epsilon:
                return E_new, i + 1, E_valores  # Retorna el valor final de E, el número de iteraciones y los valores de E
            E = E_new
        return E, max_iter, E_valores  # Si no converge, retorna el último valor de E y la lista
