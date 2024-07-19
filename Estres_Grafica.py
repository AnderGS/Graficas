import matplotlib.pyplot as plt

# Datos combinados de las tres encuestas para la pregunta "¿Qué te causa estrés?"
categorias = [
    "Parciales",
    "Actividades extracurriculares",
    "Actividades orales",
    "Problemas domésticos",
    "Trabajo",
    "Problemas con amigos",
    "Problemas amorosos",
    "Problemas financieros",
    "Problemas familiares",
    "Otros"
]

# Frecuencias de las tres encuestas
frecuencias_encuesta_1 = [
    71, 27, 46, 23, 5, 34, 34, 16, 58, 30
]

frecuencias_encuesta_2 = [
    70, 31, 37, 36, 13, 36, 34, 28, 59, 25
]

frecuencias_encuesta_3 = [
    59, 27, 31, 26, 14, 24, 32, 15, 42, 19
]

# Sumando las frecuencias de las tres encuestas
frecuencias_totales = [
    frecuencias_encuesta_1[i] + frecuencias_encuesta_2[i] + frecuencias_encuesta_3[i]
    for i in range(len(categorias))
]

# Crear la gráfica de barras combinada
plt.figure(figsize=(10, 6))
plt.barh(categorias, frecuencias_totales, color='skyblue')
plt.xlabel('Frecuencia')
plt.ylabel('Causas de Estrés')
plt.title('Causas de Estrés en los Encuestados (Combinado)')
plt.xlim(0, max(frecuencias_totales) + 10)

# Añadir etiquetas de valores en las barras
for index, value in enumerate(frecuencias_totales):
    plt.text(value, index, str(value))

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
