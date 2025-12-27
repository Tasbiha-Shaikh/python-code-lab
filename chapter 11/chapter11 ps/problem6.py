class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Vector addition
    def __add__(self, v):
        return Vector(
            self.x + v.x,
            self.y + v.y,
            self.z + v.z
        )

    # Dot product
    def dot(self, v):
        return (self.x * v.x +
                self.y * v.y +
                self.z * v.z)

    def __str__(self):
        return f"({self.x}i+ {self.y}j+ {self.z}k)"


# Creating objects
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Sum of vectors
v_sum = v1 + v2
print("Sum of vectors:", v_sum)

# Dot product
dot_product = v1.dot(v2)
print("Dot product:", dot_product)
