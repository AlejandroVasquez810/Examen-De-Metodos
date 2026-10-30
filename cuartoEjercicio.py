import pandas as pd
import numpy as np

# Datos del ejercicio
datos = {
    'Precio': [64000, 59000, 61500, 79000, 87500, 92500, 95000, 113000, 115000, 138000, 142500, 144000, 145000, 147500, 144000, 155500, 165000],
    'Pies': [1670, 1339, 1712, 1840, 2300, 2234, 2311, 2377, 2736, 2500, 2500, 2479, 2400, 3124, 2500, 4062, 2854],
    'Dormitorios': [2, 2, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 3, 4, 3, 4, 3]
}

df = pd.DataFrame(datos)

# Preparar matrices para regresión lineal múltiple
X = np.column_stack([np.ones(len(df)), df['Pies'], df['Dormitorios']])
y = df['Precio'].values

# Resolver por mínimos cuadrados
beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
b0, b1, b2 = beta

# Calcular R^2
y_pred_all = X @ beta
ss_res = np.sum((y - y_pred_all) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - (ss_res / ss_tot)

# Predicción solicitada: 2,000 pies cuadrados y 3 dormitorios
prediccion = b0 + b1 * 2000 + b2 * 3

print("=== EJERCICIO 4 (PYTHON) ===")
print(f"Ecuación: Precio = {b0:.2f} + ({b1:.4f} * Pies) + ({b2:.2f} * Dormitorios)")
print(f"R²: {r2:.4f}")
print(f"-> Predicción (2,000 pies, 3 dorms): ${prediccion:,.2f}")

