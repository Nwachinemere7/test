class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_perimeter(self):
        sum_sides = self.a + self.b + self.c
        return sum_sides

t1 = Triangle(2, 3, 4)
t2 = Triangle(3, 4, 5)
sum_sides = t1.get_perimeter()
print(sum_sides)
sum_sides = t2.get_perimeter()
print(sum_sides)
# print(sum_sides)