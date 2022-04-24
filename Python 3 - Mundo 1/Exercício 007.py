# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: ')) 

media = (nota_um + nota_dois) / 2

print('A sua média é {:.2f} pontos.'.format(media))