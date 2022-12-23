import testes_fisicos

#peso_corporal = float(input("Peso corporal: "))

#experiencia (1/3)
#recebe os inputs
#tempo_ininterrupto_treinamento = int(input("Tempo inintterrupto de treinamento: "))
#experiencia_treinamento = int(input("Experiência de treinamento: "))
#tempo_destreinamento = int(input("Tempo de destreinamento: "))

print("Vamos descobrir seus níveis de mobilidade glenoumeral!")
tamanho_mao = float(input("Tamanho da mão: "))
glenoumeral_lado_direito = float(input("Mobilidade ombro direito: "))
glenoumeral_lado_esquerdo = float(input("Medida ombro esquerdo: "))

mobilidade_ombro_direito = testes_fisicos.mobilidade_ombro(glenoumeral_lado_direito, tamanho_mao)
mobilidade_ombro_esquerdo = testes_fisicos.mobilidade_ombro(glenoumeral_lado_esquerdo, tamanho_mao)
percentual_assimetria_ombro = testes_fisicos.calcula_assimetria(glenoumeral_lado_direito, glenoumeral_lado_esquerdo)
nivel_assimetria_ombro = testes_fisicos.classifica_assimetria(percentual_assimetria_ombro)
print("\n")
print("*** Mobilidade do quadril. ****")
quadril_lado_direito = float(input("Mobilidade quadril direito: "))
quadril_lado_esquerdo = float(input("Mobilidade quadril esquerdo: "))

mobilidade_quadril_direito = testes_fisicos.mobilidade_quadril(quadril_lado_direito)
mobilidade_quadril_esquerdo = testes_fisicos.mobilidade_quadril(quadril_lado_esquerdo)
percentual_assimetria_quadril = testes_fisicos.calcula_assimetria(quadril_lado_direito, quadril_lado_esquerdo)
nivel_assimetria_quadril = testes_fisicos.classifica_assimetria(percentual_assimetria_quadril)
print("\n")
print("***** Mobilidade do tornozelo. ****")
tornozelo_lado_direito = float(input("Mobilidade tornozelo direito: "))
tornozelo_lado_esquerdo = float(input("Mobilidade tornozelo esquerdo: "))

mobilidade_tornozelo_direito = testes_fisicos.mobilidade_tornozelo(tornozelo_lado_direito)
mobilidade_tornozelo_esquerdo = testes_fisicos.mobilidade_tornozelo(tornozelo_lado_esquerdo)
percentual_assimetria_tornozelo = testes_fisicos.calcula_assimetria(tornozelo_lado_direito, tornozelo_lado_esquerdo)
nivel_assimetria_tornozelo = testes_fisicos.classifica_assimetria(percentual_assimetria_tornozelo)
#nivel de força (2/3)
#recebe RM dos 4 exercícios
#rm_agachamento = float(input("RM no agachamento: "))
#rm_supino = float(input("RM no supino: "))
#rm_terra = float(input("RM no terra: "))
#rm_barra_fixa = float(input("RM na barra fixa: "))

#classifica niveis de força
#forca_relativa_agachamento = testes_fisicos.calcula_forca_relativa(rm_agachamento, peso_corporal)
#forca_relativa_supino = testes_fisicos.calcula_forca_relativa(rm_supino, peso_corporal)
#forca_relativa_terra = testes_fisicos.calcula_forca_relativa(rm_terra,peso_corporal)
#forca_relativa_barra = testes_fisicos.calcula_forca_relativa(rm_barra_fixa, peso_corporal)

#nivel de técnica (3/3) -> opci,onal (VAI ENTRAR NO FINAL)
#tecnica_agachamento = 2
#tecnica_supino = 2
#tecnica_terra = 4
#tecnica_barra = 1
#media_tecnica = (tecnica_agachamento + tecnica_supino + tecnica_terra + tecnica_barra) / 4
#print("Nível técnica: {}".format(media_tecnica)
print("\n\n")
#saida
print("******************************")
print("***** Relatório final ********")
print("******************************\n")
print("Mobilidade glenoumeral")
print("Direito: {} ({})  Esquerdo: {} ({})".format(glenoumeral_lado_direito, mobilidade_ombro_direito,glenoumeral_lado_esquerdo, mobilidade_ombro_esquerdo))
print("Percentual de assimetria: {:.2f} ({})".format(percentual_assimetria_ombro, nivel_assimetria_ombro))
print("\n")
print("Mobilidade quadril")
print("Direito: {} ({})  Esquerdo: {} ({})".format(quadril_lado_direito, mobilidade_quadril_direito, quadril_lado_esquerdo, mobilidade_quadril_esquerdo))
print("Percentual de assimetria: {:.2f} ({})".format(percentual_assimetria_quadril, nivel_assimetria_quadril))
print("\n")
print("Mobilidade tornozelo")
print("Direito: {} ({})  Esquerdo: {} ({})".format(tornozelo_lado_direito, mobilidade_tornozelo_direito, tornozelo_lado_esquerdo, mobilidade_tornozelo_esquerdo))
print("Percentual de assimetria: {:.2f} ({})".format(percentual_assimetria_tornozelo, nivel_assimetria_tornozelo))