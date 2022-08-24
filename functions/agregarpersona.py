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

		if datonombre.get()=="" or datoapellido.get()=="" or datocedula.get()=="":

			messagebox.showinfo('Aviso','Verifique que todos los recuadros esten llenos')

		if len(datonombre.get()) < 3 or len(datoapellido.get())< 3 or len(datocedula.get())< 5:

			messagebox.showerror('Error', 'Cantidad de caracteres incorrecta')

		miconexcion=pymysql.connect()
		micrusor=miconexcion.cursor()

		sql=('INSER INTO Datos (Nombre, Apellidos, Cedula) Values (%s, %s, %s)')
		datos=(datonombre.get(), datoapellido.get(), datocedula.get())

		micrusor.execute(sql, datos)

		miconexcion.commit()
		miconexcion.close()
except:
	messagebox.showwarning("Aviso", "Error al intentar agregar persona")