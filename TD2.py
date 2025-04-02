class Polynomial:
    def __init__(self,coefficients):
        #initialise un polynôme avec une liste de coefficients.
        #le terme d'indice i correspond au coefficient de degré i.
        self.coefficients = coefficients
    def __str__(self):
        #retourne une représentation en chaîne du polynome
        polynome = []
        for i,coeff in enumerate(self.coefficients):
            if coeff != 0 :
                terme = f"{coeff}x^{i}" if i>0 else f"{coeff}"
                polynome.append(terme)
        if polynome :
            return "+".join(polynome[::-1])
        else:
            return "0"
    
    def __add__(self,other):
        #additionne deux polynomes
        max_length= max( len(self.coefficients),len(other.coefficients) )
        new_coeffs = [0]*max_length
        
        for i in range(len(self.coefficients)):
            new_coeffs[i] += self.coefficients[i]
        for i in range(len(other.coefficients)):
            new_coeffs[i] += other.coefficients[i]
        return Polynomial(new_coeffs)





p1 = Polynomial([-1,0,1])
print(p1)
p2 = Polynomial([2,1,5])
p3 = p1+p2
print(p3)
