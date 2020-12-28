def sucet_cisel(cislo1, cislo2):
    result = cislo1 + cislo2
    return result
                
sucet = sucet_cisel(cislo2 = 2, cislo1 = 5) #Poradie argumentov sa da aj otocit.
print("Sucet je", sucet) 

print("\n")

#Retazenie funkcie:
def sucet_cisel(cislo1, cislo2):
    result = cislo1 + cislo2
    return result

#x = (5 + 4) + 3
sucet = sucet_cisel(sucet_cisel(cislo1 = 5, cislo2 = 4), 3) 
print("Sucet je", sucet)

print("\n")

def string_addition_with_delimiter(string1, string2, delimiter):  #delimiter je v tomto pripade ciarka.
    return string1 + delimiter + string2 

temp = string_addition_with_delimiter("Michal", "Hucko", ", ")
print(temp)  

print("\n")
#Definicia optional parameter:
def string_addition_with_delimiter(string1, string2, delimiter=", "): 
    return string1 + delimiter + string2 

temp = string_addition_with_delimiter("Michal", "Hucko")
print(temp)  

print("\n")

#Definicia funkcie, ktora vrati sucet pola:
cisla = list(range(0, 9))  
print(cisla)

def sum_array(array):
    sucet = 0                   #Premenna, do ktorej budem davat ten sucet
    for number in array: 
        sucet = sucet + number  #Da sa toto napisat aj sucet += number
    return sucet 

#Zavolanie funkcie a vyprintovanie:
print(sum_array(cisla)) 

print("\n")
def simple_sum(a, b):
    return a + b

print("Dalsi priklad")
if (simple_sum(4, 3) > simple_sum(5, 2)):
    print("First is bigger")
elif (simple_sum(4, 3) == simple_sum(5, 2)):
    print("First is equal to second")
else: 
    print("Second is bigger")

print("\n")
#Vypise sa [7, 6]
temp = [simple_sum(3, 4), simple_sum(simple_sum(1, 2), 3)]   #Dam to do nejakej premennej temp
print(temp) 