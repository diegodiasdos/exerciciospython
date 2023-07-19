#Exemplos com dicionpários 
#Progse seus albuns 
progs = {'Yes': ['Close to the Edge', 'Fragile'],
         'Genesis':['Foxtrot', 'The Nursery Crime'],
         'ELP': ['Brain Salad Surgery']}

#Mais progs
progs['King Crimson'] = ['Red', 'Discipline']

#items() retorna uma lista de 
#tuplascom a chave e o valor 
for prog, albuns in progs.items():
    print(prog, '=>', albuns)
print(len(progs), 'bandas')

#Se tiver 'ELP',deleta
if 'ELP' in progs:
    del progs['ELP']
print('Agora,', len(progs),'bandas')