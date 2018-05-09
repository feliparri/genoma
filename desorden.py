#FUNCION LAMBDA PARA ITERAR SOBRE LA FUNCION DESORDE
#la variable F es el nombre de la funcion que necesitamos usar, en este caso "desorden" 
#la variable S es el valor del string que estamos desordenando

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
            #en caso que los caracteres no se cumpla "ACGT"
            raise Exception("seciencia desconocida")
     
    return diferencia    

#LEE EL ARCHIVO ADN.DAT Y OBTIENE EL ARRAY 
lineas = [line.rstrip('\n') for line in open('ADN.DAT')]

#CREA ARCHIVO DE SALIDA ADN.RES PARA SER LLENADO EN LA ITERACION FOR MAS ABAJO
adnres = open("ADN.RES", "w")

#SACA LA PRIMERA LINEA DEL ARCHIVO LEIDO
lineas.pop(1) 


#SORTED   = toma cada string de cada linea y la pasa a la funcion DESORDEN ya que al tomar un String lo divide como un array
#MAP      = itera sobre la variable "lineas" con la funcion alias "desorden" que a su vez llama a la funcion "desorden"
#ENVUELVE = retorna el resultado de la variable enviada a la funcion "desorden" iterando por cada valor en la variable "lineas"

#RECORRE EL ARRAY Y LO PASA POR LA FUNCION DESORDEN
for score, str in sorted(map(envuelve(desorden), lineas)):
    #print(str, score)
    adnres.write(str+'\n')

#CIERRA EL ARCHIVO
adnres.close()  
