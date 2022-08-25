import sqlite3
from tkinter import messagebox
import datetime

def createbbdd():

	try:
		miConexion=sqlite3.connect("bbdd/Listado.db")

		miCursor=miConexion.cursor()

		miCursor.execute("CREATE TABLE Lista (Nombre VARCHAR(50) NOT NULL, Apellidos VARCHAR(50) NOT NULL, Cedula INT(10) NOT NULL, Fecha_Ingreso TIMESTAMP NOT NULL)")

		miConexion.commit()

		miConexion.close()
		
		messagebox.showinfo("Aviso", "BBDD creada")
	except:
		messagebox.showwarning("Aviso", "LA BBDD YA EXISTE")
