
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

def DatosRestantes():
    Nombre=input("Ingrese su nombre: ")
    FechaNacimiento=input("Ingrese su Fecha de Nacimiento: ")
    MomentoRegistro=datetime.datetime.now()

def ProporcionarDatos():
    global Correo
    Correo=input("Ingrese su correo electronico: ")
    Nombre=input("Ingrese su nombre: ")
    FechaNacimiento=input("Ingrese su Fecha de Nacimiento: ")
    MomentoRegistro=datetime.datetime.now()

ProporcionarDatos()

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
    global Ciclo
    Ciclo=False
    while (Ciclo==False):
        RegistrarCorreo=input("Ingrese su correo electronico")
        if RegistrarCorreo=="":
            Ciclo=True
        elif RegistrarCorreo == Correo:
            print("Ese correo ya está registrado")
            Ciclo=True
        else:
            DatosRestantes()

def buscarParticipantes():
    while (Ciclo==False):
        BuscarCorreo=input("Ingrese su correo electronico")
        if BuscarCorreo=="":
            Ciclo=True
        elif BuscarCorreo == Correo:
            print("Ese correo ya está registrado")
            Ciclo=True
            print

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





