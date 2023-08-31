#Taller 1
def Taller1_punto1():
    cantidad=int(input("Cantidad de datos: "))
    c=1
    si_primo=0
    si_fibo=0
    while c<=cantidad:
        numero=int(input("Numero: "))
        c_2=1
        div=0
        while c_2<=numero:
            if numero%c_2==0:
                div+=1
            c_2+=1
        if div==2:
            si_primo+=1   
            if si_primo==1:
                primo_mayor=numero
            elif numero>primo_mayor:
                primo_mayor=numero

        a=0
        b=1
        t=0
        while t<numero:
            t=a+b
            a=b
            b=t
        if numero==t:
            si_fibo+=1
            if si_fibo==1:
                fibo_menor=numero
            elif numero<fibo_menor:
                fibo_menor=numero
        c+=1
    print("Primo mayor: ",primo_mayor,"Fibonacci menor: ",fibo_menor)
    if primo_mayor<fibo_menor:
        aux=fibo_menor
        fibo_menor=primo_mayor
        primo_mayor=aux

    suma_pares=0
    contar_pares=0
    c_3=fibo_menor+1
    print("Numeros pares entre estos dos datos: ")
    while c_3<primo_mayor:
        if c_3 % 2==0:
            print(c_3)
            suma_pares+=c_3
            contar_pares+=1
        c_3+=1

    if contar_pares>0:
        promedio=suma_pares/contar_pares
        print("Promedio de los numeros pares entre el primo mayor y el fibonacci menor: ",promedio)
    else:
        print("No hay numeros pares entre el primo mayor y el fibonacci menor")

def Taller1_punto2():
    cantidad=int(input("Cantidad de datos: "))
    c=1
    si_primo=0
    si_fibo=0
    while c<=cantidad:
        numero=int(input("Numero: "))
        c_2=1
        div=0
        while c_2<=numero:
            if numero%c_2==0:
                div+=1
            c_2+=1
        if div==2:
            si_primo+=1   
            if si_primo==1:
                primo_mayor=numero
            elif numero>primo_mayor:
                primo_mayor=numero

        a=0
        b=1
        t=0
        while t<numero:
            t=a+b
            a=b
            b=t
        if numero==t:
            si_fibo+=1
            if si_fibo==1:
                fibo_menor=numero
            elif numero<fibo_menor:
                fibo_menor=numero
        c+=1
    print("Primo mayor: ",primo_mayor,"Fibonacci menor: ",fibo_menor)
    if primo_mayor<fibo_menor:
        aux=fibo_menor
        fibo_menor=primo_mayor
        primo_mayor=aux

    suma_facrial=0
    contador_factorial=0
    c_2=fibo_menor+1
    while c_2<primo_mayor:
        if c_2 % 2!=0:
            c_1=c_2
            c_factorial=1
            while c_1>0:
                c_factorial*=c_1
                c_1-=1
            print("Numero impar: ",c_2,"Su factorial= ",c_factorial)    
            suma_facrial+=c_factorial
            contador_factorial+=1
        c_2+=1    
    if contador_factorial>0:
        promedio=suma_facrial/contador_factorial
        print("El promedio de estos factoriales= ",promedio)
    else:
        print("No hay impares entre el primo mayor y el fibonacci menor")                

def Taller1_punto3():
    cantidad=int(input("Cantida de edatos: "))
    c=1
    suma=0
    contador=0
    while c<=cantidad:
        numero=int(input("Numero: "))
        c_1=1
        div=0
        while c_1<=numero:
            if numero%c_1==0:
                div+=1
            c_1+=1

        a=0
        b=1
        t=0
        while t<numero:
            t=a+b
            a=b
            b=t
        if numero==t and div==2:
            print(numero,"Es fibonacci y primo a la vez")
            suma+=numero
            contador+=1
        c+=1

    if c>0:
        promedio=suma/contador
        print("Promedio de estos numeros= ",promedio)
    else:
        print("No hay numeros primos y fibonaccis a la vez")            

def Taller1_punto4():
    v=[]
    cantidad=int(input("Cantidad de datos: "))
    c=1
    si_primo=0
    while c<=cantidad:
        numero=int(input("Numero: "))
        v.append(numero)
        c_2=1
        div=0
        while c_2<=numero:
            if numero%c_2==0:
                div+=1
            c_2+=1
        if div==2:
            si_primo+=1
            if si_primo==2:
                segundo_primo=numero   
        c+=1
    if si_primo>0:
        veces_segundo_pri=0    
        for i in range(len(v)):
            if v[i]==segundo_primo:
                veces_segundo_pri+=1
        print("Segundo ptimo encontrado: ",segundo_primo,"Veces que se repite: ",veces_segundo_pri)         
    else:
        print("No se encontro el segundo primo en la cantidad de numeros")           
def Taller1_punto5():
    cantidad = int(input("Cantidad de ternas: "))
    contador_equilateros = 0
    contador_isosceles = 0
    contador_escalenos = 0
    suma_isosceles = 0
    
    for _ in range(cantidad):
        terna = [int(input(f"Lado {i+1}: ")) for i in range(3)]
        
        lados_iguales = len(set(terna))
        
        if lados_iguales == 1:
            contador_equilateros += 1
        elif lados_iguales == 2:
            contador_isosceles += 1
            suma_isosceles += sum(terna)
        else:
            contador_escalenos += 1
    
    print("Cantidad de triángulos equiláteros:", contador_equilateros)
    print("Cantidad de triángulos isósceles:", contador_isosceles)
    print("Cantidad de triángulos escalenos:", contador_escalenos)
    print("Suma de los triángulos isósceles:", suma_isosceles)

