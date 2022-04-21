from classes.personagens import *

## FASE DE TESTES

heroi = Player('arqueiro')
vilao = Monstro('vampiro')

heroi.exibirAtributos()
vilao.exibirAtributos()

luta = Combate(heroi, vilao)

luta.setVida()
luta.Luta()