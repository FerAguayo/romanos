"""
1- Crear una funcion que pase de entro >0 y <4000 a romano
2- Que cualquier otra entrada de error
3- limite de 3999

Casos de prueba
a) 1994 -> MCMXCIV
b)4000 ->RomanNumberError() El valor debe ser menor de 3999
c)"uncatena" -> RomanNumerError Debe ser un entero

M -> 1000
D -> 500
C -> 100
L -> 50
X -> 10
V -> 5
I -> 1


"""
#Base de datos de los número romanos
diccionario = {1000: "M",500: "D", 100: "C" ,50: "L", 10: "X", 5:"V", 1:"I"}
unidades = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
decenas = {10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC"}
centenas = {100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM"}
millares = {1000: "M", 2000: "MM", 3000: "MMM"}


#primer paso descomponer el numero
#segundo paso pasarlo a unidades, decenas, centenas y millares
#tercero buscar en el diccionario para que nos devuelva un resultado

class RomanNumberError():
    pass
#a) 1994 -> MCMXCIV
def entero_a_romano(numero):
    #Lo primero que hay que hacer es descomponerlo
    # 1994 -> ["1","9","9","4"]
    numero = str(numero)#Transformamos en cadena el valor numérico
    numero_list = list(numero)#Guardamos en una lista
    print(numero_list)
    for i in range(0,len(numero_list)):
        if i == 0:
            numero_list[i] = int(numero_list[i])*1000
        if i == 1:
            numero_list[i] = int(numero_list[i])*100
        if i == 2:
            numero_list[i] = int(numero_list[i])* 10
        
    return "MCMXCIV"


