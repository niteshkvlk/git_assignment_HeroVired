import math 

class GeopmetryCalculator:
    
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2
    
    def calculate_rectangle_area(self, length, width):
        return length * width
    
if __name__ == "__main__":
    
    calculator = GeopmetryCalculator()
    
    radius = 5
    print("Circle Area:", calculator.calculate_circle_area(radius))
    
    length = 10
    width = 6
    print("Rectangle Area:", calculator.calculate_rectangle_area(length, width))
    