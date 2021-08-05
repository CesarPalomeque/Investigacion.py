class Basico:
    def __init__(self):
        pass
    
    def numerosN(self,n):
        for i in range(1,n+1):
            print(i)
            
    
    def multiplo(self, numero1, numero2):
        if numero1 % numero2 == 0:
            print("El numero {} si es multiplo de {}".format(numero1,numero2))
        else:
            print("El numero {} no es multiplo de {}".format(numero1,numero2))
            
    def divisoresNumero(self, numero):
        lista = []
        for i in range (1, numero+1):
            if numero % i == 0:
                lista.append(i)
        return lista
    
    def primo(self, numero):
        contador = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                contador += 1
        if contador == 2:
            print("Es un numero primo: ",numero)
        else:
            print("El numero {} No es un numero primo".format(numero),':´(')

    def perfecto(self, numero):
        acu=0
        for i in range(1, numero):
            if numero % i == 0:
                acu = acu+i
        if acu == numero:
            print("El Numero {} si es Perfecto".format(numero))
        else:
            print("El Numero {} no es perfecto".format(numero))
            
        
class Intermedio(Basico):
    def __init__(self):
        pass
        
    def numerosN(self,n):
        cont = 1
        suma = 0
        while n >= cont :
            suma = suma + cont
            cont += 1
        return suma
        # i = 1
        # while i <= n:
        #     print(i)
        #     i = i + 1
            
    def factorial(self,numero):
        resultado = 1
        for i in range(1, numero + 1):
            resultado = resultado * i
        return resultado
    
    
    def fibonacci(self,n):
        a,b = 0,1

        while a < n:
            print(a,end='')
            c = a+b
            a,b = b, a+b
            print('\n')
         
        
    def primosGemelos(self,numero1,numero2):
        a = 0
        if numero1 > 0 and numero2 > 0 and numero1 != numero2:
            if numero1 > numero2:
                numero1 ^= numero2
                numero2 ^= numero1
                numero1 ^= numero2
            for i in range (numero1, numero2+1):
                creciente = 2
                esPrimo = True
                
                while esPrimo and creciente < i:
                    if i % creciente == 0:
                        esPrimo = False
                    else:
                        creciente += 1
                if esPrimo and not a:
                    a = i
                elif esPrimo and a:
                    b = i
                    if b-a == 2:
                        print("{} y {} son numeros primos gemelos".format(a, b))
                        a=i
                    
        else:
            if numero1 == numero2:
                print("incorrecto los numeros son Iguales.")    
            else:
                print("Los numeros son incorrectos.")
                
    def amigos(self, numero1, numero2):
        acu1 = 0
        lista1 = []
        for i in range(1, numero1):
            if numero1 % i == 0:
                lista1.append(i)
                acu1 = acu1 + i
                
        acu2 = 0
        lista2 = []
        for x in range(1, numero2):
            if numero2 % x == 0:
                lista2.append(x)
                acu2 = acu2 + x
                
        if acu1 == numero2 and acu2 == numero1:
            print("Los numeros {} y {} son numeros amigos.".format(numero1, numero2))
        else:
            print("Los numeros {} y {} no son numeros amigos.".format(numero1, numero2))


# ope=Basico()
# print(ope.numerosN(53)) 
# print(ope.multiplo(6,6))  
# print(ope.divisoresNumero(54))
# print(ope.primo(6))
# print(ope.perfecto(6))
ope1=Intermedio()
print(ope1.numerosN(8))
# print(ope1.factorial(5))
# print(ope1.fibonacci(5))
# print(ope1.primosGemelos(3,5))
# print(ope1.amigos(220,284))

