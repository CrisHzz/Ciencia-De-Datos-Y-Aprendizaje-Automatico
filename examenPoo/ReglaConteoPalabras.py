from examenPoo import ReglaAnalisis
class ReglaConteoPalabras(ReglaAnalisis):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def analizar(self, texto: str):
        words=self._separar_palabras(texto)
        count_words=len(words)
        return count_words
        
        pass  