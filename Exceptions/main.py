

from utils import dividebyZero
from exceptions import myExceptions

try:
    result=dividebyZero(4,0)
    print("Resultado",result)
except myExceptions as e:
    print(e.msg)
  
    