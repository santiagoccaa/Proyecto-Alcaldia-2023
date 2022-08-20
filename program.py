from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from functions.crearBBDD import createbbdd

#-----------------BASE-------------------------------
root=Tk()
root.geometry("750x550") #tamaño de la ventana
root.resizable(0,0) # 1 para permitir agrandar 0 para no permitir
root.title("Programa") # titulo
root.config(bg="#FFFFFF") # color ventana
root.iconbitmap('images/logo.ico') # icono de la ventana

#-----IMAGEN-----------------------------------------

image =Image.open('images/imagen.jpg') #directorio de imagen
image =image.resize((400,360))

img=ImageTk.PhotoImage(image)
lbl_img=Label(root, image=img).place(x=-25,y=10)# ubicacion de la imagen

#----------------MENU--------------------------------

menubd = Menu(root) # nombre del menu
root.config(menu=menubd)

bbddmenu = Menu(menubd, tearoff=0) # para eliminar unas lineas feas que salen
bbddmenu.add_command(label="Crear BBDD", command=lambda:createbbdd()) # contenido de caja de BBDD
bbddmenu.add_command(label="Abrir Listado")
bbddmenu.add_separator()
bbddmenu.add_command(label="Salir")

helpmenu = Menu(menubd, tearoff=0) # contenido de caja de Informacion
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubd.add_cascade(label="BBDD", menu=bbddmenu) # Caja que se muestra en la interfaz
menubd.add_cascade(label="Informacion", menu=helpmenu)


#-----------------PRIMER FRAME-----------------------
framebd=Frame(root, width=400, height=500, relief='raised', bd=5 ,bg='#36F1FD').place(x=340, y=10) #para el borde de la caja de contenido (flat raised sunken groove ridge)
framecontenido=Frame(root, width=380, height=480, bg='#CEFFFF').place(x=350, y=20) # caja donde va el contenido


titulo=Label(framecontenido, text="Registro", font=("Poppins 25 bold"), bg='#CEFFFF').place(x=470, y=50) # para el titulo

#----------------DATOS-------------------------------

nombre=Label(framecontenido, text="Nombre:", font=("Poppins 15"), bg='#CEFFFF').place(x=400, y=110) # titulo nombre
nentry=Entry(framecontenido, font=("Poppins 14"), justify=CENTER).place(x=410, y=150) # caja de texto para escribir nombre

apellidos=Label(framecontenido, text="Apedillos:", font=("Poppins 15"), bg='#CEFFFF').place(x=400, y=190) #titulo apellido
aentry=Entry(framecontenido, font=("Poppins 14"), justify=CENTER).place(x=410, y=230) #caja de texto para escribir apellido

cedula=Label(framecontenido, text="Numero CC:", font=("Poppins 15"), bg='#CEFFFF').place(x=400, y=270) #titulo cedula
centry=Entry(framecontenido, font=("Poppins 14"), justify=CENTER).place(x=410, y=310) # caja para escribir la cedula

#---------------Botones-----------------------------

botonregistro=Button(framecontenido, text="Registrar", font=("Poppins 14 bold"), bd=4).place(x=420, y=360)

root.mainloop() # bucle para que la interfaz no se cierre