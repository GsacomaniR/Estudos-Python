# Manipulação de arquivos de texto.

#print(f'\Método read():\n)
#print(manipulador.read())

# print(f'Método readline():\n')
# print(manipulador.readline())
# print(manipulador.readline())

# print(f'Método readline():\n')
# print(manipulador.readlines())
# texto = input('Qual termo deseja procurar no arquivo? ')
# try:
#     manipulador = open('arquivo.txt', 'r', encoding='utf-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#            print(f'A string foi encontrada!')
#            print(linha)
#         else:
#             print(f'String não encontada!')
# except IOError:
#      print(f'Não foi possível abrir o arquivo')
# else:
#    manipulador.close()

#Escrever em arquivos de texto
# texto = 'Python é usado em Ciência de Dados Extensivamente'
# try:
#     manipulador = open('arquivo.txt', 'a', encoding='utf-8')
#     manipulador.write(texto)
# except IOError:
#      print(f'Não foi possível abrir o arquivo')
# else:
#    manipulador.close()

frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola']

# Criar e grarvar o arquivo
try:
    manipulador = open('frutas.dat', 'w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
     print(f'Não foi possível abrir o arquivo')
else:
   manipulador.close()

# Ler o arquivo criado:
try:
    manipulador = open('frutas.dat', 'r', encoding='utf-8')
    print(manipulador.read())
except IOError:
     print(f'Não foi possível abrir o arquivo')
else:
   manipulador.close()