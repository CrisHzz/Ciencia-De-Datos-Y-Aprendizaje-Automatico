from examenPoo import ReglaAnalisis
class ReglaPalabraMasUsada(ReglaAnalisis):
    def __init__(self, nombre:str):
        super().__init__(nombre)
    
    def analizar(self, texto:str):
        words=self._separar_palabras(texto)
        wordsdict={}
        for i in words:
            if i in wordsdict:
                wordsdict[i]+=1
            else:
                wordsdict[i]=1
        for palabra, cantidad in wordsdict.items():
         print(f"Palabra: {palabra}, Cantidad: {cantidad}")

        palabra_mas_usada = max(wordsdict, key=wordsdict.get)
        cantidad_palabra_mas_usada = wordsdict[palabra_mas_usada]
        return cantidad_palabra_mas_usada


        





        