#Taller 2
def Taller2_Punto1():
    print("Ejercicio 1 (ordenar la mitad del vector en forma ascendente y la otra mitad de forma descendente)")
    cantidad_datos=int(input("Cantidad de datos= "))
    a=[]
    for i in range(cantidad_datos):
        a.append(int(input("Dato({})=".format(i))))

    i=0
    while i< (len(a)//2):
        Menor=a[i]
        pos_menor=i
        j=i+1
        while j< len(a)//2:
            if a[j]<Menor:
                Menor=a[j]
                pos_menor=j
            j+=1

        aux_0=a[i]
        a[i]=a[pos_menor]
        a[pos_menor]=aux_0
        i+=1

    i=len(a)//2
    while i < len(a)-1:
        mayor=a[i]
        pos_mayor=i
        j=i+1
        while j< len(a):
            if a[j]>mayor:
                mayor=a[j]
                pos_mayor=j
            j+=1

        aux_1=a[i]
        a[i]=a[pos_mayor]
        a[pos_mayor]=aux_1
        i+=1        

    for i in range(len(a)):
        print("Posicion: ",i,"Dato= ",a[i])

    print("Fin algoritmo")

def Taller2_Punto2():
    print("Ejercicio 2 (apartir de un vector formar otros dos, uno con los datos pares y otro con los primos, ordenarlos ascendente y descendente respectivamente)")
    cantidad_datos=int(input("Cantidad de datos= "))
    a=[]
    v_pares=[]
    v_primos=[]
    for i in range(cantidad_datos):
        a.append(int(input("Dato({})=".format(i))))

    for i in range(len(a)):
        if a[i]%2==0:
            print(a[i],"es par")
            dato_par= a[i] in v_pares
            if dato_par==False:
                v_pares.append(a[i])

    for i in range(len(a)):
        c=1
        div=0
        while c<=a[i]:
            if a[i]%c==0:
                div+=1
            c+=1

        if div==2:
            print(a[i],"Es primo")
            dato_primo= a[i] in v_primos
            if dato_primo== False:
                v_primos.append(a[i])

    for i in range(len(v_pares)-1):
        menor=v_pares[i]
        pos_menor=i
        j=i+1
        while j< len(v_pares):
            if v_pares[j]<menor:
                menor=v_pares[j]
                pos_menor=j
            j+=1

        aux_0=v_pares[i]
        v_pares[i]=v_pares[pos_menor]
        v_pares[pos_menor]=aux_0

    print("Vector con pares ordenado ascendentemente:",v_pares)
    for i in range(len(v_primos)-1):
        mayor=v_primos[i]
        pos_mayor=i
        j=i+1
        while j< len(v_primos):
            if v_primos[j]>mayor:
                mayor=v_primos[j]
                pos_mayor=j
            j+=1

        aux_1=v_primos[i]
        v_primos[i]=v_primos[pos_mayor]
        v_primos[pos_mayor]=aux_1

    print("Vector con primos ordenados descendentemente:",v_primos)
    print("Fin algoritmo")

def Taller2_Punto3():
    print("Ejercicio 3(Se tiene vector con datos numericos ordenados y repetidos, mostrar los numeros y veces que se repiten, utilizar rompimiento de control)")
    cantidad_datos=int(input("Cantidad de datos= "))
    a=[]
    for i in range(cantidad_datos):
        a.append(int(input("Dato({})=".format(i))))

    aux=a[0]
    i=0
    while i < cantidad_datos:
        contador=0
        while i < cantidad_datos and a[i]==aux:
            contador+=1
            i+=1    

        if contador==1:
            print("Dato: ",aux,"Se repite= ",contador,"vez")
        else:
            print("Dato: ",aux,"Se repite= ",contador,"veces")
                
        if i < cantidad_datos:
            aux=a[i] 

    print("Fin algoritmo")

def Taller2_Punto4():
    print("Ejercicio 4 (Se tienen dos vectores, el primero determina el rango de datos que tendrá el segundo vector)")
    datos = []
    rango = []
    cantidad_datos_rango = int(input("Cantidad de datos de la lista de rango: "))
    cantidad_datos_lista = int(input("Cantidad de elementos de la lista datos: "))

    for i in range(cantidad_datos_rango):
        rango.append(int(input("Digitar valor rango({})=".format(i))))

    for j in range(cantidad_datos_lista):
        datos.append(int(input("Digitar valor dato({})=".format(j))))

    i = 0
    c = 0

    while i < cantidad_datos_rango:
        limite_final = c + rango[i]-1  # Usamos c como inicio del rango
        mayor = datos[c]
        menor = datos[c]
        contador = 0
        sumador = 0
        while c < limite_final:  # Usamos c para iterar sobre los datos del rango
            contador += 1
            sumador += datos[c]
            if datos[c] > mayor:
                mayor = datos[c]
            elif datos[c] < menor:
                menor = datos[c]
            c += 1  # Incrementamos c
        
        promedio = sumador / contador  # Cálculo del promedio fuera del bucle interno
        print("Rango", i, "Mayor:", mayor, "Menor:", menor, "Promedio del rango:", promedio)
        i += 1

    print("Fin algoritmo")


def Taller2_Punto5():
    print("Ejercicio 5 (Se tienen dos vectores, forman un tercero con los primos comunes sin repetirse)")
    a=[]
    v=[]
    p=[]
    cantidad_datosA=int(input("Cantidad de datos en vector a="))
    for i in range(cantidad_datosA):
        a.append(int(input("Dato({})=".format(i))))

    cantidad_datosB=int(input("Cantidad de datos en vector b="))
    for j in range(cantidad_datosB):
        v.append(int(input("Dato({})=".format(j))))

    for i in range(cantidad_datosA):
        c=1
        div=0
        while c<=a[i]:
            if a[i]%c==0:
                div+=1
            c+=1

        if div==2:
            dato= a[i] in v
            if dato== True:
                print(a[i],"Es primo comun")
                dato_2= a[i] in p
                if dato_2==False:
                    p.append(a[i])

    print("Vector con primos comunes sin repetirse:",p)
    print("Fin algoritmo")

def Taller2_Punto6():
    print("Ejercicio 6 (Se tienen dos vectores, formar un tercero con la union de los fibonaccis sin repetirse)")
    a=[]
    v=[]
    p=[]
    cantidad_datosA=int(input("Cantidad de datos en vector a="))
    for i in range(cantidad_datosA):
        a.append(int(input("Dato({})=".format(i))))

    cantidad_datosB=int(input("Cantidad de datos en vector b="))
    for j in range(cantidad_datosB):
        v.append(int(input("Dato({})=".format(j))))

    contador=0
    for i in range(cantidad_datosA):
        a_1=0
        b=1
        t=0
        while t<a[i]:
            t=a_1+b
            a_1=b
            b=t
            
        if a[i]==t:
            print(a[i],"Es fibonacci")
            dato= a[i] in p
            if dato== False:
                p.append(a[i])

    for j in range(cantidad_datosB):
        a_1=0
        b=1
        t=0
        while t<v[j]:
            t=a_1+b
            a_1=b
            b=t

        if v[j]==t:
            print(v[j],"Es fibonacci")
            dato_2= v[j] in p
            if dato_2== False:
                p.append(v[j])    

    print("Vector con la union de fibonaccis sin repetirse:",p)
    print("Fin algoritmo")

def Taller2_Punto7():
    print("Ejercicio 7 (Se tienen dos vectores, crear un tercer vecotor de forma descendente organizado por mezcla)")
    cantidad_datosA = int(input("Cantidad de datos en vector a= "))
    print("Vector ordenado ascendentemente")
    a = []
    for i in range(cantidad_datosA):
        a.append(int(input("Dato({})=".format(i))))

    cantidad_datosB = int(input("Cantidad de datos en vector b= "))
    print("Vector ordenado descendentemente")
    v = []
    for j in range(cantidad_datosB):
        v.append(int(input("Dato({})=".format(j))))

    p = []
    i = 0
    j = cantidad_datosB-1

    while i < cantidad_datosA and j >= 0:
        if v[j] < a[i]:
            p.append(v[j])
            j -= 1
        else:
            p.append(a[i])
            i += 1

    while j>=0:
        p.append(v[j])
        j-=1

    while i<cantidad_datosA:
        p.append(a[i])
        i+=1

    for x in range(len(p)-1):
        c=x+1
        mayor=p[x]
        pos=x
        while c<len(p):
            if p[c]>mayor:
                mayor=p[c]
                pos=c
            c+=1

        aux=p[x]
        p[x]=p[pos]
        p[pos]=aux

    print(p)
    print("Fin algoritmo")

def Taller2_Punto8():
    print("Ejercicio 8 (Se tienen dos vectores, crear un tercer vecotor de forma descendente organizado por mezcla)")
    cantidad_datosA = int(input("Cantidad de datos en vector a= "))
    print("Vector ordenado ascendentemente")
    a = []
    for i in range(cantidad_datosA):
        a.append(int(input("Dato({})=".format(i))))

    cantidad_datosB = int(input("Cantidad de datos en vector b= "))
    print("Vector ordenado descendentemente")
    v = []
    for j in range(cantidad_datosB):
        v.append(int(input("Dato({})=".format(j))))

    p = []
    i = 0
    j = cantidad_datosB-1

    while i < cantidad_datosA and j >= 0:
        if v[j] < a[i]:
            if v[j]%2==0:
                p.append(v[j])
            j -= 1
        else:
            if a[i]%2==0:
                p.append(a[i])
            i += 1

    while j>=0:
        if v[j]%2==0:
            p.append(v[j])
        j-=1

    while i<cantidad_datosA:
        if a[i]%2==0:
            p.append(a[i])
        i+=1

    for x in range(len(p)-1):
        c=x+1
        mayor=p[x]
        pos=x
        while c<len(p):
            if p[c]>mayor:
                mayor=p[c]
                pos=c
            c+=1

        aux=p[x]
        p[x]=p[pos]
        p[pos]=aux

    print(p)
    print("Fin algoritmo")

def Taller2_Punto9():
    print("Ejercicio 9 (Se tiene un vector con datos fibonaccis, formar un tercer vector con los primos entre el fibonacci menor y mayor)")
    cantidad_datos=int(input("cantidad de datos= "))
    a=[]
    v=[]
    for i in range(cantidad_datos):
        a.append(int(input("Dato({})=".format(i))))

    sifibo=0
    for i in range(cantidad_datos):
        a_1=0
        b=1
        t=0
        while t<a[i]:
            t=a_1+b
            a_1=b
            b=t

        if a[i]==t:
            sifibo+=1 
            if sifibo==1:
                fibo_menor=a[i]
                fibo_mayor=a[i]
            else:
                if a[i]<fibo_menor:
                    fibo_menor=a[i]
                elif a[i]>fibo_mayor:
                    fibo_mayor=a[i]

    print("Fibonacci menor:",fibo_menor)
    print("Fibonacci mayor:",fibo_mayor)
    print("Numeros primos entre estos fibonaccis:")
    c=fibo_menor+1
    while c<fibo_mayor:
        c_2=1
        div=0
        while c_2<=c:
            if c%c_2==0:
                div+=1
            c_2+=1

        if div==2:
            print(c)
            dato=c in v
            if dato==False:
                v.append(c)

        c+=1            

    print("Vector con numeros primos entre fibpnacci mayor y menor:",v)
    print("Fin algoritmo")

def Taller2_Punto10():
    print("Ejercicio 10 (Encontrar segundo y tercer fibonacci, sus posiciones...)")
    cantidad_datos=int(input("cantidad de datos= "))
    a=[]
    v=[]
    for i in range(cantidad_datos):
        a.append(int(input("Dato({})=".format(i))))

    sifibo=0
    for i in range(cantidad_datos):
        a_1=0
        b=1
        t=0
        while t<a[i]:
            t=a_1+b
            a_1=b
            b=t

        if a[i]==t:
            sifibo+=1 
            if sifibo==2:
                pos_segundo=i
                fibo_segundo=a[i]
            else:
                if sifibo==3:
                    pos_tercero=i
                    fibo_tercero=a[i]
                    
    print("Segundo fibonacci:",fibo_segundo,"Su posicion es:",pos_segundo)
    print("Tercer fibonacci:",fibo_tercero,"Su posicion es:",pos_tercero)
    if fibo_segundo<fibo_tercero:
        fibo_menor=fibo_segundo
    elif fibo_segundo>fibo_tercero:
        fibo_menor=fibo_tercero
    elif fibo_segundo==fibo_tercero:
        fibo_menor=fibo_segundo

    c=fibo_menor
    factorial=1
    while c>=1:
        factorial=factorial*c
        c-=1

    print("El fibonacci menor es:",fibo_menor,"su factorial es:",factorial)
    print("Posiciones entre el segundo y terces fibonaccis reemplazados por el factorial:")
    i=pos_segundo
    while i<=pos_tercero:
        print("Posicion:",i,"Dato:",factorial)
        i+=1

    print("Fin algoritmo")

#TALER 3
def Taller3_Punto1():
    print("Punto 1 (Se tiene una matriz cuadrada, formar un vector con los primos de la diagonal principal y los primos de la diagonal secundaria)")
    dimension=int(input("Numero de filas y columnas: "))
    matriz=[]
    for i in range(dimension):
        fila=[]
        for j in range(dimension):
            fila.append(int((input(f'Dato({i},{j})= '))))

        matriz.append(fila)    

    v_primos_dprincipal=[]
    v_primos_dsecundaria=[]
    for i in range(dimension):
        for j in range(dimension):
            if i==j:
                c=1
                div=0
                while c<= matriz[i][j]:
                    if matriz[i][j] % c==0:
                        div+=1
                    c+=1

                if div==2:
                    print("Primo de diagonal principal: ",matriz[i][j])
                    v_primos_dprincipal.append(matriz[i][j])

    for i in range(dimension):
        for j in range(dimension):
            if i+j==dimension-1:
                c=1
                div=0
                while c<= matriz[i][j]:
                    if matriz[i][j] % c==0:
                        div+=1
                    c+=1

                if div==2:
                    print("Primo de diagonal secundaria: ",matriz[i][j])
                    v_primos_dsecundaria.append(matriz[i][j])

    print("Vector con los primos de la diagonal principal: ",v_primos_dprincipal)
    print("Vector con los primos de la diagonal secundaria: ",v_primos_dsecundaria)

def Taller3_Punto2():
    print("Punto 2 (Se tiene una matriz cuadrada con datos numéricos, Comparar el promedio de los números pares que están sobre la diagonal principal)")
    dimension=int(input("Numero de filas y columnas: "))
    matriz=[]
    for i in range(dimension):
        fila=[]
        for j in range(dimension):
            fila.append(int((input(f'Dato({i},{j})= '))))

        matriz.append(fila) 

    sum_pares = 0
    count_pares = 0
    sum_impares = 0
    count_impares = 0

    for i in range(dimension):
        for j in range(dimension):
            if i < j and matriz[i][j] % 2 == 0:
                sum_pares += matriz[i][j]
                count_pares += 1

    for i in range(dimension):
        for j in range(dimension):
            if i > j and matriz[i][j] % 2 != 0:
                sum_impares += matriz[i][j]
                count_impares += 1

    if count_pares > 0:
        promedio_pares = sum_pares / count_pares
    else:
        promedio_pares = 0
        print("No hay números pares sobre la diagonal principal.")

    if count_impares > 0:
        promedio_impares = sum_impares / count_impares
    else:
        promedio_impares = 0
        print("No hay números impares bajo la diagonal principal.")

    if promedio_pares > 0 and promedio_impares > 0:
        if promedio_pares > promedio_impares:
            print(f"El promedio de los números pares sobre la diagonal principal ({promedio_pares}) es mayor que el promedio de los números impares bajo la diagonal principal ({promedio_impares}).")
        elif promedio_impares > promedio_pares:
            print(f"El promedio de los números impares bajo la diagonal principal ({promedio_impares}) es mayor que el promedio de los números pares sobre la diagonal principal ({promedio_pares}).")
        else:
            print("Los promedios son iguales.")

def Taller3_Punto3():
    print("punto 3 (Determinar si el segundo primo es consecutivo con el cuarto primo al recorrer la matriz por COLUMNAS)")
    matriz=[]
    filas=int(input("Numero de filas= "))
    columnas=int(input("Numero de columnas= "))

    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})=')))

        matriz.append(fila)

    print(matriz)
    si_primo=0
    print("Primos encontrados al recorrer matriz por COLUMNAS: ")
    for j in range(columnas):
        for i in range(filas):
            c=1
            div=0
            while c<=matriz[i][j]:
                if matriz[i][j] % c==0:
                    div+=1
                c+=1

            if div==2:
                si_primo+=1
                if si_primo==2:
                    segundo_primo=matriz[i][j]
                    print("Segundo primo: ",matriz[i][j])
                    print("Ubicado en la columna: ",j)
                    print("Fila: ",i) 
                elif si_primo==4:
                    cuarto_primo=matriz[i][j]
                    print("Cuarto primo: ",matriz[i][j])
                    print("Ubicado en la columna: ",j)
                    print("Fila: ",i)

    if cuarto_primo<segundo_primo:
        aux=segundo_primo
        segundo_primo=cuarto_primo
        cuarto_primo=aux

    c_remplazo=segundo_primo+1
    b=0
    while c_remplazo < cuarto_primo and b==0:
        c_2=1
        div=0
        while c_2<=c_remplazo:
            if c_remplazo % c_2==0:
                div+=1
            c_2+=1

        if div==2:
            b+=1
        else:
            c_remplazo+=1            

    if b==0:
        print("El segundo y cuarto primo son consecutivos ya que no hay ningun primo entre estos")
    else:
        print("El segundo primo y el cuarto primo No son consecutivos ya que en estos hay numeros primos")


