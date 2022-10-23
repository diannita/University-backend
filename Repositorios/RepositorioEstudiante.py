#importando de clase padre
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
#importando el modelo que necesitamos en este caso Estudiante
from Modelos.Estudiante import Estudiante

#clase hija
class RepositorioEstudiante(InterfaceRepositorio[Estudiante]): #objeto a tener en cuenta es el modelo estudiante y/o objetos de tipo estudiante
    #palabra reservada pass - sirve para mantener la clase vacia - no implementar nada
    pass