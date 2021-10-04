
#Extraída do livro Algoritmos Estruturados – Autor: Harry Farrer e outros – Editora: LTC 3a Ed., Pág 75-861.12.1. 

#Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo. A última linha que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule e escreva a idade média deste grupo de indivíduos


#declaração de variávies
soma = int(0)
media = float(0.0)
i = int(0)

#comando while
idade = int(input())
while idade != 0:
  soma = soma + idade
  i = i + 1
  idade = int(input())
media = soma/i

#saída
print("A média é: " , media)
