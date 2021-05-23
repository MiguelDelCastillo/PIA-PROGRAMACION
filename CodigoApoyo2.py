import os
import csv

class  Contacto:
    def __init__(self,USUARIO, NOMBRE, CORREO):
            self.USUARIO = USUARIO
            self.NOMBRE = NOMBRE
            self.CORREO = CORREO


# Guardo en una variable la ruta absoluta, del directorio actual de trabajo (cwd)
ruta = os.path.abspath(os.getcwd())
archivo_trabajo=ruta+"\\contactos2.csv"
archivo_respaldo=ruta+"\\contactos2.bak"

# if os.path.exists(archivo_trabajo):
#     Si el archivo existe, entonces verifico si hay respaldo y lo borro.
#     if os.path.exists(archivo_respaldo):
#         os.remove(archivo_respaldo)

#     Establezco el achivo de datos, como respaldo
#     os.rename(archivo_trabajo,archivo_respaldo)

# Genera el archivo CSV
if os.path.exists(archivo_trabajo):
    pass
else:
    f = open(archivo_trabajo,"w")
# f.write("USUARIO|NOMBRE|CORREO\n")
# for elemento in Contactos:
#     f.write(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')

# Cierro el archivo


Contactos = []

while True:
    pregunta = input('Desea registrar un dato?')
    if pregunta.upper() =='SI':
        usuario = input('Ingrese un usuario')
        nombre = input('Ingrese su nombre')
        correo = input('Ingrese su correo')
        objeto = Contacto(usuario,nombre,correo)
        Contactos.append(objeto)
        with open('contactos2.csv') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter='|')
            a = 0
            # Creando una lista vacía.
            # Lectura secuencial.
            for linea_datos in lector_csv:
                if int(a) == 0:
                    # Si es la primer línea, muestro los nombres de campo y no guardo nada
                    # en la lista.
                    print(f'Los nombres de columna son {", ".join(linea_datos)}')
                else:
                # Si son datos (línea uno y posteriores)...
                # Genero una instancia de la clase Incidente, y le proporciono al constructor
                # los valores leidos del archivo.
                # RETO: Aquí se convierte el primer valor a su equivalente datetime
                    objeto_temporal = Contacto({linea_datos[0]},{linea_datos[1]},{linea_datos[2]})
                    Contactos.append(objeto_temporal)
                    # Escribimos en el CSV, a partir de la lista de objetos.
                    for elemento in Contactos:
                        Contactos.append(objeto_temporal)
                        f.write(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')
                        print(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')
        
        with open('contactos2.csv') as file:
            file = open(archivo_trabajo,'w')
            file.write("USUARIO|NOMBRE|CORREO\n")
            for elemento in Contactos:
                file.write(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')

                # # Cierro el archivo
            file.close()        
                    
        for elemento in Contactos:
            print(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')
            
    else:
        break
        



