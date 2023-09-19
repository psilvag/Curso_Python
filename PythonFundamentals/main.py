# DECLARACION Y DEFINICION DE VARIABLES 
nombre="pablo"
edad=30
_Direccion1="zona villa dolores"
sexo="masculino"
nombre=45
CONSTANTE="python"
print(type(_Direccion1))
print(type(CONSTANTE))

# TIPOS DE DATOS

#INT,FLOAT,BOOLEANO, STRING
numero1=56 
print(type(numero1))
numero2=45
print(type(numero2))
numero3=-5
print(type(numero3))
numeroDouble=4.5
print(type(numeroDouble))
variableBool=True
print(type(variableBool))
texto="esto es un string"
print(type(texto))

#CONCATENACION
# USANDO +
nombre="pablo marcelo"
apellido="silva gutierrez"
edad=30
bool=True
resultado="Me llamo"+" "+nombre+" "+apellido+" "+"y tengo"+" "+str(edad)+"años"
print(resultado)

#USANDO %  para versiones menores a 3.6 de python
instituto="academlo"
minombre="pablo"
text= "Hola %s mi nombre es %s" % (instituto,minombre)
print(text)

#USANDO METODO .format
var_1="estoy aprendiendo"
var_2="python"
var_3="version 3.11.0"

text="{} {} {}".format(var_1,var_2,var_3)
print(text)

print("DEFINIENDO EL ORDEN")
text="{0} {2} {1}".format(var_1,var_2,var_3)
print(text)

#USANDO f STRINGS
producto="curso de python"
precio=19.99
text=f"El {producto} tiene un precio de {precio} dolares y se agrega un impuesto de {precio+(precio*0.1)}"
print(text)

var1="Esto es una cadena de texto"
print("longitud",len(var1))
print(var1[0:9])  #[limiteinferior:limitesuperior] no toma el ultimo valor
print(var1[1:20:7]) #[limiteinferior:limitesuperior:posicionesDesalto]
print(var1[:7])
print(var1[5:])
print(var1[:])
print(var1[::-1])# obtener la cadena al reves

