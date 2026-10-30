library(readxl)

calcular_metricas <- function(ruta_archivo) {
  # Leer el archivo de Excel sin encabezados
  df <- read_excel(ruta_archivo, col_names = FALSE)
  
  # Buscar la columna que contenga datos numéricos
  datos <- NULL
  for (col in df) {
    num_col <- suppressWarnings(as.numeric(as.character(col)))
    if (sum(!is.na(num_col)) > 5) {
      datos <- num_col[!is.na(num_col)]
      break
    }
  }
  
  # Calcular métricas
  media <- mean(datos)
  varianza <- var(datos)
  desv_est <- sd(datos)
  maximo <- max(datos)
  minimo <- min(datos)
  rango <- maximo - minimo
  
  # Retornar vector nombrados
  resultado <- c(
    "Media" = media,
    "Varianza" = varianza,
    "Desviación estándar" = desv_est,
    "Máximo" = maximo,
    "Mínimo" = minimo,
    "Rango" = rango
  )
  return(resultado)
}

cat("=== RESULTADOS EN R ===\n")
cat("\n--- Sexenio 1 ---\n")
print(calcular_metricas("/home/juice/Documentos/Examen_Metodos/sexenio-1.xls"))

cat("\n--- Sexenio 2 ---\n")
print(calcular_metricas("/home/juice/Documentos/Examen_Metodos/sexenio-2.xls"))
