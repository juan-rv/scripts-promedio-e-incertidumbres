import numpy as np
import math

# Datos del volumen desplazado medido con la probeta en ml
volumen_desplazado = np.array([40.05, 41, 41, 41, 41, 41, 41, 41.2, 41.2, 41])  # volumen en ml
volumen_inicial = 40  # volumen inicial en ml

# Paso 1: Calcular el volumen neto desplazado por cada esfera hueca (restando el volumen inicial)
volumenes_huecos = volumen_desplazado - volumen_inicial

# Paso 2: Calcular el volumen promedio de las esferas huecas
volumen_promedio_hueco = np.mean(volumenes_huecos)

# Paso 3: Cálculo manual de la desviación estándar
# a. Calcular la diferencia de cada volumen respecto a la media
diferencias = volumenes_huecos - volumen_promedio_hueco

# b. Elevar cada diferencia al cuadrado
diferencias_cuadrado = diferencias ** 2

# c. Sumar las diferencias al cuadrado
suma_cuadrados = np.sum(diferencias_cuadrado)

# d. Dividir por n - 1 para obtener la varianza
n = len(volumenes_huecos)
varianza = suma_cuadrados / (n - 1)

# e. Raíz cuadrada para obtener la desviación estándar
desviacion_estandar = math.sqrt(varianza)

# Paso 4: Calcular la incertidumbre de irrepetibilidad (desviación estándar / raíz de n)
incertidumbre_irrepetibilidad = desviacion_estandar / math.sqrt(n)

# Paso 5: Calcular la incertidumbre de resolución (resolución de la probeta: 1 ml)
resolucion_probeta = 1  # resolución en ml
incertidumbre_resolucion = resolucion_probeta / (2 * math.sqrt(3))

# Paso 6: Incluir la incertidumbre de calibración de la probeta (±0.5 ml)
incertidumbre_calibracion = 0.5

# Paso 7: Calcular la incertidumbre total combinada
incertidumbre_total = math.sqrt(incertidumbre_irrepetibilidad**2 + incertidumbre_resolucion**2 + incertidumbre_calibracion**2)

# Redondear resultados a 2 decimales al final
volumen_promedio_hueco = round(volumen_promedio_hueco, 2)
desviacion_estandar = round(desviacion_estandar, 2)
incertidumbre_irrepetibilidad = round(incertidumbre_irrepetibilidad, 2)
incertidumbre_resolucion = round(incertidumbre_resolucion, 2)
incertidumbre_calibracion = round(incertidumbre_calibracion, 2)
incertidumbre_total = round(incertidumbre_total, 2)

# Resultados finales
print("Volumen promedio de las esferas huecas:", volumen_promedio_hueco, "ml")
print("Desviación estándar (manual):", desviacion_estandar, "ml")
print("Incertidumbre de irrepetibilidad:", incertidumbre_irrepetibilidad, "ml")
print("Incertidumbre de resolución:", incertidumbre_resolucion, "ml")
print("Incertidumbre de calibración:", incertidumbre_calibracion, "ml")
print("Incertidumbre total:", incertidumbre_total, "ml")