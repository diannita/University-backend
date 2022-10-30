from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Inscripcion import Inscripcion
from bson import ObjectId

class RepositorioInscripcion(InterfaceRepositorio[Inscripcion]):
    #Esta funcion nos muestra el listado de los estudiantes que realizaron la materia
    def getListadoInscritosEnMateria(self, id_materia):
        theQuery = {"materia.$id": ObjectId(id_materia)}
        return self.query(theQuery)


    #Esta funcion nos muestra quien obtuvo la mayor nota en la materia
    #Group - esta operacion de agregacion agrupara las materias por id para buscar cada una en las materias
    #mayor nota por curso
    def getMayorNotaporCurso(self):
        query = {
            "$group": {
                "_id": "$materia",
                "max": {
                    "$max": "$nota_final"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)


    #buscar el promedio de la materias de todos los estudiantes
    def promedioNotasEnMateria(self, id_materia):
        query1 ={
            "$match":{"materia.$id": ObjectId(id_materia)}
        }
        query2 ={
            "$group":{
                "_id":"$materia",
                "promedio": {
                    "$avg": "$nota_final"
                }
            }
        }
        pipeline=[query1, query2]
        return self.queryAggregation(pipeline)

