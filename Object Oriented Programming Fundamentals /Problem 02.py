# Implement the methods get_num and get_den that will return the numerator and denominator of a fraction.

class Fraction:
  def __init__(self, num, den):
    self.num = num
    self.den = den

  def get_num(self):
    return self.num

  def get_den(self):
    return self.den

fraction = Fraction(2, 3)
print(f"Numerator is - {fraction.get_num()}")
print(f"Denominator is - {get_den.get_den()}")
