from tkinter import messagebox
import sqlite3
from datetime import datetime


def agregarperson(datoNom,datoAPE,datoC):

	miConexion=sqlite3.connect("bbdd/Listado.db")
	
	miCursor=miConexion.cursor()

	try: 
		datos=datoNom, datoAPE, datoC, datetime.today().strftime('%Y-%m-%d')

		miCursor.execute("INSERT INTO Lista VALUES(?,?,?,?)", (datos))

		miConexion.commit()

		messagebox.showinfo('Aviso','Registros exitoso')

	except:
		messagebox.showerror("Error", "Algo salio mal, revisa que todos los campos este llenos")
		pass