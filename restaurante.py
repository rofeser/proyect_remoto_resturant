import sqlite3

def crear_bd():
	conexion = sqlite3.connect("restaurant.db")
	cursor = conexion.cursor()

	try:
		cursor.execute('''CREATE TABLE categoria(
			    id INTEGER PRIMARY KEY AUTOINCREMENT,
			    nombre VARCHAR(100) UNIQUE NOT NULL)''')

	except sqlite3.OperationalError:
		print("La tabla categorias ya existe.")

	else:
		print("La tabla categorias se ha creado correctamente")

	try:
		cursor.execute('''CREATE TABLE plato(
			    id INTEGER PRIMARY KEY AUTOINCREMENT,
			    nombre VARCHAR(100) UNIQUE NOT NULL,
			    categoria_id INTEGER NOT NULL,
			    FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
	except sqlite3.OperationalError:
		print("La tabla platos ya existe")

	else:
		print("La tabla platos se ha creado correctamente.")

	conexion.close()

def agregar_categoria():
	categoria = input("¿Nombre de la nueva categoria\n> ")

	conexion = sqlite3.connect("restaurant.db")
	cursor = conexion.cursor()

	try:
		cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))
	except sqlite3.OperationalError:
		print("La categoria '{}' ya existe.".format(categoria))
	else:
		print("categoria '{}'creada correctemente.".format(categoria))
		
	conexion.commit()
	conexion.close()

def agregar_plato():

	conexion = sqlite3.connect("restaurant.db")
	cursor = conexion.cursor()



	categorias = cursor.execute("SELECT * FROM categoria").fetchall()
	print("Seleccionar una categoria para añadir el plato:")
	for categoria in categorias:
		print("[{}] {}".format(categoria[0], categoria[1]))

	categoria_usuario = int(input(">  "))

	plato = input("¿Nombre del nuevo plato?\n> ")

	try:
		cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(plato, categoria_usuario))
	except sqlite3.integrityError:
		print("El plato '{}' ya existe.".format(plato))
	else:
		print("Plato '{}' creado correctamente.".format(plato))

		
	conexion.commit()
	conexion.close()

def mostrar_menu():

	conexion = sqlite3.connect("restaurant.db")
	cursor = conexion.cursor()

	

	categorias = cursor.execute("SELECT * FROM categoria").fetchall()
	for categoria in categorias:
		print(categoria[1])
		platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
		for plato in platos:
			print("\t{}".format(plato[1]))

	conexion.close()		


# Crear la base de datos	
crear_bd()

# Menu de opciones del programa

while True:
	print("\nBienvenidos al gestor del Restaurante!")
	opcion = input("\nIntroduce una opcion:\n[1] Agregar una categoria\n[2] Agregar un plato\n[3] Mostrar el menu\n[4] Salir del programa\n\n> ")

	if opcion == "1":
		agregar_categoria()

	elif opcion == "2":	
		agregar_plato()
		

	elif opcion == "3":
		mostrar_menu()

	elif opcion == "4":
		print("Nos vemos!")
		break
		

	else:
		print("Opcion incorrecta")
		