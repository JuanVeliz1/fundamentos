
opc = None
sushi1 = 4500
sushi2 = 5000
sushi3 = 5200
sushi4 = 4800
menuPrincipal = True
menuPedido = False
contSushi1 = 0
contSushi2 = 0
contSushi3 = 0
contSushi4 = 0
totalSushi1 = 0
totalSushi2 = 0
totalSushi3 = 0
totalSushi4 = 0
subTotal = 0
codigoDeDescuento = None
descuento = "soyotaku"
while True:
  if menuPrincipal :
    print(" bienvenido a nuestro sushi ")
    print("****************************")
    print(" ingrese que opcion desea \n" )
    print("1. menu")
    print("2. boleta")
    print("3. salir")
    try:
        opc = int(input("ingrese opcion del 1 al 3 \n"))
        if 1 <= opc <= 3:
          if opc == 1:
            print("bienvenido al menu")
            menuPedido = True
            menuPrincipal = False  
          elif opc == 2:
            print("esta es su boleta" )
            print("picachu roll", contSushi1 )
            print("otaku roll", contSushi2 )
            print("pulpo venenoso", contSushi3 )
            print("anguila electrica", contSushi4 )
            subTotal = (totalSushi1+totalSushi2+totalSushi3+totalSushi4)
            print("su subtotal es de ", subTotal )
            if codigoDeDescuento == descuento:
              descAplicado = subTotal * 0.10
              totalDescuento = subTotal - descAplicado
              print("el total del descuento fue de ", descAplicado)
              print ("el total se su boleta es de ", totalDescuento)
          elif opc == 3:
            print("escogio salir de la aplicacion")
            break
    except ValueError as errorOpcionMenu:
      print(" escoger una opcion valida de la opcion 1 a la 6 ")
  if menuPedido:
      print(" este es el menu de pedido")
      print("1. picachu roll $4.500")
      print("2. otaku roll $5.000")
      print("3. pulpo venenoso $5200")
      print("4. anguila electrica $4.800")
      print("5. ingrese cupon")
      print("6. volver al menu principal") 
      try:
        opcMenu = int(input("ingrese opcion a elegir \n"))  
        if 1 <= opcMenu <= 6 :
          if  opcMenu == 1:
            while True:
              numSushi1 = int(input("ingrese la cantidad que desea llevar "))
              if numSushi1 > 0:
                contSushi1 = contSushi1 * 1
                totalSushi1 = contSushi1 * sushi1
                break      
              else:
                print("la cantidad debe ser mayor a 0")      
          elif opcMenu == 2:
            while True: 
              numSushi2 = int(input("ingrese la canttidad que desea llevar "))
              if numSushi2 > 0: 
                contSushi2 = contSushi2 + 1
                totalSushi2 = contSushi2 * sushi2 
                break
              else:
                print("la cantidad debe ser mayor a 0")
          elif opcMenu == 3:
            while True: 
              numSushi3 = int(input("ingrese la canttidad que desea llevar "))
              if numSushi3 > 0: 
                contSushi3 = contSushi3 * 1
                totalSushi3 = contSushi3 * sushi3   
                break
              else:
                print("la cantidad debe ser mayor a 0")       
          elif opcMenu == 4:
            while True: 
                numSushi4 = int(input("ingrese la canttidad que desea llevar "))
                if numSushi4 > 0: 
                  contSushi4 = contSushi4 * 1
                  totalSushi4 = contSushi4 * sushi4
                  break
                else:
                  print("la cantidad debe ser mayor a 0")
          elif opcMenu == 5:
            codigoDeDescuento = input(" introdusca un codigo de descuento ") 
            if codigoDeDescuento == descuento:
              print(" codigo ingresado correctamente")
            else:
              if codigoDeDescuento != descuento:
                print(" codigo de descuento ingresado erroneamente")
          elif opcMenu == 6:
            print("volviendo al menu principal")
            print("***************************")
            menuPedido = False 
            menuPrincipal = True        
      except ValueError as errorOpcionMenu:
        print("ingrese una opcion del 1 a la opcion 6")

    




    