class Rectangle:
  
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return ((self.width + self.height) * 2)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        width = '*' * self.width
        picture = ""
        for i in range(self.height):
            picture = f"{picture}{width}\n"
        return picture

    def get_amount_inside(self, cls):
        if cls.height < self.height:
            h = self.height // cls.height
            return (self.width // cls.width) * (h if h > 0 else 1)
        elif cls.height == self.height:
            return (self.width // cls.width) * (self.height // cls.height)
        else:
            return 0


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.set_width(side)

    def set_width(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)
        
