from ClaseAlumno import Alumno
from ClaseMaterias import Materia
import datetime

UnAlumno=Alumno()
UnaMateria=Materia()

UnAlumno.AgregarNombre("Pepe")
UnAlumno.AgregarApellido("Sanchez")
UnAlumno.AgregarFechaNac(datetime.date(2000, 10, 20))
UnAlumno.AgregarTodasLasNotas(2)



UnaMateria.AgregarMateria("Matematica")
UnaMateria.AgregarNotasAMateria(3)
UnaMateria.AgregarNotasAMateria(2)
UnaMateria.AgregarNotasAMateria(2)


print ("Nombre: ", UnAlumno.Nombre)
print ("Apellido: ", UnAlumno.Apellido)
print ("Fecha de nacimiento: ", UnAlumno.Fecha_n)
print ("Notas: ", UnAlumno.Lista_Notas)
print ("Nota Mayor: ", UnAlumno.NotaMayor())
print ("Nota Menor: ", UnAlumno.NotaMenor())
print ("Promedio Notas: ", UnAlumno.PromedioNotas())
print (UnaMateria.Lista_Notas_Materia)