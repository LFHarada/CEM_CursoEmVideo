# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço

preco = float(input('Digite o preço do produto: '))

aumento = preco * 0.05

precofinal = preco + aumento

print('O preço com o aumento de 5% é: {}'.format(precofinal))