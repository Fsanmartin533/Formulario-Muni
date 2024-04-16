#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def coneccionBD():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        port = 3306,
        passwd ="",
        database = "formulario"
    )

    if mydb:
        print ("Conexion exitosa")
    else:
        print ("Error en la conexion a BD")
    return mydb