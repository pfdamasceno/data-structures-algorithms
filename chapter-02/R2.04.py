'''
R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
'''
class Flower:
    '''
    Initializes and retrieves variables from class.
    _name: name of flower (str)
    _number_of_petals (int)
    _price (float)
    '''
    def __init__(self, name, num_petals, price):

        if not isinstance(num_petals,int):
            raise TypeError('number of petals should be an integer')

        try:
            self._price = float(price)
        except ValueError as e:
            print("Price must be integer or float:", e)

        self._name               = str(name)
        self._number_of_petals   = num_petals

    def get_name(self):
        return(self._name)

    def get_num_petals(self):
        return(self._number_of_petals)

    def get_price(self):
        return(self._price)

    def set_name(self, name):
        self._name = name

    def set_num_petals(self, num_petals):
        self._number_of_petals = num_petals

    def set_price(self, price):
        self._price = price

###########################

new_flower = Flower(3, 4, 4)
new_flower.set_price(3)
new_flower.get_price()
