
from clase import Participante
from csv import writer
import os
import re
import datetime

Participante('','','','')
class Participante(Participante):
    pass

def muestra_datos():
    pass

# RUTA DONDE SE GUARDARA EL ARCHIVO
ruta=os.path.abspath(os.getcwd())

# NOMBRE DE ARCHIVO PARA TRABAJO.
archivo_a_trabajar = ruta+"\\Participantes.csv"

def carga_datos_csv():
    global clientes
    f = open(archivo_a_trabajar,"w+")
    # Escribo la primer línea del archivo, con los encabezados.
    f.write(f"CORREO|NOMBRE|FECHA DE NACIMIENTO|MOMENTO DE REGISTRO\n")
    for elemento in Participantes:
    f.write(f'{elemento.Correo}|{elemento.Nombre}|{elemento.FechaNacimiento}|{elemento.MomentoRegistro}\n')
    f.close()

def registroParticipantes():
    pass

def buscarParticipantes():
    pass

def modParticipantes():
    pass

def delParticipante():
    pass

def seeListaParticipantes():
    pass

def actualizarInfoCSV():
    pass

def serializacionJSON():
    pass





