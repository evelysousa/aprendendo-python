import jogo_forca
import jogo_chute_numero

print("*******Escolha o seu jogo!*******")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
    jogo_forca.jogar()
elif (jogo == 2):
    jogo_chute_numero.jogar()
    print("Jogando adivinhação")