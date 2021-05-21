import os
import csv
from posixpath import normcase
# Importo el módulo para trabajar con CSV

# Declarar la clase Contacto.
# Esta clase servirá para poblar una lista que me permite manejar
# en memoria los datos. La lista se vacía al CSV al final del programa
class  Contacto:
    def __init__(self,USUARIO, NOMBRE, CORREO):
            self.USUARIO = USUARIO
            self.NOMBRE = NOMBRE
            self.CORREO = CORREO

# Lista en la cual vamos a trabajar con los Contactos
Contactos = []
# Se cargan dos elementos.
# Contactos.append(Contacto('master','José Ruiz','jose.ruiz@hotmail.com'))
# Contactos.append(Contacto('student','Alma Pérez','almitarules@hotmail.com'))
# Contactos.append(Contacto('miguee','Miguel del Castillo','miguel@hotmail.com'))
# Contactos.append(Contacto('JFCC','Fernando','chaves@hotmail.com'))
# En el programa final, realmente la lista se carga a partir del CSV.

# Guardo en una variable la ruta absoluta, del directorio actual de trabajo (cwd)
ruta = os.path.abspath(os.getcwd())
archivo_trabajo=ruta+"\\contactos.csv"
archivo_respaldo=ruta+"\\contactos.bak"

# Determinar si el archivo de trabajo ya existe.
if os.path.exists(archivo_trabajo):
    # Si el archivo existe, entonces verifico si hay respaldo y lo borro.
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)

    # Establezco el achivo de datos, como respaldo
    os.rename(archivo_trabajo,archivo_respaldo)

# Genera el archivo CSV
f = open(archivo_trabajo,"w+")


with open('contactos.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    contador_lineas = 0
    # Creando una lista vacía.
    lista_incidentes = []
    # Lectura secuencial.
    
    print('Agregar datos')
    usuario = input('Miguee')
    nombre = input('Miguel')
    correo = input('m@correo.com')
    
    objeto_temporal = Contacto(usuario,nombre,correo)
    Contactos.append(objeto_temporal)
    
    
    for linea_datos in lector_csv:
        
        if contador_lineas == 0:
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

        # Se incrementa el número de líneas, pase lo que pase.
        contador_lineas += 1

    print(f'Procesadas {len(Contactos)} líneas.')
    
f.write("USUARIO|NOMBRE|CORREO\n")
# Escribimos en el CSV, a partir de la lista de objetos.
for elemento in Contactos:
    f.write(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')

# Cierro el archivo
f.close()