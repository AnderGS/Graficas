import matplotlib.pyplot as plt

# Datos combinados de las tres encuestas para la pregunta "¿Has experimentado algunos de estos síntomas propios de una depresión?"
categorias = [
    "Tristeza",
    "Ansiedad",
    "Soledad",
    "Dificultad para dormir",
    "Desesperanza",
    "No he experimentado ninguno"
]

# Frecuencias de las tres encuestas
frecuencias_encuesta_1 = [
    15, 35, 23, 24, 1, 25
]

frecuencias_encuesta_2 = [
    73, 69, 42, 64, 45, 26
]

frecuencias_encuesta_3 = [
    45, 35, 31, 39, 25, 13
]

# Sumando las frecuencias de las tres encuestas
frecuencias_totales = [
    frecuencias_encuesta_1[i] + frecuencias_encuesta_2[i] + frecuencias_encuesta_3[i]
    for i in range(len(categorias))
]

# Crear la gráfica de sectores (pastel)
plt.figure(figsize=(8, 8))
plt.pie(frecuencias_totales, labels=categorias, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Síntomas propios de una depresión experimentados por los encuestados')
plt.show()
