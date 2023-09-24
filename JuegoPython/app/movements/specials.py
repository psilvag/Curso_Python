from base import Special
from settings import PLAYER1,PLAYER2
from constants import TaladokenEnergy,TaladokenCombination,RemuyukenCombination,RemuyukenEnergy,SpecialNames

class Taladoken(Special):
    def __init__(self,fighter):
        if fighter==PLAYER1:
            self.combination=TaladokenCombination.PLAYER1_COMBINATION.value
            self.energy=TaladokenEnergy.PLAYER1_COMBINATION.value
            self.name=SpecialNames.TALADOKEN.value
        if fighter==PLAYER2:
            self.combination=TaladokenCombination.PLAYER2_COMBINATION.value
            self.energy=TaladokenEnergy.PLAYER2_COMBINATION.value
            self.name=SpecialNames.TALADOKEN.value
            

class Remuyuken(Special):
    def __init__(self,fighter):
        if fighter==PLAYER1:
            self.combination=RemuyukenCombination.PLAYER1_COMBINATION.value
            self.energy=RemuyukenEnergy.PLAYER1_COMBINATION.value
            self.name=SpecialNames.REMUYUKEN.value
        if fighter==PLAYER2:
            self.combination=RemuyukenCombination.PLAYER2_COMBINATION.value
            self.energy=RemuyukenEnergy.PLAYER2_COMBINATION.value
            self.name=SpecialNames.REMUYUKEN.value
            




