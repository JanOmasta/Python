"""
Zadanie: Z datovej mnoziny data_file.txt zistite minimalny a maximalny pocet bodov z testu skupiny 100 studentov. Dalej vypocitajte priemerny pocet bodov, 
pocet studentov, ktori dosiahli nadpriemerny vysledok a percentualny pocet studentov, ktori ziskali menej ako minimalny pocet - 60 bodov zo 100. 
V pripade, ze je toto percento vyssie ako 15, algoritmus upozorni ucitela zopakovat ucivo.
"""

import statistics

with open("data_file.txt", "r") as file:
    string_array = []
    for line in file.readlines():
        string_array.append(line.strip())
    int_array = [int(i) for i in string_array]

print("The data set shows that", len(int_array), "students participated on the exam.")

min_value = min(int_array)
print("The minimal number of points from the exam is", min_value, "and", int_array.count(min_value), "students achieved such a score.")

max_value = max(int_array)
print("The maximal number of points from the exam is", max_value, "and", int_array.count(max_value), "students achieved this maximal number.")

mean_value = statistics.mean(int_array)
rounded_mean_value = round(mean_value, 1)
print("The mean score of the exam is", rounded_mean_value, "points.")

above_average_score = []
for i in int_array:
    if i > rounded_mean_value:
        above_average_score.append(i)
print("Above-average score was achieved by", len(above_average_score),"students.")

failed_students = []
for i in int_array:
    if i < 60:
        failed_students.append(i)
len(failed_students)
failed_percents = (len(failed_students) * 100) / len(int_array)
print("A percentage of unsuccessful students is", round(failed_percents, 1), "%.")
if round(failed_percents, 1) > 15:
    print("Information for the teacher: The number of unsuccessful students is high so it is needed to review the subject matter for the students.")
