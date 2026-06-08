import requests 

#cria variavel perguntando qual pokemon deseja pesquisar
pokemon = input ("Qual Pokemon deseja? ")

#joga na api o nome do pokemon
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}" 

#verifica a resposta
resposta = requests.get(url)

#exibe a resposta se for encontrado ou não
if resposta.status_code == 200:
    print ("status:", resposta.status_code)
    dados = resposta.json()

    print ("Dados do Pokémon:")
    print ("nome:", dados ['name'])
    print ("id:", dados ['id'])
    print ("altura:", dados ['height'])
    print ("peso:", dados ['weight'])

    print ("habilidade:")
    for habilidade in dados ['abilities']:
        print (">",habilidade ['ability']['name'])

    print ("tipo:")
    for tipo in dados ['types']:
        print (">",tipo ['type']['name'])

else:
    print ("Pokemon não encontrado")


#lista acessa posição, dicionario acessa chave
#for percorre a lista abilities pegando um dicionario de cada vez
#habilidade ['ability']['name']) pega o valor da chave name do dicionario ability
#se tiver mais de 1 resposta mostra todas
#abilities = lista, cada valor = dicionario