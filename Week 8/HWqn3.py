import math

class Diff:
    def __init__(self, func, h = 10**(-4)):
        self.func = func
        self._h = h

    def __call__(self, x):
        df_value = (self.func(x + self._h) - self.func(x))/self._h
        return df_value

def log(x):
    return math.log(x)

df = Diff(ln, 0.1) # make function -like object df
print(df(10))
df = Diff(ln, 0.5)
print(df(10))
df = Diff(ln, 10**(-5))
print(df(10))
df = Diff(ln, 10**(-9))
print(df(10))
df = Diff(ln, 10**(-11))
print(df(10))




