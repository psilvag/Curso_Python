
from data import json_1_arnaldor,json_2_tony,json_3_arnaldor
from constants import Moves, Attacks

def replace_values_string(infostr:str)->str:
    """
    Replace each value of string to movements
    params: string Ejm: DAD
    return: String with corresponding moves Ej: DERECHA-IZQUIERDA-DERECHA
    """
    infostr=infostr.upper()
    new_str=[]
    instructions={
        "W":Moves.A.value,
        "S":Moves.S.value,
        "A":Moves.A.value,
        "D":Moves.D.value,
        "P":Attacks.P.value,
        "K":Attacks.K.value
    }
    for c in infostr:
        new_str.append(instructions[c])
    return "-".join(new_str)

