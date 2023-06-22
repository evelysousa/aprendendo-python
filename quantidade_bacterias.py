bactA = 4
bactB = 10

taxa_A= 0.03
taxa_B=0.015
dias = 0
while bactA <= bactB:
    bactA *=1+ taxa_A
    bactB *=1+ taxa_B
    dias +=1
print (f'Levará {dias} para as bactérias de A {bactA} ultrapassar a quantidade das de B {bactB}')