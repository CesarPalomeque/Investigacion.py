class Cadena():
    def __init__(self,cadena):
        self.cadena=cadena
   
    def  recorrerCadena(self):
        print('\n')
        print("1.. Recorrer y presentar los datos de una cadena")
        print('\n')
        for i in self.cadena:
            print(i,'',end='')

    def  buscarCaracter(self,buscado):
        print('\n')
        print("2.. Buscar el carácter en la cadena")
        
        acum=0
        for j,i in enumerate(self.cadena):
            if i== buscado:
                acum=acum+1
        print("Su caracter se encuentra {} vez dentro de la cadena".format(acum))
        print("\n")

    def  listaPosiciones(self,caracter):
        print('\n')
        print("3... Retornar una lista con la posiciones dado un carácter de la cadena")
        print('\n')
        acum=0
        aux=[]
        for j,i in enumerate(self.cadena):
            acum=acum+1
            if i == caracter:
                aux.append(acum)
                lista=aux
        print(lista)        
                

    def listaPalabras(self):
        print('\n')
        print("4... Retornar una lista con todas las palabras de una cadena")
     
        print(self.cadena.split())
 
    def cadenaLista(self):
        print('\n')
        print("5... Retornar una cadena a partir de una lista")
        
        print(" ".join(self.cadena))

    def insertarDato(self,insertar,posicion):
        print('\n')
        print("6...Insertar un dato en una cadena dada lo Posición")
        
        if posicion <= len(self.cadena):
            izquierda = self.cadena[:posicion]
            derecha =self.cadena[posicion+1:]
            
            print("{} {} {}".format(izquierda, insertar, derecha))
        else:
            print("La posicion no existe")
        

    def eliminarOcurrencias(self,buscado):
        print('\n')
        print("7..Eliminar todas las ocurrencias en una cadena :) ")
        

        print("El elemento buscado se encontro {} veces en la cadena".format(self.cadena.count(buscado)))

    def retornaValor(self,posicion):
        print('\n')
        print("8.. Retornar cualquier valor de una cadena eliminándolo ")
        

        lista = []
        lista2 = []
        for pos, ele in enumerate (self.cadena):
            if pos == posicion:
                lista.append(self.cadena[pos])      
            else:
                lista2.append(self.cadena[pos])
        print("Se retorna la cadena de esta forma:")
        print(" ".join(lista2))     
        print("Letra de la posicion removido:")           
        print(" ".join(lista))

    def concatenarCadena(self,nombre):
        print('\n')
        print("9.. Concatenar Cadena")
        print('\n')
        dato = "Bienvenido al programa"
        final= "Gracias por usar el programa"
        frase= dato+" "+nombre+" "+final
        print(frase)


cadena='Las cosas salen mejor con DIOS de nuestro lado'
cad1= Cadena(cadena)
cad1.recorrerCadena()
cad1.buscarCaracter('m')
cad1.listaPosiciones('n')
cad1.listaPalabras()
cad1.cadenaLista()
cad1.insertarDato("Siempreeee",46)
cad1.eliminarOcurrencias("o")
cad1.retornaValor(26)
cad1.concatenarCadena("adorable usuario")