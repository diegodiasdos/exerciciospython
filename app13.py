import string

#Cria uma string temsplate 
st = string.Template('$aviso aconteceu em $quando')

#Preenche o modelo com um dicionario 

s = st.substitute({'aviso': 'Falta de eletricidade', 'quando': '03 de abril de 2002'})