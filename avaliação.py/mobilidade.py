print("Mobilidade de tornozelo\n")

tornozelo_direito = int(input("Lado direito em graus: "))
tornozelo_esquerdo = int(input("Lado esquerdo em graus: "))

dorsiflexao = 0
mobilidade = "a"

#if(dorsiflexao >= 45):
#    print("mobilidade = normal")

#else:
#    mobilidade = "reduzida"
#    print("mobilidade = reduzida")

#score = int(input("Tamanho da mão: "))

def teste_mobilidade (dorsiflexao):
        if (dorsiflexao >= 45):
            classificacao = "normal"
        else:
            classificacao = "reduzida"
        return classificacao

teste_mobilidade(dorsiflexao)