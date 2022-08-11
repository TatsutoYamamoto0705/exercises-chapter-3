from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Number):
            return Polynomial((self.coefficients[0]-other,) + self.coefficients[1:])
        
        elif isinstance(other, Polynomial):
            other_minus = tuple(-c for c in other.coefficients)
            return self + Polynomial(other_minus)

        else:
            return NotImplemented
    
    def __rsub__(self, other):
        minus = tuple(-c for c in self.coefficients)
        return other + Polynomial(minus)
   
    def __mul__(self, other):

        if isinstance(other, Number):
            mult = tuple([c*other for c in self.coefficients])
            return Polynomial(mult)
        
        elif isinstance(other, Polynomial):
            mults = [[0]*i for i in range(self.degree()+1)]
            final_mults = []
            for i in mults:
                i += [*other.coefficients]
            for i in range(self.degree()+1):
                final_mults.append(list(map(lambda x: x*self.coefficients[i], mults[i])))
            final_mults = [tuple(i) for i in final_mults]
            final_mults = [Polynomial(i) for i in final_mults]
            return sum(final_mults)
        
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):

        if isinstance(other, Number):
            multiplier = self
            for i in range(other-1):
                self = self*multiplier
            return self

        else:
            return NotImplemented

    def __call__(self, other):

        if isinstance(other, Number):
            val = self.coefficients[0]
            for i, v in enumerate(self.coefficients[1:]):
                val += v*(other**(i+1))
            return val

        else:
            return NotImplemented

    def dx(self):

        if self.degree() == 0:
            tup = tuple([0])
            print(tup)
            return Polynomial(tup)
        else:
            deriv = []
            for i,v in enumerate(self.coefficients[1:], 1):
                deriv.append(i*v)
            return Polynomial(tuple(deriv))


def derivative(poly):
    return poly.dx()

