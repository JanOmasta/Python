# https://www.w3schools.com/python/default.asp

"""
Priklad 1:
Napiste kod, ktory na zaklade 2 premennych (rows a columns) vypise mriezku vyplnenu hviezdickami. Pouzite cyklus for a potom aj cyklus while.
rows = 5
columns = 2
Vystup:
* *
* *
* *
* *
* *
"""
# Riesenie pomocou cyklu for:
number_of_rows = 5 
number_of_columns = 2
for row in range(0, number_of_rows):
    for column in range(0, number_of_columns):  
        print("* ", end="")                      
    print("")                                   

print("")

# Riesenie pomocou cyklu while:
number_of_columns = 2
number_of_rows = 5
while number_of_rows > 0:
    print("* " * number_of_columns)  
    if number_of_rows == 0:
        break
    number_of_rows -= 1

"""
Priklad 2:
Pouzite cyklus for a potom aj cyklus while.
number_of_rows = 4
Vystup:
*
* *
* * *
* * * *
* * *
* *
*
"""
print("")
# Riesenie pomocou cyklu for:
number_of_rows = 4
counter = 1
for counter in range(1, number_of_rows + 1):    
    for star in range(0, counter):
        print("* ", end="")
    print("") 
for counter in range(number_of_rows - 1, 0, -1):  #Pamatat na uzatvoreny a otvoreny interval.
    for star in range(0, counter):
        print("* ", end="")
    print("")

print("")

# Riesenie pomocou cyklu while:
number_of_rows = 4
counter = 1
while counter <= number_of_rows:
    print ("* " * counter)
    if counter == number_of_rows:  
        break                   
    counter += 1
while counter >= 1:
    print("* " * (number_of_rows - 1))
    if number_of_rows == 0:
        break
    number_of_rows -= 1

"""
Priklad 3:
Pouzite cyklus for a potom aj cyklus while.
number_of_rows = 5
Vystup:
1
1 2 
1 2 3 
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3 
1 2 
1
"""
# Riesenie pomocou cyklu for:
number_of_rows = 5
for row_number in range(1, number_of_rows + 1):         
    for number_itself in range(1, row_number + 1):      
        print(number_itself, "", end="")
    print()
for row_number in range(number_of_rows - 1, 0, -1):
    for number_itself in range(1, row_number + 1):
        print(number_itself, "", end="")
    print()

print("")

# Riesenie pomocou cyklu while:
number_of_rows = 5
counter1 = 1
while counter1 <= number_of_rows:
    counter2 = 1
    while counter2 != counter1 + 1:
        print (counter2, "", end="")
        counter2 += 1
    print()
    counter1 += 1

counter1 = number_of_rows - 1
while counter1 != 0:
    counter2 = 1
    while counter2 <= counter1:
        print(counter2, "", end="")
        counter2 += 1
    print()
    counter1 -= 1