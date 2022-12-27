
#def calcula_status_treinamento_forca (tempo_ininterrupto_treinamento, experiencia_treinamento, tempo_destreinamento, ):

def calcula_forca_relativa(rm, peso_corporal):
    forca_relativa = rm / peso_corporal
    return forca_relativa

def calcula_assimetria(lado_direito, lado_esquerdo):
    if (lado_esquerdo < lado_direito):
        percentual_assimetria = (((lado_direito - lado_esquerdo) / lado_esquerdo) * 100)
    else:
        percentual_assimetria = (((lado_esquerdo - lado_direito) / lado_direito) * 100)
    return percentual_assimetria

def classifica_assimetria (percentual_assimetria):
    if (percentual_assimetria > 10):
        assimetria = "acima do normal"
    else:
        assimetria = "normal"
    return assimetria

def mobilidade_ombro(distancia_entre_maos, tamanho_mao):
    referencia_ombro = tamanho_mao * 1.5
    if (distancia_entre_maos <= referencia_ombro):
        mobilidade = "normal"
    else:
        mobilidade = "reduzida"
    return mobilidade, referencia_ombro

def mobilidade_quadril(graus_flexão):
    referencia_quadril = 65
    if (graus_flexão > referencia_quadril):
        mobilidade = "normal"
    else:
        mobilidade = "reduzida"
    return mobilidade

def mobilidade_tornozelo(graus_dorsiflexao):
    referencia_tornozelo = 45
    if (graus_dorsiflexao >= referencia_tornozelo):
        mobilidade = "normal"
    else:
        mobilidade = "reduzida"
    return mobilidade

def resistencia_isometrica_core (tempo):
    if (tempo <= 20):
        score = "fraco"
    elif (tempo < 40):
        score = "regular"
    elif (tempo < 60):
        score = "bom"
    elif (tempo < 80):
        score = "muito bom"
    else:
        score = "excelente"
    return score

def classifica_status_forca(forca_relativa, lista_score):
    score_final = "nada"
    def converte_status_forca(score_parcial):
            score_final = "nada"
            if (score_parcial == 0):
                score_final = "Iniciante."
            elif (score_parcial == 1):
                score_final = "Antermediário."
            elif (score_parcial == 2):
                score_final = "Avançado."
            else:
                score_final = "Altamente avançado."
            return score_final

    index = 0
    score_parcial = 0
    for score in lista_score:
        print("Score: {} Força relativa: {}".format(score, forca_relativa))
        if (forca_relativa >= score):
            score_parcial = index
        index = index + 1
    return converte_status_forca(score_parcial)












#supino_homem = [0.6,1,1.2]
#barra_homem = [0.5, 1, 1.15, 1.3]
#agachamento_homem = [0.8, 1.2, 1.5]
#terra_homem = [1, 1.5, 1.8]

#supino_mulher = [0.4, 0.6, 0.8]
#barra_mulher = [0.5, 1, 1.1]
#agachamento_mulher = [0.6, 1, 1.3]
#terra_mulher = [0.8, 1.2, 1.6]










