from db import conexionMySQL


# Create
def guardar_nuevo_paquete(nom, dest, desc, imgURL, prec, disp):

    conexion = conexionMySQL()
    result = 0

    try:
        with conexion.cursor() as cursor:
            query = "INSERT INTO Paquetes (nombre, destino, descripcion, imagen, precio, disponible) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (nom, dest, desc, imgURL, prec, disp))
            conexion.commit()
            result = cursor.rowcount
    except Exception as e:
        conexion.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        conexion.close()
        return result


# Read
def obtener_paquetes():
    # Conexion
    conexion = conexionMySQL()

    # Consulta db
    try:
        with conexion.cursor() as cursor:
            query = "SELECT * FROM paquetes"
            cursor.execute(query)
            resultados = cursor.fetchall()
            conexion.commit()

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        conexion.close()

    return resultados


# Update
def editar_paquete(id, nom, dest, desc, imgURL, prec, disp):

    conexion = conexionMySQL()
    result = 0

    try:
        with conexion.cursor() as cursor:
            query = "UPDATE Paquetes SET nombre = %s, destino = %s, descripcion = %s, imagen = %s, precio = %s, disponible = %s WHERE id = %s"
            cursor.execute(query, (nom, dest, desc, imgURL, prec, disp, id))
            conexion.commit()
            result = cursor.rowcount
    except Exception as e:
        conexion.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        conexion.close()

    return result


# Delete
def eliminar_paquete(id):

    conexion = conexionMySQL()
    result = 0

    try:
        with conexion.cursor() as cursor:
            query = "DELETE FROM paquetes WHERE id=%s"
            cursor.execute(query, id)
            result = cursor.rowcount
        conexion.commit()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        conexion.close()

    return result
