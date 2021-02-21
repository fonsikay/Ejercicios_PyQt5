# Se importa la libreria que indica que la clase es abstracta y no hereda de nadie.
from abc import ABC


# ------ INICIO DE LA CREACIÓN DE LA HERENCIA ENTRE LA CLASE PERSONA CON LAS CLASES ESTUDIANTE Y PROFESOR --------------

# Se define la clase Persona que no hereda de ninguna clase por lo que se indica que su herencia es abstracta con el
# valor "ABC".
class Persona(ABC):

    # Se define el constructor de la clase con los 3 atributos específicos de esta clase que van a compartir las otras
    # dos clases creadas.
    def __init__(self, identidad, nombre_completo, telefono):

        # Declaramos los atributos propios de la clase Persona.
        self.identidad = identidad
        self.nombre_completo = nombre_completo
        self.telefono = telefono


# Se define la clase Estudiante que va a heredar los 3 atributos propios de la clase padre Persona.
class Estudiante(Persona):

    # Se define el constructor de la clase Estudiante indicando los 3 atributos heredados de la clase Padre "Persona"
    # y los 2 atributos propios de la clase Estudiante.
    def __init__(self, identidad, nombre_completo, telefono, carnet, carrera):

        # El método "super()" hace que se pueda utilizar en esta clase los 3 atributos heredados de la clase padre
        # "Persona".
        super().__init__(identidad, nombre_completo, telefono)

        # Declaramos los atributos propios de la clase Estudiante.
        self.carnet = carnet
        self.carrera = carrera


# Se define la clase Profesor que va a heredar los 3 atributos propios de la clase padre Persona.
class Profesor(Persona):

    # Se define el constructor de la clase Profesor indicando los 3 atributos heredados de la clase Padre "Persona" y
    # el atributo propio de la clase Profesor.
    def __init__(self, identidad, nombre_completo, telefono, especialidad):

        # El método "super()" hace que se pueda utilizar en esta clase los 3 atributos heredados de la clase padre
        # "Persona".
        super().__init__(identidad, nombre_completo, telefono)

        # Declaramos los atributos propios de la clase Profesor.
        self.especialidad = especialidad


# ------- FIN DE LA CREACIÓN DE LA HERENCIA ENTRE LA CLASE PERSONA CON LAS CLASES ESTUDIANTE Y PROFESOR ----------------
# ------- CREACIÓN DE LOS OBJETOS DE LAS CLASES QUE ACABAMOS DE CREAR --------------------------------------------------

# Creación de un objeto de la clase Estudiante llamada "alumno1".
alumno1 = Estudiante('5055', 'Alfonso López Jiménez', '666207804', 'EST-00001', 'Informática')

# Se imprime el objeto en sí.
print(alumno1)
# Resultado: <__main__.Estudiante object at 0x0000017222BD69D0> - Nos indica que es una clase de tipo  Estudiante.

# Se imprime la información del atributo "identidad".
print(alumno1.identidad)
# Resultado: 5055

# Se imprime la información del atributo "nombre_completo".
print(alumno1.nombre_completo)
# Resultado: Alfonso López Jiménez

# Creación de un objeto de la clase Estudiante llamada "alumno2".
alumno2 = Estudiante('3048', 'Isabel Ferral Cabrera', '648232289', 'EST-00002', 'Imágen y Sonido')

# Se imprime el objeto en sí.
print(alumno2)
# Resultado: <__main__.Estudiante object at 0x0000028CB4E169D0> - Nos indica que es una clase de tipo  Estudiante.

# Se imprime la información del atributo "identidad".
print(alumno2.identidad)
# Resultado: 3048

# Se imprime la información del atributo "nombre_completo".
print(alumno2.nombre_completo)
# Resultado: Isabel Ferral Cabrera

# Se imprime la información del atributo "carrera".
print(alumno2.carrera)
# Resultado: Imágen y Sonido

# Si se hace una comparación entre los dos objetos utilizando los operador de igualdad "==", como tienen datos
# distintos nos devuelve el valor False.
print(alumno1 == alumno2)
# Resultado: False

# Si se hace una comparación entre los dos objetos utilizando el operador "is" que es lo mismo que el operador de
# igualdad "==", como tienen datos distintos nos devuelve el valor False.
print(alumno1 is alumno2)
# Resultado: False

