from tkinter import messagebox
import pymysql

try:
	def agregarperon():
		miconexcion=pymysql.connect(
			host='localhost',
			user='root',
			password='',
			bd='Personas'
		)

		miconexcion=pymysql.connect()
		micrusor=miconexcion.cursor()

		sql=('INSER INTO Datos (Nombre, Apellidos, Cedula) Values (%s, %s, %s)')
		datos=(datonombre.get(), datoapellido.get(), datocedula.get())

		micrusor.execute(sql, datos)

		miconexcion.commit()
		miconexcion.close()
except:
	messagebox.showwarning("Aviso", "Error al intentar agregar persona")




