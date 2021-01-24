# help: https://www.w3schools.com/python/default.asp
# help: https://docs.python.org/3/library/array.html

"""
ZADANIE:
1. nacitajte data zo suboru do dvojrozmerneho pola.
Vytvorte algoritmus, ktory:
2. zisti maximalnu intenzitu (bez ohladu na pocet pruhov)
3. zisti maximalnu intenzitu vzhladom na pocet pruhov (intenzita/pocet pruhov)
4. vypise do suboru intenzity frekventovanych usekov aj s poctom pruhov (frekventovany usek ma intenzitu aspon 15000)
5. vypise do ineho suboru intenzity na kritickych usekoch aj s poctom pruhov (kriticky usek ma intenzitu vzhladom na 1 pruh vyssiu ako 7500)
6. zisti, kolko aut v sucte prejde denne po kritickych usekoch.
"""

with open("data_file.txt", "r") as file:
    row_id = []
    x = []
    y = [] 
    for line in file.readlines():  
        p = line.split()                # Division of a line into three parts.
        row_id.append(p[0])
        x.append(int(p[1]))
        y.append(int(p[2]))

print("Data in a two-dimensional array:")
in_data = []
for i in range(len(x)):
    in_data.append([x[i], y[i]])
print(in_data)

print("The maximum intensity (without considering the traffic lanes) is:", max(x), "vehicles.")

print("The maximum intensity considering the traffic lanes is: ", end="")
lanes_intensity = []
for i in range(len(x)):
    id_intensity = (x[i] / y[i])
    lanes_intensity.append(round(id_intensity, 0))
print(int(max(lanes_intensity)), end="")
print(" vehicles. And this road corresponds with the road with identificator id", end="")
print(lanes_intensity.index(max(lanes_intensity)) + 1, end="")
print(".")

print("The most frequented roads (more than 15,000 vehicles per day) are: ") 
for i in range(len(x)):
    if x[i] > 15000:
        print(row_id[i], x[i], y[i])

# Writing into a new file:
with open("critical_roads.txt", "w") as file:
    for i in range(0, len(lanes_intensity)): 
        integer_value = int(lanes_intensity[i])
        if integer_value > 7500:
            file.write(row_id[i])
            file.write(" ")
            file.write(str(integer_value))
            file.write(" ")
            file.write(str(y[i]))
            file.write("\n") 

print("The overall daily traffic on cricical roads consists of: ", end="")
sum_array = []
for i in range(len(x)): 
    integer_value = int(lanes_intensity[i])
    if integer_value > 7500:
        sum_array.append(x[i])
print(sum(sum_array), end="")
print(" vehicles.")
