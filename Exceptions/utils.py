

from exceptions import myExceptions

def dividebyZero(num1:int,num2:int)->int:
    """
    This function divide two numbers in case the denominator is 0 return 0
    number1: int
    number2: int
    return int
    """

    # try:
    #    result= num1//num2
    # except ZeroDivisionError:  #ZeroDivisionError es un objeto de python
    #     return 0
    #  # else se ejecuta cuando no captura un error, el resultado y hoola 
    # else:              
    #     print("hola")
    # finally:
    #     print("Se ejecuta siempre")
    # return result

    # try:
    #     result=num1//num2
    # except Exception as e:
    #     print(e) # imprimo el error capturado

    if(num2==0):
        raise myExceptions("El denominador no puede ser cero")
    return num1//num2