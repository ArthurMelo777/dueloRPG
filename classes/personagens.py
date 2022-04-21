import os

class Personagem:
    def __init__(self, classe, ataque, vida):
        self.nivel = 1
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.vidaAtual = 0

    def exibirAtributos(self):
        atributos = {"Nível": self.nivel, "Classe": self.classe, "Vida": self.vida, "Ataque": self.ataque, "Vida atual": self.vidaAtual}

        print(atributos)
        
class Player(Personagem):
    def __init__(self, classe):
        classe = classe.upper()
        if classe == 'GUERREIRO':
            vida = 50
            ataque = 5

        if classe == 'ARQUEIRO':
            vida = 25
            ataque = 20

        super().__init__(classe, ataque, vida)

class Monstro(Personagem):
    def __init__(self, classe):
        classe = classe.upper()
        if classe == 'VAMPIRO':
            vida = 500
            ataque = 50
            
        if classe == 'ZUMBI':
            vida = 100
            ataque = 10

        if classe == 'ESQUELETO':
            vida = 50
            ataque = 5

        if classe == 'MORCEGO':
            vida = 25
            ataque = 2

        super().__init__(classe, ataque, vida)

class Combate:
    def __init__(self, player, monstro):
        ## INSTANCIAR ATRIBUTOS
        self.player = player
        self.monstro = monstro

    def setVida(self):
        ## DEFINIR VIDA
        self.player.vidaAtual = self.player.vida
        self.monstro.vidaAtual = self.monstro.vida
    
    def Luta(self):
        ## CÁLCULOS DE LUTA
        os.system('cls')
        i = 0
        while self.monstro.vidaAtual > 0 and self.player.vidaAtual > 0:
            i += 1
            print(f"Round {i}")
            self.player.vidaAtual -= self.monstro.ataque
            self.monstro.vidaAtual -= self.player.ataque
            print(f"Vida atual: {self.player.vidaAtual}")
            print(f"Vida do monstro: {self.monstro.vidaAtual}")
            input("Clique em qqr tecla para passar para o  próximo round")
            os.system('cls')
        
        if self.monstro.vidaAtual > 0: print("Você perdeu!")
        else: print("Você venceu!")
