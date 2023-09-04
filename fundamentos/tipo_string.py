nome = 'Saulo Pedro'
print(nome)

# imprime 'S'
print(nome[0])

# não é possível fazer esse tipo de atribuição
# strings são imutáveis
# nome[0] = 'P'

# formas de 'escapar' caracteres
print("Dias D'Avila" == 'Dias D\'Avila')
"Teste \" funciona!"
texto = 'Texto entre apostrófos pode ter "aspas"'
print(texto)

doc = """Texto com múltiplas
    ... linhas"""
print(doc)
print('Texto com múltiplas\n\t... linhas')
print(doc)

doc2 = '''Também é possível
... com 3 aspas simples'''
print(doc2)

nome = 'Ana Paula'

# primeiro caractere
print(nome[0])  # imprime 'A'
print(nome[6])  # imprime 'u'

# último caractere
print(nome[-1])  # imprime 'a'
print(nome[-3])  # imprime 'u'

# imprimindo INTERVALOS
print(nome[4:])  # imprime 'Paula'
print(nome[-5:])  # imprime 'Paula'
print(nome[:3])  # imprime 'Ana'
print(nome[2:5])  # imprime 'a P'

numeros = '1234567890'
print(numeros)  # imprime '123456789'
print(numeros[::])  # imprime '123456789'

# imprime INTERVALOS com SALTOS
print(numeros[::2])  # imprime '13579'
print(numeros[1::2])  # imprime '24680'

# imprime REVERSO
print(numeros[::-1])  # imprime '987654321'
print(numeros[::-2])  # imprime '08642'

# imprime REVERSO
print(nome[::-1])  # imprime 'aluaP anA'

frase = 'Python é uma linguagem excelente'
print('py' not in frase) # imprime 'True'
print('ing' in frase) # imprime 'True'
print(len(frase)) # imprime '32'
print(frase.lower()) # imprime 'python é uma linguagem excelente'
print(frase) # imprime 'True'
frase = frase.upper() # alterando permanentemente o conteúdo da string 'frase'
print(frase) # imprime 'PYTHON É UMA LINGUAGEM EXCELENTE'

# split(): quebra a stringem substrings
# se nenhum argumento for passado, o separador de espaço em branco será utilizado
print(frase.split()) # imprime '['PYTHON', 'É', 'UMA', 'LINGUAGEM', 'EXCELENTE]'
# o separador, nesse caso, será o caractere 'E'
# IMPORTANTE: o separador NÃO será impresso
print(frase.split('E')) # imprime '['PYTHON É UMA LINGUAG', 'M, 'XC, 'L', 'NT', '']'

# Remove os espaços em branco no início e no final da linha.
# O trecho "linha.strip()" faz o seguinte:
# - Pega uma linha da lista 'linhas'.
# - Chama o método 'strip()' nessa linha.
linha = ' Sapatinho de luxo\n'
print(linha) # imprime ' Sapatinho de luxo\n' (COM espaço inicial em branco e o caractere '\n')
print(linha.strip()) # imprime 'Sapatinho de luxo' (SEM espaço inicial em branco e o caractere '\n')

# consultando todos os atributos do tipo STRING
print(dir(str))
# consultando especificamente um dos atributos do tipo STRING
# print(help(str.center))

# Magic Methods and Operator Overloading (sobrecarga de )
a = '123'
b = ' de Oliveira 4'
# As operações abaixo produzem o mesmo resultado
print(a + b) # imprime '123 de Oliveira 4'
print(a.__add__(b)) # imprime '123 de Oliveira 4'
print(str.__add__(a, b)) # imprime '123 de Oliveira 4'

# As operações abaixo produzem o mesmo resultado
print(len(a)) # imprime '3'
print(a.__len__()) # imprime '3'

# As operações abaixo produzem o mesmo resultado
print('1' in a) # imprime 'True'
print(a.__contains__('1')) # imprime 'True'
