import sqlite3
BASE_DE_DATOS = "inventario.db"

def obtener_conexion():
    return sqlite3.connect(BASE_DE_DATOS)


def crear_tablas():
    tablas = [
        """
        CREATE TABLE IF NOT EXISTS diccionario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            significado TEXT NOT NULL
        );
        """
    ]
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    for tabla in tablas:
        cursor.execute(tabla)


def principal():
    crear_tablas()
    menu = """
1) Registrar articulo
2) Editar articulo
3) Eliminar articulo
4) Buscar articulo
6) Salir
Elige: """
    eleccion = ""
    while eleccion != "6":
        eleccion = input(menu)
        if eleccion == "1":
            palabra = input("\nRegistrar Articulo: ")
            # Comprobar si no existe
            posible_significado = buscar_significado_palabra(palabra)
            if posible_significado:
                print(f"El Articulo '{Palabra}' ya existe")
            else:
                significado = input("Descripcion del articulo: ")
                agregar_palabra(palabra, significado)
                print("Descripcion agregada")
        if eleccion == "2":
            palabra = input("\nIngresa el articulo que quieres editar: ")
            nuevo_significado = input("Ingresa la nueva descripcion: ")
            editar_palabra(palabra, nuevo_significado)
            print("Descripcion actualizada ")
        if eleccion == "3":
            palabra = input("\nIngresa la palabra a eliminar: ")
            eliminar_palabra(palabra)
        if eleccion == "4":
            palabra = input(
                "\nIngresa el articulo al cual quieres la descripcion: ")
            significado = buscar_significado_palabra(palabra)
            if significado:
                print(f"La descripcion de '{palabra}' es:\n{significado[0]}")
            else:
                print(f"Articulo '{palabra}' no encontrado")


def agregar_palabra(palabra, significado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO diccionario(palabra, significado) VALUES (?, ?)"
    cursor.execute(sentencia, [palabra, significado])
    conexion.commit()


def editar_palabra(palabra, nuevo_significado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "UPDATE diccionario SET significado = ? WHERE palabra = ?"
    cursor.execute(sentencia, [nuevo_significado, palabra])
    conexion.commit()


def eliminar_palabra(palabra):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM diccionario WHERE palabra = ?"
    cursor.execute(sentencia, [palabra])
    conexion.commit()


def obtener_palabras():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT palabra FROM diccionario"
    cursor.execute(consulta)
    return cursor.fetchall()


def buscar_significado_palabra(palabra):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT significado FROM diccionario WHERE palabra = ?"
    cursor.execute(consulta, [palabra])
    return cursor.fetchone()


if __name__ == '__main__':
    principal()
