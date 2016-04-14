from fractions import gcd
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
        
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
        
    def __mul__(self, r):
        return Rational(self.p * r.p , self.q * r.q)
        
    def __div__(self, r):
        return Rational(self.p * r.q , self.q * r.p)
        
    def __str__(self):
        g=gcd(self.p,self.q)
        if self.q/g ==1:
            return '%s/1'%(self.p/g)
        else:
            return '%s/%s'%(self.p/g,self.q/g)
    __repr__ = __str__
    
r1 = Rational(1, 2)
r2 = Rational(1, 4)
print (r1 + r2)
print (r1 - r2)
print (r1 * r2)
#print (r1 / r2)