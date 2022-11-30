nome = input("Digite seu nome: ")
print("Olá", nome)

#inputs
series_programadas = 3;
series_executadas = 1;
repeticoes = 0;
PSE = 0;

#variáveis calculadas p/
carga_media_semanal = 0;
carga = PSE * series_executadas;
desvio_padrao = 0;
strain = 0;
monotonia = 0;

peso = 0;
tonelagem = 0;
tonelagem = 0;

repeticoes_final = 0
tonelagem_final = 0

while (series_executadas <= series_programadas):

    print("\nSérie {} de {}.".format(series_executadas, series_programadas))
    peso = float(input("Peso: "))
    repeticoes = float(input("Repetições: "))
    tonelagem = peso * repeticoes

    repeticoes_final = repeticoes_final + repeticoes
    tonelagem_final = tonelagem_final + tonelagem

    print(" ** Resumo da série ** ")
    print("Repetições: ", repeticoes)
    print("Tonelagem da série: ", tonelagem)
    print("\n")
    print(" ** Resumo do treino ** ")
    print("Repetições final: ", repeticoes_final)
    print("Tonelagem final: ", tonelagem_final)

    series_executadas = series_executadas + 1;
#def controle_de_carga(float monotonia, ){
    #if (monotonia >= 2):
        #print("Necessidade de aumentar a variação na rotina de treinamento.")
    #else:
        #print("Estamos indo bem, não há necessidade de alterações na rotina de treinamento.")