import datetime


class Alumno(object):
    Nombre= None
    Apellido = None
    Fecha_n = None
    Lista_Notas = []
    Lista_Materias = []

    def AgregarNombre(self,nombre):
            self.Nombre = nombre

    def AgregarApellido(self, apellido):
            self.Apellido = apellido

    def AgregarFechaNac(self, fecha):
            self.Fecha_n = fecha

    def AgregarTodasLasNotas(self,nota):
         verifica=True
         if nota<1 or nota>10:
                print("nota invalida")
                verifica=False
         if verifica==True:
             self.Lista_Notas.append(nota)

    def NotaMayor(self):
        return max(self.Lista_Notas)

    def NotaMenor(self):
        return min(self.Lista_Notas)


    def PromedioNotas(self):
       ## for i in range (len(self.Lista_Notas)):
        ##    promedio=(self.Lista_Notas[i]+(self.Lista_Notas[i+1]))/len(self.Lista_Notas)
          ##  return (promedio)
        sum=0
        for i in range(0,len(self.Lista_Notas)):
               sum=sum+(self.Lista_Notas[i])

        return(sum/len(self.Lista_Notas))

