import math
import matplotlib.pyplot as plt

#Ejercicio 3

#Iterativa
def Suma(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum

#Recursiva
def Factorial(n):
    if(n==1 or n==0):return 1
    return n*Factorial(n-1)

def Fib_Int(n):
    arr=[1,1]
    for i in range(2,n):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n-1]

def Fib_Float(n):
    arr=[1.0,1.0]
    for i in range(2,n):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n-1]

#A partir de 79 no dan iguales los fibonacci con entero y con float
# print (Fib_Int(79),Fib_Float(79))

#Ejercicio 4

def Derivar1(f,x,h):return (f(x+h)-f(x))/h

def Derivar2(f,x,h):return (f(x+h)-f(x-h))/(2*h)

##Ejemplo
#print(Derivar1(math.sin,0,0.00000000000000001))

def f(x):return x*x
    
#print(Derivar1(f,1,0.000000000001))
#print(Derivar1(f,1,1e-6))
# print(Derivar1(f,1,1e-15))
# print(Derivar1(f,1,1e-8))#Este fue el mas preciso
# print(Derivar1(f,1,1e-16))
# print(Derivar1(f,1,1e-14))
#print(Derivar1(f,1,1e-10))
# print(Derivar1(f,1,1e-9))
# print(Derivar1(f,1,1e-7))
# print(Derivar1(f,1,1e-0))
# print(Derivar1(f,1,1e-17))

#Ejercicio 5

def Taylor_e(x,h,n):
    result=0
    f=e(x)
    for i in range(n):
        result+=f*h**i/Factorial(i)
    return result

def e(x):return math.e**x

# #Prueba
# print(Taylor_e(0,1e-18,50))

def Taylor_sen(x,h,n):
    result=0
    for i in range(n):
        if(i%4==0):
            result+=math.sin(x)*h**i/Factorial(i)
        elif(i%4==1):
            result+=math.cos(x)*h**i/Factorial(i)
        elif(i%4==2):
            result+=-math.sin(x)*h**i/Factorial(i)
        else:
            result+=-math.cos(x)*h**i/Factorial(i)
    return result

##Prueba
# print(Taylor_sen(0,3.14/2,10))

def DerivarPol(exp,term,x,n):
    result=0
    for m in range(n):
        for i in range(len(exp)):
            if(exp[i]>=0):
                term[i]*=exp[i]
                exp[i]-=1
    for i in range(len(exp)):
        if(exp[i]>=0):
            result+=term[i]*x**exp[i]
    return result

# # Prueba
# exponentes=[5,3,2,0]
# terminos=[1,6,-4,5]
# print(DerivarPol(exponentes,terminos,1,3))
# print(DerivarPol(exponentes,terminos,1,0))

def Taylor_Pol(exp,ter,x,h,n):
    result=0
    for i in range(n):
        result+=DerivarPol(exp,ter,x,1)*h**i/Factorial(i)
    return result

##Prueba
# exponentes=[5,3,2,0]
# terminos=[1,6,-4,5]
# print(Taylor_Pol(exponentes,terminos,1,1,2))


##Ejercicio 6

def graficar(f,x,n):
    dom=[]
    img=[]
    for i in range(n):
        dom.append(x)
        img.append(f(x))
    plt.plot(dom,img)
    plt.show()
    return

graficar(Suma,0,10)

##Ejercicio 7

def f1(x):return x*x
def f2(x):return x*x*x

##Pruebas                ##Resultados
# print(Derivar1(f1,1,0.1))#2.100000000000002
# print(Derivar2(f1,1,0.1))#2.0000000000000004
# print(Derivar1(f2,1,0.1))#3.310000000000004
# print(Derivar2(f2,1,0.1))#3.0100000000000016

##Ejercicio 10
##a)
# print(Derivar2(f1,1,0.5))
# print(Derivar2(f1,1,0.1))

##b)
def funcion_identidad(x):
    for i in range(10):
        x = math.sqrt(x)
    for i in range(10):
        x = x*x
    return x

# print(funcion_identidad(0.3))

##c)

# a=1e83+1e83+1e83+1e83+1e83+1e83+1e100+1e83+1e83+1e83+1e83
# b=1e83+1e83+1e83+1e83+1e83+1e83+1e83+1e83+1e83+1e83+1e100
# print(a==b)



