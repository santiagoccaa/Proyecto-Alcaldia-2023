import sqlite3
from tkinter import *
from tkinter import messagebox

def mostrarfila():

	ventana_listado=Toplevel()
	ventana_listado.title('Listado')
	ventana_listado.geometry('340x700')
	ventana_listado.config(bg='#36F1FD')

	titulo_listado=Label(ventana_listado, text="Lista Personas", font=('Poppins 20 bold')).place(x=50, y=5)
	#titulo_listado.grid(row=0, column=0, columnspan=4)

	Y=50

	diccionario={}


	try:
		miconexcion=sqlite3.connect('bbdd/Listado.db')

		micursor=miconexcion.cursor()

		sql= "SELECT * FROM Lista"

		micursor.execute(sql)

		personas = micursor.fetchall()

		for p in personas:
			diccionario

		for i in personas:

			Label(ventana_listado, text=i, font=('Poppins', 13), bg='black', fg='white').place(x=10, y=Y)

			Y=Y+30

	except:

		messagebox.showinfo('Avisto','Todo mal')


