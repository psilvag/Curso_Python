from enum import Enum

class Moves(Enum):
    W="ARRIBA"
    S="ABAJO"
    A="IZQUIERDA"
    D="DERECHA"

class Attacks(Enum):
    P="GOLPE"
    K="PATADA"


class TaladokenCombination(Enum):
    PLAYER1_COMBINATION="DSDP"
    PLAYER2_COMBINATION="ASAP"

class TaladokenEnergy(Enum):
     PLAYER1_COMBINATION=3
     PLAYER2_COMBINATION=2

class RemuyukenCombination(Enum):
    PLAYER1_COMBINATION="SDK"
    PLAYER2_COMBINATION="SAK"

class RemuyukenEnergy(Enum):
     PLAYER1_COMBINATION=2
     PLAYER2_COMBINATION=3

class SpecialNames(Enum):
     TALADOKEN="Taladoken"
     REMUYUKEN="Remuyuken"


