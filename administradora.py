from particula import Particula
import json

class Administradora:
    def __init__(self):
        self.__particulas = []
        
    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula)
        
    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)
        
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
            
    def __str__(self):
        return "".join(
            str(particula) for particula in self.__particulas
            ) 

    def __len__(self):
        return (len(self.__particulas))
    
    
    def __iter__(self):
        self.cont = 0
        
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def guardar(self,ubiacion):
        try:
            with open(ubiacion,'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista,archivo, indent = 5)
            return
        except:
            return 0
             #json.dump()

    def abrir(self,ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula)for particula in lista]
            return 1
        except:
            return 0
        
