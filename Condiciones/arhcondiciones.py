#  Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
# valor del medio es 11. No use operadores lógicos

num1=int(input("Digite un número: "))
num2=int(input("Digite un número: "))
num3=int(input("Digite un número: "))

if num1>=num2>=num3: 
    print(f'El valor del medio es {num2}')
elif num2>=num3>=num1: 
    print(f'El valor del medio es {num3}')
elif num3>=num1>=num2: 
    print(f'El valor del medio es {num1}')
elif num2>=num1>=num3: 
    print(f'El valor del medio es {num1}')
elif num1>=num3>=num2: 
    print(f'El valor del medio es {num3}')
else: 
    print(f'El valor del medio es {num2}')

