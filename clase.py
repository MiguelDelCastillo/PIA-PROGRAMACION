# Se debe crear un programa llamado clases.py que solo contenga la definición 
# de una clase llamada Participante, que represente la información a registrar. 
# Las propiedades de la clase son
# 
# correo, nombre, nacimiento y momento. 
#
# La clase debe tener un constructor que incluya todos los datos;
# 
# es importante mencionar que la propiedad momento es opcional,
# 
# y que en caso de que no se proporcione al momento de la instanciación,
# el programa debe asignar la fecha y hora del sistema al momento de la instanciación.

#la fecha de nacimiento debe estar en un formato yyyy-mm-dd, y ser una fecha válida
import datetime

class Participante:
    # PROPIEDADES
    Correo=""
    Nombre=""
    FechaNacimiento= ""
    MomentoRegistro= ""
    #METODOS
    def __init__(self,Correo,Nombre,FechaNacimiento,MomentoRegistro):
        self.Correo=Correo
        self.Nombre=Nombre
        self.FechaNacimiento=FechaNacimiento
        self.MomentoRegistro=MomentoRegistro


