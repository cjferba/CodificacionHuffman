STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_VIO  = 0x05
FOREGROUND_AMA  = 0x06
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

import ctypes
import math

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
    if len(list) < 2:
        return list
    middle = len(list) / 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)


def contador(lis):
    cont=0
    for w in range(len(lis)):
        if(str(type(lis[w]))=="<type 'list'>"):
            cont=contador(lis[w][:])+cont
        else:
            cont=cont+1
    return cont

def sublist(lis):
    l=[]
    for w in range(len(lis)):
        if(str(type(lis[w]))=="<type 'list'>"):
            l=l+sublist(lis[w][:])
        else:
            l.append(lis[w])
    return l

def codhuf(lista,alfa):
    #creacion de lista y la lista de listas
    liscod=[]#lista con los niveles del arbol
    cod=[]#variable para guardar los niveles
    aux2=[]#pares de las sumas de los arboles hijo
    a=[]#lista de las variables que metemos el el primer elemento del nodo
    aux=0
    b=0
    #metemos la lista de probablidades como hijos del arbol
    for z in range(len(lista)):
        cod.append([[z],lista[z][0]])
        cod.sort()
    #metemos primer nivel
    liscod.append(cod[:])
    for i in range(len(cod)-1):
        cod.sort()
        #si hay simbolos para cubiri nuestro alfabeto
        if len(cod)>=alfa:
            x=0
            while x<alfa:
                a.append(cod[x][0][:])
                b=b+cod[x][1]
                #print "a: "+str(a)+" b: "+str(b)
                x=x+1
            #print "a: "+str(a)
            aux2=[a,b]
            x=0
            while x<alfa:
                cod.pop(0)
                x=x+1
            x=0
        #solo nos queda 1 elemento
        elif len(cod)==1:
            #print "salida"
            break
        else:
            while x<len(cod):
                a.append(cod[x][0][:])
                b=b+cod[x][1]
                x=x+1
            x=0
            aux2=[a,b]
            while x<=len(cod):
                cod.pop(0)
                x=x+1
        cod.append(aux2)
        x=0
        b=0
        a=[]
        cod=mergesort(cod[:])
        liscod.append(cod[:])
        #print "codigo: "+str(cod)
    return liscod#[-1]
def log2(w):
	#print "elemento1: ",math.log(w),"Elemento2: -",math.log(2)
	return (math.log(w)/math.log(2.0))
	
def eficiencia(lista,cod,a):
	entropia=0
	n=0
	for i in(range(len(lista))):
		#print "lista: -",lista[i][0],"///log: -",log2(lista[i][0])
		entropia = entropia + lista[i][0] * log2(lista[i][0])
		n=n+lista[i][0]*len(cod[i])
	entropia=-entropia
	return entropia/(n * log2(a))
		
#**###############MAIN###############**#

#entrada de datos
color= (FOREGROUND_GREEN,FOREGROUND_BLUE,FOREGROUND_RED,FOREGROUND_VIO,FOREGROUND_AMA)
sim=['0','1','2','3','4','5','6','7','8','9']
set_color(FOREGROUND_VIO | FOREGROUND_INTENSITY)
alfabeto=int(raw_input("Introducir n digitos del alfabeto...([1-9])\n"))
while (alfabeto>0) and (alfabeto>9):
    set_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
    alfabeto=int(raw_input("Introducir n digitos del alfabeto...([1-9])\n"))
set_color(FOREGROUND_AMA | FOREGROUND_INTENSITY)
entrada=raw_input("Introducir texto a codificar...\n")
tam=len(entrada)
entrada=entrada.lower()
entrada1= entrada[:] 
lista=[]
entrada1=list(set(entrada))
tam1=len(entrada1)
#Problablidades
for i in range(tam1):
    cont=entrada.count(entrada1[i])
    lista.append([float(cont)/float(tam),entrada1[i]])
#ordenar lista
lista.sort()
codigo=[]
#print "lista",lista
codigo=codhuf(lista,alfabeto)
#for i in range(len(codigo)):
#print "codigo ",codigo

#el el primero puede que no sea asi
x=0
e=len(codigo[1])
l=[]
for i in range(len(codigo)):
    x=0
    if i<>0:
        #recorremos los nodos dentro de cada nivel
        while(x<e):
            #print "codigo ["+str(i)+"]["+str(x)+"][0]: "+ str(codigo[i][x][0])
            if contador(codigo[i][x][0]) <> 1:
                l.append(codigo[i][x][0])
                #recorremos los nodos por donde hemos pasado
                #for g in range(len(codigo[i][x][0])):
                    #print "  dentro"+str(codigo[i][x][0][g])
            x=x+1
        if(i<>len(codigo)-1):
            e=len(codigo[i+1])    
            #print str(i)+"e despues"+str(e)
x=len(l)
y=0
while y<x:
    aux=l.count(l[y])
    if aux>1:
        l.remove(l[y])
        x=len(l)
        y=0
    else:
        y=y+1
   
#print "esto es L: ",l
codificacion=[]
aux4=[]
l.reverse()
for z in range(len(lista)):
        codificacion.append('')
for i in range(len(l)):
    for c in range(len(l[i])):
        aux4=sublist([l[i][c]])
        #print "lista que le toca",l[i][c]
        for j in range(len(aux4)):
            #print "simbolo: ",sim[c]
            codificacion[aux4[j]]=codificacion[aux4[j]]+sim[c][:]
set_color(color[2] | FOREGROUND_INTENSITY)   
#print "codificacion: ",codificacion

huf=[]
tabla=[]
for i in range(len(lista)):
    huf.append(lista[i][1])
    tabla.append((lista[i][1],codificacion[i]))
set_color(color[3] | FOREGROUND_INTENSITY)
print "Codificacion: \n"+str(tabla)
#print "hufman total: "+str(huf)

x=0
salida =[]
sal=[]
for t in range(len(entrada)):
    x=entrada[t]
    aux4=huf.index(x)
    if x==' ':
        salida.append(sal)
        sal=[]
        salida.append(codificacion[aux4])
        sal=[]
    else:
        sal.append(codificacion[aux4])
salida.append(sal)
set_color(FOREGROUND_VIO | FOREGROUND_INTENSITY)
print "Codificacion Huffman:"
x=0
for u in range(len(salida)):
    set_color(color[x] | FOREGROUND_INTENSITY)
    if(str(type(salida[u]))<>"<type 'str'>"):
        for i in range(len(salida[u])):
            print str(salida[u][i])+" ",
    else:
        set_color(color[1])
        print str(salida[u])+" ",
        if x==0:
            x=2
        elif x==3:
            x=2
        elif x==2:
            x=0
        else:
            x=3
    
	set_color(color[x])
set_color(0x05)

print "\n\nDecodificacion\n",entrada
        
Eficiencia=eficiencia(lista,codificacion,alfabeto)
set_color(color[x])
print "\n\nEficiencia",Eficiencia
set_color(0x07)
a=raw_input("")



