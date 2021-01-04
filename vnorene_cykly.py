"""
Priklad 1:
Napiste kod, ktory na zaklade 2 premennych (rows a columns) vypise mriezku vyplnenu hviezdickami. Pouzite cyklus for a potom aj cyklus while.
rows = 5
columns = 2
**
**
**
**
**
"""

rows = 5 
columns = 2
for row in range(0, rows):
    for column in range(0, columns):  #vypise 2 hviezdicky vedla seba.
        print("*", end="")            #nezalomit riadok.
    print("")                         #za kazdnym riadkom zalomi riadok.

print("\n")

rows = 5
columns = 2
pocitadlo1 = 0
pocitadlo2 = 0

while True:
    if pocitadlo2 < rows:
        while True:
            if pocitadlo1 < columns:
                print("*", end="")
            if pocitadlo1 == columns:
                break
            pocitadlo1 += 1
    if pocitadlo2 == rows:
        break
    print("") 
    pocitadlo2 += 1 