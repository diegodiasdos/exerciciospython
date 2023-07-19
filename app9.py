s = 'Camel'

#Concatenação 
print('The' +  s + 'run away!')

#Interpolação 
print('tamanho de %s => %d' %(s,len(s)))

#String tratada como sequencia 
for ch in s:print(ch)

#Strings são objetos 
if s.startswith('C'): print(s.upper())

# O que acontecerá?
print(3 * s)
# 3 * s é consistente com s + s + s 