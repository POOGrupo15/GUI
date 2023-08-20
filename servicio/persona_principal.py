from datetime import date
from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from Dato.estudiante_dao import Estudiantedao
from Dominio.Docente import Docente
from Dominio.Estudiante import Estudiante
from UI.vtn_principal import Ui_vtn_principal


class PersonaPrincipal(QMainWindow):
  def __init__(self):
    super(PersonaPrincipal, self).__init__()
    self.ui = Ui_vtn_principal()
    self.ui.setupUi(self)
    self.ui.statusbar.showMessage('Bienvenido', 2000)
    self.ui.pBtton_Grabar.clicked.connect(self.Grabar)
    self.ui.pBtton_buscar_cedula.clicked.connect(self.buscar_x_cedula)
    self.ui.pBtton_estatura.clicked.connect(self.calculos_estatura)
    self.ui.pBtton_peso.clicked.connect(self.calculos_peso)
    self.ui.pBtton_edad.clicked.connect(self.calculos_edad)
    self.ui.line_cedula.setValidator(QtGui.QIntValidator())


    correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    validator = QRegularExpressionValidator(correo_exp, self)
    self.ui.line_email.setValidator(validator)

  def Grabar(self):
      tipo_persona = self.ui.cb_tipo_persona.currentText()
      if self.ui.line_nombre.text() == '' or self.ui.line_apellido.text() == ''\
              or len(self.ui.line_cedula.text()) < 10 or self.ui.line_email.text() == '':
         print('Completar Datos')
         QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios.')
      else:
        persona = None
        if tipo_persona == 'Docente':
          persona = Docente()
          persona.nombre = self.ui.line_nombre.text()
          persona.apellido = self.ui.line_apellido.text()
          persona.cedula = self.ui.line_cedula.text()
          persona.email = self.ui.line_email.text()
          persona.estatura = self.ui.sp_estatura.text()
        else:
          persona = Estudiante()
          persona.nombre = self.ui.line_nombre.text()
          persona.apellido = self.ui.line_apellido.text()
          persona.cedula = self.ui.line_cedula.text()
          persona.email = self.ui.line_email.text()
          persona.estatura = self.ui.sp_estatura.text()
          persona.peso = self.ui.line_peso.text()
          persona.f_nacimiento = self.ui.line_Fnacimiento.text()

          #insertar en la base de datos al estudiante
          respuesta = None
          respuesta = Estudiantedao.insertar_estudiante(persona)


        #archivo = None
        #try:
          #  archivo = open('archivo.txt', mode='a')
          # archivo.write(persona.__str__())
        # archivo.write('\n')
        #except Exception as e:
        # print('No se pudo grabar.')
        #finally:
          # if archivo:
        # archivo.close()
      if respuesta['exito']:
        self.ui.line_nombre.setText('')
        self.ui.line_apellido.setText('')
        self.ui.line_cedula.setText('')
        self.ui.line_email.setText('')
        self.ui.line_peso.setText('')
        self.ui.line_Fnacimiento.setText('')
        self.ui.sp_estatura.setValue(0)
        self.ui.statusbar.showMessage('Grabado con éxito, felicidades.', 2000)
      else:
        QMessageBox.critical(self, 'Error', respuesta['mensaje'])

  def buscar_x_cedula(self):
      cedula = self.ui.line_cedula.text()
      e = Estudiante(cedula=cedula)
      e = Estudiantedao.selecionar_por_cedula(e)
      print(e)
      self.ui.line_nombre.setText(e.nombre)
      self.ui.line_apellido.setText(e.apellido)
      self.ui.line_email.setText(e.email)
      self.ui.line_Fnacimiento.setText(e.f_nacimiento.__str__())
      self.ui.line_peso.setText(e.peso.__str__())
      self.ui.sp_estatura.setText(e.estatura)
      self.ui.cb_tipo_persona.setCurrentText('Estudiante')

  def calculos_estatura(self):
      estudiantes = Estudiantedao.seleccionar_estudiantes()
      estaturas = [estudiante.estatura for estudiante in estudiantes]
      promedio_estatura = sum(estaturas) / len(estaturas)

      # Ordenando las estaturas y calculando la mediana
      estaturas_sorted = sorted(estaturas)
      n = len(estaturas_sorted)
      if n % 2 == 0:  # Cantidad par de estaturas
          mediana_estatura = (estaturas_sorted[n // 2 - 1] + estaturas_sorted[n // 2]) / 2
      else:  # Cantidad impar de estaturas
          mediana_estatura = estaturas_sorted[n // 2]

      # Calculando la moda
      estatura_counts = {estatura: estaturas.count(estatura) for estatura in estaturas}
      max_count = max(estatura_counts.values())
      moda_estatura = [estatura for estatura, count in estatura_counts.items() if count == max_count]

      # Calculando las estaturas mínimo y máximo
      min_estatura = min(estaturas)
      max_estatura = max(estaturas)

      print(f'El promedio de estaturas es: {promedio_estatura:,.2f} Cm')
      print(f'La mediana de estaturas es: {mediana_estatura} Cm')
      print(f'La moda de estaturas es: {moda_estatura} Cm')
      print(f'La estatura mínima es: {min_estatura} Cm')
      print(f'La estatura máxima es: {max_estatura} Cm')

  def calculos_peso(self):
      estudiantes = Estudiantedao.seleccionar_estudiantes()
      pesos = [estudiante.peso for estudiante in estudiantes]
      promedio_peso = sum(pesos) / len(pesos)

      # Ordenando los pesos y calculando la mediana
      pesos_sorted = sorted(pesos)
      n = len(pesos_sorted)
      if n % 2 == 0:  # Cantidad par de pesos
          mediana_peso = (pesos_sorted[n // 2 - 1] + pesos_sorted[n // 2]) / 2
      else:  # Cantidad impar de pesos
          mediana_peso = pesos_sorted[n // 2]

      # Calculando la moda
      peso_counts = {peso: pesos.count(peso) for peso in pesos}
      max_count = max(peso_counts.values())
      moda_peso = [peso for peso, count in peso_counts.items() if count == max_count]

      # Calculando los pesos mínimo y máximo
      min_peso = min(pesos)
      max_peso = max(pesos)

      print(f'El promedio de peso es: {promedio_peso:,.2f} Kg')
      print(f'La mediana del peso es: {mediana_peso} Kg')
      print(f'La moda del peso es: {moda_peso} Kg')
      print(f'El peso mínimo es: {min_peso} Kg')
      print(f'El peso máximo es: {max_peso} Kg')

  def calculos_edad(self):
      estudiantes = Estudiantedao.seleccionar_estudiantes()
      f_nacimiento = [estudiante.f_nacimiento for estudiante in estudiantes]
      fecha_actual = date.today()

      edades = []
      for fecha in f_nacimiento:
          edad = fecha_actual.year - fecha.year - ((fecha_actual.month, fecha_actual.day) < (fecha.month, fecha.day))
          edades.append(edad)

      # Calculando el promedio de edad
      promedio_edad = sum(edades) / len(edades)

      # Ordenando las edades y calculando la mediana
      edades_sorted = sorted(edades)
      n = len(edades_sorted)
      if n % 2 == 0:  # Cantidad par de edades
          mediana_edad = (edades_sorted[n // 2 - 1] + edades_sorted[n // 2]) / 2
      else:  # Cantidad impar de edades
          mediana_edad = edades_sorted[n // 2]

      # Calculando la moda
      edad_counts = {edad: edades.count(edad) for edad in edades}
      max_count = max(edad_counts.values())
      moda_edad = [edad for edad, count in edad_counts.items() if count == max_count]

      # Calculando la edad máxima y mínima
      max_edad = max(edades)
      min_edad = min(edades)

      #for estudiante, edad in zip(estudiantes, edades):
         #print(f'Estudiante: {estudiante.nombre}, Edad: {edad} años')

      print(f'El promedio de edades es: {promedio_edad:.2f} años')
      print(f'La mediana de edades es: {mediana_edad} años')
      print(f'La moda de edades es: {moda_edad}')
      print(f'La edad máxima es: {max_edad} años')
      print(f'La edad mínima es: {min_edad} años')


'''
Integrantes grupo 15:
Darling medina Chalen 
Bryan Revelo Yagual
Katherine Sanchez Silva
'''