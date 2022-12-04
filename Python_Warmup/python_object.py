class Jelly:
    def __init__(self, size, color, growth_rate):
        self.size = size
        self.color = color
        self.grow = lambda mass : growth_rate * mass
    def combine_jelly(func):
        def inner(*args):
            args[0].color = f"dark {args[0].color}"
            func(*args)
        return inner
    @combine_jelly
    def __add__(self, other):
        self.size += self.grow(other.size)
        other.size = 0
    def __eq__(self, other):
        return self.color == other.color and self.size == other.size
    @combine_jelly
    def __sub__(self, other):
        other.size += 0.5 * self.size
        self.size *= 0.5
    def update_growth_rate(self, new_growth_rate):
        self.grow = lambda mass: new_growth_rate * mass
class SimpleJelly(Jelly):
    def __init__(self, size, color):
        super().__init__(size, color, 1)
x = SimpleJelly(20, "black")
y = Jelly(5, "green", 2)
z = SimpleJelly(10, "red")
y.update_growth_rate(3)
