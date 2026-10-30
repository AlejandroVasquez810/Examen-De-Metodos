# Definición de variables del Ejercicio 1
precio_venta = 40.0        # USD
costo_produccion = 24.0    # USD
comision_ventas = 2.0      # USD
costos_fijos = 3500.0      # USD

# Cálculo de costos variables y margen de contribución
costo_variable_unitario = costo_produccion + comision_ventas
margen_contribucion = precio_venta - costo_variable_unitario

# Cálculo del punto de equilibrio en unidades
punto_equilibrio = costos_fijos / margen_contribucion

# Mostrar resultados
print(f"--- ANÁLISIS DE PUNTO DE EQUILIBRIO ---")
print(f"Costo variable unitario: ${costo_variable_unitario:.2f} USD")
print(f"Margen de contribución unitario: ${margen_contribucion:.2f} USD")
print(f"Punto de equilibrio: {int(punto_equilibrio)} unidades de camisas")
