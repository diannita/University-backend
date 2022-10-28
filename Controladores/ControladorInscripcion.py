from Repositorios.RepositorioInscripcion import RepositorioInscripcion
from Repositorios.RepositorioMateria import RepositorioMateria
from Repositorios.RepositorioEstudiante import RepositorioEstudiante

from Modelos.Materia import Materia
from Modelos.Estudiante import Estudiante
from Modelos.Inscripcion import Inscripcion


class ControladorInscripcion():
    def __init__(self):
        #objeto de los repositorios
        self.repositorioInscripcion = RepositorioInscripcion()
        self.repositorioEstudiante = RepositorioEstudiante()
        self.repositorioMateria = RepositorioMateria()
        print("Creando Controlado de Inscripcion")

    def create(self, infoInscripcion,id_estudiante,id_materia):
        print("crear Inscripcion")
        crearInscripcion = Inscripcion(infoInscripcion)
        estudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        materia = Materia(self.repositorioMateria.findById(id_materia))
        crearInscripcion.estudiante = estudiante
        crearInscripcion.materia = materia
        return self.repositorioInscripcion.save(crearInscripcion)


    def mostrarInscripcion(self, id):
        print("Mostrando la Inscripcion con ID:"+str(id))
        elInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return elInscripcion.__dict__

    def mostrarInscripcions(self):
        print("Listar todos los Inscripciones")
        return self.repositorioInscripcion.findAll()

    def delete(self, id):
        print("Se elimino la Inscripcion con el id: "+str(id))
        return self.repositorioInscripcion.delete(id)

    def update(self,id,InscripcionDatos,id_estudiante,id_materia):
        print("Se Actualizo el Inscripcion con id: "+str(id))
        inscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcion.year= InscripcionDatos["year"]
        inscripcion.semestre = InscripcionDatos["semestre"]
        inscripcion.nota_final = InscripcionDatos["nota_final"]
        estudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        materia = Materia(self.repositorioMateria.findById(id_materia))
        inscripcion.estudiante = estudiante
        inscripcion.materia = materia
        return self.repositorioInscripcion.save(inscripcion)

    #obtener todos los inscritos en una materia
    def listarInscritos(self,id_materia):
        return self.repositorioInscripcion.getListadoInscritosEnMateria(id_materia)

    #obtener la mayor nota en materias
    def notaMasAltaPorMateria(self):
        return self.repositorioInscripcion.getMayorNotaporCurso()

    #obtener promedio de notas materias
    def promedioMaterias(self, id_materia):
        return self.repositorioInscripcion.promedioNotasEnMateria(id_materia)