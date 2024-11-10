# Proyecto de Cálculo de Incertidumbres en Medición

Este repositorio contiene scripts en Python para calcular volúmenes, masas y sus respectivas incertidumbres en un laboratorio de metrología. Cada script corresponde a un tipo de instrumento de medición, e incluye arrays de datos que pueden modificarse para adaptarse a diferentes cálculos.

## Contenido del Proyecto

### Archivos Principales

- **`calculo_volumen_regla_escolar.py`**:
  - Calcula el volumen promedio y sus incertidumbres usando la regla escolar para medir los diámetros de esferas huecas.
  - Incluye arrays (`diametros_externos_regla` y `diametros_internos_regla`) con valores en milímetros para los diámetros externos e internos. Estos valores se pueden reemplazar para realizar nuevos cálculos.
  - Contiene comentarios sobre las fórmulas de cálculo para el volumen promedio y las incertidumbres de irrepetibilidad, resolución e incertidumbre total.

- **`calculo_volumen_calibrador_vernier.py`**:
  - Calcula el volumen promedio y sus incertidumbres usando un calibrador vernier para medir los diámetros de esferas huecas.
  - Incluye arrays (`diametros_externos_vernier` y `diametros_internos_vernier`) con valores en milímetros que representan los diámetros externos e internos de las esferas. Puedes cambiar estos valores para nuevos cálculos.
  - Este archivo también contiene comentarios detallados sobre las fórmulas y cálculos utilizados para obtener el volumen promedio y las incertidumbres.

- **`calculo_volumen_probeta.py`**:
  - Calcula el volumen promedio y sus incertidumbres usando una probeta y el método de desplazamiento de volumen.
  - Incluye un array de datos de volumen (`volumen_desplazado`) en mililitros (ml) que representa el volumen total medido en la probeta.
  - La probeta tiene una incertidumbre de calibración de **±0.5 ml** que se incluye en el cálculo de la incertidumbre total.
  - Puedes ajustar los valores en el array para realizar nuevos cálculos y observar cómo afectan los resultados.

- **`calculo_masa_balanza_tres_brazos.py`**:
  - Calcula la masa promedio y sus incertidumbres utilizando una balanza de tres brazos.
  - Contiene un array de datos de masa (`masas_trozos`) en gramos. Puedes reemplazar los valores en `masas_trozos` para adaptar el cálculo a tus propios datos.
  - Incluye comentarios sobre las fórmulas de promedio, desviación estándar, incertidumbre de irrepetibilidad, resolución e incertidumbre total.

- **`calculo_masa_balanza_digital.py`**:
  - Calcula la masa promedio y sus incertidumbres utilizando una balanza digital.
  - Contiene un array (`masas_trozos`) que puedes modificar con tus propios valores de masa en gramos.
  - Incluye comentarios sobre las fórmulas utilizadas en el cálculo.
 
  - **`Contacto`**:
  - jrodriguezvar@unal.edu.co

## Requisitos

- **Python 3.6 o superior**.
- **Biblioteca NumPy**: Puedes instalarla ejecutando el siguiente comando:
  ```bash
  pip install numpy# scripts-promedio-e-incertidumbres
