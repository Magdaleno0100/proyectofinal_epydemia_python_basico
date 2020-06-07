import random
import string
from datetime import datetime

from materias import materias


class Usuario(object):
    def __init__(self, email, password, nombre):
        self.email = email
        self.password = password
        self.nombre = nombre

    def __str__(self):
        return f'{self.nombre} - {self.email}'


class Alumno(Usuario):

    def __init__(self, email, password, nombre):
        self.email = email
        self.password = password
        self.nombre = nombre
        self.matricula = 'matric' # Cambiar a matricula en prod
        self.colegiatura = datetime.now()
        self.materias = []
        self.calificaciones = {llave: 0 for llave in materias}

    def crear_matricula(self):
        letras = string.ascii_lowercase
        return ''.join(random.choice(letras) for i in range(5))
    
    def cambiar_calificacion(self, materia, calificacion):
        self.calificaciones.update({materia: calificacion})
        print('Se agrego la califacion con exito')


    @staticmethod
    def agregar_materia(matricula, materia):
        alumno = Alumno.obtener_por_matricula(matricula)
        if alumno is None:
            print('El alumno no existe en la base de datos')
        else:
            materia.alumnos.append(alumno)
            print(f'El alumno se ha agregado con exito a la materia {materia}')

    @staticmethod
    def obtener_por_matricula(matricula):
        for alumno in alumnos:
            if alumno.matricula == matricula:
                return alumno
        return


class Profesor(Usuario):
    def __init__(self, *args, **kwargs):
        super(Profesor, self).__init__(*args, **kwargs)
        self.materias = []

    def agregar_materia(self, indice):
        try:
            materia = materias[indice]
        except IndexError:
            print(f'La materia con el indice {indice} no existe')
        else:
            self.materias.append(materia)


def validate_email(email):
    for user in (alumnos + profesores):
        if user.email == email:
            return user
    return None

alumnos, profesores = [Alumno('ivanl@mail.com', '12345', 'Ivan Lopez')], [Profesor('chris@mail.com', '12345', 'Christian')]
