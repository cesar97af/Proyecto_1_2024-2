****Simulación de Órbitas Planetarias****
Este programa implementa una simulación numérica del movimiento orbital de los planetas del sistema solar utilizando el método de Newton-Raphson para resolver la ecuación de Kepler.Además, se incluye la visualización de las órbitas.

**Requisitos**
Para ejecutar se requiere tener instaladas las siguientes dependencias:

Python 3.11 (Aunque creo que incluso se puede desde la versión 3.5)
Matplotlib (para graficar las órbitas)
NumPy (para operaciones matemáticas (en algunas gráficas))

A continuación, se describe la estructura:

cuerpo_celeste.py: Define como la clase base CuerpoCeleste, que integra las propiedades generales de un cuerpo celeste.
kepler.py: Define la clase Keepler, este archivo implementa el método de Newton-Raphson para resolver la ecuación de Kepler.
anomalia.py: Contiene las clases para calcular la anomalía verdadera y la distancia del planeta al Sol.
grafica_orbital.py: Gráfica la órbita elíptica y calcula la velocidad orbital.
resultados.py: Muestra los resultados finales del cálculo.
main.py: Integra todos los módulos y ejecuta la simulación y visualización de las órbitas planetarias.
Ejecución

Para ejecutar el código, simplemente corre el archivo main.py, luego ingresa los datos que te sugieren


3. Ver los resultados
El programa mostrará una gráfica que muestra la órbita elíptica de los planeta seleccionado y la posición actual del planeta. Además, se imprimirá la velocidad orbital y otros parámetros importantes en la terminal:

Anomalía excéntrica: Resultado obtenido con el método de Newton-Raphson.
Anomalía verdadera: Calculada a partir de la anomalía excéntrica.
Distancia: La distancia actual del planeta al Sol.
Velocidad orbital: La velocidad del planeta en el punto actual de su órbita.

Nota
Este proyecto es parte de un ejercicio académico donde se aplican conceptos algunos de programación orientada a objetos, cálculo numérico y visualización de datos.