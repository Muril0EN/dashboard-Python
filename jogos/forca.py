def jogar():
    print("**************************************")
    print("** Seja bem vindo ao jogo de forca! **")
    print("**************************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = (input("Qual letra? "))

        index = 0 #posição
        for letra in palavra_secreta: #elemento in lista
            if(chute == letra):
                print("Econtrei a letra {} na posição {}".format(letra, index))
            index = index + 1 #incrementando
        print("Jogando...")

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()

