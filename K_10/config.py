# def main():
#     try:
#         configutation = open('config.txt')
#     except FileNotFoundError:
#         print("No se pudo encontrar el archivo config.txt")

# if __name__ == '__main__':
#     main()

from distutils.command.config import config
import errno


def main():
    # try:
    #     configuration = open("config.txt")
    # #except Exception: # La excepcion Exception captura todas las excepciones que puedan haber
    # # Se pueden agrupar excepciones cuando los errores sean del mismo tipo 
    # # Eg. except (BlockingIOError, TimeoutError):
    #     #print("Filesystem under heavy load, can't complete reading configuration file")
    # except FileNotFoundError:
    #     print("Couldn't find the config.txt file!")
    # except IsADirectoryError:
    #     print ("El archivo es un directorio, no puede abrirse")
    # # añadiendo as "err" se agrega el contenido del error (descripcion)
    # except PermissionError as err:    
    #     print ("No existen los permisos para acceder a este directorio", err)

    # Se pueden agrupar los errores de la misma categoria
    try:
        open('config.txt')
    except OSError as err:
        if err.errno == 13:
            print("No existen permisos para abrir este archivo")
        elif err.errno == 21:
            print("Este archivo es un directorio")

if __name__ == '__main__':
    main()
