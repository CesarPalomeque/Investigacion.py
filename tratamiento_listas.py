
class Tratamiento_Listas():
    
    def __init__(self,lista):
        self.lista=lista
        


    def presentarLista(self):
        print('Recorrer y presentar los datos de una lista')
        for list in self.lista:
            print(list,end="   ")
        print('\n') 

        
    
    def buscarLista(self,buscado):
        print("buscar un valor en una lista")
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:
           print("Su valor se encuentra en la lista, se encuentra en la posicion: {}".format(pos+1))
        else:
            print('Su valor no se encuentra en esta lista')

  
    
    def listaFactorial(self):
        print('Retornar una lista con los factoriales')
        for pos,i in enumerate(self.lista): 
            if i >= 0:
                acu=1
                for num in range(i,1,-1):
                    acu =acu*num
                print("numero:  {}  ,Factorial:  {} ".format(i,acu))
        print()           

 
    
    def listaPrimo(self):
        print('retornar una lista de números primos')
        listaprimo=[]
        for pos,i in enumerate(self.lista): 
            if i >= 0:
                primo=True
                divisor=2
                while divisor < i and primo ==True :
                    Res= i%divisor
                    if Res == 0:
                        primo+=1
                    divisor+=1
                if primo ==True:
                    listaprimo.append(i)
            else:
                print('su numero es negativo ')
        print()
        print('lista de numeros Primos: ')    
        print(listaprimo)

        


    
    def listaNotas(self,listaNotasDicccionario):
        print('Recorrer una lista de diccionario con notas')
        for nom in listaNotasDicccionario:
            for clave,valor in nom.items():
                print(clave,":",valor,end="  ")
            print()

  
    
    def insertarLista(self,valor,posicion):
        print('Insertar un dato en una Lista dada la Posición')
        print('\n')
        auxlista=[]        
        for posicion,ele in enumerate(self.lista):
            if valor < ele:
                break
        for i in range(posicion):
            auxlista.append(self.lista[i])
        auxlista.append(valor)

        for j in range(posicion,len(self.lista)):
            auxlista.append(self.lista[j])
        self.lista=auxlista
        return self.lista

  
    
    def eliminarLista(self,lista):
        print('Eliminar todos los elementos de la lista en la Lista')
        print('\n')
        lista2 = {}
        for i in lista:
            if i in lista2:
                lista2[i] += 1
            else:
                lista2[i] = 1 
        print("Queda lo siguiente:",lista2)
        print("En total son {} elementos sin contar las repeticiones".format(len(lista2)))
        lista3 = []        
        for clave,valor in enumerate(lista2):
            lista3.append(valor)
        return (lista3)   

        
  
    
    def retornaValorLista(self,lista):
        print(' Retornar valor de una lista eliminándolo ')
        print()
        n=int(input('Que valor vais a eliminar: '))      
        for j,i in enumerate(lista):
            if i == n:
                del lista[j]  
        return (lista)

  
    
    def copiarTuplaLista(self):
        print(' copiar cada elemento de una tupla en una lista ')
        aux1=list(self.lista)
        return aux1      

  
    
    def vueltoLista(self,listaClientesDiccionario):
        print(' dar el vuelto a varios clientes ')
        pago=float(input("Ingrese pago del cliente: "))
        nom=(input("Ingrese nombre del cliente: ")).capitalize()
        print(nom)
        for i in listaClientesDiccionario:
            for clave, valor in i.items():     
                if clave == nom:
                    if valor > 0:
                        cambio=pago-valor
                        print(cambio)
                    else:
                        cambio=pago
        if cambio <= -1:                
            print(" Mantiene una deuda de:",cambio,"$ con nosotros")
        else:
            print("su cambio es: ",cambio, "$ no tiene deuda con nosotros")  
  
 

lista=[5,4,3,2,1]
lista=(3,4,6,8,71,53)
listaClientesDiccionarios=[{'julio':6},{'cesar':25},{'hannah':11},{'jocabed':19},{'mishel':27},{'Emanuel':30}]
ord1= Tratamiento_Listas(lista)
ord1.presentarLista()
ord1.buscarLista(8)
ord1.listaFactorial()
ord1.listaPrimo()
ord1.listaNotas(listaClientesDiccionarios)
print(ord1.insertarLista(12,3))
print('\n')
lista1 = []       
num = int(input("Cuantos elementos desea en la lista: "))
for i in range(num):
    valor = int(input("Ingrese el elemento:")) 
    lista1.append(valor)
aux=lista1
print(ord1.eliminarLista(aux))
lista2 = []       
num = int(input("Cuantos elementos desea en la lista: "))
for i in range(num):
    valor = int(input("Ingrese el elemento: ")) 
    lista2.append(valor)
aux=lista2
print(ord1.retornaValorLista(aux))
print(ord1.copiarTuplaLista())
diccionario={}
lista=[]
num=int(input("ingrese cuantos diccionarios desea ingresar: "))
for i in range(num):
    clave=(input("ingrese su clave para el diccionario: ")).capitalize()
    valor=int(input("ingrese el valor de la clave para el diccionario: "))

    diccionario[clave]=valor
    lista.append(diccionario)
    diccionario={} 
ord1.vueltoLista(lista)
