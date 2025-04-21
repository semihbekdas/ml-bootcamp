###############################################
# DÖNGÜLER (LOOPS)
###############################################
# for loop

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)


for salary in salaries:
    print(int(salary*20/100 + salary))

for salary in salaries:
    print(int(salary*30/100 + salary))

for salary in salaries:
    print(int(salary*50/100 + salary))

def new_salary(salary, rate):
    return int(salary*rate/100 + salary)


for salary in salaries:
    print(new_salary(salary, 20))


salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 15))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))




# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz. tek indexi küçült çift indexi büyült
# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

range(len("Semih")) # range(0, 5)le aynı şey
range(0, 5) # 0dan 5e kadar olan sayıları verir 5 dahil değildir

for i in range(len("Semih")):
    print(i)


def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("Semih Bekdas")




#######################
# break & continue & while
#######################

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break # döngüden çık
    print(salary)


for salary in salaries:
    if salary == 3000:
        continue #döngüde adımı atla
    print(salary)


# while

number = 1
while number < 5:
    print(number)
    number += 1

#######################
# Enumerate: Otomatik Counter/Indexer ile for loop
#index bilgisini de almak için kullanılır.
#######################

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students): #enumerate(students, start=6) dersen indexi 6dan başlatır
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)



# divide_students fonksiyonu yazalım.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)




#######################
# Zip birbirinden farklı olan listeleriin elemanlarını eşler birleştirir
#######################

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages))



###############################################
# lambda, map, filter, reduce
###############################################

def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b #normalde böyle kullanma (atama yaparak kullanma)

new_sum(4, 5)

# map , fonksiyon ve iterable alır sonra verdiği fonksiyonu iterable üzerinde uygular
# map() fonksiyonu, birinci argüman olarak verilen fonksiyonu, ikinci argüman olarak verilen iterable (örneğin liste, demet, vb.) nesnenin
# her bir elemanına uygular ve sonuçları bir map nesnesi olarak döndürür.
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))


list(map(new_salary, salaries))

list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2 , salaries))

# FILTER
#filter fonksiyonu
# 	•	function: Her bir eleman için uygulanacak koşulu belirleyen fonksiyon. Bu fonksiyon, her eleman için True veya False döndürmelidir.
# 	•	iterable: Filtreleme yapılacak veri koleksiyonu (örneğin liste, tuple).
# 	•	Sonuç: filter() bir filter object döndürür. Sonuçları görmek için genellikle list() veya tuple() gibi bir dönüşüme ihtiyaç duyulur.
#   filter(function, iterable)

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store)) # çift sayıları alır

# REDUCE
# reduce(), iterable’ın ilk iki elemanını alır, belirtilen işlemi uygular, sonucu saklar ve bunu sonraki elemanla işlemeye devam eder.
# İşlem, iterable’ın tüm elemanları bitene kadar devam eder.
from functools import reduce

list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)
# 1 + 2 = 3 , 3 + 3 = 6 , 6 + 4 = 10

