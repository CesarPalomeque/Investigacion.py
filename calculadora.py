class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1=numero1
        self.num2=numero2
        
    def suma(self):
        total_Suma= self.num1 + self.num2
        print("La suma del {} y {} es: {}".format(self.num1,self.num2,total_Suma))
    
    def resta(self):
        total_Resta= self.num1 - self.num2
        print("La resta del {} y {} es: {}".format(self.num1, self.num2, total_Resta))
    
    def multiplicacion(self):
        total_Multiplicacion= self.num1 * self.num2
        print("La multiplicación de los numeros {} y {} es de: {}".format(self.num1,self.num2,total_Multiplicacion))
                
    def division(self):
        total_Division=self.num1 / self.num2
        print("La division de los numeros es de: {}".format(total_Division))
        
class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(self,numero1, numero2)
        
        
    def multiplicacion(self):
        Resultado= self.num1 * self.num2
        return Resultado
    
    def exponente(self):
        total_Exp = self.num1**self.num2
        print("la respuesta es: ",total_Exp)

    def valorAbsoluto(sefl,numero3):
        if numero3 < 0:
            numero3 = numero3 *- 1
        return numero3

    
class calCientifica(Calculadora):
                        #Radio , #Lado.
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
    def circunferencia(self):
        PI = 3.1416
        Perimetro = 2 * PI * self.num1
        return Perimetro
    
    def areaCirculo(self):
        PI = 3.1416
        area = PI * (self.num1**2)
        return area
    
    def areaCuadrado(self):
        return self.num2 ** 2
cal=Calculadora(1,1)
print(cal.suma())
print(cal.resta())
print(cal.multiplicacion())
print(cal.division())
cal1 = calCientifica(1,4)
print('La circuferencia es',cal1.circunferencia())
print('El area del circulo es',cal1.areaCirculo())
print('area del cuadrado',cal1.areaCuadrado())        