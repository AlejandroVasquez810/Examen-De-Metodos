# Datos de la tabla (Precio, Pies, Dormitorios, Antigüedad)
precio <- c(64000, 59000, 61500, 79000, 87500, 92500, 95000, 113000, 115000, 138000, 142500, 144000, 145000, 147500, 144000, 155500, 165000)
pies <- c(1670, 1339, 1712, 1840, 2300, 2234, 2311, 2377, 2736, 2500, 2500, 2479, 2400, 3124, 2500, 4062, 2854)
dormitorios <- c(2, 2, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 3, 4, 3, 4, 3)
antiguedad <- c(30, 25, 30, 40, 18, 39, 19, 7, 10, 1, 3, 3, 1, 0, 2, 10, 3)

df <- data.frame(Precio = precio, Pies = pies, Dormitorios = dormitorios, Antiguedad = antiguedad)

# Modelo de regresión lineal múltiple con las tres variables independientes
modelo <- lm(Precio ~ Pies + Dormitorios + Antiguedad, data = df)

# Predicción solicitada: casa de 2,000 pies, 3 dormitorios y 10 años de antigüedad
pred <- predict(modelo, newdata = data.frame(Pies = 2000, Dormitorios = 3, Antiguedad = 10))

# Mostrar resultados
cat("=== EJERCICIO 5 (R) ===\n")
cat(sprintf("Ecuación: Precio = %.2f + (%.4f * Pies) + (%.2f * Dormitorios) + (%.2f * Antigüedad)\n", 
            coef(modelo)[1], coef(modelo)[2], coef(modelo)[3], coef(modelo)[4]))
cat(sprintf("R² (Coef. de Determinación): %.4f\n", summary(modelo)$r.squared))
cat(sprintf("-> Predicción (2,000 pies, 3 dorms, 10 años): $%.2f\n", pred))
