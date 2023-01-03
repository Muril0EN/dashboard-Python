def jogar():
    print("**************************************")
    print("** Seja bem vindo ao jogo de forca! **")
    print("**************************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou): #game-loop
        #tratando entrada do usuário
        chute = (input("Qual letra? "))
        chute = chute.strip()#devolve a variável sem espaços

        index = 0 #posição
        for letra in palavra_secreta: #elemento in lista
            if(chute.upper() == letra.upper()):#trata para diferenças entre letras maiúsculas e minúsculas
                print("Econtrei a letra {} na posição {}".format(letra, index))
            index = index + 1 #incrementando
        print("Jogando...")

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()

