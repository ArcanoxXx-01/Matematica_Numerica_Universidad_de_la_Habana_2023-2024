#==========EJERCICIO 3========================================================================================
#a)

def euler(n):return(1 + 1/n)**n
    
# print(euler(1000000000000000000))

# #R/ El valor de la parte izquierda se aproxima a uno ya que cuando 1/n sea menor que el epsilon de la
# # maquina se representara como 0 y (1+0)^n = 1.0  
# #b)
# print(euler(9007199254740992-1))
# print(euler(9007199254740992))
#R/ El menor N (de mi computadora) a partir del cual la funcion anterior da 1 es 9007199254740992
#R/ EL menor N que cumple para una aritmetica F=(b,p,m,M) seria el menor n<1/e donde e es el epsilon de dicha aritmnetica
#c)
#R/ Converge a 0.1000...e1 a partir del mismo n del inciso anterior

#============EJERCICIO 4======================================================================================

#fl(1 + n)=1 <=> 

#a) n < b^(k-p) (Truncamiento)
#b) n < b^(k-p)/2 (Aproximacion al flotante mas cercano)
#En este caso el espaciamiento es b^(1-p) que es igual al epsilon 

#============EJERCICIO 5=======================================================================================

#fl(b^n + x)=b^n 

#Sea d=b^{k-p} (El espaciamiento de b^n)=> d=b^{n-p} 
#a) x < d (Truncamiento)
#b) x < d/2 (Aproximacion al flotante mas cercano)

#============EJERCICIO 6======================================================================================

#F=(10,3,-5,5)

#R/ S1 = 1 ya que 1+0.001 = 0.100e1 + 0.100e-2 = 0.100e1 + 0.000e1 = 0.100e1 (pierde informacion)
# En cambio S2=2 ya que 0.001 + 0.001 = 0.100e-2 + 0.100e-2 = 0.200e-2 (no pierde informacion)

#============EJERCICIO 7====================================================================================== 

#R/ Para n=p ya que b^-n=0.100...e-p = 0.00... 

#============EJERCICIO 8======================================================================================

#R/ { (N,n)| N es natural && n >= p}

#=========Pregunta secreta (20 000)============================================================================

#R/ Oooh! Obviamente la antesala de "hasta que se seque el malecon" 8-)

#======Pregunta Secreta (35 000 creditos + 5000 por encontrarla)===============================================

#R/ El estandar IEEE-754 es la norma o estandar tecnico empleado para la computacion de punto flotante
#con el objetivo de evitar problemas existentes en las diveresas formas de imolementacion de punto flotante 
#que hacian que fueran poco fiables y no reutilizables.

#=======Ejercicio 9============================================================================================

#a)R/ Esto se debe a que en el estandar IEEE-754 como los numeros solo se pueden representar con una presicion finita
# por lo que muchos no se pueden guardar de manera exacta y se pierde informacion como pasa al sumar un numero muy grande 
# con otro que es muy pequeño en comparacion con el otro al punto que se podria considerar despresiable por lo que hay muchos
# casos en que la respuesta difiere grandemente del valor esperado como es el caso de 1e100 + 1e50 = 1e100 ya que 1e50 es tan 
# pequeño repecto a 1e100 que llega a ser despreciable 

# En b) y c) pasa algo parecido y es que como dijimos hay muchos numeros que no se pueden representar de manera exacta, por 
# lo que al realizar operaciones con estos los resultados tampoco van a dar exactos.Tambien puede darse el caso en que se opera 
# con dos numeros que si se pueden representar de manera exacta y sin envalgo el resultado puede que no se pueda

# ======EJERCICIO 10============================================================================================

# R/Como ya dijimos al operar con numeros que no se representan de manera exacta siempre existe una mayor perdida de informacion 
# en comparacion a si lo haecmos con numeros que si se representen de manera exacta donde es muy probable que no exista perdida de informacion
# o que si existe sea minima ,como es el caso del 30 que da el valor esperado sin perder infomacion

# ======EJERCICIO 11============================================================================================

def Pot(n):return n*n

def der(f,point,h):return (f(point+h)-f(point-h))/(2*h)

# print(der(Pot,1,30))
# print(der(Pot,1,1000000000000000000))
# print(der(Pot,1,0.5))
# print(der(Pot,1,0.125))

#R/Para todos los enteros que sean posibles de representar se puede hacer sin perder informacion, a demas existen numeros como 0.5 o 0.125 (hay infinitos numeros que cumplen) 

#======EJERCICIO 12==============================================================================================







