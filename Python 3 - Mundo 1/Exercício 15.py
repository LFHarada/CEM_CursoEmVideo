# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos 
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos KM foram percorridos? '))
dias = int(input('Quantidade de dias alugados:'))
aluguel = 0.15

total = (km * 0.15) + (dias * 60)

print('O valor total do aluguel é de: R$ {:.2f}'.format(total))