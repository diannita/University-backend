from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Departamento import Departamento

class ControladorDepartamento():
    #constructor
    def __init__(self):
        self.repositorioDepartamento = RepositorioDepartamento()

    #Crear un departamento
    def crear(self, infoDepartamento):
        nuevoDepartamento = Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(nuevoDepartamento)


    #mostrar un departamebto en particular
    def mostrarDepartamento(self, id):
        departamento = Departamento(self.repositorioDepartamento.findById(id))
        return departamento.__dict__

    #mostrar los departamentos
    def mostrarDepartamentos(self):
        return self.repositorioDepartamento.findAll()

    #update datos del departamento by id
    def actualizar(self, id, infoDepartamento):
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id))
        departamentoActual.nombre = infoDepartamento["nombre"]
        return self.repositorioDepartamento.update(id, departamentoActual)

    #delete, elimina el departamento
    def eliminar(self, id):
        return self.repositorioDepartamento.delete(id)
