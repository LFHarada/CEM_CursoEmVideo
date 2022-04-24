# Faça um programa que leia a largura  e a altrura de uma parede, calcule a sua área e a quantidade necesária para pintá-la.
# obs.: cada litro de tinta consegue pintar uma área de 2m^2
print('\n')
print('-' * 32)
print('Welcome to the paint calculator.')
print('-' * 32)

while True:
    print('\nWhat measurement unit do you use?\n')
    print('1 - Meters')
    print('2 - Centimeters')
    print('3 - Inches')

    unit = int(input("\nOption number: "))
    
    if unit == 1:  #meters
        height = float(input('What is the  height of the wall? '))
        width = float(input('What is the width of the wall? '))
        layers = float(input('How many layers do you want to use? '))

        area = height * width
        liters = 2 * area * layers
        gallon = liters * 0.264172
        
        print('\nYout wall measures {}m x {}m, and the area is {}m².'.format(height, width, area))
        print('\nYou will need aproximately {:.2f} liters ({:.2f} gallons) of paint.'.format(liters, gallon)) 

    elif unit == 2:  #centimeters
        height = float(input('What is the  height of the wall? '))
        width = float(input('What is the width of the wall? '))
        layers = float(input('How many layers do you want to use? '))

        area = (height*0.01) * (width*0.01)
        liters = 2 * area * layers
        gallon = liters * 0.264172
        
        print('\nYout wall measures {}cm x {}cm, and the area is {}m².'.format(height, width, area))
        print('\nYou will need aproximately {:.2f} liters ({:.2f} gallons) of paint.'.format(liters, gallon)) 

    elif unit == 3:  #inches
        height = float(input('What is the  height of the wall? '))
        width = float(input('What is the width of the wall? '))
        layers = float(input('How many layers do you want to use? '))

        area = (height*0.0254) * (width*0.0254)
        liters = 2 * area * layers
        gallon = liters * 0.264172

        print('\nYout wall measures {}in x {}in, and the area is {}m².'.format(height, width, area))
        print('\nYou will need aproximately {:.2f} liters ({:.2f} gallons) of paint.'.format(liters, gallon)) 

    else:
        print('\nPlease, answer correctly.')