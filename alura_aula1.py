import random

print("*Bem vindo ao nosso jogo*")

num_secret = random.randrange(1, 101)
tentativas = 0
pontuacao = 1000

print("Escolha o nível de dificuldade")
print("1- fácil 2- médio 3 - dificil")
nivel= int(input("Escolha o nível de dificuldade: "))
print("você escolheu o nível:", nivel)
print("Você tem 1000 pontos para começar!")

if(nivel == 1):
    tentativas = 15
elif(nivel==2):
    tentativas = 10
else:
    tentativas = 5  

for chances in range(1,tentativas + 2):
    print("Você tem:", tentativas, "tentativas")
    print("Tentativa {} de {}".format(chances, tentativas))
    
    chute_num  = input("Digite um numero entre 1 e 100: ")
    print("Você digitou", chute_num)
    chute = int(chute_num)

    
    if(chute<1 or chute >100):
       print("Você dee digitar um número de 1 a 100")
       continue

    acertou = num_secret == chute 
    chute_maior = chute > num_secret
    chute_menor = chute < num_secret

    if (acertou):
        print("Você acertou e fez {}".format(pontuacao),)
        break
         
    else: 
        p_perdidos = abs(num_secret-chute)
        pontuacao = pontuacao - p_perdidos 
        
        if(chute_maior):
            print("Seu chute foi maior do que o número secreto")
            if(chances==tentativas):
               print("O número secreto era: {}. Você fez {}". format(num_secret, pontuacao))     
        elif(chute_menor):
            print("Seu chute foi menor do que o número secreto") 
            if(chances==tentativas):
               print("O número secreto era: {}. Você fez {}". format(num_secret, pontuacao)) 

        
        
print("**Fim do jogo**")
    

