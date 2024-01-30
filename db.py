import mysql.connector

#Conexión a la BD y creo las tablas si no existen.

def conect():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='destiniadb'
    )

def crear_tablas():
    connection = conect()
    cursor = connection.cursor()
    
    
    cursor.execute("SHOW TABLES LIKE 'Ubicacion'")
    if not cursor.fetchone():        
        cursor.execute("""
            CREATE TABLE Ubicacion (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre_ciudad VARCHAR(100) NOT NULL,
                nombre_provincia VARCHAR(100) NOT NULL
            )
        """)
    
    
    cursor.execute("SHOW TABLES LIKE 'Hoteles'")
    if not cursor.fetchone():
        cursor.execute("""
            CREATE TABLE Hoteles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                estrellas INT NOT NULL,
                tipo_habitacion_estandar VARCHAR(50) NOT NULL,
                ubicacion_id INT,
                FOREIGN KEY (ubicacion_id) REFERENCES Ubicacion(id)
            )
        """)

    
    cursor.execute("SHOW TABLES LIKE 'Apartamentos'")
    if not cursor.fetchone():
        cursor.execute("""
            CREATE TABLE Apartamentos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                cantidad_apartamentos INT NOT NULL,
                capacidad_adultos INT NOT NULL,
                ubicacion_id INT,
                FOREIGN KEY (ubicacion_id) REFERENCES Ubicacion(id)
            )
        """)

    connection.commit()
    connection.close()
