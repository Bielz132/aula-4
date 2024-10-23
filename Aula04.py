#Notas de um aluno

nota1 = float(input('digite a nota 1: '))
nota2 = float(input('digite a nota 2: '))
nota3 = float(input('digite a nota 3: '))

media = (nota1 + nota2 + nota3)//3

nome = input('digite seu nome: ')

print('média:', media)

situacao = media >=7
print('situação do aluno', nome, 'aprovado ---> ',situacao)



#ATIVIDADE 01

nome = str(input('Digite seu nome: '))
gg = 'ótimo'
texto = 'agora Digite um numero, elevarei ao quadrado'
print(gg,nome,texto)
num1 = (float(input('-->')))
quadrado = num1 * num1
print(quadrado)



#ATIVIDADE 02

nome = str(input('Digite seu nome: '))
sobrenome = str(input("agora digite seu sobrenome: "))
total = nome + sobrenome
pergunta = '?'
print('então seu nome é:',total, pergunta)


 
#ATIVIDADE 03

print('Digite um Numero inteiro, APENAS inteiro')
n1 = (str(input('coloque o numero aqui ---> ')))
n2 = (str(input('coloque outro, irei juntar-los: ')))
resultado = n1 + n2
print('o numero que deu foi: ',resultado)



#ATIVIDADE 04

n = 'Python'
n2 = (str(input('Digite um numero: ')))
soma = n + n2
print(soma)



#ATIVIDADE 05

frase = 'seja bem vindo a cidade'
cidade = input('digite uma cidade ')
print(frase,cidade)

#listas 

n = list(range(1,11))
tupla = tuple(range(1,11))
conjunto = set(range(1,11))
print(n,tupla,conjunto)

