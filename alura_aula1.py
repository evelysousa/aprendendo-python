print("*Bem vindo ao nosso jogo*")

num_secret = 42
tentativas = 3
chances = 1

for chances in range(1,tentativas + 1):
    print("Tentativa {} de {}".format(chances, tentativas))
    chute_num  = input("Digite um numero entre 1 e 100: ")
    print("Você digitou", chute_num)
   
    chute = int(chute_num)
    acertou = num_secret == chute 
    chute_maior = chute > num_secret
    chute_menor = chute < num_secret

    if(chute<1 or chute >100):
       print("Você dee digitar um número de 1 a 100")
       continue

    if (acertou):
        print("Você acertou!\n")
        break
    else: 
        if(chute_maior):
            print("Chute errado! Seu chute foi maior do que o número secreto")
        elif(chute_menor):
            print("Chute errado! Seu chute foi menor do que o número secreto") 
            
print("**Fim do jogo**")
    

