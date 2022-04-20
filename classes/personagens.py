class Personagem:
    def __init__(self, id, nivel, classe, defesa, ataque, vida):
        self.id = id
        self.nivel = nivel
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.vidaAtual = 0

    def exibirAtributos(self):
        print(f"Nível = {self.nivel}; Classe = {self.classe}; Vida = {self.vida}; Ataque = {self.ataque}; Defesa = {self.defesa}; Vida atual = {self.vidaAtual}")

class Player(Personagem):
    def __init__(self, id, nivel, classe):
        classe = classe.upper()
        if classe == 'GUERREIRO':
            vida = 50
            ataque = 5
            defesa = 10

        if classe == 'ARQUEIRO':
            vida = 25
            ataque = 20
            defesa = 5

        super().__init__(id, nivel, classe, defesa, ataque, vida)

class Monstro(Personagem):
    def __init__(self, id, nivel, classe):
        classe = classe.upper()
        if classe == 'VAMPIRO':
            vida = 500
            ataque = 50
            defesa = 20
            
        if classe == 'ZUMBI':
            vida = 100
            ataque = 10
            defesa = 6

        if classe == 'ESQUELETO':
            vida = 50
            ataque = 5
            defesa = 3

        if classe == 'MORCEGO':
            vida = 25
            ataque = 2
            defesa = 1

        super().__init__(id, nivel, classe, defesa, ataque, vida)