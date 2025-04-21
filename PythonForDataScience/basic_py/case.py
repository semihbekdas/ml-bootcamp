###############################################
# Python Alıştırmalar
###############################################
###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################
x = 8
y = 3.2
z = 8j + 5
a = "Hello World"
b = True
type(x)
type(y)
type(z)
type(a)
type(b)

listt = [1, 2, 3, 4,"String",3.2, False]
type(listt)
# Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir

dictt = {"name":"semih","age": 19,"adress":"istanbul"}
type(dictt)
# Değiştirilebilir
# Kapsayıcı
# Sırasız
# Key değerleri farklı olacak

tuplee = ("Machine Learning", "Data Science")
type(tuplee)
# Değiştirilemez
# Kapsayıcı
# Sıralı

sett = {"Python", "Machine Learning", "Data Science","Python"}
type(sett)
# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcı

###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################
text = "The goal is to turn data into information, and information into insight."
text1 = text.upper().replace(".", " ").replace(",", " ").split()
print(text1)

##############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################
lst = ["D","A","T","A","S","C","I","E","N","C","E"]
# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)
# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0],lst[10]
# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
lst[0:4]
# Adım 4: Sekizinci index'teki elemanı silin.
lst.pop(8)
# Adım 5: Yeni bir eleman ekleyin.
lst.append("N")
# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
lst.insert(8,"N")


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################
dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

#Adım 1: Key değerlerine erişiniz.
dict.keys()

#Adım 2: Value'lara erişiniz.
dict.values()

#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.update({"Daisy": ["England",13]})
dict.get("Daisy")[1] = 13

#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict["Ahmet"] = ["Turkey",24]
dict.update({"Ahmet": ["Turkey", 24]})

#Adım 5: Antonio'yu dictionary'den siliniz.
del dict["Antonio"]
dict.pop("Antonio")

#Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
#return eden fonksiyon yazınız

def myfunc(numbers):
    even = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even ,odd

l = [2,13,18,93,22]

çift,tek = myfunc(l)

#Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
#bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
#tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for sira ,ogrenci in enumerate(ogrenciler):
    if sira < 3:
        sira += 1
        print("Mühendislik Fakültesi", sira, ". öğrenci: ", ogrenci)
    else:
        sira -= 2
        print("Tıp Fakültesi", sira, ". öğrenci: ", ogrenci)


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list_of_courses =list(zip(ders_kodu, kredi, kontenjan))
print(list_of_courses)

for ders_kodu, kredi, kontenjan in list_of_courses:
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
  print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

#Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
#eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
#Kapsayıp kapsamadığını kontrol etmek için issuperset() metodunu,

#farklı ve ortak elemanlar için ise intersection ve difference metodlarını kullanınız.



kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "semih"])

def func2(kume1,kume2):
    if kume1.issuperset(kume2):
        print(kume1.intersection(kume2))
    else:
        kume2.difference(kume1)



#######################
# difference(): İki kümenin farkı
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
# intersection(): İki kümenin kesişimi
# union(): İki kümenin birleşimi
# isdisjoint(): İki kümenin kesişimi boş mu?
# issubset(): Bir küme diğer kümenin alt kümesi mi?
# issuperset(): Bir küme diğer kümeyi kapsıyor mu?
#######################