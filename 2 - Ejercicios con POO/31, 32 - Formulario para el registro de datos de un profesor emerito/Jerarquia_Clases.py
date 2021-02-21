# Se importa la clase abstracta para objetos.
from abc import ABC


# Creación de la clase principal Persona.
class Persona(ABC):

    # Creación del constructor cargando sus tres atributos propios.
    def __init__(self, identidad, nombre_completo, telefono):

        # Se cargan los atributos propios.
        self.identidad = identidad
        self.nombre_completo = nombre_completo
        self.telefono = telefono


# Creación de la clase Estudiante que es subclase de la clase Persona.
class Estudiante(Persona):

    # Creación del constructor cargando sus tres atributos heredados de Persona y sus dos atributos propios.
    def __init__(self, identidad, nombre_completo, telefono, carnet, carrera):

        # Se cargan los atributos heredados de la clase Persona.
        super().__init__(identidad, nombre_completo, telefono)

        # Se cargan los atributos propios.
        self.carnet = carnet
        self.carrera = carrera


# Creación de la clase Profesor que es subclase de la clase Persona.
class Profesor(Persona):

    # Creación del constructor cargando sus tres atributos heredados de Persona y su atributo propio.
    def __init__(self, identidad, nombre_completo, telefono, especialidad):

        # Se cargan los atributos heredados de la clase Persona.
        super().__init__(identidad, nombre_completo, telefono)

        # Se cargan los atributos propios.
        self.especialidad = especialidad


# Creación de la clase Catedrático que es subclase de la clase Profesor.
class Catedratico(Profesor):

    # Creación del constructor cargando sus tres atributos heredados de Persona, su atributo heredado de Profesor  y
    # su atributo propio.
    def __init__(self, identidad, nombre_completo, telefono, especialidad, horas_semana):

        # Se cargan los atributos heredados de la clase Persona y Profesor.
        super().__init__(identidad, nombre_completo, telefono, especialidad)

        # Se cargan el atributo propio.
        self.horas_semana = horas_semana


# Creación de la clase Emérito que es subclase de la clase Profesor.
class Emerito(Profesor):

    # Creación del constructor cargando sus tres atributos heredados de Persona, su atributo heredado de Profesor  y
    # su atributo propio.
    def __init__(self, identidad, nombre_completo, telefono, especialidad, reconocimiento):

        # Se cargan los atributos heredados de la clase Persona y Profesor.
        super().__init__(identidad, nombre_completo, telefono, especialidad)

        # Se cargan el atributo propio.
        self.reconocimiento = reconocimiento