def Taller3_Punto4():
    print("Punto 4 (Ordenar las columas pares de forma ascendente y las impares de forma descendente)")
    matriz = []
    filas = int(input("Numero de filas: "))
    columnas = int(input("Numero de columnas: "))

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})=')))
        matriz.append(fila)

    print("Matriz original:")
    for i in range(filas):
        for j in range(columnas):
            print("Fila: ",i," Columna: ",j," Dato= ",matriz[i][j])

    for j in range(columnas):
        if j % 2 == 0:  # Columnas pares
            for i in range(filas - 1):
                for k in range(i + 1, filas):
                    if matriz[k][j] < matriz[i][j]:
                        aux = matriz[i][j]
                        matriz[i][j] = matriz[k][j]
                        matriz[k][j] = aux
        else:  # Columnas impares
            for i in range(filas - 1):
                for k in range(i + 1, filas):
                    if matriz[k][j] > matriz[i][j]:
                        aux = matriz[i][j]
                        matriz[i][j] = matriz[k][j]
                        matriz[k][j] = aux

    print("Matriz ordenada en columnas pares ascendentes y columnas impares descendentes:")
    for i in range(filas):
        for j in range(columnas):
            print("Fila: ",i," Columna: ",j," Dato= ",matriz[i][j])

def Taller3_Punto5():
    print("Punto 5 (dos matrices ordenadas ascendentemente, obtener un vector ordenado ascendentemente por mezcla )")
    matriz_1 = []
    matriz_2 = []
    vector = []

    filas_1 = int(input("Filas en matriz 1: "))
    columnas_1 = int(input("Columnas en matriz : "))
    print("Digite los datos de la matriz 1 en orden ascendente: ")
    for i in range(filas_1):
        fila_1 = []
        for j in range(columnas_1):
            fila_1.append(int(input(f'Dato({i},{j})= ')))
        matriz_1.append(fila_1)

    filas_2 = int(input("Filas en matriz 2: "))
    columnas_2 = int(input("Columnas en matriz 2: "))
    print("Digite los datos de la matriz 2 en orden ascendente: ")
    for i in range(filas_2):
        fila_2 = []
        for j in range(columnas_2):
            fila_2.append(int(input(f'Dato({i},{j})= ')))
        matriz_2.append(fila_2)

    print("Matriz 1: ", matriz_1, " Matriz 2: ", matriz_2)

    i = 0  # filas matriz 1
    j = 0  # columnas matriz 1
    z = 0  # filas matriz 2
    x = 0  # columnas matriz 2

    while i < filas_1 or z < filas_2:
        if i == filas_1:
            vector += matriz_2[z][x:]
            break
        elif z == filas_2:
            vector += matriz_1[i][j:]
            break
        elif matriz_1[i][j] < matriz_2[z][x]:
            vector.append(matriz_1[i][j])
            j += 1
            if j == columnas_1:
                j = 0
                i += 1
        else:
            vector.append(matriz_2[z][x])
            x += 1
            if x == columnas_2:
                x = 0
                z += 1

    print("Vector ordenado por mezcla: ", vector)

