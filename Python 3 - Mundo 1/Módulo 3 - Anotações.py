"""
AULA 6 - TIPOS PRIMITIVOS E SAÍDAS DE DADOS

int - número inteiro, positivo ou negativo
float - número decimal, positivo ou negativo
bool - binário, true ou false
str - texto, entre aspas simples ou duplas



SINTAXES E FORMATAÇÃO

QUEBRA DE LINHA: \n

print('Primeiro print', end = '')
print('Segundo print')

# resultado: Primeiro print Segundo Print


NÃO QUEBRAR A LINHA: , end = ''

print('Primeiro print', end = '')
print('Segundo print')

# resultado: Primeiro print Segundo Print

.FORMAT() - Serve para colocar as variáveis após o texto, dentro das chaves. 
A ordem de inserção será determinada pela ordem das variáveis escritas dentro 
da função format.

print('A soma vale {}'.format(s))



Ex.: 

nome = Lucas
idade = 19
sexo = masculino

print('Meu nome é {}, tenho {} anos de idade e sou do sexo {}'.format(nome, 
idade, sexo))

# output: Meu nome é Lucas, tenho 19 anos de idade e sou do sexo masculino



TIPO PRIMITIVO

------ INT ------

n1 = int(input('Digite um valor: '))  
# input: 10

n2 = int(input('Digite um valor: '))  
# input: 15

s1 = n1 + n2

print('A soma entre {} e {} vale {}.'.format(n1, n2, s1))  
# output: A soma entre 10 e 15 vale 25

Observação:

n1 = int(input('Digite um valor: '))  # input: 10.0  # erro

ValueError: invalid literal for int() with base 10: '10.5'



------ FLOAT ------

n1 = float(input('Digite um valor: '))
# input: 10 - n1 vai se tornar um float, 10.0

n2 = float(input('Digite um valor: '))
# input: 15 - n2 vai se tornar um float, 15.0

s1 = n1 + n2

print('A soma entre {} e {} vale {}.'.format(n1, n2, s1))  
# output: A soma entre 10.0 e 15.0 vale 25.0



------ BOOL ------

n = bool(input('Digite um valor: '))  # input: qualquer coisa
print(n)  # output: true

n = input('Digite um valor: ')  # input: nada
print(n)  # output: false



------ STRING ------

n = input('Digite um valor)



--------------------------------------------------------------------------------------------------------------



AULA 7 - OPERADORES ARITMÉTICOS

+ - Adição
- - Subtração
* - Multiplicação
/ - Divisão
// - Divisão arredondada
** - Potenciação
% - Resto da Divisão, Módulo
() - Alterar a ordem das contas


print(10 + 10)  # Resultado: 20
print('10' + '10')  # Resultado: 1010

print(10 - 5)  # Resultado: 5

print(10 * 10)  # Resultado: 100
print('10' * '10')  # Resultado: Erro, impossível multiplicar str por str
print(10 * '10')  # Resultado: 10101010101010101010

print(10 / 2)  # Resultado: 5
print(10 / 3)  # Resultado: 3.3333333333333335

print(10 // 3)  # Resultado: 3
print(10.0 // 3)  # Resultado: 3.0

print(10 % 3)  # Resultado: 1

print(5+2*10)  # Resultado: 25
print((5+2)*10)  # Resultado: 70



--------------------------------------------------------------------------------------------------------------



AULA 8 - UTILIZANDO MÓDULOS

Bibliotecas

Import biblioteca

from biblioteca import função

ex.:

MATH

ceil - arredondamento para cima
floor - arredondamento para baixo
trunc - truncate, eliminar da vírgula pra frente
pow - potencia, semelhante a **
sqrt - raiz quadrada
factorial - fatorial
etc...

para usar toda a biblioteca: import math

Exemplo:

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))


para usar somente uma função: from math import sqrt

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

"""
