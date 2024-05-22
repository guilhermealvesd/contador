# Importando as bibliotecas

import os
import time

# Usuário informa um número

contador = int(input('Informe um número inteiro: '))

# Função responsável por limpar o terminal a cada valor

os.system('cls')

# Conta a partir do número informado até o 0

while contador >= 0:
    print(f'Contagem regressiva: {contador}...')
    time.sleep(1) # Para determinar o programa vai esperar até o próximo comando
    os.system('cls')
    contador -= 1

print('BOOOOM!!!')