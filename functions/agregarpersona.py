from tkinter import messagebox
import sqlite3
from datetime import datetime

def agregarperson(datoNom,datoAPE,datoC):

	erro1=False
	erro2=False
	erro3=False

	if datoC.isdigit() == False:

		messagebox.showerror('Aviso','Ingrese solo valores numericos en el campo -Numero Cc-')

		erro1=True
	
	if len(datoNom) < 3 or len(datoAPE) < 3 or len(datoC) < 5:

		messagebox.showerror('Aviso','Nombre, apellido o cedula muy corto')

		erro1=True

	if len(datoNom) > 12 or len(datoAPE) > 12:

		messagebox.showerror('Aviso','Nombre o apellido con muchos caracteres')

		erro3=True

	if erro1==False and erro2==False and erro3==False:

		try:
			miConexion=sqlite3.connect("bbdd/Listado.db")
		
			miCursor=miConexion.cursor()

			datos=datoNom, datoAPE, datoC, datetime.today().strftime('%Y-%m-%d')

			miCursor.execute("INSERT INTO Lista VALUES(?,?,?,?)", (datos))

			miConexion.commit()

			messagebox.showinfo('Aviso','Registros exitoso')

		except:

			messagebox.showerror('Aviso','Algo salio mal')