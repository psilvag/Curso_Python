

#CAPITALIZE
texto= 'hola desde python'
texto2=texto.capitalize() # Pone en mayuscula el primer caracter
print(texto2)

#CASEFOLD o LOWER
texto3='Hola como estas'
texto4=texto3.casefold() # convierte a minusculas el primer caracter y elimina tildes
print(texto4)

#CENTER
texto5='Python'
texto6=texto5.center(25,'-') # centrear la palabra entre 25 caracteres '-' o tambien puede ser espacios
print(texto6)

#COUNT
texto7="Esto es un texto dentro de un archivo de python"
valor=texto7.count('un',0,10) # devuelve un entero cuantas veces se repite una palabra,caracter,numero desde un limite a otro
print(valor)

#ENDSWITH
texto8="Esto es un texto de ejemplo en python.js"
t=texto8.endswith('u',0,9) # devuelve un boolean, si termina o no en esa frase,o caracter
print(t)


#FIND 
texto9="Esto es un texto EN PYTHON 8"
res=texto9.find('tex') # retorna el indice donde encuentra ese valor
print(res)

#UPPER- ISUPPER / LOWER -ISLOWER
texto10="texto de ejemplo"
v=texto10.upper().isupper() # lo mismo seria lower(), is lower()
print(v)

#replace
texto11="hola a todos desde academlo"
salida=texto11.replace('academlo','mi casa') # reemplaza un string por otro
print(salida)

#SPLIT: de texto a array- #JOIN: de array a texto
texto12="Python es muy divertido para programar"
resp=texto12.split()
print(resp)

resp2=" ".join(resp)
print(resp2)



