import forca
import adivinhação

print("**********************")
print("** Escolha seu jogo **")
print("**********************")

print("(1) forca  (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if (jogo == 1):
    print("Jogando Forca!")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação!")
    adivinhação.jogar()
