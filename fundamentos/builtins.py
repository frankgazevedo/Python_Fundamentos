# O script abaixo deve ser executado no terminal

import math
type(1)
__builtins__.type('Fala Galera!')
__builtins__.print(10 / 3)

# equivale à chamada help(dir)
# o comando help() exibirá as informações sobre o argumento passado
# __builtins__.help(__builtins__.dir)

# dir() returns the list of valid attributes of the passed object
# Se nenhum argumento for passado, o ESCOPO GLOBAL será exibido
dir()

a = 7
# Em razão da declaração de variável e do import, o objeto do ESCOPO GLOBAL armazenará
# exibirá a variável 'a' e o módulo importado 'math'
dir()

# exibirá todo o módulo builtins
dir(__builtins__)

nome = 'João da Silva'
type(nome)
# equivale à chamada len(nome)
__builtins__.len(nome)

# 'nome' Se nenhum argumento for passado, o ESCOPO GLOBAL será exibido
dir()
