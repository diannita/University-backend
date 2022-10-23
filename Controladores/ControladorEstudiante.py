#los controladores se encargan de manipular los modelos donde se puede realizar el CRUD

from Modelos.Estudiante import Estudiante
from Repositorios.RepositorioEstudiante import RepositorioEstudiante

class ControladorEstudiante():
    #creacion de metodos
    #metodo init
    def __init__(self):
        self.repositorioEstudiante = RepositorioEstudiante()
        print("creando controlador Estudiante") #print informativo

    #metodos de la operacion del CRUD
    #metodo crear
    def create(self, estudianteDatos):
        print("crear un estudiante")
        #creando una variable donde se recibe la informacion
        crearEstudiante = Estudiante(estudianteDatos)
        return self.repositorioEstudiante.save(crearEstudiante)
        # ya no vamos a usar las lineas siguientes lineas ya que ahora vamos a usar los respositorios se comenta para informacion (previours code -codigo de test quemado)
            #se retorna la informacion y se convierte a diccionario
            # return crearEstudiante.__dict__
            #llamando el repositorio y el metodo repositorio estudiante para retornar la data
        # ya no vamos a usar las lineas anteriores ya que ahora vamos a usar los respositorios se comenta para informacion (previours code -codigo de test quemado)


    #metodo mostrar (unico - 1 estudiante)
    def mostrarEstudiante(self, id):
        print("mostrando el estudiante con id: "+str(id)) # dejamos este mensaje como informativo
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__
        #informacion quemada de prueba
        # elEstudiante = {
        #     "_id": id,
        #     "cedula":"1234",
        #     "nombre":"Juan",
        #     "apellido":"Caicedo"
        # }
        # return elEstudiante

    #metodo mostrar todos los estudiantes
    def mostrarEstudiantes(self):
        print("listar todos los estudiantes")
        return self.repositorioEstudiante.findAll()
        # informacion quemada de prueba
        # estudiantes = {
        #     "_id":"abc123",
        #     "cedula": "1234",
        #     "nombre": "Juan",
        #     "apellido": "Caicedo"
        # }
        # return [estudiantes]

    #metodo eliminar
    def delete(self, id):
        print("se elimino el estudiante con id "+ str(id))
        return self.repositorioEstudiante.delete(id)
        # informacion quemada de prueba
        #se retorna un json donde muestra los elementos que se elimino
        # return{"delete_count":1}

    #metodo actualizar
    def update(self, id, estudianteDatos):
        print("se actualizo el estudiante con id "+ str(id))
        estudiante = Estudiante(self.repositorioEstudiante.findById(id))
        estudiante.nombre = estudianteDatos["nombre"]
        estudiante.apellido = estudianteDatos["apellido"]
        estudiante.cedula = estudianteDatos["cedula"]
        return self.repositorioEstudiante.update(id, estudiante)
        # informacion quemada de prueba
        # actualizarEstudiante = Estudiante(estudianteDatos)
        # #retorna conviertiendo el objeto o informacion en diccionario
        # return actualizarEstudiante.__dict__
