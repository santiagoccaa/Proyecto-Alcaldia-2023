import sqlite3
from tkinter import messagebox

def createbbdd():
	#----------CREAR BASE DE DATOS--------------------

		micursor=miconexion.cursor()
		micursor.execute("CREATE DATABASE IF NOT EXISTS Personas")
		miconexion.close()
		micursor.close()

	#--------CREAR TABLA EN BASE DE DATOS-------------

		micursor=miconexion.cursor()

		micursor.execute("CREATE TABLE IF NOT EXISTS Datos (ID INT(100) AUTO_INCREMENT, Nombre VARCHAR(20) NOT NULL, Apellidos VARCHAR(50) NOT NULL, Cedula INT(12) NOT NULL UNIQUE, CONSTRAINT persona_pk PRIMARY KEY (ID))")

		messagebox.showinfo("Aviso","La BBDD se ha creado correctamente")

		micursor.close()
		miconexion.close()
	except:
		messagebox.showwarning("Aviso","ERROR AL INTENTAR CREAR LA BBDD")