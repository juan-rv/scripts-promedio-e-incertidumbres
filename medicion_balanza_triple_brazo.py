import numpy as np
import math

# Datos de las mediciones de masa de los trozos de balso con la balanza de tres brazos (en gramos)
masas_trozos = np.array([1.2, 1.2, 1.3, 1.3, 1.3, 1.1, 1.4, 1.3, 1.3, 1.3])  # en gramos

# Paso 1: Calcular la masa promedio de los trozos de balso
masa_promedio = np.mean(masas_trozos)

# Paso 2: Cálculo manual de la desviación estándar
# a. Calcular la diferencia de cada masa respecto a la media
diferencias = masas_trozos - masa_promedio

# b. Elevar cada diferencia al cuadrado
diferencias_cuadrado = diferencias ** 2

# c. Sumar las diferencias al cuadrado
suma_cuadrados = np.sum(diferencias_cuadrado)

# d. Dividir por n - 1 para obtener la varianza
n = len(masas_trozos)
varianza = suma_cuadrados / (n - 1)

# e. Raíz cuadrada para obtener la desviación estándar
desviacion_estandar = math.sqrt(varianza)

# Paso 3: Calcular la incertidumbre de irrepetibilidad (desviación estándar / raíz de n)
incertidumbre_irrepetibilidad = desviacion_estandar / math.sqrt(n)

# Paso 4: Calcular la incertidumbre de resolución (resolución de la balanza de tres brazos: 0.1 g)
resolucion_balanza = 0.1  # resolución en gramos
incertidumbre_resolucion = resolucion_balanza / (2 * math.sqrt(3))

# Paso 5: Calcular la incertidumbre total combinada
incertidumbre_total = math.sqrt(incertidumbre_irrepetibilidad**2 + incertidumbre_resolucion**2)

# Redondear resultados a 2 decimales al final
masa_promedio = round(masa_promedio, 2)
desviacion_estandar = round(desviacion_estandar, 2)
incertidumbre_irrepetibilidad = round(incertidumbre_irrepetibilidad, 2)
incertidumbre_resolucion = round(incertidumbre_resolucion, 2)
incertidumbre_total = round(incertidumbre_total, 2)

# Resultados finales
print("Masa promedio de los trozos de balso:", masa_promedio, "g")
print("Desviación estándar (manual):", desviacion_estandar, "g")
print("Incertidumbre de irrepetibilidad:", incertidumbre_irrepetibilidad, "g")
print("Incertidumbre de resolución:", incertidumbre_resolucion, "g")
print("Incertidumbre total:", incertidumbre_total, "g")