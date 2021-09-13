import json
import numpy

with open('dicionario.json', 'r') as file:
    dicionario_json = json.loads(file.read())

#print(dicionario_json['variaveis'])

codigo = open('codigo.txt', 'r')

listaprincipal = []
novaLinha = []
ultimaPalavraJunta = []
tamanhoLinha = 0
superNovaLinha = []
ultimaPalavraJunta = []


def buscar(lista):
    print("*********CÓDIGO*************")
    print(lista)
    print("****************************")
    print("**********SAÍDA*************")
    for lista_item in lista:
        pos = lista.index(lista_item)      
        for chave,valor in dicionario_json.items():
            #print(valor)
            for val in valor:
                if val == lista_item:
                    print(chave, lista_item)
    



for linha in codigo:
    linha = linha.rstrip()
    novaLinha = linha.split()
    #print(novaLinha,"NOVA LINHA ***********")
    tamanhoNovaLinha = numpy.size(novaLinha)
    #print(tamanhoNovaLinha,"TAMANHO DA LINHA *****************")
    ultimapalavra = list(novaLinha[tamanhoNovaLinha-1])
    tamanhoUltimaPalavra = numpy.size(ultimapalavra)
    #print(tamanhoUltimaPalavra)
    #print(ultimapalavra[tamanhoUltimaPalavra-1])
    #print(novaLinha[tamanhoNovaLinha-1])
    listaprincipal = novaLinha
    #print(listaprincipal)
    
    if ultimapalavra[tamanhoUltimaPalavra-1] == ";":
        num = tamanhoNovaLinha-1
        listaprincipal.pop(num)
        superNovaLinha = ultimapalavra[tamanhoUltimaPalavra-1]
        ultimaPalavraJunta =''.join(ultimapalavra[:len(ultimapalavra)-1])
        listaprincipal.append(ultimaPalavraJunta)
        listaprincipal.append(superNovaLinha)

    #print(listaprincipal)
    buscar(listaprincipal)


codigo.close()