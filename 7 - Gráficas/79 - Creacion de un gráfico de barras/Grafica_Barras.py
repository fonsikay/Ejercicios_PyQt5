# Se importa la libreria necesaria para crear gráficas.
import matplotlib.pyplot as plot

# Nuestra gráfica va a tener por cada año entre 2016 al 2021 el salario anual de una persona.

# Se indica un título al gráfico.
plot.title('Salario por años')

# Se indica una etiqueta para mostrarla en el eje "X de la gráfica.
plot.xlabel('Años')

# Se indica una etiqueta para mostrarla en el eje "Y" de la gráfica.
plot.ylabel('Salario')

# Se guardan los años que va a tener la gráfica.
w_anos = [2016, 2017, 2018, 2019, 2020, 2021]

# Se guarda el salario de la persona por cada uno de los años.
w_salario = [15000, 19000, 20000, 17000, 22000, 25000]

# Se indica que el tipo de gráfico va a ser de tipo "Barras" con el método "bar()".
plot.bar(w_anos, w_salario)

# Se muestra el gráfico por pantalla.
plot.show()