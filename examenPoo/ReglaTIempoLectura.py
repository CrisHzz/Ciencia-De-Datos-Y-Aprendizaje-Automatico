from examenPoo import ReglaAnalisis
import math
class ReglaTiempoLectura(ReglaAnalisis):
    TIEMPO_LECTURA:int=238
    def __init__(self, nombre:str):
        super().__init__(nombre)

    def analizar(self, texto:str):
        words=self._separar_palabras(texto)
        words_Number=len(words)
        time_operation_words :float=words_Number/self.TIEMPO_LECTURA
        minutes,seconds=math.modf(time_operation_words )
        tupleData:tuple=(minutes,seconds)
        return tupleData
