from flask import Flask, jsonify, render_template, request
from confiDB import *
from validaciones import *

app = Flask(__name__)

@app.route('/formulario')
def inicio():
    return render_template('index.html')


@app.route('/from', methods = ['GET', 'POST'])
def registrarForm():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        nacimiento = request.form['nacimiento']
        genero = request.form['genero']
        correo = request.form['correo']
        confirmar_correo = request.form['confirmar_correo']
        residencia = request.form['residencia']
        telefono = request.form['telefono']

    #--------------------Validaciones------------------------
    
    if not validacionNombre(nombre):
        error_nombre = "El nombre no es valido. Debe contener solo letras y menos de 40 caracteres"
        return render_template('index.html', error_nombre = error_nombre)

    if not validacionApellido(apellido):
        error_apellido = "El apellido no es valido. Debe contener solo letras y menos de 40 caracteres"
        return render_template('index.html', error_apellido = error_apellido)
    
    if not validar_edad(edad):
        error_edad = "La edad no corresponde. Debe ser mayor de 18 años"
        return render_template('index.html', error_edad = error_edad)
    
    if not validar_nacimiento(nacimiento):
        error_nacimiento = "La fecha no es correcta"
        return render_template('index.html', error_nacimiento = error_nacimiento)

    if not validar_correo(correo, confirmar_correo):
        error_correo = "Los correos no coisiden"
        return render_template('index.html', error_correo = error_correo)
    
    if not validar_telefono(telefono):
        error_telefono = "No se permiten caracteres de tipo letras"
        return render_template('index.html', error_telefono = error_telefono)

    #--------------------------------------------------------

    conexion_MySQLdb = coneccionBD()
    cursor           = conexion_MySQLdb.cursor(dictionary=True)

    sql = "INSERT INTO datos_personales (nombre, apellido, edad, nacimiento, genero, correo, residencia, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (nombre, apellido, edad, nacimiento, genero, confirmar_correo, residencia, telefono)
    cursor.execute(sql, valores)

    conexion_MySQLdb.commit()

    cursor.close() #cerrando conecion SQL
    conexion_MySQLdb.close() # cerrando coneccion de la BD


    return render_template('index.html')




app.run(host = '0.0.0.0', port = 3000, debug = True)