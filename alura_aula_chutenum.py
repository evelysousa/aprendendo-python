print("*Bem vindo ao nosso jogo*")

num_secret = 42
tentativas = 3
chances = 1

while (chances<=tentativas):
    chute_num  = input("Digite o seu numero: ")
    print("Você digitou", chute_num)
    print("Tentativa {} de {}".format(chances,tentativas))
    chute = int(chute_num)
    acertou = num_secret == chute 
    chute_maior = chute > num_secret
    chute_menor = chute < num_secret
    if (acertou):
        print("Você acertou!\n")
    else: 
        if(chute_maior):
            print("Chute errado! Seu chute foi maior do que o número secreto")
        elif(chute_menor):
            print("Chute errado! Seu chute foi menor do que o número secreto") 
    chances=chances+1
print("**Fim do jogo**")
    

