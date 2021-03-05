# Se ha de instalar las siguientes librerias.
# pip install pandas
# pip install xlrd
# pip install openpyxl

# Se importa la libreria necesaria, en este caso "pandas".
import pandas

# Se guarda el nombre del archivo Excel en una variable.
w_path_file = 'libros.xlsx'

# Se crea un diccionario que va a tener el tipo de la columna "isbn" para que sepa que es un string y no un número.
w_tipo_columna = {'Codigo': int,
                  'Titulo': str,
                  'Autor': str,
                  'Precio': float,
                  'ISBN': str,
                  'ISBN13': str,
                  'Idioma': str,
                  'Num_pag': int}

# Se guarda el nombre de la hoja en una variable.
w_nombre_hoja = 'Datos'

# Se lee el archivo Excel con el método "pandas.read_excel()".
# Se indican los siguientes parámetros:

# - ruta del archivo completa si no esta en el mismo directorio.
# - sheet_name: Nombre de la hoja.
# - dtype: lista de tipos de los campos.

w_datos_excel = pandas.read_excel(w_path_file, sheet_name=w_nombre_hoja, dtype=w_tipo_columna)

# Se imprime los nombres de las columnas que tiene el Excel.
print(w_datos_excel.columns.values)

# Se imprime todos los datos del Excel por consola.
print(w_datos_excel)

''' 
----------------------------------------------------------------------------------------------------------------
| FILTRADO DE DATOS
----------------------------------------------------------------------------------------------------------------
'''

# Vamos a guardar en una variable los registros que tengan como idioma el valor "Español".
w_datos_espanol = w_datos_excel[w_datos_excel['Idioma'] == 'Español']

# Se imprime por pantalla cuantos libros son en español.
print('\nNº de libros en español: {}\n'.format(len(w_datos_espanol)))

# Se imprimen los datos de los libros en español.
print(w_datos_espanol)

# De esos libros en español, quiero que me muestren los que tienen mas de 100 paginas.
w_datos_filtrados = w_datos_espanol[w_datos_espanol['Num_pag'] > 100]

# Se imprime por pantalla cuantos libros son en español con más de 100 páginas.
print('\nNº de libros en español con más de 100 páginas: {}\n'.format(len(w_datos_filtrados)))

# Se imprimen los libros en español que tienen mas de 100 páginas.
print(w_datos_filtrados)

# Se imprimne por pantalla cuantos registros y cuantas columnas tiene en total el archivo Excel.
# Para ello se utiliza el método "shape" y devuelve una tupla (nº fila, nº columna).
w_numexcel = w_datos_excel.shape
w_numfilas = w_numexcel[0]
w_numcolumnas = w_numexcel[1]

print('\nEl archivo Excel tiene {} filas y {} columnas en total.'.format(w_numfilas, w_numcolumnas))