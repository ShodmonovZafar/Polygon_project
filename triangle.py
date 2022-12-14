from math import sqrt

class Triangle:
    
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def sum_(self):
        return self.a + self.b + self.c
    
    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        if self.a > 0 and self.b > 0 and self.c > 0:
            a = max(self.a, self.b, self.c)
            if a < (self.sum_() - a):
                return True
            else:
                return False
        else:
            return False

    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        ''' 
        pass

    def perimeter(self):
    
        '''
        This method finds the perimeter of the triangle.

        Args:
            No
        Returns:
            int or float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        if self.is_valid():
            return self.sum_()
        else:
            return 0

    def area(self):
        '''
        This method finds the area of the triangle.

        Args:
            NO
        Returns:
            int or float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        pass
