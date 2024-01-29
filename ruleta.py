import random

class Ruleta:
    res_ruleta: str
    valores_ruleta: list ["Pierde turno", "Quiebra","X2", "1/2","Comodin","50", "150", "200"]

    def girar_ruleta(self,jugador: str)-> str:
        res_ruleta = random.choice(valores_ruleta)
        return res_ruleta
        
