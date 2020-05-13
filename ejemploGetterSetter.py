class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None  #No me muestra valor al ser None #Privado, no puedo involarlo desde fuera salgo si genero función
        
    def setPropiedadPrivada(self, valor): #genero una función para fijar (setter) el valor de propiedad privada, ya que al ser privado no lo puedo invocar directamente
        self.__propiedad_privada = valor
    
    def getPropiedadPrivada(self): #genero una función para determinar (getter) el valor de propiedad privada, ya que es privado no lo puedo hacer directamente
        return self.__propiedad_privada
    

  # regular el acceso a una parte privada  #Podrías no hacerlo privado, pero te da más control

    def propiedadPrivada(self, valor = None):
        if valor == None: #Si el valor no ha sido informado
            #Actúa como getter
            return self.__propiedad_privada
        else:
            #Actúa como setter
            self.__propiedad_privada = valor
 
    
    def __str__(self): #Genero una función cadena para que me devuelva un valor 
        return "ClaseConGetterySetter con propiedadPrivada -> {}".format(self.__propiedad_privada)
    

if __name__ == '__main__':
    c = ClaseConGetterySetter()
    
    
    
'''
EJEMPLO:
    
import turtle
    
#Creo una variable t para el módulo Turtle
    t = turtle.Turtle()
    
    t.shape()  #Me informa de la forma del elemento (GETTER)
    
    t.shape('turtle')  #Establece la forma del elemento  (SETTER)