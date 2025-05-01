# 📘 ENTREGABLE1 - Propiedades Aritméticas con NumPy

Este proyecto forma parte del curso de Inteligencia Artificial, Machine Learning y Deep Learning en SENATI. El objetivo es aplicar teoría matemática mediante programación en Python utilizando la librería NumPy, demostrando dominio en la generación y manipulación de vectores, así como en la verificación de propiedades aritméticas fundamentales.

## 🧠 Objetivo

Desarrollar un script interactivo en Python que permita:

- Generar vectores personalizados desde entrada del usuario.
- Verificar las siguientes propiedades aritméticas con NumPy:
  - Conmutativa: A + B = B + A
  - Asociativa: (A + B) + C = A + (B + C)
  - Distributiva: k(A + B) = kA + kB
  - Inverso aditivo: A + (-A) = 0
  - Identidad aditiva: A + 0 = A

También incluye validaciones para evitar errores por entradas vacías o incompatibles.

## 🛠️ Tecnologías utilizadas

- Python 3.x
- NumPy

## 📂 Archivo principal

- `ENTREGABLE1.py`: Contiene todo el código funcional del proyecto, incluyendo:
  - Menú interactivo
  - Validación de entradas
  - Funciones para cada propiedad aritmética

## ▶️ Cómo ejecutar

1. Asegúrate de tener Python y NumPy instalados:
   ```bash
   pip install numpy
   ```

2. Ejecuta el script:
   ```bash
   python ENTREGABLE1.py
   ```

3. Sigue las instrucciones por consola para ingresar vectores, elegir propiedades y verificar los resultados.

## 💡 Ejemplo de uso

```
Ingrese los elementos del vector A separados por espacios: 1 2 3
Ingrese los elementos del vector B separados por espacios: 4 5 6

Conmutativa:
A + B = [5. 7. 9.]
B + A = [5. 7. 9.]
¿A + B == B + A? True
```

## 🧑‍🎓 Créditos

Alumno: **Efrén Hiroshi Hernández Vicente**  
Instructor: **Saul Sneider Chavez Chico**  
**SENATI**