def Taller3_Punto6():
    print("Punto 6 (Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila)")
    matriz_1 = []
    filas_1 = int(input("Filas en matriz 1: "))
    columnas_1 = int(input("Columnas en matriz : "))
    print("Digite los datos de la matriz 1 en orden ascendente: ")
    for i in range(filas_1):
        fila_1 = []
        for j in range(columnas_1):
            fila_1.append(int(input(f'Dato({i},{j})= ')))
        matriz_1.append(fila_1)

    print("Matriz original:")
    for fila in matriz_1: #me saca la matriz de una forma mas lejible, como uma matriz en papel
        print(fila)

    promedios = []
    for i in range(filas_1):
        suma = sum(matriz_1[i])
        promedio = suma / columnas_1
        print("promedio fila ",i," = ",promedio)
        promedios.append(promedio)

    for i in range(filas_1 - 1):
        for j in range(i + 1, filas_1):
            if promedios[i] > promedios[j]:
                matriz_1[i], matriz_1[j] = matriz_1[j], matriz_1[i]
                promedios[i], promedios[j] = promedios[j], promedios[i]

    print("Matriz con filas intercambiadas por promedios ascendentes:")
    for fila in matriz_1:
        print(fila)

#######  Punto 7
def leer_matriz():
    matriz=[]
    cantidad=int(input("Numero de filas * columnas: "))
    for i in range(cantidad):
        fila=[]
        for j in range(cantidad):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)
    print("Matriz original:")    
    for fila in matriz:
        print(fila)
    return matriz

def promedio_diagonal_principal_secundaria():
    print(">Subprograma  Promedio de la diagonal principal y secundaria<")
    valor_1=leer_matriz()
    suma=0
    contador=0
    print("Datos de la diagonal principal: ")
    for i in range(len(valor_1)):
        for j in range(len(valor_1[i])):
            if i == j:
                print(valor_1[i][j])
                suma+=valor_1[i][j]
                contador+=1

    promedio_1=suma/contador
    print("Promedio de la diagonal principal: ",promedio_1)

    suma=0
    contador=0
    print("Datos de la diagonal secundaria: ")
    for i in range(len(valor_1)):
        for j in range(len(valor_1[i])):
            if i+j==len(valor_1)-1:
                print(valor_1[i][j])
                suma+=valor_1[i][j]
                contador+=1

    promedio_2=suma/contador
    print("Promedio de la diagonal secundaria: ",promedio_2)           

def orden_diagonal_principal():
    print(">Subprograma diagonal principal unicamente<")
    valor_2=leer_matriz()
    for i in range(len(valor_2)-1):
        for j in range(i+1,len(valor_2)):
            if valor_2[j][j]<valor_2[i][i]:
                aux=valor_2[i][i]
                valor_2[i][i]=valor_2[j][j]
                valor_2[j][j]=aux
    print("Orden de la diagonal principal: ")
    for fila in valor_2:
        print(fila)   

def promedio_encima_diagonales():
    print(">Subprograma promedio por encima de las diagonales<")
    matriz=leer_matriz()
    suma_pares = 0
    contador_pares = 0
    suma_impares = 0
    contador_impares = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i:  # Por encima de la diagonal principal
                if matriz[i][j] % 2 == 0:  # Número par
                    suma_pares += matriz[i][j]
                    contador_pares += 1
            if i + j < len(matriz) - 1:  # Por encima de la diagonal secundaria
                if matriz[i][j] % 2 != 0:  # Número impar
                    suma_impares += matriz[i][j]
                    contador_impares += 1
    
    if contador_pares > 0:
        promedio_pares = suma_pares / contador_pares
        print("Promedio de los pares encima de la diagonal principal:", promedio_pares)
    else:
        print("No hay números pares encima de la diagonal principal.")
    
    if contador_impares > 0:
        promedio_impares = suma_impares / contador_impares
        print("Promedio de los impares encima de la diagonal secundaria:", promedio_impares)
    else:
        print("No hay números impares encima de la diagonal secundaria.")

def relllenar_diagonales():
    print(">Subprograma rellenar las diagonales<")
    matriz=leer_matriz()
    si_primo=0
    si_fibonacci=0
    si_par=0
    si_impar=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            div=0
            c=1
            while c<=matriz[i][j]:
                if matriz[i][j]%c==0:
                    div+=1
                c+=1
            if div==2:
                si_primo+=1
                if si_primo==1:
                    primo_menor=matriz[i][j]
                elif matriz[i][j]<primo_menor:
                    primo_menor=matriz[i][j]
            a=0
            b=1
            t=0
            while t<matriz[i][j]:
                t=a+b
                a=b
                b=t
            if matriz[i][j]==t:
                si_fibonacci+=1
                if si_fibonacci==1:
                    fibonacci_mayor=matriz[i][j]
                elif matriz[i][j]>fibonacci_mayor:
                    fibonacci_mayor=matriz[i][j]

            if matriz[i][j] % 2==0:
                si_par+=1
                if si_par==1:
                    par_mayor=matriz[i][j]
                elif matriz[i][j]>par_mayor:
                    par_mayor=matriz[i][j]
            else:
                si_impar+=1
                if si_impar==1:
                    impar_menor=matriz[i][j]
                elif matriz[i][j]<impar_menor:
                    impar_menor=matriz[i][j]

    print("Primo menor de la matriz: ",primo_menor," Fibonacci mayor de la matriz: ",fibonacci_mayor)
    print("Diagonales reemplazadas por los anteriores datos: ")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i==j:
                matriz[i][j]=primo_menor
            elif i+j==len(matriz)-1:
                matriz[i][j]=fibonacci_mayor
    for fila in matriz:
        print(fila)
    return par_mayor,impar_menor                

def llenar_contorno_interior():
    print(">Subprograma llenar el contorno de la matriz y la parte interior<")
    matriz=leer_matriz()
    par_mayor,impar_menor=relllenar_diagonales()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0 or i == len(matriz) - 1 or j == 0 or j == len(matriz[i]) - 1:
                matriz[i][j] = par_mayor
            else:
                matriz[i][j] = impar_menor

    print("Matriz con contorno de par_mayor y parte interna de impar_menor:")
    for fila in matriz:
        print(fila)
####punto 8
def leer_dos_matrices():
    matriz_1 = []
    matriz_2 = []

    filas_1 = int(input("Filas en matriz 1: "))
    columnas_1 = int(input("Columnas en matriz 1: "))
    print("Digite los datos de la matriz 1 en orden ascendente: ")
    for i in range(filas_1):
        fila_1 = []
        for j in range(columnas_1):
            fila_1.append(int(input(f'Dato({i},{j})= ')))
        matriz_1.append(fila_1)

    print("Matriz 1: ")
    for fila in matriz_1:
        print(fila)  

    filas_2 = int(input("Filas en matriz 2: "))
    columnas_2 = int(input("Columnas en matriz 2: "))
    print("Digite los datos de la matriz 2 en orden ascendente: ")
    for i in range(filas_2):
        fila_2 = []
        for j in range(columnas_2):
            fila_2.append(int(input(f'Dato({i},{j})= ')))
        matriz_2.append(fila_2)
    
    print("Matriz 2: ")
    for fila in matriz_2:
        print(fila)

    return matriz_1, matriz_2

