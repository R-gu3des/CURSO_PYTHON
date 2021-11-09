"""
No Python, o comportamento dos operadores é deifnido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.
"""

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getArea(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class> 'Retangulo({self.x, self.y})'"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)
    
    def __lt__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()

        if a1 > a2:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.X == other.x and self.y == other.y:
            return True
        else:
            return False    


r1 = Retangulo(12, 20)
r2 = Retangulo(5, 10)

r3 = r1 + r2

print(r3)