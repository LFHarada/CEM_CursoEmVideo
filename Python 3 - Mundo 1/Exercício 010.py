# Crie um progreama que leia quanto dinheiro uma pessoa tem na cateira e mostre quantos dólares ela pode comprar.

reais = float(input('Digite a quantia em dinheiro: '))
cotdol = 5.03
dolar = reais / cotdol

print('Você pode comprar aproximente {:.2f} dólares americanos.'.format(dolar))
546