def vector_elementos_comunes():
    print(">Subprograma vector con los elementos comunes<")
    matriz_1,matriz_2=leer_dos_matrices()
    vector = []
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            dato = matriz_1[i][j] in matriz_2[i]
            if dato==True:
                print(matriz_1[i][j], "Dato en común en su respectiva fila")
                dato_2 = matriz_1[i][j] in vector
                if not dato_2:
                    vector.append(matriz_1[i][j])

    print("Vector resultante con los datos comunes sin repetir: ", vector)
    return vector

def vector_primos_comunes():
    print(">Subprograma vector con los primos comunes<")
    matriz_1,matriz_2=leer_dos_matrices()
    vector_2=[]
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            c=1
            div=0
            while c<=matriz_1[i][j]:
                if matriz_1[i][j] % c==0:
                    div+=1
                c+=1
            if div==2:
                dato= matriz_1[i][j] in matriz_2[i]
                if dato==False:
                    print(matriz_1[i][j],"Es primo no comun en su respectiva fila")
                    dato_2= matriz_1[i][j] in vector_2
                    if dato_2==False:
                        vector_2.append(matriz_1[i][j]) 

    for i in range(len(matriz_2)):
        for j in range(len(matriz_2[i])):
            c=1
            div=0
            while c<=matriz_2[i][j]:
                if matriz_2[i][j] % c==0:
                    div+=1
                c+=1
            if div==2:
                dato= matriz_2[i][j] in matriz_1[i]
                if dato==False:
                    print(matriz_2[i][j],"Es primo no comun en su respectiva fila")
                    dato_2= matriz_2[i][j] in vector_2
                    if dato_2==False:
                        vector_2.append(matriz_2[i][j])

    print("Vector resultante con los primos NO comunes sin repetir: ",vector_2)
    return vector_2

def Taller3_Punto9():
    print("Punto 9 (Formar un vector con aquellos contadores de datos que se repiten y que sean numeros fibonaccis, sin repetidos)")
    matriz=[]
    filas=int(input("Numero de filas: "))
    columnas=int(input("Numero de columnas: "))
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila) 

    datos_no_repetidos=[]
    contador=[]
    print(matriz)
    for i in range(filas):
        for j in range(columnas):
            aux=matriz[i][j]
            if aux not in datos_no_repetidos:
                datos_no_repetidos.append(aux)
                contador.append(1)
            else:
                contador[datos_no_repetidos.index(aux)]+=1

    for i in range(len(contador)):
        print("Dato: ",datos_no_repetidos[i]," Veces: ",contador[i])  

    vector_contador=[]
    for i in range(len(contador)):
        if contador[i]>1:
            a=0
            b=1
            t=0
            while t<contador[i]:
                t=a+b
                a=b
                b=t

            if contador[i]==t:
                print(contador[i],"es fibonacci")
                dato= contador[i] in vector_contador
                if dato==False:
                    vector_contador.append(contador[i])

    print("Vector con los contadores fibonaccis de los datos repetidos, (agregados sin repetir): ",vector_contador)

##Taller 3 Punto 10
def intercambio_columnas():
    print(">Subprograma intercambiar las columnas de la matriz<")
    matriz=leer_matriz()
    for i in range(len(matriz)):
        aux=matriz[i][0]
        matriz[i][0]=matriz[i][-1]
        matriz[i][-1]=aux

    print("Matriz con la primera columna intercambiada por la ultima: ")
    for fila in matriz:
        print(fila)


def mayor_menor_promedio_columnas():
    print(">Subprograma mayor, menor y promedio de las columnas")
    matriz=leer_matriz()
    for j in range(len(matriz[0])):
        mayor = matriz[0][j]
        menor = matriz[0][j]
        suma = 0
        for i in range(len(matriz)):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
            elif matriz[i][j] < menor:
                menor = matriz[i][j]

            suma += matriz[i][j]
        promedio = suma / len(matriz)
        print("Columna", j, "Mayor:", mayor, "Menor:", menor, "Promedio:", promedio)

def ordenar_filas_pares_impares():
    print(">Subprograma ordenar filas pares e impares<")
    matriz=leer_matriz()
    for i in range(len(matriz)):
        if i % 2 == 0:  # Fila par
            for j in range(len(matriz[i]) - 1):
                for k in range(j + 1, len(matriz[i])):
                    if matriz[i][k] < matriz[i][j]:
                        aux = matriz[i][j]
                        matriz[i][j] = matriz[i][k]
                        matriz[i][k] = aux
        else:  # Fila impar
            for j in range(len(matriz[i]) - 1):
                for k in range(j + 1, len(matriz[i])):
                    if matriz[i][k] > matriz[i][j]:
                        aux = matriz[i][j]
                        matriz[i][j] = matriz[i][k]
                        matriz[i][k] = aux
    print("Matriz ordenada en columnas pares ascendentes y columnas impares descendentes:")
    for fila in matriz:
        print(fila)

def orden_matriz_descendente():
    print(">Subprograma ordenar la matriz descendentemente<")
    matriz=leer_matriz()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            p=i
            q=j
            while p<len(matriz):
                while q<len(matriz[i]):
                    if matriz[p][q]>matriz[i][j]:   
                        aux=matriz[i][j]
                        matriz[i][j]=matriz[p][q]
                        matriz[p][q]=aux
                    q+=1
                p+=1
                q=0 #Para garantizar que la siguiente fila inicie en 0
    print("Matriz ordenada descendentemente: ")
    for fila in matriz:
        print(fila)
    return matriz    

def intercambiar_filas_promedio_ascendente():
    print(">Subprograma intercambiar filas segun el promedio ascendente<")
    matriz=leer_matriz()
    promedios = []
    
    for i in range(len(matriz)):
        suma = sum(matriz[i])
        promedio = suma / len(matriz[i])
        promedios.append((promedio, i))
    
    promedios.sort()  # Ordenar por promedio en orden ascendente
    
    nueva_matriz = []
    for promedio, fila_index in promedios:
        nueva_matriz.append(matriz[fila_index])
    
    print("Matriz ordenada de acuero al promedio de cada fila: ")
    for fila in nueva_matriz:
        print(fila)

def intercambiar_filas_mayor_menor():
    print(">Subprograma intercambiar filas de mayor a menor")
    matriz=leer_matriz()
    mayor = matriz[0][0]
    menor = matriz[0][0]
    fila_mayor = 0
    fila_menor = 0
    
    for i in range(len(matriz)):
        suma_fila = sum(matriz[i])
        
        if suma_fila > mayor:
            mayor = suma_fila
            fila_mayor = i
        
        if suma_fila < menor:
            menor = suma_fila
            fila_menor = i
    
    matriz[fila_mayor], matriz[fila_menor] = matriz[fila_menor], matriz[fila_mayor]
    
    print("Matriz con filas intercambiadas según el mayor y el menor de cada fila: ")
    for fila in matriz:
        print(fila)

def encontrar_fibonacci(numero):
    a = 0
    b = 1
    t = 0
    
    while t < numero:
        t = a + b
        a = b
        b = t
    
    return t == numero

def intercambiar_filas_fibonacci_2_4():
    matriz=leer_matriz()
    print(">Subprograma intercambiar las filas de fibonaccis<")
    fila_fibonacci_2 = None
    fila_fibonacci_4 = None
    
    for i in range(len(matriz)):
        suma_fila = sum(matriz[i])
        
        if encontrar_fibonacci(suma_fila):
            if fila_fibonacci_2 is None:
                fila_fibonacci_2 = i
            elif fila_fibonacci_4 is None:
                fila_fibonacci_4 = i
    
    if fila_fibonacci_2 is not None and fila_fibonacci_4 is not None:
        matriz[fila_fibonacci_2], matriz[fila_fibonacci_4] = matriz[fila_fibonacci_4], matriz[fila_fibonacci_2]
        print("Matriz con filas intercambiadas entre Fibonacci 2 y Fibonacci 4: ")
        for fila in matriz:
            print(fila)
    else:
        print("No se encontraron filas con Fibonacci 2 y Fibonacci 4.")

