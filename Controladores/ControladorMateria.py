from Modelos.Materia import Materia
from Repositorios.RepositorioMateria import RepositorioMateria

class ControladorMateria():
    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        print("creando controlador Materia")

    # metodo crear
    def create(self, MateriaDatos):
        print("crear una Materia")
        crearMateria = Materia(MateriaDatos)
        return self.repositorioMateria.save(crearMateria)
        # informacion quemada de prueba
        # return crearMateria.__dict__

    # metodo mostrar (unico - 1 materia)
    def mostrarMateria(self, id):
        print("mostrando una Materia con id: "+str(id))
        materiaRegistrada = Materia(self.repositorioMateria.findById(id))
        return materiaRegistrada.__dict__
        # informacion quemada de prueba
        # laMateria = {
        #     "_id": id,
        #     "nombre":"Introduccion a la Ingenieria",
        #     "creditos":"4"
        # }
        # return laMateria

    # metodo mostrar todos las materias
    def mostrarMaterias(self):
        print("listar todos los estudiantes")
        return self.repositorioMateria.findAll()
        # informacion quemada de prueba
        # Materias = {
        #     "_id":"xyz445",
        #     "nombre": "Redes Computacionales",
        #     "creditos":"3"
        # }
        # return [Materias]

    # metodo eliminar
    def delete(self, id):
        print("se elimino la Materia con id "+ str(id))
        return self.repositorioMateria.delete(id)
        # informacion quemada de prueba
        # return{"delete_subject_count":1}

    # metodo actualizar
    def update(self, id, MateriaDatos):
        print("se actualizo la Materia con id " + str(id))
        ActualizarMateria = Materia(self.repositorioMateria.findById(id))
        ActualizarMateria.nombre = MateriaDatos["nombre"]
        ActualizarMateria.creditos = MateriaDatos["creditos"]
        return self.repositorioMateria.update(id, ActualizarMateria)
        # informacion quemada de prueba
        # actualizarMateria = Materia(MateriaDatos)
        # return actualizarMateria.__dict__