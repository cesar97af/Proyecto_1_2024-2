# Clase para mostrar los resultados finales
class Resultados:
    def __init__(self, v_valores, r_valores, result, iterations, epsilon):
        self.v_valores = v_valores
        self.r_valores = r_valores
        self.result = result
        self.iterations = iterations
        self.epsilon = epsilon

    def mostrar_resultados(self):
        print(f"v es {self.v_valores[-1]} rad")
        print(f"La distancia del planeta es {self.r_valores[-1]} kilómetros.")
        print(f"Para lograr estos resultados, la anomalía excéntrica {self.result} se obtuvo en {self.iterations} iteraciones con un error de {self.epsilon}.")