def intercambiar_filas_primo_fibonacci_menor():
    print(">Subprograma intercambiar las filas del primo con el fibonacci menor<")
    matriz=leer_matriz()
    primo_mayor = None
    fibonacci_menor = None
    
    for i in range(len(matriz)):
        suma_fila = sum(matriz[i])
        
        if suma_fila > primo_mayor and encontrar_primo(suma_fila):
            primo_mayor = suma_fila
        
        if suma_fila < fibonacci_menor and encontrar_fibonacci(suma_fila):
            fibonacci_menor = suma_fila
    
    if primo_mayor is not None and fibonacci_menor is not None:
        fila_primo_mayor = None
        fila_fibonacci_menor = None
        
        for i in range(len(matriz)):
            suma_fila = sum(matriz[i])
            if suma_fila == primo_mayor:
                fila_primo_mayor = i
            if suma_fila == fibonacci_menor:
                fila_fibonacci_menor = i
        
        if fila_primo_mayor is not None and fila_fibonacci_menor is not None:
            matriz[fila_primo_mayor], matriz[fila_fibonacci_menor] = matriz[fila_fibonacci_menor], matriz[fila_primo_mayor]
            print("Matriz con filas intercambiadas entre primo mayor y Fibonacci menor: ")
            for fila in matriz:
                print(fila)
        else:
            print("No se encontraron filas con los valores adecuados.")
    else:
        print("No se encontraron filas con primo mayor y Fibonacci menor.")

def encontrar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def consecutivos_primo_2_4(matriz):
    print(">Subprograma primos consecutivos<")
    matriz=leer_matriz()
    posicion_primo_2 = None
    posicion_primo_4 = None
    
    for i in range(len(matriz)):
        suma_fila = sum(matriz[i])
        if suma_fila == 2 and encontrar_primo(suma_fila):
            posicion_primo_2 = i
        if suma_fila == 4 and encontrar_primo(suma_fila):
            posicion_primo_4 = i
    
    if posicion_primo_2 is not None and posicion_primo_4 is not None:
        if abs(posicion_primo_2 - posicion_primo_4) == 1:
            print("Los primos 2 y 4 son consecutivos.")
        else:
            print("Los primos 2 y 4 no son consecutivos.")
    else:
        print("No se encontraron filas con primos 2 y 4.")

#PARCIAL 1

def Parcial1_Punto1():
    cantidad_datos=int(input("Cantidad de datos: "))
    c=1
    si_primo=0
    si_fibo=0
    si_par=0
    while c<=cantidad_datos:
        numero=int(input("Numero: "))
        c_1=1
        div=0
        while c_1<=numero:
            if numero%c_1==0:
                div+=1
            c_1+=1

        if div==2:
            si_primo+=1
            if si_primo==1:
                primo_mayor=numero
            elif numero>primo_mayor:
                primo_mayor=numero

        a=0
        b=1
        t=0
        while t<numero:
            t=a+b
            a=b
            b=t

        if numero==t:
            si_fibo+=1
            if si_fibo==1:
                fibo_menor=numero
            elif numero<fibo_menor:
                fibo_menor=numero

        if numero%2==0:
            si_par+=1
            if si_par==1:
                par_menor=numero
            elif numero<par_menor:
                par_menor=numero
        c+=1

    print("Primo mayor= ",primo_mayor," Fibonacci menor: ",fibo_menor," Par menor: ",par_menor)
    multiplicacion_1=fibo_menor
    c_3=1
    while c_3<primo_mayor:
        multiplicacion_1+=fibo_menor
        c_3+=1

    multiplicacion_2=par_menor
    c_3=1
    while c_3<multiplicacion_1:
        multiplicacion_2+=par_menor
        c_3+=1

    print("La multiplicacion entre estos 3= ",multiplicacion_2)


def Parcial1_Punto2():

    cantidad_datos = int(input("Cantidad de datos = "))
    c = 1
    si_fibo = 0
    c_fibos = 0
    segundo_fibonacci = 0

    while c <= cantidad_datos:
        numero = int(input("Numero: "))
        a = 0
        b = 1
        t = 0
        
        while t < numero:
            t = a + b
            a = b
            b = t

        if numero == t:
            si_fibo += 1
            if si_fibo == 2:
                segundo_fibonacci = numero
                c_fibos = 1
            elif numero == segundo_fibonacci:
                c_fibos += 1
        c += 1

    print("Segundo fibonacci:", segundo_fibonacci, "Contador de numeros iguales a este:", c_fibos)

    c = 1
    div = 0

    while c <= c_fibos:
        if c_fibos % c == 0:
            div += 1
        c += 1

    if div == 2:
        print("Esta contador de datos es un número primo")
    else:
        print("Esta contador de datos no es un número primo")


def Parcial1_Punto3():

    Cantidad_datos=int(input("Cantidad de ternas o triangulos: "))
    perimetro_equilatero = 0
    contador_equilateros = 0
    contador_isosceles = 0
    contador_escalenos = 0
    c=1
    c_equilateros=1
    while c<=Cantidad_datos:
        lado1 = int(input("Lado 1= "))
        lado2 = int(input("Lado 2= "))
        lado3 = int(input("Lado 3= "))
        
        if lado1 > 0 and lado2 > 0 and lado3 > 0:
            perimetro_equilatero_contado=0
            if lado1 == lado2 == lado3:
                print("Triangulo equilatero")
                perimetro_equilatero+= lado1 * 3
                perimetro_equilatero_contado=lado1*3
                print("Perimetro del triangulo",c_equilateros," = ",perimetro_equilatero_contado)
                c_equilateros+=1
                contador_equilateros += 1
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("Triangulo isosceles")
                contador_isosceles += 1
            else:
                print("Triangulo escaleno")
                contador_escalenos += 1
        else:
            print("Triangulo no valido")

        c+=1

    print("Cantidad de triangulos equilateros:", contador_equilateros)
    print("Cantidad de triangulos isosceles:", contador_isosceles)
    print("Cantidad de triangulos escalenos:", contador_escalenos)
    a=0
    b=1
    t=0
    while t<perimetro_equilatero:
        t=a+b
        a=b
        b=t

    if perimetro_equilatero==t:
        print("Suma de los perimetros equilateros:", perimetro_equilatero," Esta suma es numero fibonacci")
    else:
        print("Suma de los perimetros equilateros:", perimetro_equilatero," Esta suma No es numero fibonacci") 


def Parcial1_Punto4():

    cantidad_datos=int(input("Cantidad de datos: "))
    c=1
    si_fibo=0
    while c<=cantidad_datos:
        numero=int(input("Numero: "))
        a=0
        b=1
        t=0
        while t<numero:
            t=a+b
            a=b
            b=t

        if numero==t:
            si_fibo+=1
            if si_fibo==1:
                primer_fibo=numero
            elif si_fibo==2:
                segundo_fibo=numero
            elif si_fibo==3:
                tercer_fibo=numero 
        c+=1

    print("Primer fibonacci: ",primer_fibo," Segundo fibonacci: ",segundo_fibo," Tercer fibonaccii: ",tercer_fibo)
    if primer_fibo>segundo_fibo and primer_fibo>tercer_fibo:
        fibo_mayor=primer_fibo
    elif segundo_fibo>primer_fibo and segundo_fibo>tercer_fibo:
        fibo_mayor=segundo_fibo
    elif tercer_fibo>primer_fibo and tercer_fibo>segundo_fibo:
        fibo_mayor=tercer_fibo

    if primer_fibo<segundo_fibo and primer_fibo<tercer_fibo:
        fibo_menor=primer_fibo
    elif segundo_fibo<primer_fibo and segundo_fibo<tercer_fibo:
        fibo_menor=segundo_fibo
    elif tercer_fibo<primer_fibo and tercer_fibo<segundo_fibo:
        fibo_menor=tercer_fibo

    print("Fibonacci mayor: ",fibo_mayor," Fibonacci menor: ",fibo_menor)
    print("Numeros pares entre estos (Sin tomar los respectivos fibonaccis)")
    c=fibo_menor+1
    suma_pares=0
    c_pares=0
    while c<fibo_mayor:
        if c%2==0:
            print(c)
            suma_pares+=c
            c_pares+=1
        c+=1    

    if c_pares>0:
        promedio_pares=suma_pares/c_pares
        print("El promedio de estos numeros pares es= ",promedio_pares)
    else:
        print("No hay numeros pares entre estos dos fibonaccis") 

