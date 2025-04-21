###############################################
# VERİ YAPILARI (DATA STRUCTURES)
###############################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set


###############################################
# Veri Yapılarına Giriş ve Hızlı Özet
##############################################

# Sayılar: integer
x = 46
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False
type(True)
5 == 4
3 == 2
1 == 1
type(3 == 2)

# Liste
#listeler çok önemlidir köşeli parantez içinde tanımlanır
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (dictionary)
# süslü parantez içinde key-value şeklinde tanımlanır
# key:value
x = {"name": "Peter", "Age": 36}
type(x)

# Tuple
# tuple (demet) değiştirilemez normal parantez içinde tanımlanır
x = ("python", "ml", "ds")
type(x)

# Set
# set (küme) tekrar eden elemanları almaz süslı parantez içinde tanımlanır
x = {"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.


###############################################
# Sayılar (Numbers): int, float, complex
###############################################

a = 5
b = 10.5

#sayı ve işlemlerin arasını boşluk bırakarak yazmalıyız
a * 3
a / 7
a * b / 10
a ** 2 # sayının karesini alırız
a % 3 #mod alma

7 / 3 # float bölümü
7 // 3 # tam sayı bölümü

#######################
# Tipleri değiştirmek
#######################

int(b)
float(a)

int(a * b / 10)

c = a * b / 10

int(c)


###############################################
# Karakter Dizileri (Strings)
###############################################

print("John")
print('John')

"John"
name = "John"
name = 'John'

#######################
# Çok Satırlı Karakter Dizileri
#######################

"""Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

long_str = """Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

#######################
# Karakter Dizilerinin Elemanlarına Erişmek
#######################

name
name[0]
name[3]
name[2]

#######################
# Karakter Dizilerinde Slice İşlemi
#######################

name[0:2] # 0dan 2'ye kadar 2 dahil değil 0 ve 1
long_str[0:10]

#######################
# String İçerisinde Karakter Sorgulamak
#######################

long_str

"veri" in long_str

"Veri" in long_str

"bool" in long_str

###############################################
# String (Karakter Dizisi) Metodları
###############################################

#veri yapılarında kullanılabilecek tüm metodları görmek için
dir(str)

#######################
# len boyut bilgisi
#######################

name = "john"
type(name)
type(len)

len(name)
len("semihbekdaş")
len("semih")

#######################
# upper() & lower(): küçük-büyük dönüşümleri
#######################

"machine".upper()
"LEARNING".lower()



#######################
# replace: karakter değiştirir
#######################

hi = "Hello AI Era"
hi.replace("l", "p")

#######################
# split: böler ön tanımı boşluktur
#######################

"Hello AI Era".split()

#######################
# strip: kırpar
# ön tanımlı olarak boşlukları alır
#######################

" ofofo ".strip()
"ofofo".strip("o") #baştaki ve sondaki "o" harflerini siler


#######################
# capitalize: ilk harfi büyütür
#######################

"foo".capitalize()

dir("foo")

"foo".startswith("f")
"foo".endswith("o")

###############################################
# Liste (List)
###############################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.(farklı veri tiplerini içerebilir)

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

type(not_nam[6])

type(not_nam[6][1])

notes[0] = 99

not_nam[0:4]


###############################################
# Liste Metodları (List Methods)
###############################################

dir(notes)

#######################
# len: builtin python fonksiyonu, boyut bilgisi.
#######################

len(notes)
len(not_nam)

#######################
# append: eleman ekler
#######################

notes
notes.append(100)

#######################
# pop: indexe göre siler
#######################

notes.pop(0)

#######################
# insert: indexe ekler
#######################

notes.insert(2, 99)


###############################################
# Sözlük (Dictonary)
###############################################

# Değiştirilebilir.
# Sırasız. (3.7 sonra sıralı.)
# Kapsayıcı.

# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]


dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["CART"][1]

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}


#######################
# Key Sorgulama
#######################

"REG" in dictionary
"YSA" in dictionary

#######################
# Key'e Göre Value'ya Erişmek
#######################

dictionary["REG"]
dictionary.get("REG")
#ikiside doğru


#######################
# Value Değiştirmek
#######################

dictionary["REG"] = ["YSA", 10]

#######################
# Tüm Key'lere Erişmek
#######################
dictionary.keys()

#######################
# Tüm Value'lara Erişmek
#######################

dictionary.values()


# 1. Anahtar (key) sorgulama
print("name" in dictionary)  # True (Sözlükte "name" anahtarı var mı?)

# 2. Değer (value) sorgulama
print("Ali" in dictionary.values())  # False ("Ali" bir değer olarak var mı?)


#######################
# Tüm Çiftleri Tuple Halinde Listeye Çevirme
#######################

dictionary.items() # bir liste içerisinde key ve valueları tuple şeklinde döner
type(dictionary.items())

#######################
# Key-Value Değerini Güncellemek
#######################

dictionary.update({"REG": 11})

#######################
# Yeni Key-Value Eklemek
#######################

dictionary.update({"RF": 10})


#######################
# Key silmek del ile
#######################
dictionary = {"name": "Ali", "age": 25, "city": "Istanbul"}
print(dictionary)

# "age" anahtarını silme
del dictionary["age"]
print(dictionary)  # Çıktı: {'name': 'Ali', 'city': 'Istanbul'}

###############################################
# Demet (Tuple)
###############################################

# - Değiştirilemez.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

t[0] = 99

t = list(t)
t[0] = 99
t = tuple(t)



###############################################
# Set  genelde küme işlemlerinde kullanılır
###############################################

# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

#######################
# difference(): İki kümenin farkı
#######################

set1 = set([1, 3, 5]) #liste üzerinden set oluşturma
set2 = set([1, 2, 3])


# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1

#######################
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
#######################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#######################
# intersection(): İki kümenin kesişimi
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


#######################
# union(): İki kümenin birleşimi
#######################

set1.union(set2)
set2.union(set1)


#######################
# isdisjoint(): İki kümenin kesişimi boş mu?
#######################

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)


#######################
# issubset(): Bir küme diğer kümenin alt kümesi mi?
#######################

set1.issubset(set2) # set1, set2'nin alt kümesi mi?
set2.issubset(set1) # set2, set1'in alt kümesi mi?

#######################
# issuperset(): Bir küme diğer kümeyi kapsıyor mu?
#######################

set2.issuperset(set1) # set2, set1'i kapsıyor mu?
set1.issuperset(set2) # set1, set2'yi kapsıyor mu?








