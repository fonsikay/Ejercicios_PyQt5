# Se importa la libreria necesaria para crear gráficas.
import matplotlib.pyplot as plot

# Se indica un título al gráfico.
plot.title('Línea Recta')

# Se indica una etiqueta para mostrarla en el eje "X de la gráfica.
plot.xlabel('Eje X')

# Se indica una etiqueta para mostrarla en el eje "Y" de la gráfica.
plot.ylabel('Eje Y')

# Se crean los datos para dibujar una grafica con una línea recta.
# Se crea una lista con los datos que va a tener el eje X e Y de la gráfica.
w_datos_eje_x = [10, 20, 30, 40, 50]
w_datos_eje_y = [20, 30, 40, 50, 60]

# Se carga la gráfica indicándole los datos primero del eje X y luego del eje Y de las listas.
plot.plot(w_datos_eje_x, w_datos_eje_y)

# Se muestra la gráfica por pantalla.
plot.show()