#Parcial 2

def Parcial2_punto1():
    numero=int(input("Numero: "))
    c=0
    while numero!=-5:
        aux=numero
        cantidad_datos=0
        while numero==aux:
            cantidad_datos+=1
            numero=int(input("Numero: "))
        c+=1
        if c==1:
            grupo_mayor=aux
            cantidad_mayor=cantidad_datos
            grupo_menor=aux
            cantidad_menor=cantidad_datos
        else:
            if cantidad_datos>cantidad_mayor:
                cantidad_mayor=cantidad_datos
                grupo_mayor=aux
            elif cantidad_datos<cantidad_menor:
                cantidad_menor=cantidad_datos
                grupo_menor=aux

    print("Grupo mayo: ",grupo_mayor," Veces ",cantidad_mayor)
    print("Grupo menor: ",grupo_menor," Veces: ",cantidad_menor)
    c_2=cantidad_menor
    c_3=1
    while c_3<cantidad_mayor:
        c_2+=cantidad_menor
        c_3+=1

    print("Su multiplicacion es= ",c_2)

def Parcial2_punto2():
    cantidad_datos1=int(input("Cantidad de datos vector 1: "))
    v_1=[]
    print("Datos en lista 1: ")
    for i in range(cantidad_datos1):
        v_1.append(int(input("Dato({})=".format(i))))

    cantidad_datos2=int(input("Cantidad de datos en vector 2: "))
    v_2=[]
    print("Datos en lista 2: ")
    for j in range(cantidad_datos2):
        v_2.append(int(input("Dato({})=".format(j))))

    v_fibonaccis=[]
    v_multiplos=[]
    for i in range(cantidad_datos1):
        a=0
        b=1
        t=0
        while t<v_1[i]:
            t=a+b
            a=b
            b=t

        if v_1[i]%3==0:
            dato_1=v_1[i] in v_2
            if dato_1==True:
                v_multiplos.append(v_1[i]) 
                if v_1[i]%5==0:
                    print("Multiplo de 3 en comun y no multiplo de 5: ",v_1[i],"(ingresa a la lista)")
                    v_multiplos.remove(v_1[i])  

        if v_1[i]==t:
            dato_1=v_1[i] in v_2
            if dato_1==False:
                print("Fibonacci  no comun",v_1[i])
                dato_2=v_1[i] in v_fibonaccis
                if dato_2==False:
                    v_fibonaccis.append(v_1[i])

    for j in range(cantidad_datos2):
        a=0
        b=1
        t=0
        while t<v_2[j]:
            t=a+b
            a=b
            b=t

        if v_2[j]%3==0:
            dato_1=v_2[j] in v_1
            if dato_1==True:
                v_multiplos.append(v_2[j])
                if v_2[j]%5==0:
                    print("Multiplo de 3 en comun y no multiplo de 5: ",v_2[j],"(ingresa a la lista)")
                    v_multiplos.remove(v_2[j])    

        if v_2[j]==t:
            dato_1=v_2[j] in v_1
            if dato_1==False:
                print("Fibonacci no comun",v_2[j])
                dato_2=v_2[j] in v_fibonaccis
                if dato_2==False:
                    v_fibonaccis.append(v_2[j])    

    print("Vector de fibonaccis no comunes y sin repetir: ",v_fibonaccis)
    print("Vector con multiplos de 3 comunes que no son multiplos de 5: ",v_multiplos)

def Parcial2_punto3():
    cantidad_datos1 = int(input("Cantidad de datos en vector 1: "))
    v_1 = []
    print("Datos en vector 1: ")
    for i in range(cantidad_datos1):
        v_1.append(int(input("Dato({})=".format(i))))

    cantidad_datos2 = int(input("Cantidad de datos en vector 2: "))
    v_2 = []
    print("Datos en vector 2: ")
    for j in range(cantidad_datos2):
        v_2.append(int(input("Dato({})=".format(j))))

    sifibo = 0
    v_rango = []
    for i in range(cantidad_datos1):
        a = 0
        b = 1
        t = 0
        while t < v_1[i]:
            t = a + b
            a = b
            b = t

        if v_1[i] == t:
            sifibo += 1
            if sifibo == 3:
                tercer_fibonacci = v_1[i]
                print("Tercer fibonacci: ", tercer_fibonacci)
                v_rango.append(v_1[i])

    dato = cantidad_datos2 - tercer_fibonacci
    v_rango.insert(1, dato)
    print("El primer rango tendra una cantidad de:", v_rango[0], "datos", "El segundo rango tendra una cantidad de:", v_rango[1], "datos")
    i = 0
    j = 0
    c = 0
    while i < len(v_rango):
        c += 1
        if c == 1:
            # Orden ascendente
            limite_final_a = j + v_rango[i]
            while j < limite_final_a:
                x = j + 1
                while x < limite_final_a:
                    if v_2[x] < v_2[j]:
                        aux = v_2[j]
                        v_2[j] = v_2[x]
                        v_2[x] = aux
                    x += 1
                j += 1
            i += 1
        else:
            # Orden descendente
            limite_final_b = j + v_rango[i]
            while j < limite_final_b:
                x_1 = j + 1
                while x_1 < limite_final_b:
                    if v_2[x_1] > v_2[j]:
                        aux = v_2[j]
                        v_2[j] = v_2[x_1]
                        v_2[x_1] = aux
                    x_1 += 1
                j += 1
            i += 1

    print("Lista ordenada ascendente y descendentemente: ")
    for z in range(len(v_2)):
        print("Posicion:", z, "Dato:", v_2[z])

def Parcial2_punto4():
    v = []
    cantidad_datos = int(input("Cantidad de datos en vector: "))
    print("Datos en vector:")
    for i in range(cantidad_datos):
        v.append(int(input("Dato({})=".format(i))))

    matriz = []
    Filas = int(input("Numero de filas: "))
    Columnas = int(input("Numero de columnas: "))
    for i in range(Filas):
        fila = []
        for j in range(Columnas):
            fila.append(int(input(f'Dato {i},{j} = ')))
        matriz.append(fila)

    print("Vector:", v)
    print("Matriz:")
    for fila in matriz:
        print(fila)

    si_primo = 0
    for primo in v:
        c = 1
        div = 0
        while c <= primo:
            if primo % c == 0:
                div += 1
            c += 1

        if div == 2:
            si_primo += 1
            if si_primo == 1:
                for i in range(Filas):
                    j = 0
                    while j < Columnas:
                        if primo == matriz[i][j]:
                            fila_primo_1 = i
                            print("Fila del primer primo en común:", fila_primo_1)
                            break
                        j += 1
            elif si_primo == 2:
                for i in range(Filas):
                    j = 0
                    while j < Columnas:
                        if primo == matriz[i][j]:
                            fila_primo_2 = i
                            print("Fila del segundo primo en común:", fila_primo_2)
                            break
                        j += 1

    for j in range(Columnas):
        aux=matriz[fila_primo_1][j]
        matriz[fila_primo_1][j]=matriz[fila_primo_2][j]
        matriz[fila_primo_2][j]=aux

    for fila in matriz:
        print(fila)


#CONTROL DEL MENU
def desarrolloDelPunto(num):
    print("\n_________________________________________")
    print(f">  Respectivo desarrollo del punto {num}:  <")
    print("_________________________________________")

def menuPuntos(tipoDeEvaluacion,puntos,volver):
    print(f'''
|_________________________________________|
                {tipoDeEvaluacion}                       ''')
    for i in range(1,puntos+1):
        print(f"{i}. Punto {i}")
    print("_________________________________________")
    print(f"0. {volver}")
    print("|_________________________________________|")

def menuVolverAEjecutar():
    print("|_________________________________________|")
    print("1. Ejecutar codigo nuevamente")
    print("0. Atras")
    print("|_________________________________________|")

def menuParciales(tipoDeEvaluacion,puntos,volver):
    print(f'''
|-----------------------------------------|
                {tipoDeEvaluacion}                       ''')
    for i in range(1,puntos+1):
        print(f"{i}. Parcial {i}")
    print("------------------------------------------")
    print(f"0. {volver}")
    print("|-----------------------------------------|")    
