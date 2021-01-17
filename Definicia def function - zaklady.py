# Zadefinujte funkciu, ktora vrati sucet pola list(range(0, 101)).
def function_sum_array(array):
    variable_sum = 0
    for number in array:
        variable_sum = variable_sum + number
    return variable_sum

print(function_sum_array(list(range(0, 101))))

# Zadefinujte funkciu, ktora vrati priemernu hodnotu pola array = [7, 9, 15, 22, 23]
def function_mean(array):
    variable_sum = 0
    for number in array:
        variable_sum = variable_sum + number
    variable_mean = variable_sum / len(array) 
    return (variable_mean)

array = [7, 9, 15, 22, 23] 
print(function_mean(array))

# Zadefinujte funkciu, ktora vrati hraciu plochu hry piskvorky velkosti 5x5 s oznacenim riadkov a stlpcov.
#   1 2 3 4 5
# 1 _ _ _ _ _
# 2 _ _ _ _ _
# 3 _ _ _ _ _
# 4 _ _ _ _ _
# 5 _ _ _ _ _

def create_headings(array_grid, number_of_rows, number_of_columns):
    print("  ", end="")
    for column in range(1, number_of_columns):
        print(column, end=" ")                         
    print() 
    for row in range(1, number_of_rows):
        print(row, end=" ")
        for column in range(1, number_of_columns):
            print(array_grid[row][column], end=" ")      
        print()

def create_underscore_grid(number_of_rows, number_of_columns, sign = "_"):
    array_grid = []
    for row in range(1, number_of_rows+1):
        row_array = []
        for column in range(1, number_of_columns+1):
            row_array.append(sign)   
        array_grid.append(row_array) 
    return array_grid

#print(create_underscore_grid(5, 5))
create_headings(create_underscore_grid(6, 6), 6, 6)