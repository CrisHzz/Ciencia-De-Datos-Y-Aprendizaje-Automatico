import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Tus datos
periodos = np.array([1, 2, 3]).reshape((-1, 1))
legalizados = np.array([560, 427, 473])
udem = np.array([59, 46, 30])

# Crear y entrenar el modelo para "LEGALIZADOS"
modelo_legalizados = LinearRegression().fit(periodos, legalizados)

# Crear y entrenar el modelo para "UDEM"
modelo_udem = LinearRegression().fit(periodos, udem)

# Predecir los valores para 2024-1 (periodo 4)
prediccion_legalizados = modelo_legalizados.predict(np.array([4]).reshape((-1, 1)))
prediccion_udem = modelo_udem.predict(np.array([4]).reshape((-1, 1)))

print(f'Predicción para LEGALIZADOS en 2024-1: {prediccion_legalizados[0]}')
print(f'Predicción para UDEM en 2024-1: {prediccion_udem[0]}')

legalizados = np.append(legalizados, prediccion_legalizados[0]) #np.append, pide una array de numpy a ingresar y el dato a añadir
udem = np.append(udem, prediccion_udem[0])

periodos = np.array([1,2,3,4])  # Ahora es un array 1D

fig, ax = plt.subplots() #Usar esta nomenclatura de fig para no tener problemas

anchoBarra = 0.30

ax.bar(periodos, legalizados, width=anchoBarra, color="mediumpurple", label='Legalizados en sapiencia')

ax.bar(periodos + anchoBarra, udem, width=anchoBarra, color="crimson", label="Sapiencia en Udem")

ax.set_title("Proyeccion de legalizados para el periodo 2024-1 (4)")

plt.legend()

ax.set_xlabel("Periodos")

ax.set_ylabel("Personas")

ax.set_xticks(periodos) #Esto hace que los numeros solamente sean los de al lista, sin decimales ni extra

plt.show()

