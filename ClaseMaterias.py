from ClaseAlumno import Alumno
class Materia(object):
    Nombre_Materia=None
    Lista_Notas_Materia=None


    def AgregarMateria(self,nombre):
        self.Nombre_Materia=nombre

    def AgregarNotasAMateria(self,notaMateria):
        verifica=True
        if notaMateria<1 or notaMateria>10:
                print("nota invalida")
                verifica=False
        if verifica==True:
            self.Lista_Notas_Materia.append(notaMateria)

    def PromedioNotasPorMateria(self):
        materia=None

        for item in Lista_Materias:
            if item == materia:
                print (Lista_Notas_Materia)
