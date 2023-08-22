from pyodbc import IntegrityError, ProgrammingError

from Dato.conexion import Conexion
from Dominio.Estudiante import Estudiante


class Estudiantedao:
    _INSERTAR = "INSERT INTO Estudiantes (Cedula,Nombre,Apellido,Email,Carrera,Activo,Estatura,Peso, F_nacimiento)" \
                " VALUES (?,?,?,?,?,?,?,?,?)"
    _SELECIONAR_X_CEDULA = "select id, cedula, nombre, apellido, email, carrera, activo, estatura, peso, f_nacimiento "\
                           "from Estudiantes " "where cedula = ?"

    _SELECIONAR = "select id, cedula, nombre, apellido, email, carrera, activo, estatura, peso, f_nacimiento " \
                  "from Estudiantes where Activo = 1 "
    @classmethod
    def insertar_estudiante(cls,Estudiante):
        respuesta= {'exito':False,'mensaje':''}
        flag_exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                dato= (Estudiante.cedula,Estudiante.nombre, Estudiante.apellido,Estudiante.email,Estudiante.carrera,
                        Estudiante.activo, Estudiante.estatura, Estudiante.peso, Estudiante.f_nacimiento)
                cursor.execute(cls._INSERTAR, dato)
                flag_exito = True
                mensaje = 'Ingreso Exitoso'
        except IntegrityError as e:
            flag_exito = False
            

            if e.__str__().find('cedula') > 0:
                print('Cédula ya ingresada.')
                mensaje = 'cedula ya ingresada'
            elif e.__str__().find('email') > 0:
                print('Email ya ingresado.')
                mensaje = 'email ya ingresado'
            else:
                print('Error de integridad')
                mensaje = 'error de integridad'

        except ProgrammingError as e:
            flag_exito = False
            print('Los datos ingresados no son del tamaño permitido')
            mensaje ='Los datos ingresados no son del tamaño permitido'

        except Exception as e:
            flag_exito = False
            print(e)

        finally:
            respuesta['exito'] = flag_exito
            respuesta['mensaje'] = mensaje
            return respuesta

    @classmethod
    def selecionar_por_cedula(cls, estudiante):
        persona_encontrada = None
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECIONAR_X_CEDULA, datos)
                persona_encontrada = resultado.fetchone()
                estudiante.email = persona_encontrada[4]
                estudiante.nombre = persona_encontrada[2]
                estudiante.apellido = persona_encontrada[3]
                estudiante.carrera = persona_encontrada[5]
                estudiante.activo = persona_encontrada[6]
                estudiante.cedula = persona_encontrada[1]
                estudiante.id = persona_encontrada[0]
                estudiante.estatura = persona_encontrada[7]
                estudiante.peso = persona_encontrada[8]
                estudiante.f_nacimiento = persona_encontrada[9]
        except Exception as e:
            print(e)
        finally:
            return estudiante

    @classmethod
    def seleccionar_estudiantes(cls):
        list_estudiantes = list()
        try:
            with Conexion.obtenerCursor() as cursor:
                resultado = cursor.execute(cls._SELECIONAR)
                for tupla_estudiante in resultado.fetchall():
                    estudiante = Estudiante()
                    estudiante.id = tupla_estudiante[0]
                    estudiante.cedula = tupla_estudiante[1]
                    estudiante.nombre = tupla_estudiante[2]
                    estudiante.apellido = tupla_estudiante[3]
                    estudiante.email = tupla_estudiante[4]
                    estudiante.carrera = tupla_estudiante[5]
                    estudiante.activo = tupla_estudiante[6]
                    estudiante.estatura = tupla_estudiante[7]
                    estudiante.peso = tupla_estudiante[8]
                    estudiante.f_nacimiento = tupla_estudiante[9]
                    list_estudiantes.append(estudiante)
        except Exception as e:
            list_estudiantes =None
        finally:
            return list_estudiantes

if __name__ == '__main__':
    estudiantes = Estudiantedao.seleccionar_estudiantes()
    for estudiante in estudiantes:
        print(estudiante)

'''
Integrantes grupo 15:
Darling medina Chalen 
Bryan Revelo Yagual
Katherine Sanchez Silva
'''
