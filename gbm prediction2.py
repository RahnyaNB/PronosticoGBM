# Se importaron las bibliotecas necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import locale

# Establecemos la localización en español para reconocer los nombres de los meses
locale.setlocale(locale.LC_TIME, 'Spanish_Spain')

#Cargamos el dataset CSV
data = pd.read_excel(r"C:\Users\rahny\Desktop\OTROS\Energiadataset.csv")

# Crear una columna de fecha combinando 'MES' y 'AÑO'
data['fecha'] = pd.to_datetime(data['MES'] + ' ' + data['AÑO'].astype(str), format='%B %Y')

# Eliminar columnas innecesarias (MES, AÑO) y mantener solo los campos necesarios
data = data.drop(columns=['MES', 'AÑO'])

# X contiene 'SECTOR' y 'fecha' como variables predictoras
X = data[['fecha', 'SECTOR']]
y = data['ENERGIA ENTREGADA GWh']  # Variable objetivo del proyecto: Energía entregada

# Convertir la fecha en características numéricas (mes, año)
X['month'] = X['fecha'].dt.month
X['year'] = X['fecha'].dt.year

# Convertir las variables categóricas (SECTOR) a variables dummy/indicadoras
X = pd.get_dummies(X, columns=['SECTOR'], drop_first=True)

# Eliminar la columna de fecha ya que no la necesitamos más
X = X.drop(columns=['fecha'])

# División en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo GBM
gbm = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gbm.fit(X_train, y_train)
y_pred = gbm.predict(X_test)

# Efectividad del modelo
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Error cuadrático medio (RMSE): {rmse}')
print(f'Coeficiente de determinación (R2 Score): {r2}')

# Tabla de resultados:
comparison = pd.DataFrame({'Valores Reales': y_test, 'Predicciones': y_pred})
print("\nTabla de comparación de valores reales y predicciones:\n")
print(comparison.to_string(index=False))

# Explicación
print("\nExplicación de los resultados:")
print(f"El modelo ha sido evaluado con un RMSE de {rmse:.4f}, lo que indica que el promedio de los errores de predicción es aproximadamente {rmse:.2f} GWh. "
      f"El coeficiente de determinación R² es {r2:.4f}, lo que significa que el {r2 * 100:.2f}% de la variación en la demanda de energía puede explicarse "
      "a partir de las variables predictoras que hemos utilizado en el modelo (mes, año y sector). Esto indica un ajuste muy preciso del modelo a los datos.")
      
# Grafica de las predicciones frente a los valores reales
plt.scatter(y_test, y_pred, color='blue', label="Predicciones")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2, label="Línea ideal")
plt.xlabel('Valores Reales de Energía Entregada')
plt.ylabel('Predicciones de Energía Entregada')
plt.title('Predicción vs Valores Reales de Energía Entregada')
plt.legend()
plt.show()


