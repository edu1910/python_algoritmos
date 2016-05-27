arquivo = open('arquivo.txt', 'r')
print("Conteúdo: " + str(arquivo.readlines()))
arquivo.close()