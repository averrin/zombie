# coding=utf8

class Fraction(object):
    """Класс дробь с числителем и знаминателем"""
    def normalize(self):
        k, d = self.numerator, self.denominator
        while d != 0:
            k, d = d, k % d
        self.numerator /= k
        self.denominator /= k

    def __init__(self, numerator, denominator=1):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.normalize()

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __div__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __float__(self):
        return float(self.numerator) / self.denominator

    def __str__(self):
        return '%d / %d' % (self.numerator, self.denominator)
