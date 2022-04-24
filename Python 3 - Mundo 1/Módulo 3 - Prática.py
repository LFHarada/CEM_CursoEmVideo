#def validaPeso():

try:
    peso = float(input('Insira o peso de um item: '))

    if peso >= 0:
        valorretornado = True
        print(valorretornado)

    if peso < 0:
        valorretornado = False
        print(valorretornado)

except:
    print('Por favor, insira um peso válido.')
