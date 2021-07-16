"""
principal1: Es el "Motor" debe correrse este codigo para que comience la aplicacion, contine la coneccion a 
los otros archivos y el menu 
"""


from BD.conexion1 import DAO
import funciones1

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print("================ MENU PRINCIPAL ================")
            print("1- Listar cursos")
            print("2- Registrar curso")
            print("3- Modificar curso")
            print("4- Eliminar curso")
            print("5- Salir")
            print("=================================================")
            opcion = int(input("Selectione una opción:  "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente ...")
            elif opcion == 5:
                continuar = False
                print("Gracias por usar este sistema")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()
    
    if opcion == 1:
        try:
            cursos=dao.listarCursos()
            if len(cursos)>0:
                funciones1.listarCursos(cursos)
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrio un error...")
    
    elif opcion == 2:
        curso = funciones1.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except:
            print("Ocurrio un error...")  
    
    elif opcion == 3:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                curso = funciones1.pedirDatosActualizacion(cursos)
                if curso:
                    dao.actualizarCurso(curso)
                else:
                    print("Codigo de curso a actulizar no encontrado...\n")
            else:
                print("No se encontraron los cursos...")
        except:
            print("Ocurrio un error...")

    elif opcion == 4:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones1.pedirDatosEliminacion(cursos)
                if not(codigoEliminar ==""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print("Codigo de curso no encontrado... \n")
            else:
                print("No se encontraron los cursos...")
        except:
            print("Ocurrio un error...")
    
    else:
        print("Opcion no valida")

menuPrincipal()