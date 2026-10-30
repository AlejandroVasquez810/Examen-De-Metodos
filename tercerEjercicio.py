import pandas as pd
import numpy as np

# Datos de la tabla del Ejercicio 3
datos = {
    'Precio': [64000, 59000, 61500, 79000, 87500, 92500, 95000, 113000, 115000, 138000, 142500, 144000, 145000, 147500, 144000, 155500, 165000],
    'Pies_Cuadrados': [1670, 1339, 1712, 1840, 2300, 2234, 2311, 2377, 2736, 2500, 2500, 2479, 2400, 3124, 2500, 4062, 2854],
    'Dormitorios': [2, 2, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 3, 4, 3, 4, 3],
    'Antiguedad': [30, 25, 30, 40, 18, 39, 19, 7, 10, 1, 3, 3, 1, 0, 2, 10, 3]
}

df = pd.DataFrame(datos)
y = df['Precio']

variables = ['Pies_Cuadrados', 'Dormitorios', 'Antiguedad']

print("=== MODELOS DE REGRESIÓN LINEAL SIMPLE ===\n")

for var in variables:
    x = df[var]
    # Cálculo de la pendiente (m) y la ordenada al origen (b) por mínimos cuadrados
    m, b = np.polyfit(x, y, 1)
    
    # Coeficiente de correlación y R^2
    correlacion = np.corrcoef(x, y)[0, 1]
    r2 = correlacion**2
    
    print(f"Modelo para: {var}")
    print(f"  Ecuación: Precio = {m:.4f} * ({var}) + {b:.4f}")
    print(f"  R² (Coef. de Determinación): {r2:.4f}")
    print("-" * 50)
