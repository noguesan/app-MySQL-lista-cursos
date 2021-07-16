"""
funciones1: contine las funciones de la aplicacion
"""


def listarCursos(cursos):    
    """
    Lista todos los cursos que esten en la tabla, recorre curso por curso a traves de un ciclo "for"
    (En conexion hay una funcion con el mismo nombre) 
    """
    print("\n Cursos: \n ")
    contador = 1
    for cur in cursos:
        datos ="{0}.Código: {1} | Nombre: {2} ({3} créditos)" 
        print(datos.format(contador,cur[0],cur[1],cur[2]))
        contador = contador +1
    print(" ")



def pedirDatosRegistro ():
    """
    Pide los datos para ingresar un nuevo dato (codigo, nombre y creditos),
    y devuelve estos valores como la varible curso
    """
    codigoCorrecto=False
    while(not codigoCorrecto):
        codigo = input("Ingrese codigo: ")
        if len(codigo)==6:
            codigoCorrecto = True
        else:
            print("Codigo incorrecto: Debe tener 6 digitos")

    nombre = input("Ingrese nombre: ")
    
    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese créeditos: ")
        if creditos.isnumeric():
            if (int(creditos)>0): # ya de por si no acepta numeros negativos creo que int no recnoce numeros negativos, esto es solo para que no tome el 0
                creditosCorrecto = True
                creditos=int(creditos)
            else:
                print("Los creditos deben ser mayor a 0")
        else:
            print("Creditos incorrectos: Debe ser un número únicamente.")
    
    curso = (codigo, nombre, creditos)
    return curso


def pedirDatosActualizacion(cursos):
    """
    Pide los datos para modificar un registro, y devuelve los nuevos datos como la varible curso
     para actulziar el dato correspondiente 
    """
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = int(input("Ingrese el codigo del curso a editar: ")) #el int no estaba en la tutorial
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("Ingrese nombre nuevo: ")
        
        creditosCorrecto = False
        while(not creditosCorrecto):
            creditos = input("Ingrese créeditos: ")
            if creditos.isnumeric():
                if (int(creditos)>0): # ya de por si no acepta numeros negativos creo que int no recnoce numeros negativos, esto es solo para que no tome el 0
                    creditosCorrecto = True
                    creditos=int(creditos)
                else:
                    print("Los creditos deben ser mayor a 0")
            else:
                print("Creditos incorrectos: Debe ser un número únicamente.")
        
        curso = (codigoEditar, nombre, creditos)
    else:
        curso = None

    return curso


def pedirDatosEliminacion(cursos):
    """
    Pide los datos para la eliminacion de un codigo y devuelve el dato a eliminar como la varible "codigoEliminar"
    """
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = int(input("Ingrese el codigo del curso a eliminar: ")) #el int no estaba en la tutorial
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar

