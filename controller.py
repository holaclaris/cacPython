from db import conexionMySQL

#Read

def obtener_paquetes():
    #Conexion
    conexion = conexionMySQL()
    
    # Consulta db
    with conexion.cursor() as cursor:
        query = "SELECT * FROM paquetes"
        cursor.execute(query)
        resultados = cursor.fetchall()
        conexion.commit()

    # Cerrar conexion
        conexion.close()

        return resultados

# Pendientes:
# Create
# Update


#Delete

def eliminar_paquete(id):

    conexion= conexionMySQL()
    
    with conexion.cursor() as cursor:
        query = "DELETE FROM paquetes WHERE id=%s"
        cursor.execute(query, id)
        result = cursor

    conexion.commit()
    conexion.close()

    return result
