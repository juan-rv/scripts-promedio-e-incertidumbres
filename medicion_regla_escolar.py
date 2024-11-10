import numpy as np
import math

# Datos de los diámetros externos e internos medidos con la regla escolar (en mm)
diametros_externos_regla = np.array([15, 15, 16, 15, 15, 15, 15, 15, 15, 15])  # diámetros externos en mm
diametros_internos_regla = np.array([8, 8, 9, 8, 8, 8, 9, 9, 8, 8])  # diámetros internos en mm

# 1. Convertir diámetros de mm a cm
diametros_externos_cm = diametros_externos_regla / 10  # convertir a cm
diametros_internos_cm = diametros_internos_regla / 10  # convertir a cm

# 2. Calcular radios en cm a partir de los diámetros
radios_externos_cm = diametros_externos_cm / 2
radios_internos_cm = diametros_internos_cm / 2

# 3. Calcular el volumen de la esfera completa (volumen externo) y de la cavidad interna (volumen interno)
volumenes_externos = (4/3) * math.pi * (radios_externos_cm ** 3)
volumenes_internos = (4/3) * math.pi * (radios_internos_cm ** 3)

# 4. Calcular el volumen de cada esfera hueca
volumenes_huecos = volumenes_externos - volumenes_internos

# 5. Calcular el volumen promedio de las esferas huecas
volumen_promedio_hueco = np.mean(volumenes_huecos)

# 6. Cálculo manual de la desviación estándar
diferencias = volumenes_huecos - volumen_promedio_hueco
diferencias_cuadrado = diferencias ** 2
suma_cuadrados = np.sum(diferencias_cuadrado)
n = len(volumenes_huecos)
varianza = suma_cuadrados / (n - 1)
desviacion_estandar = math.sqrt(varianza)

# 7. Calcular la incertidumbre de irrepetibilidad (desviación estándar / raíz de n)
incertidumbre_irrepetibilidad = desviacion_estandar / math.sqrt(n)

# 8. Calcular la incertidumbre de resolución (considerando que la resolución de la regla es de 1 mm)
resolucion_regla_cm = 0.1  # Convertimos 1 mm a 0.1 cm
incertidumbre_resolucion = resolucion_regla_cm / (2 * math.sqrt(3))

# 9. Calcular la incertidumbre total combinada
incertidumbre_total = math.sqrt(incertidumbre_irrepetibilidad**2 + incertidumbre_resolucion**2)

# Redondear resultados a 2 decimales
volumen_promedio_hueco = round(volumen_promedio_hueco, 2)
desviacion_estandar = round(desviacion_estandar, 2)
incertidumbre_irrepetibilidad = round(incertidumbre_irrepetibilidad, 2)
incertidumbre_resolucion = round(incertidumbre_resolucion, 2)
incertidumbre_total = round(incertidumbre_total, 2)

# Resultados finales
print("Volumen promedio de las esferas huecas:", volumen_promedio_hueco, "cm³")
print("Desviación estándar:", desviacion_estandar)
print("Incertidumbre de irrepetibilidad:", incertidumbre_irrepetibilidad, "cm³")
print("Incertidumbre de resolución:", incertidumbre_resolucion, "cm³")
print("Incertidumbre total:", incertidumbre_total, "cm³")