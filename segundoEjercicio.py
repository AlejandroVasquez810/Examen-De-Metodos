import pandas as pd

def calcular_metricas(nombre_archivo):
    # Cargar el archivo de Excel (leemos la primera hoja)
    df = pd.read_excel(nombre_archivo, header=None) # Usamos header=None por si no tiene títulos arriba
    
    # Tomamos la segunda columna (índice 1) o primera (índice 0) dependiendo de dónde estén los números.
    # Usemos la columna 1 o la que tenga los datos. Probemos tomando la columna numérica directamente:
    # Vamos a buscar la primera columna que tenga datos numéricos:
    for col in df.columns:
        # Intentar convertir a numérico
        serie = pd.to_numeric(df[col], errors='coerce')
        if serie.dropna().count() > 5: # Si tiene varios números válidos
            datos = serie.dropna()
            break
    else:
        # Si no encontró por el loop, agarramos la columna 1 por defecto
        datos = pd.to_numeric(df.iloc[:, 1], errors='coerce').dropna()

    # Calcular las métricas solicitadas
    metricas = {
        "Media": datos.mean(),
        "Varianza": datos.var(),              
        "Desviación estándar": datos.std(),   
        "Máximo": datos.max(),
        "Mínimo": datos.min(),
        "Rango": datos.max() - datos.min()
    }
    return pd.Series(metricas)

# Ejecutar para ambos sexenios
print("=== RESULTADOS EN PYTHON ===")
print("\n--- Sexenio 1 ---")
print(calcular_metricas("/home/juice/Documentos/Examen_Metodos/sexenio-1.xls"))

print("\n--- Sexenio 2 ---")
print(calcular_metricas("/home/juice/Documentos/Examen_Metodos/sexenio-2.xls"))

