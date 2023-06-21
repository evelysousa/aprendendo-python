num1 = int(input('Digite o lado AB do triangulo: '))
num2 = int(input('Digite o lado AC do triangulo: '))
num3= int(input('Digite o lado BC do triangulo: '))

if (num1 + num2 < num3):
    print('Esses numeros não podem formar um triangulo')
    print('Vamos tentra mais uma vez!')
else: 
    if(num2 + num3 != num1):
     
     print('Esse triangulo existe!')
     print('Continue digitando os lados do triangulo para classifica-lo')

num1 = int(input('Digite o lado AB do triangulo: '))
num2 = int(input('Digite o lado AC do triangulo: '))
num3= int(input('Digite o lado BC do triangulo: '))

if (num1 == num2 == num3 ):
    print('Esse Triangulo é Equilátero!')
elif(num1 != num2 != num3):
    print('Este triangulo é Escaleno!')
else:
    num1 == num2 == num3 
    print('Esse triangulo é isosceles!')    