import classes
from classes.personagens import Monstro, Player

## FASE DE TESTES

heroi = Player(1, 1, 'arqueiro')
vilao = Monstro(1, 1, 'morcego')

heroi.exibirAtributos()
vilao.exibirAtributos()