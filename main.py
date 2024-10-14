from kepler import Kepler
from visualizacion import Visualizacion
from anomalia import AnomaliaVerdadera, Distancia
from grafica_orbital import GraficaOrbital
from resultados import Resultados

# Datos de los planetas del sistema solar
planetas = [
    Kepler("Mercurio", 0.2056, 174.796),
    Kepler("Venus", 0.0068, 50.115),
    Kepler("Tierra", 0.0167, 358.617),
    Kepler("Marte", 0.0934, 19.412),
    Kepler("Júpiter", 0.0489, 20.020),
    Kepler("Saturno", 0.0565, 317.020),
    Kepler("Urano", 0.0463, 142.590),
    Kepler("Neptuno", 0.0097, 256.228)
]

# Solicitar al usuario que elija un planeta y la distancia media
'''Donde la numeración será del 0 al 7
    con 0 = Mercurio
        1 = Venus
        2 = Tierra
        ...
        7 = Neptuno.'''
print("Seleccione el número del planeta:")
for i, planeta in enumerate(planetas):
    print(f"{i}: {planeta.nombre}")

# El usuario selecciona el planeta
indice_planeta = int(input("Ingrese el número correspondiente al planeta: "))
planeta = planetas[indice_planeta]

# El usuario ingresa la distancia media del planeta al Sol en km
a = float(input(f"Ingrese la distancia media del planeta {planeta.nombre} al Sol en kilómetros: "))

# Imprimir los valores ingresados
print(f"Has seleccionado {planeta.nombre} con una distancia media de {a} km al Sol.")


# Calculamos la anomalía excéntrica con Newton-Raphson
E0 = 0  # Valor inicial
result, iterations, E_valores = planeta.newton_raphson(E0)
E_valores = [result]

# Calculamos la anomalía verdadera
anomalia = AnomaliaVerdadera()
v_valores = [anomalia.calcular_v(E, planeta.e) for E in E_valores]

# Calculamos las distancias
dist = Distancia(a=a, e=planeta.e)
r_valores = [dist.calcular_r(v) for v in v_valores]

# Graficamos la órbita y mostramos la velocidad orbital
grafica = GraficaOrbital(a, planeta.e, r_valores, v_valores, planeta.nombre)
grafica.velocidad_orbital()
grafica.graficar_orbita()

# Mostramos los resultados
resultados = Resultados(v_valores, r_valores, result, iterations, 1e-6)
resultados.mostrar_resultados()