import pandas as pd
import numpy as np

# Datos de la tabla (Precio, Pies, Dormitorios, Antigüedad)
datos = {
    'Precio': [64000, 59000, 61500, 79000, 87500, 92500, 95000, 113000, 115000, 138000, 142500, 144000, 145000, 147500, 144000, 155500, 165000],
    'Pies': [1670, 1339, 1712, 1840, 2300, 2234, 2311, 2377, 2736, 2500, 2500, 2479, 2400, 3124, 2500, 4062, 2854],
    'Dormitorios': [2, 2, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 3, 4, 3, 4, 3],
    'Antiguedad': [30, 25, 30, 40, 18, 39, 19, 7, 10, 1, 3, 3, 1, 0, 2, 10, 3]
}

df = pd.DataFrame(datos)

# Preparar matriz X con intercepto y las tres variables independientes
X = np.column_stack([np.ones(len(df)), df['Pies'], df['Dormitorios'], df['Antiguedad']])
y = df['Precio'].values

# Resolver por mínimos cuadrados
beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
b0, b1, b2, b3 = beta

# Calcular R²
y_pred_all = X @ beta
ss_res = np.sum((y - y_pred_all) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - (ss_res / ss_tot)

# Predicción solicitada: casa de 2,000 pies, 3 dormitorios y 10 años de antigüedad
prediccion = b0 + b1 * 2000 + b2 * 3 + b3 * 10

# Mostrar resultados
print("=== EJERCICIO 5 (PYTHON) ===")
print(f"Ecuación: Precio = {b0:.2f} + ({b1:.4f} * Pies) + ({b2:.4f} * Dormitorios) + ({b3:.4f} * Antigüedad)")
print(f"R²: {r2:.4f}")
print(f"-> Predicción (2,000 pies, 3 dorms, 10 años): ${prediccion:,.2f}")
