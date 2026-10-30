# Datos de la tabla
precio <- c(64000, 59000, 61500, 79000, 87500, 92500, 95000, 113000, 115000, 138000, 142500, 144000, 145000, 147500, 144000, 155500, 165000)
pies <- c(1670, 1339, 1712, 1840, 2300, 2234, 2311, 2377, 2736, 2500, 2500, 2479, 2400, 3124, 2500, 4062, 2854)
dormitorios <- c(2, 2, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 3, 4, 3, 4, 3)

df <- data.frame(Precio = precio, Pies = pies, Dormitorios = dormitorios)

# Modelo de regresión lineal múltiple (Precio en función de Pies y Dormitorios)
modelo <- lm(Precio ~ Pies + Dormitorios, data = df)

# Predicción para una casa con 2,000 pies y 3 dormitorios
pred <- predict(modelo, newdata = data.frame(Pies = 2000, Dormitorios = 3))

# Mostrar resultados
cat("=== EJERCICIO 4 (R) ===\n")
cat(sprintf("Ecuación: Precio = %.2f + (%.4f * Pies) + (%.2f * Dormitorios)\n", coef(modelo)[1], coef(modelo)[2], coef(modelo)[3]))
cat(sprintf("R² (Coef. de Determinación): %.4f\n", summary(modelo)$r.squared))
cat(sprintf("-> Predicción (2,000 pies, 3 dorms): $%.2f\n", pred))
