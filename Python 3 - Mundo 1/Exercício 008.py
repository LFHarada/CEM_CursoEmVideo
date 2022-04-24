# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite o valor em metros: '))

centimetros = metros * 100
milímetros = metros * 1000

print('{:.2f} metros equivalem a:\n{:.2f} centímetros\n{:.2f} milímetros'.format(metros, centimetros, milímetros))