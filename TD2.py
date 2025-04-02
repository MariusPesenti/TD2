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
            return "+".join(polynome[::])
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
#exercice3 : on crée une fonction scalar qui multiplie les polynomes ci-dessous
    
    def scalar(self,c):
        new_coeffs = [c*coeff for coeff in self.coefficients]
        return Polynomial(new_coeffs)
        

p1 = Polynomial([2,-3,5])
print(p1)
p2 = Polynomial([-3,-1,-4])
c = 2
p3 = Polynomial.scalar(p1,c)
print(p3)   




# Exercice 2
#On propose ceci pour la classe des polynome modulo q : 

class PolynomialMod:
    def __init__(self, coefficients, q, n):
        self.q = q
        self.n = n
        self.coefficients = [c%q for c in coefficients]
        self.reduire_modq()

#il faut definir une methode reduire_modq qui permet de reduire le polynome en utilisant X^n = -1 [X^(n+1)]

    def reduire_modq(self):
       """ Réduit le polynôme en appliquant X^n ≡ -1 mod q """        
       while len(self.coefficients) > self.n:
            exces = self.coefficients.pop()  # Dernier terme (degré >= n)
            if exces:  # Si non nul, on l'ajoute à X^0 sous forme -excess mod q
                self.coefficients[0] = (self.coefficients[0] - exces) % self.q
       return self

    def __str__(self):
        #retourne une représentation en chaîne du polynome
        polynome = []
        for i,coeff in enumerate(self.coefficients):
            if coeff != 0 :
                terme = f"{coeff}x^{i}" if i>0 else f"{coeff}"
                polynome.append(terme)
        if polynome :
            return "+".join(polynome[::])
        else:
            return "0"

#on peut également definir une multiplication par scalaire modulo q pour les polynomes.
    def scalar(self, c):
        #Multiplie chaque coefficient par un scalaire c modulo q
        new_coeffs = [(c * coeff) % self.q for coeff in self.coefficients]
        return PolynomialMod(new_coeffs, self.q, self.n)     
        

       
        
        





