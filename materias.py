class Materia:

    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []
        self.profesor = None

    def __repr__(self):
        return self.nombre

    def __str__(self):
        # print()
        return self.nombre

    def existe_alumno(self, matricula):
        for alumno in self.alumnos:
            if alumno.matricula == matricula:
                return alumno
        return

materias = [Materia(nombre) for nombre in ['Español', 'Matemáticas', 'Civismo', 'Ciencias', 'Programación']]
