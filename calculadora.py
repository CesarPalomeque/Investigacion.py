class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1=numero1
        self.num2=numero2
        
    def suma(self):
        result_Suma= self.num1 + self.num2
        print("La suma del los numeros: {} y {} es: {}".format(self.num1,self.num2,result_Suma))
    
    def resta(self):
        result_Resta= self.num1 - self.num2
        print("La resta del los numeros {} y {} es: {}".format(self.num1, self.num2, result_Resta))
    
    def multiplicacion(self):
        result_Multiplicacion= self.num1 * self.num2
        print("La multiplicación de los numeros {} y {} es de: {}".format(self.num1,self.num2,result_Multiplicacion))
                
    def division(self):
        total_Division=self.num1 / self.num2
        print("La division de los numeros es de: {}".format(total_Division))
        
class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1,numero2)
        
        
    def multiplicacion(self):
        Resultado= self.num2 * self.num1
        return Resultado
    
    def exponente(self,base,exponente):
        resultado=1
        for i in range(exponente):
            resultado*=base
        return resultado    

        

    def valorAbsoluto(sefl,numero):
        if numero >= 0:
            return numero
        else:

             numero = -numero
        return numero

    
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
cal=Calculadora(12,2)

cal.suma()
print('\n')
cal.resta()
print('\n')
cal.multiplicacion()
print('\n')
cal.division()
print('\n')
cal1=CalEstandar(8,1)

print('la multiplicacio es: ',cal1.multiplicacion())
print('\n')
print('el resultado del metodo_exponente es: ',cal1.exponente(2,5))
print('\n')
print('el valor absoluto es: ',cal1.valorAbsoluto(-4))
print('\n')
cal2 = calCientifica(2,2)
print('La circuferencia es: ',cal2.circunferencia())
print('\n')
print('El area del circulo es: ',cal2.areaCirculo())
print('\n')
print('area del cuadrado: ',cal2.areaCuadrado())    
    