class GeometricShape:
    def __init__(self, high, width):
        self._high = high
        self._width = width

    def __str__(self) -> str:
        return f"GeometricShape[high: {self._high}, width: {self._width}]"
    
    @property
    def high(self):
        return self._high
    
    @high.setter
    def high(self, high):
        self._high = high
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        self._width = width

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
    

