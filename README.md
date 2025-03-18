# Pronóstico de la Demanda de Energía con el algoritmo de Gradient Boosting Machines para regresión.
## Recolección de la data
El dataset que estamos utilizando contiene información proporcionada en el apartado de documentos públicos de Edesur, una de las empresas de distribución eléctrica de la República Dominicana. Este dataset se enfoca en la energía entregada y pérdida en GWh (Gigavatios hora), clasificada por sector, mes y año, lo cual es clave para poder hacer un análisis histórico y predictivo de la demanda energética en diferentes sectores.
### Campos del Dataset:
1.	SECTOR: Categoría que identifica a qué tipo de sector fue entregada la energía (industrial, residencial, comercial, etc.). Este campo es importante porque distintos sectores pueden tener patrones de consumo de energía muy diferentes. Por ejemplo, el sector industrial tiende a tener una demanda constante y alta, mientras que el sector residencial puede tener variaciones más marcadas en función de la hora del día y las estaciones del año.
2.	ENERGÍA ENTREGADA GWh: Esta columna muestra la cantidad de energía (en gigavatios hora) que fue entregada a cada sector en un mes específico. La energía entregada es un indicador directo de la demanda real en ese sector. Al analizar los patrones de entrega de energía a lo largo del tiempo, podemos inferir cómo ha cambiado la demanda eléctrica y proyectar futuras necesidades.
3.	PÉRDIDA GWh: Esta columna indica la cantidad de energía que se pierde en el proceso de distribución. Aunque no es un dato directo sobre la demanda, la pérdida de energía puede afectar la eficiencia del sistema y, por lo tanto, tiene un impacto en la oferta disponible para los consumidores.
4.	MES y AÑO: Estos campos especifican el tiempo en el que se registraron los datos. La combinación de mes y año nos permite observar la variación de la demanda energética a lo largo del tiempo, detectando patrones estacionales o tendencias a largo plazo.
### ¿Cómo esta data puede ayudar a predecir la demanda eléctrica?
La energía entregada en un mes específico es una representación directa de la demanda de energía de ese sector durante ese período. Utilizando datos históricos de energía entregada, es posible identificar patrones de consumo y realizar predicciones futuras sobre la demanda de energía eléctrica. Factores como la estacionalidad (los meses fríos o cálidos pueden alterar la demanda en ciertos sectores) y el crecimiento económico (reflejado en sectores industriales o comerciales) juegan un papel crucial.

Al entrenar un modelo con estos datos, podemos:

•	Predecir cómo cambiará la demanda de energía en un sector específico.

•	Identificar cuáles sectores tienen un mayor crecimiento en demanda y necesitan más infraestructura eléctrica.

•	Ayudar a las empresas distribuidoras como Edesur a planificar la distribución y producción de energía de manera más eficiente.

### Definición de Conceptos:
1.	Demanda de Energía: Es la cantidad de energía eléctrica que los usuarios de un sistema eléctrico requieren en un período de tiempo determinado. En este caso, la demanda puede variar por sector y depende de múltiples factores como la hora del día, la temporada, y el nivel de actividad económica.
2.	Energía Entregada: Cantidad de energía que fue consumida realmente por los sectores después de las pérdidas en el sistema de distribución. Esto refleja de manera efectiva la demanda eléctrica.
3.	Predicción de la Demanda: Utilizando los datos históricos de consumo (energía entregada), podemos hacer estimaciones futuras de la demanda eléctrica mediante algoritmos de inteligencia artificial, como el Gradient Boosting Machines (GBM).
