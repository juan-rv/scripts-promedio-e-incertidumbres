import numpy as np
import math

# Datos de los diámetros externos e internos medidos con el calibrador vernier (en mm)
diametros_externos_vernier = np.array([15.30, 15.28, 15.30, 15.30, 15.32, 15.34, 15.26, 15.52, 15.44, 15.38])  # en mm
diametros_internos_vernier = np.array([8.58, 8.00, 8.24, 8.32, 8.20, 8.84, 8.64, 8.58, 8.22, 8.44])  # en mm

# Paso 1: Convertir diámetros de mm a cm
diametros_externos_cm = diametros_externos_vernier / 10  # convertir a cm
diametros_internos_cm = diametros_internos_vernier / 10  # convertir a cm

# Paso 2: Calcular radios en cm a partir de los diámetros
radios_externos_cm = diametros_externos_cm / 2
radios_internos_cm = diametros_internos_cm / 2

# Paso 3: Calcular el volumen de la esfera completa (volumen externo) y de la cavidad interna (volumen interno)
volumenes_externos = (4/3) * math.pi * (radios_externos_cm ** 3)
volumenes_internos = (4/3) * math.pi * (radios_internos_cm ** 3)

# Paso 4: Calcular el volumen de cada esfera hueca
volumenes_huecos = volumenes_externos - volumenes_internos

# Paso 5: Calcular el volumen promedio de las esferas huecas sin redondeo prematuro
volumen_promedio_hueco = np.mean(volumenes_huecos)

# Paso 6: Cálculo manual de la desviación estándar
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

# Paso 7: Calcular la incertidumbre de irrepetibilidad (desviación estándar / raíz de n)
incertidumbre_irrepetibilidad = desviacion_estandar / math.sqrt(n)

# Paso 8: Calcular la incertidumbre de resolución (resolución del calibrador vernier: 0.02 mm)
resolucion_vernier_cm = 0.002  # Convertimos 0.02 mm a 0.002 cm
incertidumbre_resolucion = resolucion_vernier_cm / (2 * math.sqrt(3))

# Paso 9: Calcular la incertidumbre total combinada
incertidumbre_total = math.sqrt(incertidumbre_irrepetibilidad**2 + incertidumbre_resolucion**2)

# Redondear resultados a 2 decimales al final
volumen_promedio_hueco = round(volumen_promedio_hueco, 2)
desviacion_estandar = round(desviacion_estandar, 2)
incertidumbre_irrepetibilidad = round(incertidumbre_irrepetibilidad, 2)
incertidumbre_resolucion = round(incertidumbre_resolucion, 2)
incertidumbre_total = round(incertidumbre_total, 2)

# Resultados finales
print("Volumen promedio de las esferas huecas:", volumen_promedio_hueco, "cm³")
print("Desviación estándar (manual):", desviacion_estandar, "cm³")
print("Incertidumbre de irrepetibilidad:", incertidumbre_irrepetibilidad, "cm³")
print("Incertidumbre de resolución:", incertidumbre_resolucion, "cm³")
print("Incertidumbre total:", incertidumbre_total, "cm³")
