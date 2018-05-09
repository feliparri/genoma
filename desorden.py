
def envuelve(f):
    return lambda s: (f(s), s)

#FUNCION QUE DESORDENA LA CADENA DESDE EL ARCHIVO
def desorden(x):
    letras = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
    diferencia = 0
     
    for caracter in x:
        letras[caracter] += 1
         
    for caracter in x:
        if caracter == 'A':
            letras['A'] -= 1
        elif caracter == 'C':
            letras['C'] -= 1
            diferencia += letras['A']
        elif caracter == 'G':
            letras['G'] -= 1
            diferencia += letras['A'] + letras['C']
        elif caracter == 'T':
            letras['T'] -= 1
            diferencia += letras['A'] + letras['C'] + letras['G']
        else:
            raise Exception("seciencia desconocida")
     
    return diferencia    

#LEE EL ARCHIVO ADN.DAT Y OBTIENE EL ARRAY 
lineas = [line.rstrip('\n') for line in open('ADN.DAT')]
#print(lineas.pop(1))

#CREA ARCHIVO DE SALIDA ADN.RES
adnres = open("ADN.RES", "w")
#adnres.write(lineas[1])

lineas.pop(1)
#RECORRE EL ARRAY Y LO PASA POR LA FUNCION DESORDEN
for score, str in sorted(map(envuelve(desorden), lineas)):
    #print(str, score)
    adnres.write(str+'\n')

adnres.close()  
