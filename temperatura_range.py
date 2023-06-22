cont = 0
soma_temp = 0
temp = float(input('Digite a temperatura: '))

while temp !=-273:
    soma_temp += temp
    cont =+1
    temp=float(input('Digite a temperatura: '))
    media = soma_temp/cont
    print(f'A média das temperaturas é: {media}')
