from Repositorios.RepositorioMateria import RepositorioMateria
from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Repositorios.RepositorioInscripcion import RepositorioInscripcion

from Modelos.Materia import Materia
from Modelos.Estudiante import Estudiante
from Modelos.Inscripcion import Inscripcion

class ControladorInscripcion():
    def __init__(self):
        print("Creando controlador Inscripcion")
        self.repositorioMateria = RepositorioMateria()
        self.repositorioEstudiante = RepositorioEstudiante()
        self.repositorioInscripcion = RepositorioInscripcion()

    def crear(self,infoInscripcion,id_estudiante,id_materia):
        nuevaInscripcion = Inscripcion(infoInscripcion)
        estudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        materia = Materia(self.repositorioMateria.findById(id_materia))
        nuevaInscripcion.estudiante = estudiante
        nuevaInscripcion.materia = materia
        return self.repositorioInscripcion.save(nuevaInscripcion)

    def mostrarInscripcion(self,id):
        inscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return inscripcion.__dict__

    def mostrarInscripciones(self):
        return self.repositorioInscripcion.findAll()

    def actualizar(self,id,infoInscripcion,id_estudiante,id_materia):
        inscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcion.año = infoInscripcion['año']
        inscripcion.semestre=infoInscripcion['semestre']
        inscripcion.nota_final = infoInscripcion['nota_final']
        estudiante1 = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        materia1 = Materia(self.repositorioMateria.findById(id_materia))
        inscripcion.estudiante = estudiante1
        inscripcion.materia = materia1
        return self.repositorioInscripcion.save(inscripcion)

    def eliminar(self,id):
        return self.repositorioInscripcion.delete(id)

    #Obtener todos los inscritos en una materia
    def listarInscritosMateria(self,id_materia):
        return self.repositorioInscripcion.getListadoInscritosEnMateria(id_materia)

    #Obtener nota mayor en materias
    def notaMasAltaporMateria(self):
        return self.repositorioInscripcion.getMayorNotaporCurso()

    #OBtener promedio de notas materia
    def promedioNotasMateria(self,id_materia):
        return self.repositorioInscripcion.promedioNotasEnMateria(id_materia)