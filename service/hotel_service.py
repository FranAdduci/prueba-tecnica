from db import conect
from models.hotel import Hotel

class HotelService:
    @staticmethod
    def insertar_hotel(hotel):
        connection = conect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Hoteles (nombre, estrellas, tipo_habitacion_estandar, ubicacion_id) VALUES (%s, %s, %s, %s)",
                       (hotel.nombre, hotel.estrellas, hotel.tipo_habitacion_estandar, hotel.ubicacion_id))
        connection.commit()
        connection.close()
        
    @staticmethod
    def buscar_hospedajes_por_letras_hotel(primeras_letras):
        connection = conect()
        cursor = connection.cursor()
        query = """
            SELECT h.nombre AS nombre_hotel, h.estrellas, h.tipo_habitacion_estandar, u.nombre_ciudad, u.nombre_provincia
            FROM Hoteles h
            INNER JOIN Ubicacion u ON h.ubicacion_id = u.id
            WHERE h.nombre LIKE %s
            ORDER BY h.nombre
        """
        cursor.execute(query, (primeras_letras + '%',))
        hospedajes = cursor.fetchall()
        connection.close()
        return hospedajes
    
        
   

