#exemplo de dicionário 
dic = {'nome': 'Shirley Manson', 'Banda': 'Garbage'}

#Acessando elementos:
print('Nome:', dic['nome'])

#Adicionando elementos:
dic['album'] = 'Version 2.0'

#apagando um elemento do cionário:
del dic['album']

#Obtendo os itens, chaves e valores:
print('itens:', dic.items())
print('chaves:', dic.keys())
print('valores:', dic.values())