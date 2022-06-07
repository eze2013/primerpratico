#creamos el titulo del programa y lo centramos

print(" Calculadora ISPC ".center(50,"*"))
#creamos el menu
print("""
..: Seleccione la Opcion Deseada del siguiente Menu :..
1 - Sumar
2 - Restar
3 - Multiplicar
4 - Dividir
5 - Salir
""")
# iniciamos un bloque try ("intenta") para capturar el error en 
# caso de que el usuario ingrese otra cosa que no sea un numero
try:    
    #solicitamos el numero de opcion a verificar
    opcion = int(input("ingresa la opcion deseada: "))
#en el exept solo se ingresara en caso de que hubiese un error al seleccionar una opcion
except Exception as e:
    #indicamos al usuario el error
    print("Error, opcion incorrecta, elije una opcion del Menu")
#ingresamos al bloque else solo si no hubo un error previo 
else:

    #con el bloque de condicionales ingresamos nuevamente a otro bloque try...
    if opcion == 1:
        
        try:
            #solicitamos los datos para la operacion de la opcion 1
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            num3 = float(input("Ingresa el tercer numero: "))
        except Exception as e:
            print("Error solo puedes digitar numeros!, vuelve a intentar")
        else:
            #realizamos la operacion
            resultado = num1 + num2 + num3
            #imprimimos con un "f" str ya que nos da la posibilidad de mostrar datos y 
            # variables de una forma mas prolija... la "\n" es para hacer un salto de linea.
            print(f"De la suma {num1} + {num2} + {num3} el resultado es : {resultado}\n")
    elif opcion == 2:
        try:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
        except Exception as e:
            print("Error solo puedes digitar numeros!, vuelve a intentar")
        else:
            resultado= num1 - num2  
            print(f"De la resta {num1} - {num2}  el resultado es : {resultado}\n")
    elif opcion == 3:
        # pide hacer la multiplicacion de 4 numeros asi que vamos ingresando los 4 
        try:
            num1 = float(input("ingresa tu primer numero a multiplicar: "))
            num2 = float(input("ingresa tu segundo numero: "))
            num3 = float(input("ingresa el tercer numero: "))
            num4 = float(input("ingresa el cuarto numero: "))
        except Exception as e:
            print("Error solo puede digitar numeros!, vuelve a intentar")
        else:
            resultado = num1 * num2 * num3 * num4 #la operacion
            print(f"De la multiplicacion {num1} * {num2} * {num3} * {num4} el resultado es : {resultado: .2f}\n")       

    elif opcion == 4:
        # pide hacer la división de 4 numeros asi que vamos ingresando los 4 
        try:
            num1 = float(input("ingresa tu primer numero a dividir: "))
            num2 = float(input("ingresa tu segundo numero: "))
            num3 = float(input("ingresa el tercer numero: "))
            num4 = float(input("ingresa el cuarto numero: "))
        except Exception as e:
            print("Error solo puede digitar números!, vuelve a intentar")
        else:
            resultado = num1 / num2 / num3 / num4 #la operacion
            print(f"De la división {num1} / {num2} / {num3} / {num4} el resultado es : {resultado:.2f}\n")
    elif opcion == 5:
        print("Terminando operacion, Saliendo....\n")

# como el bloque finally siempre se ejecuta lo utilizamos para saludar al terminar la operacion al usuario
finally:
    print("Gracias por utilizar nuestro programa...")
        

