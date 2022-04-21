from classes.personagens import *

## FASE DE TESTES

heroi = Player('guerreiro')
vilao = Monstro('zumbi')

heroi.exibirAtributos()
vilao.exibirAtributos()

luta = Combate(heroi, vilao)

luta.setVida()
luta.Luta()