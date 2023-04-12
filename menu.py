import sqlite3
from tkinter import *

# Configuracion de la raiz
root = Tk()
root.title("Pulpa de mar - Menu")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="  Pulpa de mar   ", fg="darkgreen", font=("Times New Roman",28,"bold italic")).pack()
Label(root, text="Menu del dia", fg="darkblue", font=("Times New Roman",24,"bold italic")).pack()

# Separacion de titulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurant.db")
cursor = conexion.cursor()

# Buscar las categorias y platos de la bd

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
	Label(root, text=categoria[1], fg="black", font=("Times New Roman",20, "bold italic")).pack()
	
	platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
	for plato in platos:
		Label(root, text=plato[1], fg="gray", font=("Verdana",15,"italic")).pack()

	# Separacion entre categorias
	Label(root, text="").pack()	

conexion.close()

# Presio del menu
Label(root, text="10000$ (IVA incl.)", fg="darkgreen", font=("Times New Roman",20,"bold italic")).pack(side="right")

#Finalmente ejecutamos el bucle
root.mainloop()
