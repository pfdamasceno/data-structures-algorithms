import copy

class Vector():
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if type(d) == int:
            self._coords = [0]*d
        else:
            self._coords = [0]*len(d)
            for j in range(len(d)):
                self._coords[j] = d[j]

    def __len__(self):
        """Return the dimension of the vector."""
        return(len(self._coords))

    def __getitem__(self,j):
        """Return jth coordinate of vector."""
        return(self._coords[j])

    def __setitem__(self,j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, v2):
        """Return sum of two vectors."""
        if len(self) != len(v2):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + v2[j]
        return(result)

    def __radd__(v2, self):
        """Return sum of list plus vectors."""
        if len(self) != len(v2):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + v2[j]
        return(result)

    def __sub__(self, v2):
        """Return difference between vectors."""
        if len(self) != len(v2):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - v2[j]
        return(result)

    def __neg__(self):
        """Return negated values of vector."""
        neg_vector = copy.deepcopy(self)
        for j in range(len(self)):
            neg_vector._coords[j] *= -1
        return(neg_vector)

    def __mul__(self,n):
        """Return product between two vector."""
        new_vector = copy.deepcopy(self)
        for j in range(len(self)):
            new_vector._coords[j] *= n
        return(new_vector)

    def __rmul__(self,n):
        """Return product between a number and a vector."""
        new_vector = copy.deepcopy(self)
        for j in range(len(self)):
            new_vector._coords[j] *= n
        return(new_vector)
