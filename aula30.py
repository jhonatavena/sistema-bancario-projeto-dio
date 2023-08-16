cep_carro = 129
kmh = 60

RADAR1 = 80
CEP_RADAR = 130
ZONA_ATUACAO = 1

if kmh > (RADAR1):
    print('Você esta acima da velocidade...')

if cep_carro >= (CEP_RADAR - ZONA_ATUACAO) and \
cep_carro <= (CEP_RADAR + ZONA_ATUACAO):
    print('Você passou no radar')