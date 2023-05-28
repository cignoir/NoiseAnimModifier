# encoding:utf-8

# -----------------------------------
# Noise Anim Modifier
#
# Copyright (c) 2023 cignoir
# https://github.com/cignoir
# -----------------------------------

from enum import Enum

class OperatorType(Enum):
    Addition = 1
    Subtraction = 2
    Multiplication = 3
    Division = 4

    @classmethod
    def find_by(cls, id):
        if id == 1:
            return cls.Addition
        elif id == 2:
            return cls.Subtraction
        elif id == 3:
            return cls.Multiplication
        elif id == 4:
            return cls.Division
        else:
            return cls.Addition