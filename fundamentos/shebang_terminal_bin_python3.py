#!/usr/bin/python3
# shebang: chamada do interpretador indicado pelo PATH
from math import pi
import sys
import errno

# Criando classe para definir cores para o console/terminal
class TerminalColor:
    # Definindo cores para as mensagens no console/terminal
    ERRO = '\033[91m' # código para a cor VERMELHA
    NORMAL = '\033[0m' # código para a cor "default"


def area_circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("É necessário informar o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][:]))


# Verificando o nome do módulo
if __name__ == '__main__':

    # validando a existência dos argumentos
    if len(sys.argv) < 2:
        help()
        # informa ao SO o status da execução:
        # 0 - execução bem sucedida
        # =! 0 - erro na execução
        # nada após esse exit() será executado
        sys.exit(errno.EPERM) # retorna '1' para o SO

    # argumento é numérico?
    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO + 'O raio deve ser um valor numérico' + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)
    
    # primeiro argumento passado pela linha de comando do Terminal: nome do Script
    print('Nome do Script: ' + sys.argv[0])
    # segundo argumento passado pela linha de comando do Terminal
    print('Argumento argv[1]: ' + sys.argv[1])

    # utilizando o segundo argumento passado pela linha de comando do Terminal
    raio = sys.argv[1]
    area = area_circulo(raio)
    print('Área do círculo', area)
