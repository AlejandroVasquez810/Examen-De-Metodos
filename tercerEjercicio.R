# Datos de la tabla del Ejercicio 3
precio <- c(64000, 59000, 61500, 79000, 87500, 92500, 95000, 113000, 115000, 138000, 142500, 144000, 145000, 147500, 144000, 155500, 165000)
pies <- c(1670, 1339, 1712, 1840, 2300, 2234, 2311, 2377, 2736, 2500, 2500, 2479, 2400, 3124, 2500, 4062, 2854)
dormitorios <- c(2, 2, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 3, 4, 3, 4, 3)
antiguedad <- c(30, 25, 30, 40, 18, 39, 19, 7, 10, 1, 3, 3, 1, 0, 2, 10, 3)

df <- data.frame(Precio = precio, Pies = pies, Dormitorios = dormitorios, Antiguedad = antiguedad)

cat("=== MODELOS DE REGRESIÓN LINEAL SIMPLE EN R ===\n\n")

# 1. Pies Cuadrados
modelo_pies <- lm(Precio ~ Pies, data = df)
s_pies <- summary(modelo_pies)
cat("Modelo: Precio vs Pies Cuadrados\n")
cat(sprintf("  Ecuación: Precio = %.4f * Pies + %.4f\n", coef(modelo_pies)[2], coef(modelo_pies)[1]))
cat(sprintf("  R²: %.4f\n", s_pies$r.squared))
cat("--------------------------------------------------\n")

# 2. Dormitorios
modelo_dorm <- lm(Precio ~ Dormitorios, data = df)
s_dorm <- summary(modelo_dorm)
cat("Modelo: Precio vs Dormitorios\n")
cat(sprintf("  Ecuación: Precio = %.4f * Dormitorios + %.4f\n", coef(modelo_dorm)[2], coef(modelo_dorm)[1]))
cat(sprintf("  R²: %.4f\n", s_dorm$r.squared))
cat("--------------------------------------------------\n")

# 3. Antigüedad
modelo_ant <- lm(Precio ~ Antiguedad, data = df)
s_ant <- summary(modelo_ant)
cat("Modelo: Precio vs Antigüedad\n")
cat(sprintf("  Ecuación: Precio = %.4f * Antiguedad + %.4f\n", coef(modelo_ant)[2], coef(modelo_ant)[1]))
cat(sprintf("  R²: %.4f\n", s_ant$r.squared))
cat("--------------------------------------------------\n")

