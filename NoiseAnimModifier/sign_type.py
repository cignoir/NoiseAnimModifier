# encoding:utf-8

# -----------------------------------
# Noise Anim Modifier
#
# Copyright (c) 2023 cignoir
# https://github.com/cignoir
# -----------------------------------

from enum import Enum

class SignType(Enum):
    Both = 1
    Plus = 2
    Minus = 3

    @classmethod
    def find_by(cls, id):
        if id == 1:
            return cls.Both
        elif id == 2:
            return cls.Plus
        elif id == 3:
            return cls.Minus
        else:
            return cls.Both