
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
    return mobilidade

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
    elif(tempo < 40):
        score = "regular"
    elif (tempo < 60):
        score = "bom"
    elif (tempo < 80):
        score = "muito bom"
    else:
        score = "excelente"
    return score


