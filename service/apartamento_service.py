from db import conect
from models.apartamento import Apartamento

class ApartamentoService:
    @staticmethod
    def insertar_apartamento(apartamento):
        connection = conect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Apartamentos (nombre, cantidad_apartamentos, capacidad_adultos, ubicacion_id) VALUES (%s, %s, %s, %s)",
                       (apartamento.nombre, apartamento.cantidad_apartamentos, apartamento.capacidad_adultos, apartamento.ubicacion_id))
        connection.commit()
        connection.close()
        
    
   
    @staticmethod
    def buscar_hospedajes_por_letras_apart(primeras_letras):
        connection = conect()
        cursor = connection.cursor()
        query = """
            SELECT a.nombre AS nombre_apartamento, a.cantidad_apartamentos, a.capacidad_adultos, u.nombre_ciudad, u.nombre_provincia
            FROM Apartamentos a
            INNER JOIN Ubicacion u ON a.ubicacion_id = u.id
            WHERE a.nombre LIKE %s
            ORDER BY a.nombre
        """
        cursor.execute(query, (primeras_letras + '%',))
        hospedajes = cursor.fetchall()
        connection.close()
        return hospedajes
