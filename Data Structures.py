numbers_list = [9, 12, 8, 7, 10, 51, -8, 77, 200, 1, 66, 1120]

numbers_list.append(150)
print(numbers_list)

numbers_list.pop()      #Takes the last item in the list and delete it.
print(numbers_list)

numbers_list.pop()      #The same. Result is [9, 12, 8, 7, 10, 51, -8, 77, 200, 1, 66]          
print(numbers_list)

numbers_and_lists = [1, 2, 3, 4, 5, 0, [1, 2], [3, 4, [5, 6]]]     #Defining array in array.
print(numbers_and_lists[-1])
print(numbers_and_lists[-1][-1])
print(len(numbers_and_lists[-1][-1]))       #Return length of [-1][-1] array.       
print(numbers_and_lists[-1][-1][0])
print(numbers_and_lists[0:3])
print(numbers_and_lists[:3])                #Equivalent syntax of previous example.
numbers_and_lists[:3] = [10, 20, 30]
print(numbers_and_lists)

#Defining matrix - Python does not have a built-in type for matrices. It is treated as a list of lists. It is needed to use lib numpy. 
A = [
    [2, -5, -11, 0, 11],
    [-9, 4, 6, 13, 19],
    [4, 7, 12, -16, 9]
    ] 

print("A =", A) 
print("The first row of matrix A is:", A[0])
print("The second row of matrix A is:", A[1])
print("The third row of matrix A is:", A[2])
print("The fourth item of second row of matrix A is:", A[1][3])  #The result is 13.

languages = ["French", "English"]
latin_am_languages = ["Spanish", "Portuguese"] 
languages.extend(latin_am_languages)                #Extends the list.
print("Languages list:", languages)

fruits = ["orange", "apple", "kiwi", "banana", "mango"]
fruits.reverse()                                            #Reverse the elements of the list.
print(fruits)

fruits = ["apple", "kiwi", "orange", "apple", "mango", "apple"]
fruits.sort()                   #Sort the items of the list in alphabetical order.
print(fruits)

numbers_list = [9, 12, 8, 7, 10]
numbers_list.sort()          #Sort the items of the list in ascending order.
print(numbers_list)

my_dictionary = {           #Dictionary definition - keys and values.    
    "key" : "value",
    "Jorge" : 23,
    "Felipe" : 30,
    "key4" : "value4",
    "key5" : "value5",
    True : "True",
    False : False,
}
print(my_dictionary)

print(type(my_dictionary["Jorge"]))     #Prints type of the value when defining key (in this case Int).
print(my_dictionary["Jorge"])           #Prints value - 23.           

my_dictionary["Felipe"] = 50            #Changes the value from 30 to 50.
print("Felipe is", my_dictionary["Felipe"], "years old.")

del my_dictionary[True]                 #Deleting one key from dictionary.
print(my_dictionary) 

rem_list = ["key4", False]
[my_dictionary.pop(key) for key in rem_list]    #Remove multiple keys from dictionary.
print(my_dictionary)

dict_people = {                                 #Defining nested dictionary in dictionary.
    1: {
        "name" : "John",
        "age" : "27",
        "sex" : "Male",
        "married" : "No"
    },
    2: {
        "name" : "Marie",
        "age" : "22",
        "sex" : "Female",
        "married" : "Yes"
    }
}  
print(dict_people) 

print(dict_people[2]["name"])           #Printing from a certain dictionary.
print(dict_people[2]["age"])
print(dict_people[2]["sex"])

del dict_people[1]["married"]           #Deleting key from a nested dictionary. 
del dict_people[2]["married"]
print(dict_people)

dict_personal_info = {
    "name" : "Jan",
    "surname" : "Omasta",
    "languages" : ["Wolfram Mathematica", "Python", "xhtml", "SQL", "PHP"],
    "email": "@janomasta",
    "address" : {
        "permanent" : {
            "city" : "Prague",
            "street" : "Wilsonova",
            "street_number": 302
        },
        "temporary" : {
            "city" : "New York",
            "street" : "Wall Street",
            "street_number": 440
        }
    }
}

print(dict_personal_info["languages"][1])           #Prints second item from the list in dictionary.
print(dict_personal_info["address"]["permanent"]["street_number"])

print(list(dict_personal_info.items()))             #Prints the whole dictionary as a list using function items().
print("")
for key, value in list(dict_personal_info.items()):
    print("Key is:", key)
    print("Value is:", value)

print("")
print(list(dict_personal_info.keys()))              #Prints all first dict. keys as a list using function keys().
print(list(dict_personal_info.values()))            #Prints all values using function values().

#Defining tuples.
tuple1 = (1, 2, 3, 5, 7, 8, 10)
tuple2 = ("string", 10000.5, True, [50, 60, 66])
single_element_tuple_1 = (234.558, )
tuple4 = 1, 2, 3, 4
single_element_tuple_2 = 235.698,

print(tuple4[0])                                #Prints the first item in tuple called tuple3.

tuple_merged = tuple1 + (15,) + tuple2 + single_element_tuple_2 + tuple1[:5]      #Merging tuples using plus.
print("The merged tuple is:", tuple_merged)
list_tuple = list(tuple_merged)                                                   #Changing a tuple on a list. 
print(list_tuple)

#The ways how to define squares.
squares_1 = []
for i in range(0, 11):
    squares_1.append(i**2)
print(squares_1)

squares_2 = [i**2 for i in range(11)]
print(squares_2)  