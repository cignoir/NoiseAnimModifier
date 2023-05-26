# encoding:utf-8

# -----------------------------------
# Noise Anim Modifier
#
# Copyright (c) 2023 cignoir
# https://github.com/cignoir
# -----------------------------------

import math

class Easing:
    NO_EASING = 'No Easing'
    SINE = 'Sine'
    QUAD = 'Quad'
    CUBIC = 'Cubic'
    QUART = 'Quart'
    QUINT = 'Quint'
    EXPO = 'Expo'
    CIRC = 'Circ'
    BACK = 'Back'
    ELASTIC = 'Elastic'

    @classmethod
    def all_types(cls):
        return [cls.NO_EASING, cls.SINE, cls.QUAD, cls.CUBIC, cls.QUART, cls.QUINT, cls.EXPO,
                cls.CIRC, cls.BACK, cls.ELASTIC]

    @classmethod
    def calc(cls, easing_type, ease_in, ease_out, x):
        f = cls.func(easing_type, ease_in, ease_out)
        return f(x)

    @classmethod
    def func(cls, easing_type, ease_in=True, ease_out=True):
        if easing_type == cls.SINE:
            if ease_in and ease_out:
                return cls.sine_ease_in_out
            elif ease_in:
                return cls.sine_ease_in
            elif ease_out:
                return cls.sine_ease_out
            else:
                return cls.no_easing
        elif easing_type == cls.QUAD:
            if ease_in and ease_out:
                return cls.quad_ease_in_out
            elif ease_in:
                return cls.quad_ease_in
            elif ease_out:
                return cls.quad_ease_out
            else:
                return cls.no_easing
        elif easing_type == 'Cubic':
            if ease_in and ease_out:
                return cls.cubic_ease_in_out
            elif ease_in:
                return cls.cubic_ease_in
            elif ease_out:
                return cls.cubic_ease_out
            else:
                return cls.no_easing
        elif easing_type == 'Quart':
            if ease_in and ease_out:
                return cls.quart_ease_in_out
            elif ease_in:
                return cls.quart_ease_in
            elif ease_out:
                return cls.quart_ease_out
            else:
                return cls.no_easing
        elif easing_type == 'Quint':
            if ease_in and ease_out:
                return cls.quint_ease_in_out
            elif ease_in:
                return cls.quint_ease_in
            elif ease_out:
                return cls.quint_ease_out
            else:
                return cls.no_easing
        elif easing_type == 'Expo':
            if ease_in and ease_out:
                return cls.expo_ease_in_out
            elif ease_in:
                return cls.expo_ease_in
            elif ease_out:
                return cls.expo_ease_out
            else:
                return cls.no_easing
        elif easing_type == 'Circ':
            if ease_in and ease_out:
                return cls.circ_ease_in_out
            elif ease_in:
                return cls.circ_ease_in
            elif ease_out:
                return cls.circ_ease_out
            else:
                return cls.no_easing
        elif easing_type == 'Back':
            if ease_in and ease_out:
                return cls.back_ease_in_out
            elif ease_in:
                return cls.back_ease_in
            elif ease_out:
                return cls.back_ease_out
            else:
                return cls.no_easing
        elif easing_type == 'Elastic':
            if ease_in and ease_out:
                return cls.elastic_ease_in_out
            elif ease_in:
                return cls.elastic_ease_in
            elif ease_out:
                return cls.elastic_ease_out
            else:
                return cls.no_easing
        else:
            return cls.no_easing

    @classmethod
    def no_easing(cls, x):
        return x

    @classmethod
    def sine_ease_in(cls, x):
        return 1 - math.cos((x * math.pi) / 2)

    @classmethod
    def sine_ease_out(cls, x):
        return math.sin(x * math.pi / 2)

    @classmethod
    def sine_ease_in_out(cls, x):
        return -(math.cos(math.pi * x) - 1) / 2

    @classmethod
    def quad_ease_in(cls, x):
        return math.pow(x, 2)

    @classmethod
    def quad_ease_out(cls, x):
        return 1 - math.pow(1 - x, 2)

    @classmethod
    def quad_ease_in_out(cls, x):
        return 2 * math.pow(x, 2) if x < 0.5 else 1 - math.pow(-2 * x + 2, 2) / 2

    @classmethod
    def cubic_ease_in(cls, x):
        return math.pow(x, 3)

    @classmethod
    def cubic_ease_out(cls, x):
        return 1 - math.pow(1 - x, 3)

    @classmethod
    def cubic_ease_in_out(cls, x):
        if x < 0.5:
            return 4 * math.pow(x, 3)
        else:
            return 1 - math.pow(-2 * x + 2, 3) / 2

    @classmethod
    def quart_ease_in(cls, x):
        return math.pow(x, 4)

    @classmethod
    def quart_ease_out(cls, x):
        return 1 - math.pow(1 - x, 4)

    @classmethod
    def quart_ease_in_out(cls, x):
        return 8 * math.pow(x, 4) if x < 0.5 else 1 - math.pow(-2 * x + 2, 4) / 2

    @classmethod
    def quint_ease_in(cls, x):
        return math.pow(x, 5)

    @classmethod
    def quint_ease_out(cls, x):
        return 1 - math.pow(1 - x, 5)

    @classmethod
    def quint_ease_in_out(cls, x):
        return 16 * math.pow(x, 5) if x < 0.5 else 1 - math.pow(-2 * x + 2, 5) / 2

    @classmethod
    def expo_ease_in(cls, x):
        return 0 if x == 0 else math.pow(2, 10 * x - 10)

    @classmethod
    def expo_ease_out(cls, x):
        return 1 if x == 1 else 1 - math.pow(2, -10 * x)

    @classmethod
    def expo_ease_in_out(cls, x):
        if x == 0 or x == 1:
            return x
        else:
            if x < 0.5:
                return math.pow(2, 20 * x - 10) / 2
            else:
                return (2 - math.pow(2, -20 * x + 10)) / 2

    @classmethod
    def circ_ease_in(cls, x):
        return 1 - math.sqrt(1 - math.pow(x, 2))

    @classmethod
    def circ_ease_out(cls, x):
        return math.sqrt(1 - math.pow(x - 1, 2))

    @classmethod
    def circ_ease_in_out(cls, x):
        if x < 0.5:
            return (1 - math.sqrt(1 - math.pow(2 * x, 2))) / 2
        else:
            return (math.sqrt(1 - math.pow(-2 * x + 2, 2)) + 1) / 2

    @classmethod
    def back_ease_in(cls, x):
        c1 = 1.70158
        c3 = c1 + 1
        return c3 * math.pow(x, 3) - c1 * math.pow(x, 2)

    @classmethod
    def back_ease_out(cls, x):
        c1 = 1.70158
        c3 = c1 + 1
        return 1 + c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)

    @classmethod
    def back_ease_in_out(cls, x):
        c1 = 1.70158
        c2 = c1 * 1.525
        if x < 0.5:
            return (math.pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2
        else:
            return (math.pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2

    @classmethod
    def elastic_ease_in(cls, x):
        c4 = 2 * math.pi / 3
        if x == 0 or x == 1:
            return x
        else:
            return -math.pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * c4)

    @classmethod
    def elastic_ease_out(cls, x):
        c4 = 2 * math.pi / 3
        if x == 0 or x == 1:
            return x
        else:
            math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1

    @classmethod
    def elastic_ease_in_out(cls, x):
        c5 = 2 * math.pi / 4.5
        if x == 0 or x == 1:
            return x
        else:
            if x < 0.5:
                return -(math.pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * c5)) / 2
            else:
                return (math.pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * c5)) / 2 + 1
