class Menu_Principal:
    def __init__(self):
        pass
    def Principal_menu():
        print("1)calculadora")
        print("2) operaciones con numero")
        print("3)tratamientos de listas")
        print("4)Operaciones de cadenas")
        print("5)salir")
        opc=int(input("Elige una opción[1....5]: ") )

        if opc == "1":
            print("calculalo")
    # # class Calculadora:
    # #  def __init__(self, numero1, numero2):
    # #      self.num1=numero1=int(input("ingrese el primer numero: "))
        
    # #      self.num2=numero2=int(input("ingrese el segundo numero: "))

         

    # # def suma(self):
    # #     self.suma+=self.num1, self.num2
    # #     print('la suma es: '+str(self.suma))
    # # def resta(self):
    # #     self.resta-= self.num1, self.num2 
    # #     print('la resta es: '+str(self.resta))
    # # def mutiplicacion(self):
    # #     self.multiplicacion*=self.num1,self.num2
    # #     print('la multiplicacion es: '+str(self.multiplicacion))
    # # def división(self):
    # #     self.division/=self.num1,self.num2
    # #     print('la Division es: '+str(self.division))

    # # class calEstandar(Calculadora):
    # #             def __init__(self, numero1, numero2):
    # #              super().__init__()
    # # def mutiplicacion(self):mutiplicacion# aplicar polimorfismo
    # #     #print('5)la multiplicacion es')
    # # def exponente(base,Exponente):
    # #     resultado=1
    # #     for i in range(Exponente):
    # #         resultado*=base
    # #     return resultado
    # #     print(5**5)
    # #     print(pow(5,5))
    # #     print(exponente(self.num1,self.num2))
    # #      #print('6)el exponente es')
    # # def valorAbsoluto(numero):

    # #       #print('7)el valor absoluto es')


    # #       class calCientifica(Calculadora):
    # #        PI = 3.1416 
    # # def __init__(self, numero1, numero2):
    # #  super(self).__init__(numero1,numero2)
    # # def circunferencia(radio):
    # #     #print('8)la circuferencia es')
    # #     def areaCirculo(radio):
    # #      #print('9)El area es')
    # #      def areaCuadrado(lado):
    # #         #print('10)salir')
    # # #opccal=int(input("Elige una opción: ") )       
               
    #       print("2) operaciones con numero")
        elif opc == "2":
            print('operaciones con numereiss')       
    # # class Basico:
    # #      def  numerosN(n):
    # #       def multiplo(numero):
    # #        def DivisoresNumero(numero):
    # #         def primo(numero):
    # #          def perfecto(numero):

    # #           class Intermedio(Basico):
    # #            def numerosN(n): # aplicar polimorfismo....
    # #             def factorial(numero): # 
    # #              def fibonacci(n):
    # #               def primosGemelos(num1,num2):
    # #                def  amigos(num1,num2):
    #                   print("3)tratamientos de listas")
        elif opc == "3":
            print('tratamiento con listas')
                    # #   class Lista(Intermedio):
                    # #    def __init__(self, lista):
                    # #     def  presentarLista():
                    # #      def  buscarLista(valor):
                    # #       def  listaFactorial():
                    # #        def listaPrimo():
                    # #         def listaNotas(listaNotasDicccionario):
                    # #          def insertarLista(valor,posicion):
  
                    # #           def eliminarLista(valor):
                    # #            def retornaValorLista(posicion):
                    # #             def copiarTuplaLista(tupla):
                    # #              def vueltoLista(listaClientesDiccionario):
                    #               print("4)Operaciones de cadenas")
        elif opc == "4":
            print('cadenas de operaciones')
                                # #   class Cadena:
                                # #    def __init__(self, cadena):
                                # #     def  recorrerCadena():
                                # #      def  buscarCaracter(buscado):
                                # #       def  listaPosiciones(caracter):
                                # #        def listaPalabras():
                                # #         def cadenaLista():
                                # #          def insertarDato(buscado,posicion):
                                # #           def eliminarOcurrencias(buscado):
                                # #            def retornaValor(posicion):
                                # #             def concatenarCadena(dato):
                                #              print("5)salir")
        elif opc == "5":
            print('salirss')
        else:
            print('Opcion no validad')    
opc=int(input("Elige una opción[1....5]: ") )

Menu_Principal()

    