#Simples, Composto e Encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#Cacular a média aritmética das notas
media = (n1 + n2) / 2

if (media >= 7.0):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif (media >= 5.0):
    print('Você está de Recuperação')
else:
    print('Aluno Reprovado...')

print('Sua Média é {}'.format(media))
