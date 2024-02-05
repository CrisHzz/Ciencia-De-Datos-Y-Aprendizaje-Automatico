from abc import ABC, abstractmethod

class ReglaAnalisis(ABC):  # Heredar de ABC

    def __init__(self, nombre: str):
        self.nombre = nombre

    def _separar_palabras(self, texto: str) -> list:
        if texto.strip() == "":
            return []  
        else:
            palabras = texto.split()  
            return palabras



    @abstractmethod    
    def analizar(self, texto: str):
        pass

    

