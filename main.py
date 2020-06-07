from usuarios import validate_email, Alumno, Profesor, alumnos, profesores
from sistema_profesor import sistema_profesor

print('Bienvenido al sistema de administracion del personal')
print('Ingresa en el sistema:\n')
email = input('Ingresa tu correo electronico\n')

user = validate_email(email)

if user is not None:
    password = input('Ingresa tu contraseña:\n')
    while password != user.password:
        password = input('Contraseña incorrecta, intentalo de nuevo\n')
        # agregar contador de intentos
    if isinstance(user, Profesor):
        sistema_profesor(user)
    else:
        pass
else:
    response = input('No encontramos un usuario con este email, ¿Quieres crear uno? \nSi: Y\nNo: N\n')
    if response in ['Y', 'y']:
        email = input('Ingresa el correo electronico\n')
        password = input('Ingresa la contraseña\n')
        password2 = input('Repite la contraseña\n')
        nombre = input('Ingresa tu nomnbre\n')
        while password != password2:
            print('Las contraseñas no coinciden vuelve a intentarlo\n')
            password = input('Ingresa la contraseña\n')
            password2 = input('Repite la contraseña\n')
        print('Escoge el tipo de usuario\n')
        tipo = input('Profesor: P\nAlumno: A\n')
        while tipo not in ['P', 'p', 'A', 'a']:
            print('Opcion incorrecta escoge el tipo de usuario\n')
            tipo = input('Profesor: P\nAlumno: A\n')
        if tipo in ['P', 'p']:
            user = Profesor(email, password, nombre)
            profesores.append(user)
            sistema_profesor(user)
        else:
            user = Alumno(email, password, nombre)
            alumnos.append(user)
    else:
        print('Gracias por utilizar nuestro sistema')
