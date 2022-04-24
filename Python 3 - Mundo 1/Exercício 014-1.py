# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

print("\nConversor de demperaturas\n")
print("Qual conversão deseja fazer?\n")

print("1 - Kelvin")
print("2 - Fahrenheit")
print("3 - Celsius")

print("\nDigite apenas o número correspondente.\n")

option1 = input("Temperatura de Origem: ")
option2 = input("Temperatura de Destino: ")


# kelvin = float(input('Temperatura em K: '))
# fahrenheit = float(input('Temperatura em °F: '))
# celsius = float(input('Temperatura em °C: '))


if option1 == 1 and option2 == 2:  # Kelvin to Fahrenheit
    kelvin = float(input('Temperatura em K: '))
    temp = (((kelvin - 273)*1.8) + 32)
    print("{} K equivalem a {} °F".format(kelvin, temp))

elif option1 == 1 and option2 == 3:  # Kelvin to Celsius
    kelvin = float(input('Temperatura em K: '))
    temp = kelvin - 273
    print("{} K equivalem a {} °C".format(kelvin, temp))



elif option1 == 2 and option2 == 1:  # Fahrenheit to Kelvin
    fahrenheit = float(input('Temperatura em °F: '))
    temp = (((fahrenheit - 32) * (5 / 9)) + 273)
    print("{} °F equivalem a {} K".format(fahrenheit, temp))

elif option1 == 2 and option2 == 3:  # Fahrenheit to Celsius
    fahrenheit = float(input('Temperatura em °F: '))
    temp = (fahrenheit - 32) / 1.8
    print("{} °F equivalem a {} °C".format(fahrenheit, temp))



elif option1 == 3 and option2 == 1:  # Celsius to Kelvin
    celsius = float(input('Temperatura em °C: '))
    temp = celsius + 273
    print("{} °C equivalem a {} K".format(celsius, temp))

elif option1 == 3 and option2 == 2:  # Celsius to Fahrenheit
    celsius = float(input('Temperatura em °C: '))
    temp = celsius * 1.8 + 32
    print("{} °C equivalem a {} °F".format(celsius, temp))