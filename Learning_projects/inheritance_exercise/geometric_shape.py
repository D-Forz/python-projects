#ABC Abstract Base Class
from abc import ABC, abstractmethod

class GeometricShape(ABC):
    def __init__(self, high, width):
        if self._validate(high):
            self._high = high
        else:
            self._high = 0
            raise ValueError(f"ValueError on High {high}")
        if self._validate(width):
            self._width = width
        else:
            self._width = 0
            raise ValueError(f"ValueError on Width {width}")

    def __str__(self) -> str:
        return f"GeometricShape[high: {self._high}, width: {self._width}]"
    
    @property
    def high(self):
        return self._high
    
    @high.setter
    def high(self, high):
        if self._validate(high):
            self._high = high
        else:
            raise ValueError(f"ValueError on High {high}")
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if self._validate(width):
            self._width = width
        else:
            raise ValueError(f"ValueError on Width {width}")
    
    @abstractmethod
    def calculate_area(self):
        pass

    def _validate(self, value):
        return True if 0 < value < 20 else False

class Color:
    def __init__(self, color):
        self._color = color
    
    def __str__(self) -> str:
        return f"Color[color: {self._color}]"
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

class Square(GeometricShape, Color):
    def __init__(self, side, color):
        GeometricShape.__init__(self, side, side)
        Color.__init__(self, color)
    
    def calculate_area(self):
        return self.high * self.width

    def __str__(self) -> str:
        return f"{GeometricShape.__str__(self)} {Color.__str__(self)}"

class Rectangle(GeometricShape, Color):
    def __init__(self, high, width, color):
        #super().__init__(high, width)
        GeometricShape.__init__(self, high, width)
        Color.__init__(self, color)
    
    def calculate_area(self):
        return self.high * self.width
    
    def __str__(self) -> str:
        return f"{GeometricShape.__str__(self)} {Color.__str__(self)}"

new_square = Square(10, "red")
new_rectangle = Rectangle(5, 10, "blue")
print(new_rectangle.calculate_area())
    

