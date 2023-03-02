
# Convenção sobre constantes
# CONSTANTE_1 = 10
# CONSTANTE_2 = 20
#    <-- Contagem de complexidade (Muitos blocos dentro de blocos não é bom)

velocidade = 60 # Velocidade atual do carro
local_carro = 90 # Quilometro da estrada

RADAR_1 = 60 # Velocidade Máxima do radar
LOCAL_1 = 100 # Quilometro onde está o radar
RADAR_RANGE = 1 # Até que ponto o radar pega

if velocidade > RADAR_1:
    print('velocidade do carro acima do radar 1!')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <=(LOCAL_1 + RADAR_RANGE):
    print('')