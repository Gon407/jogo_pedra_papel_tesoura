# Jogo da pedra, papel e tesoura
#
# Coder: Gonçalo Morais        V:0.0

# 01 - instancias da variaveis

import random

jogador = input ("escolhe uma opção ")
pc = random.choice (("tesoura", "papel", "pedra"))

# 02 - logica

if jogador == "papel" and pc == "papel":
    resultado = "jogador empatou"


if jogador == "tesoura" and pc == "papel":
    resultado = "jogador ganhou"


if jogador == "pedra" and pc == "papel":
    resultado = "jogador perdeu"


if jogador == "papel" and pc == "tesoura":
    resultado = "jogador perdeu"


if jogador == "tesoura" and pc == "tesoura":
    resultado = "jogador empatou"


if jogador == "pedra" and pc == "tesoura":
    resultado = "jogador ganhou"


if jogador == "papel" and pc == "pedra":
    resultado = "jogador ganhou"


if jogador == "tesoura" and pc == "pedra":
    resultado = "jogador perdeu"


if jogador == "pedra" and pc == "pedra":
    resultado = "jogador empatou"



#03 = resultado
print(resultado)
print("jogador: ", jogador, "pc: ", pc)
