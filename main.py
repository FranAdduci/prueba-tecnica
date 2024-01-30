from db import crear_tablas
from models.ubicacion import Ubicacion
from models.hotel import Hotel
from models.apartamento import Apartamento
from service.ubicacion_service import UbicacionService
from service.apartamento_service import ApartamentoService
from service.hotel_service import HotelService

crear_tablas()

def cargar_ubicacion():
    nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
    nombre_provincia = input("Ingrese la provincia: ")
    
    # Inserto ubicación por ID
    UbicacionService.insert_ubicacion(nombre_ciudad, nombre_provincia)
    print("¡Ubicación cargada exitosamente!")

def cargar_hotel():
    nombre_hotel = input("Ingrese el nombre del hotel: ")
    estrellas = int(input("Ingrese el número de estrellas del hotel: "))
    tipo_habitacion_estandar = input("Ingrese el tipo de habitación del hotel estandar: ")

    nombre_ciudad = input("Ingrese el nombre de la ciudad donde se encuentra el hotel: ")
    nombre_provincia = input("Ingrese la provincia donde se encuentra el hotel: ")
    
    # Obtengo el ID de la ubicación
    ubicacion_id = UbicacionService.obtener_ubicacion_por_ciudad_provincia(nombre_ciudad, nombre_provincia)
    
    
    # Inserto hotel utilizando el ID de ubicación
    if ubicacion_id:        
        hotel = Hotel(nombre_hotel, estrellas, tipo_habitacion_estandar, ubicacion_id)
        HotelService.insertar_hotel(hotel)
        print("¡Hotel cargado exitosamente!")
    else:
        print("No se encontró la ubicación. Por favor, primero carga la ubicación.")

def cargar_apartamento():
    nombre_apartamento = input("Ingrese el nombre del apartamento: ")
    cantidad_apartamentos = int(input("Ingrese la cantidad de apartamentos disponibles: "))
    capacidad_adultos = int(input("Ingrese la capacidad de adultos por apartamento: "))

    nombre_ciudad = input("Ingrese el nombre de la ciudad donde se encuentra el apartamento: ")
    nombre_provincia = input("Ingrese la provincia donde se encuentra el apartamento: ")
    
    # Obtengo el ID de ubicación para el apartamento
    ubicacion_id = UbicacionService.obtener_ubicacion_por_ciudad_provincia(nombre_ciudad, nombre_provincia)
    
    if ubicacion_id:
        # Inserto apartamento utilizando el ID de ubicación
        apartamento = Apartamento(nombre_apartamento, cantidad_apartamentos, capacidad_adultos, ubicacion_id)
        ApartamentoService.insertar_apartamento(apartamento)
        print("¡Apartamento cargado exitosamente!")
    else:
        print("No se encontró la ubicación. Por favor, primero carga la ubicación.")

def buscar_hospedajes_por_letras():
    primeras_letras = input("Ingrese las tres primeras letras para buscar hospedajes: ")
    hoteles = HotelService.buscar_hospedajes_por_letras_hotel(primeras_letras)
    apartamentos = ApartamentoService.buscar_hospedajes_por_letras_apart(primeras_letras)
    if hoteles:
        print("Hospedajes encontrados:")
        for hotel in hoteles:
            print(hotel)
    
    elif apartamentos:
        print("Hospedajes encontrados:")
        for apartamento in apartamentos:
            print(apartamento)       
        
    else:
        print("No se encontraron hospedajes para las letras ingresadas.")

#MENU

def menu():
    while True:
        print("\nMenú:")
        print("1. Cargar datos de ubicación")
        print("2. Cargar datos de hotel")
        print("3. Cargar datos de apartamento")
        print("4. Buscar hospedajes por las tres primeras letras")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_ubicacion()
        elif opcion == "2":
            cargar_hotel()
        elif opcion == "3":
            cargar_apartamento()
        elif opcion == "4":
            buscar_hospedajes_por_letras()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
