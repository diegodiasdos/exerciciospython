l = [1,2,3,4,5]
a,b, *resto = l 
a,b,resto
(1,2,[3,4,5])
print(a)
print(b)
print(resto)
*resto, a,b =l
print(resto)
print(a)
print(b)
a, *resto, b= l
print(a)
print(b)
print(resto) 
