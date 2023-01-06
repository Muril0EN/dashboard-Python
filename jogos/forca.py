def jogar():
    print("**************************************")
    print("** Seja bem vindo ao jogo de forca! **")
    print("**************************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    #listas (mutável) -> nome = [elemento]
    #truplas(imutável) -> nome = (elemento)
    #lista de truplas
    #trupla1 = (2,3)
    #truplap2 = (3,4)
    #trupla3 = (5,6)
    #linha = [trupla1, trupla2, trupla3]
    #transformar lista em trupla -> nome_variável = tuple.(lista)
    #trnasformar trupla em lista -> nome_variavel = list(tuple)
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou): #game-loop
        #tratando entrada do usuário
        chute = (input("Qual letra? "))
        chute = chute.strip().upper()#devolve a variável sem espaço / letras maiúsculas

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta: #elemento in lista
                if(chute == letra):#trata para diferenças entre letras maiúsculas e minúsculas
                    # print("Econtrei a letra {} na posição {}".format(letra, index))
                    letras_acertadas[index] = letra
                index += 1 #incrementando
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas #não acertou a palavra enquanto houver esse elmento dentro da lista de letras acertadas
        print(letras_acertadas)
    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()