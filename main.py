from flask import Flask #utiliza el framework de flask
from flask import jsonify #nos permite trabajar con json un conversor de flask a json
from flask import request #recibir solicitudes y procesarlas
from flask_cors import CORS #es para de definir los origenes permitidos para los microservicios
import json #importando la libreria de json
from waitress import serve #desplegar y ejecutar los servicios en el localhost

#######################se comenta ya que se movio a interfaceRepositorios y config.json################
#################este es un ejemplo de conexion de base de satos antes de implementar interfaceRepositorios#######
# import pymongo #libreria para base de datos
# import certifi #libreria para certicar los certificados digitales
#
# #creando la conexion de la DB
# ca = certifi.where()
# client = pymongo.MongoClient("mongodb+srv://monkey:Monkey123@cluster0.2xsc4e1.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = ca)
# db = client.test
#
# print(db) #imprimiendo database conexion
# baseDatos = client['bd-registro-academico'] #mostrando colleccion
# print(baseDatos.list_collection_names()) #mostrando listado de colecciones
#######################se comenta ya que se movio a interfaceRepositorios y config.json################


#importando los controladores
from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorMateria import  ControladorMateria
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorInscripcion import ControladorInscripcion


app = Flask(__name__) #creacion instancia del servidor
cors = CORS(app)       #configuracion del cors
miControladorEstudiante = ControladorEstudiante()
miControladorMateria = ControladorMateria()
miControladorDepartamento = ControladorDepartamento()
miControladorInscripcion= ControladorInscripcion()


#creacion de variable para mostrar rutas----------------------------------------------
#Rutas estudiantes
@app.route("/estudiantes",methods =['POST'])
def crearEstudiante():
    data = request.get_json() #enviando informacion
    dictUsuario = miControladorEstudiante.create(data)
    return jsonify(dictUsuario) #convertir un dict a json

@app.route("/estudiantes/<string:id>",methods =['GET'])
def getEstudiante(id):
    dictEstudiante = miControladorEstudiante.mostrarEstudiante(id)
    return jsonify(dictEstudiante)

@app.route("/estudiantes",methods =['GET'])
def getEstudiantes():
    dictEstudiantes = miControladorEstudiante.mostrarEstudiantes()
    return jsonify(dictEstudiantes)

@app.route("/estudiantes/<string:id>",methods =['PUT'])
def putEstudiante(id):
    data = request.get_json() #obtener informacion que envian desde el body
    dictEstudiante = miControladorEstudiante.update(id,data)
    return jsonify(dictEstudiante)

@app.route("/estudiantes/<string:id>",methods =['DELETE'])
def deleteEstudiante(id):
    dictEstudiante = miControladorEstudiante.delete(id)
    return jsonify(dictEstudiante)
#end rutas estudiantes----------------------------------------------


#creacion de variable para mostrar rutas----------------------------------------------
#Rutas Materias
@app.route("/materias",methods =['POST'])
def crearMateria():
    data = request.get_json() #enviando informacion
    dictMateria = miControladorMateria.create(data)
    return jsonify(dictMateria) #convertir un dict a json

@app.route("/materias/<string:id>",methods =['GET'])
def getMateria(id):
    dictMateria = miControladorMateria.mostrarMateria(id)
    return jsonify(dictMateria)

@app.route("/materias",methods =['GET'])
def getMaterias():
    dictMaterias = miControladorMateria.mostrarMaterias()
    return jsonify(dictMaterias)

@app.route("/materias/<string:id>",methods =['PUT'])
def putMateria(id):
    data = request.get_json() #obtener informacion que envian desde el body
    dictMateria = miControladorMateria.update(id,data)
    return jsonify(dictMateria)

@app.route("/materias/<string:id>",methods =['DELETE'])
def deleteMateria(id):
    dictMateria = miControladorMateria.delete(id)
    return jsonify(dictMateria)
#end Rutas Materias----------------------------------------------


#creacion de variable para mostrar rutas----------------------------------------------
#Rutas Departamento
@app.route("/departamentos",methods=['POST'])
def CrearDepartamento():
    datos = request.get_json()
    respuesta = miControladorDepartamento.crear(datos)
    return jsonify(respuesta)

