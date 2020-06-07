from materias import materias
from usuarios import Alumno
# pista memoria persistente sqlite

def sistema_profesor(profesor):
    print(f'Bienvenido profesor {profesor.nombre}!\n')
    if profesor.materias:
        print('Esocoge una de las siguientes opciones en el menu:')
        opcion = input('1: Agregar alumno a clase\n2: Agregar calificacion\nPresiona q para salir.')
        while opcion not in ['1', '2', 'q']:
            opcion = input('Opcion invalida escoge una de las siguientes opciones.\n1: Agregar alumno a clase\n2: Agregar calificacion\nPresiona q para salir.\n')
        if opcion == '1':
            print('Escoge las materias')
            for index in range(len(profesor.materias)):
                print(f'{index}: {profesor.materias[index]}\n')
            opcion_materia = int(input())
            materia = profesor.materias[opcion_materia]
            matricula = input(f'{opcion_materia} - Ingresa la matricula del estudiante.\n')
            Alumno.agregar_materia(matricula, materia)
            sistema_profesor(profesor)
        elif opcion == '2':
            print('Escoge la materia:\n')
            for index in range(len(profesor.materias)):
                print(f'{index}: {profesor.materias[index]}\n')
            opcion_materia = int(input())
            materia = profesor.materias[opcion_materia]
            import pudb; pudb.set_trace()
            len_materias = len(materia.alumnos)
            if len_materias > 0:
                for index in range(len_materias):
                    print(f'{index}: {materia.alumnos[index]}')
            else:
                print('La materia no tiene alumnos')
                sistema_profesor(profesor)
            opcion_alumnos = int(input('Escoge el ID del alumno\n'))
            alumno = materia.alumnos[opcion_alumnos]
            calificacion = float(input('Ingresa la calificacion:\n'))
            alumno.cambiar_calificacion(materia, calificacion)
            print(alumno.calificaciones)
            sistema_profesor(profesor)
        else:
            # Fin del programa
            return
    else:
        print('Escoge las materias que impartes separandolas por comas.\n')
        for indice in range(len(materias)):
            print(f'{indice}: {materias[indice]}\n')
        response = input()  # '1,2,3'
        for indice in response.split(',') :   # ['1', '2', '3']
            profesor.agregar_materia(int(indice))
        print('Las materias fueron agregadas')
        print(profesor.materias)
        sistema_profesor(profesor)
