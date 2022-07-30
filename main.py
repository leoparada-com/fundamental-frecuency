# Este script determina la frecuencia fundamental para el conjunto de frecuencias armonicas del espectro de una señal de audio

def calcula_divisores(int_num):
    a = int_num
    divisores = []
    for k in range(2,a+1):
        b= a/k
        if b == int(b):
            divisores.append(k)
    out = divisores
    return out

def frecuencia_fundamental(array_A):
    array_B = []
    for k in array_A:
        array_B.append(calcula_divisores(k))
    j=0
    for k in array_B:
        if j==0:
            aux=set(array_B[j])
        else:
            aux = set(k) & aux
        j=j+1
    try:
        out = max(aux)
    except:
        out = []
        print('El espectrograma no es armonico al 100%')
    return out

print('El espectrograma:')
A = [150,300,600]
print(A)
print('Su frecuencia fundamental:')
f0 = frecuencia_fundamental(A)
print(f0)

