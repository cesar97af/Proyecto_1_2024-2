import math

# Clase para calcular la anomalía verdadera
class AnomaliaVerdadera:
    def calcular_v(self, E_new, e):
        return math.atan((math.sqrt((1 + e) / (1 - e))) * math.tan(E_new / 2))

# Clase para calcular la distancia del planeta al Sol
class Distancia:
    def __init__(self, a, e):
        self.a = a
        self.e = e
    
    def calcular_r(self, v):
        return (self.a * (1 - self.e**2)) / (1 + self.e * math.cos(v))