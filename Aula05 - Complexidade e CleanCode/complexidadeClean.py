
# Convenção sobre constantes
# CONSTANTE_1 = 10
# CONSTANTE_2 = 20
#    <-- Contagem de complexidade (Muitos blocos dentro de blocos não é bom)

velocidade = 60 # Velocidade atual do carro
local_carro = 90 # Quilometro da estrada

RADAR_1 = 60 # Velocidade Máxima do radar
LOCAL_1 = 100 # Quilometro onde está o radar
RADAR_RANGE = 1 # Até que ponto o radar pega

# Forma Errada
if local_carro >= (LOCAL_1 - RADAR_RANGE)\
    and local_carro <=(LOCAL_1 + RADAR_RANGE)\
    and velocidade > RADAR_1:
    print('Carro foi multado no radar 1')

# Forma Clean
velocidade_passou_do_limite = velocidade > RADAR_1
carro_ponto_antes_do_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_ponto_depois_do_radar1 = local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_sera_multado_no_radar1 = velocidade_passou_do_limite and carro_ponto_antes_do_radar1 and carro_ponto_depois_do_radar1

if carro_sera_multado_no_radar1:
    print('Carro foi multado no radar 1!')