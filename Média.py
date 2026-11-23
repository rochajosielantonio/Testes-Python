print ('------Media geral do aluno-----')
aluno = input('Digite o nome do aluno: ')

n1 = int (input('Digite a nota 1: '))
n2 = int (input('Digite a nota 2: '))
n3 = int (input('Digite a nota 3: '))
n4 = int (input('Digite a nota 4: '))

soma = n1+n2+n3+n4

media = float(soma / 4)

print ('-----------------------------------')
print ('A média do ',aluno,' é: ',media)
print ('-----------------------------------')