@app.route("/departamentos",methods=['GET'])
def ObtenerDepartamentos():
    respuesta = miControladorDepartamento.mostrarDepartamentos()
    return jsonify(respuesta)

@app.route("/departamentos/<string:id>", methods=['GET'])
def ObtenerDepartamento(id):
    respuesta = miControladorDepartamento.mostrarDepartamento(id)
    return jsonify(respuesta)

@app.route("/departamentos/<string:id>", methods=['PUT'])
def ActualizarDepartamento(id):
    datos = request.get_json()
    respuesta = miControladorDepartamento.actualizar(id,datos)
    return jsonify(respuesta)

@app.route("/departamentos/<string:id>", methods = ['DELETE'])
def EliminarDepartamento(id):
    respuesta = miControladorDepartamento.eliminar(id)
    return jsonify(respuesta)

#Ruta de departamento con materia
@app.route("/materias/<string:id>/departamentos/<string:id_departamento>",methods=['PUT'])
def AsignarDepartamento(id, id_departamento):
    respuesta = miControladorMateria.asignarDepartamento(id,id_departamento)
    return jsonify(respuesta)
#end Rutas Departamento----------------------------------------------


#creacion de variable para mostrar rutas----------------------------------------------
#Rutas Inscripcion (Se realiza la creacion y manipulacion de los datos de Inscripcion)
#Ruta de inscripcion estudiante y materia
@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante,id_materia):
    data = request.get_json()
    respuesta = miControladorInscripcion.crear(data,id_estudiante,id_materia)
    return jsonify(respuesta)

@app.route("/inscripciones",methods=['GET'])
def mostrarInscripciones():
    respuesta = miControladorInscripcion.mostrarInscripciones()
    return jsonify(respuesta)

@app.route("/inscripciones/<string:id>",methods = ['GET'])
def mostrarInscripcion(id):
    respuesta = miControladorInscripcion.mostrarInscripcion(id)
    return jsonify(respuesta)

@app.route("/inscripciones/<string:id>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods = ['PUT'])
def ActualizarInscripcion(id,id_estudiante,id_materia):
    data = request.get_json()
    respuesta = miControladorInscripcion.actualizar(id,data,id_estudiante,id_materia)
    return jsonify(respuesta)

@app.route("/inscripciones/<string:id>",methods =['DELETE'])
def EliminarInscripcion(id):
    respuesta = miControladorInscripcion.eliminar(id)
    return jsonify(respuesta)

@app.route("/inscripciones/materia/<string:id_materia>", methods =['GET'])
def inscritosMateria(id_materia):
    respuesta = miControladorInscripcion.listarInscritosMateria(id_materia)
    return jsonify(respuesta)

@app.route("/inscripciones/notas_mayores", methods =['GET'])
def notasMayores():
    respuesta = miControladorInscripcion.notaMasAltaporMateria()
    return jsonify(respuesta)

@app.route("/inscripciones/promedio/materia/<string:id_materia>", methods = ['GET'])
def promedioMateria(id_materia):
    respuesta = miControladorInscripcion.promedioNotasMateria(id_materia)
    return jsonify(respuesta)

#End Inscripcion----------------------------------------------



#las siguientes lineas se define la ruta y el microservicio donde se va a desplegar
@app.route("/",methods =['GET']) #creacion de rutas
def test():
    json={}
    json["mensaje"]="Servidor ejecutandose" #Para hacer un test y mostrar en el navegador
    return jsonify(json) #toma diccionarios a convertir en este caso json
    #luego se ejecuta la siguiente url en el navegador para ver el mensaje anterior http://127.0.0.1:9999/


#leer archivo config.json - cargando las configuraciones
def loadFileConfg():
    with open('config.json') as f:
        data = json.load(f)
    return data
if __name__=='__main__':
    dataConfig = loadFileConfg()
    print("Servidor corriendo en: " + "host: " + dataConfig["url-backend"] + " puerto: " + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