#MENU
opcion=1
while opcion!=0:
    print('''|-|_______________________________________|-|
 |       (: BIENVENIDO A MI MENU :)        |
 | 1.Taller 1                              |
 | 2.Taller 2                              |
 | 3.Taller 3                              |
 | 4.Parcial 1 y 2                         |
 |_________________________________________|
 | 0.Finalizar                             |
|-|______________________by. Nicolas z.___|-|                               
          ''')
    opcion=input("Digite la opcion-->")
    print('|_________________________________________|')
    match opcion:
        case "1":
            taller_1=1
            while taller_1!=0:
                menuPuntos("Taller 1",5,"Atras")
                taller_1=input("Que punto desea ejecutar-->")
                match taller_1:
                    case "1":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(1)
                                Taller1_punto1()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "2":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(2)
                                Taller1_punto2()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "3":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(3)
                                Taller1_punto3()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "4":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(4)
                                Taller1_punto4()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "5":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(5)
                                Taller1_punto5()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "0":
                        taller_1 = 0
                    case _:
                        print("Opcion no valida >:(")
        case "2":
            taller_2=1
            while taller_2!=0:
                menuPuntos("Taller 2",10,"Atras")
                taller_2=input("Que punto desea ejecutar-->")  
                match taller_2:
                    case "1":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(1)
                                Taller2_Punto1()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "2":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(2)
                                Taller2_Punto2()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "3":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(3)
                                Taller2_Punto3()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "4":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(4)
                                Taller2_Punto4()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))   
                    case "5":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(5)
                                Taller2_Punto5()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "6":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(6)
                                Taller2_Punto6()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "7":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(7)
                                Taller2_Punto7()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> ")) 
                    case "8":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(8)
                                Taller2_Punto8()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))   
                    case "9":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(9)
                                Taller2_Punto9()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "10":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(10)
                                Taller2_Punto10()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))   
                    case "0":
                        taller_2=0
                    case _:
                        print("Opcion no valida >:(")
        case "3":
            Taller_3=1
            while Taller_3!=0:
                menuPuntos("Taller 3",10,"Atras")
                Taller_3=input("Que punto desea ejecutar-->") 
                match Taller_3:
                    case "1":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(1)
                                Taller3_Punto1()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "2":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(2)
                                Taller3_Punto2()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "3":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(3)
                                Taller3_Punto3()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))                
                    case "4":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(4)
                                Taller3_Punto4()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> ")) 
                    case "5":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(5)
                                Taller3_Punto5()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))   
                    case "6":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(6)
                                Taller3_Punto6()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> ")) 
                    case "7":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(7)
                                print(">Este punto contiene varios subprogramas incluidos<")
                                q=1
                                while q!=0:
                                    menuPuntos("Ejercicio 7",6,"Atras")
                                    q=input("Digite la opcion-->")
                                    match q:
                                        case "1":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(1)
                                                    leer_matriz()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> ")) 
                                        case "2":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(2)
                                                    promedio_diagonal_principal_secundaria()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> ")) 
                                        case "3":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(3)
                                                    orden_diagonal_principal()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> ")) 
                                        case "4":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(4)
                                                    promedio_encima_diagonales()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> "))  
                                        case "5":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(5)
                                                    relllenar_diagonales()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> "))
                                        case "6":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(6)
                                                    leer_matriz()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> ")) 
                                        case "0":
                                            q=0
                                        case _:
                                            print("Opcion no valida >:(")                                                           
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "8":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(8)
                                print(">Este punto contiene varios subprogramas incluidos<")
                                q=1
                                while q!=0:
                                    menuPuntos("Ejercicio 8",3,"Atras")
                                    q=input("Digite la opcion-->")
                                    match q:
                                        case "1":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(1)
                                                    leer_dos_matrices()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> ")) 
                                        case "2":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(2)
                                                    vector_elementos_comunes()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> "))
                                        case "3":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(3)
                                                    vector_primos_comunes()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> ")) 
                                        case "0":
                                            q=0
                                        case _:
                                            print("Opcion no valida >:(")
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> ")) 
                    case "9":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(9)
                                Taller3_Punto9()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))
                    case "10":
                        x=1 
                        while x !=0 :
                            if (x==1):
                                desarrolloDelPunto(10)
                                print(">Este punto contiene varios subprogramas incluidos<")
                                q=1
                                while q!=0:
                                    menuPuntos("Ejercicio 10",9,"Atras")
                                    q=input("Digite la opcion-->")
                                    match q:
                                        case "1":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(1)
                                                    intercambio_columnas()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> ")) 
                                        case "2":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(2)
                                                    mayor_menor_promedio_columnas()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> "))
                                        case "3":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(3)
                                                    ordenar_filas_pares_impares()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> "))
                                        case "4":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(4)
                                                    orden_matriz_descendente()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> "))
                                        case "5":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(5)
                                                    intercambiar_filas_promedio_ascendente()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> ")) 
                                        case "6":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(6)
                                                    intercambiar_filas_mayor_menor()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> ")) 
                                        case "7":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(7)
                                                    intercambiar_filas_fibonacci_2_4()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> "))
                                        case "8":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(8)
                                                    intercambiar_filas_primo_fibonacci_menor()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> "))  
                                        case "9":
                                            z=1 
                                            while z !=0 :
                                                if (z==1):
                                                    desarrolloDelPunto(9)
                                                    consecutivos_primo_2_4()
                                                    menuVolverAEjecutar()
                                                else: 
                                                    print("\nOPCION NO VALIDA")
                                                    menuVolverAEjecutar()
                                                z=int(input("Digite su opcion-> "))                                            
                                        case "0":
                                            q=0
                                        case _:
                                            print("Opcion no valida >:(")
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            x=int(input("Digite su opcion-> "))                            
                    case "0":
                        Taller_3=0
                    case _:
                        print("Opcion no valida >:(") 
        case "4":
            Parciales=1
            while Parciales!=0:
                menuParciales("-_- Parciales -_-",2,"Atras")
                Parciales=input("Que punto desea ejecutar-->") 
                match Parciales:
                    case "1":
                        parcial1 = 1
                        while parcial1 != 0:
                            menuPuntos("Parcial 1",4,"Volver")
                            parcial1 = input('Digite la opcion->')
                            match parcial1:
                                case "1":
                                    z=1 
                                    while z !=0 :
                                        if (z==1):
                                            desarrolloDelPunto(1)
                                            Parcial1_Punto1()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        z=int(input("Digite su opcion-> "))
                                case "2":
                                    z=1 
                                    while z !=0 :
                                        if (z==1):
                                            desarrolloDelPunto(2)
                                            Parcial1_Punto2()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        z=int(input("Digite su opcion-> ")) 
                                case "3":
                                    z=1 
                                    while z !=0 :
                                        if (z==1):
                                            desarrolloDelPunto(3)
                                            Parcial1_Punto3()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        z=int(input("Digite su opcion-> "))  
                                case "4":
                                    z=1 
                                    while z !=0 :
                                        if (z==1):
                                            desarrolloDelPunto(4)
                                            Parcial1_Punto4()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        z=int(input("Digite su opcion-> "))
                                case "0":
                                    parcial1=0
                                case _:
                                    print("Opcion no valida >:(")    
                    case "2":
                        parcial2 = 1
                        while parcial2 != 0:
                            menuPuntos("Parcial 1",4,"Volver")
                            parcial2 = input('Digite la opcion->')
                            match parcial2:
                                case "1":
                                    z=1 
                                    while z !=0 :
                                        if (z==1):
                                            desarrolloDelPunto(1)
                                            Parcial2_punto1()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        z=int(input("Digite su opcion-> "))
                                case "2":
                                    z=1 
                                    while z !=0 :
                                        if (z==1):
                                            desarrolloDelPunto(2)
                                            Parcial2_punto2()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        z=int(input("Digite su opcion-> ")) 
                                case "3":
                                    z=1 
                                    while z !=0 :
                                        if (z==1):
                                            desarrolloDelPunto(3)
                                            Parcial2_punto3()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        z=int(input("Digite su opcion-> ")) 
                                case "4":
                                    z=1 
                                    while z !=0 :
                                        if (z==1):
                                            desarrolloDelPunto(1)
                                            Parcial2_punto4()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        z=int(input("Digite su opcion-> "))                      
                                case "0":
                                    parcial2=0
                                case _:
                                    print("Opcion no valida >:(")
                    case "0":
                        Parciales=0
                    case _:
                        print("Opcion no valida >:(")
        case "0":
            print("|__Espero que haya sido de tu agrado :)___|")
            break 
        case _:
            print("Opcion no valida >:(")                   