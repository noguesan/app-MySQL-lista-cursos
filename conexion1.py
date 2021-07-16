"""
conexion1: contiene la clase DAO (Data Access Object) la cual tiene las conexiones y ordenes para MySQL 
"""
import mysql.connector
from mysql.connector import Error

class DAO ():     #DAO = Data Access Object

    def __init__(self):
        """
        Conecta a la base de datos
        """
        try:
            self.conexion=mysql.connector.connect(
                host = 'localhost',
                user = 'trabajo1',
                password = 'LO QUE CORRESPONDA!!!!!!!',
                database = 'Universidad1'
                )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarCursos(self): 
        """
        Se conecta a la BD, y selecciona los datos de la table
        (En funciones hay una funcion con este nombre)
        """
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM cursos1 ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarCurso(self, curso):
        """
        Se conecta a la BD, y selecciona los datos de la table
        """
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO cursos1 (Codigo, Nombre, Creditos) VALUES ('{0}', '{1}','{2}')"
                cursor.execute(sql.format(curso[0], curso[1], curso [2]))
                self.conexion.commit()
                print(("¡Curso registrado! \n"))
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex)) 


    def actualizarCurso(self, curso):
        """
        Cambia el nombre y creditos de un dato
        """
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE cursos1 SET nombre = '{0}', creditos = {1} WHERE codigo = '{2}'"
                cursor.execute(sql.format(curso[1], curso[2], curso [0]))
                self.conexion.commit()
                print(("¡Curso actualizado! \n"))
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex)) 

  
    def eliminarCurso(self, codigoCursoEliminar):
        """
        Elimina un dato
        """
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM cursos1 WHERE Codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print(("¡Curso eliminado! \n"))
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex)) 