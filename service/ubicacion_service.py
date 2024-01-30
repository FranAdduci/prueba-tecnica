from db import conect

class UbicacionService:
    @staticmethod
    def insert_ubicacion(nombre_ciudad, nombre_provincia):
        connection = conect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO ubicacion (nombre_ciudad, nombre_provincia) VALUES (%s, %s)",
                       (nombre_ciudad, nombre_provincia))
        connection.commit()
        connection.close()
        
        
    @staticmethod
    def obtener_ubicacion_por_ciudad_provincia(nombre_ciudad, nombre_provincia):
        connection = conect()
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM Ubicacion WHERE nombre_ciudad = %s AND nombre_provincia = %s", (nombre_ciudad, nombre_provincia))
        result = cursor.fetchone()
        connection.close()
        
        if result:
            return result[0]  # Devuelve el ID de ubicación si se encontró
        else:
            return None
