# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
print('')
num = float(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** 0.5

print('')
print('O número que você digitou é: {}'.format(num))
print('O DOBRO do número que você digitou é: {}'.format(dobro))
print('O TRIPLO do número que você digitou é: {}'.format(triplo))
print('A RAIZ QUADRADA do número que você digitou é: {:.3f}'.format(raiz))
print('')