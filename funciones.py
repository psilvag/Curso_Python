#Funciones 

# los valores int , int son types en python
def minmax(num1:int,num2:int)->int:
    # las triples comillas me permiten documentar el codigo
    """
    Function: return amin max between two numbers 
    """
    if(num1>num2):
        return num1
    return num2
print(minmax(-1,-3))


