# Python Ders 5: Döngüler ve İlgili Yapılar - Ayrıntılı Notlar

Bu notlar, Python'da **döngüler (loops)** ve ilgili yapıları (`enumerate`, `zip`, `lambda`, `map`, `filter`, `reduce`) ayrıntılı bir şekilde açıklamaktadır. Döngüler, veri yapıları üzerinde yinelemeli işlemler yapmak için kullanılırken, diğer yapılar döngülerin daha etkili ve kısa bir şekilde kullanılmasını sağlar. Notlar, veri bilimi ve makine öğrenmesi projelerine yönelik pratik örneklerle zenginleştirilmiştir. Eksik noktalar tamamlanmış ve her bölümün kullanım senaryoları netleştirilmiştir.

---

## 1. Döngüler Nedir?

Döngüler, bir kod bloğunu belirli bir koşul sağlandığı sürece veya bir veri yapısında gezinmek için tekrar tekrar çalıştırmak için kullanılır. Python'da iki ana döngü türü bulunur:

- **`for` Döngüsü:** Bir veri yapısında (örneğin, liste, string) sırayla gezinmek için kullanılır.
- **`while` Döngüsü:** Bir koşul doğru olduğu sürece çalışır.

Döngüler, veri bilimi projelerinde veri işleme, filtreleme, dönüştürme ve modelleme gibi görevlerde sıkça kullanılır.

---

## 2. `for` Döngüsü

`for` döngüsü, bir veri yapısında (liste, string, tuple, vb.) veya bir `range` nesnesinde sırayla gezinmek için kullanılır.

### 2.1. Temel Kullanım

**Örnek: Liste Üzerinde Gezinme**

```python
students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)
# Çıktı:
# John
# Mark
# Venessa
# Mariam
```

**Örnek: String Dönüşümü**

```python
for student in students:
    print(student.upper())
# Çıktı:
# JOHN
# MARK
# VENESSA
# MARIAM
```

### 2.2. Sayısal İşlemler

**Örnek: Maaş Artışı**

```python
salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(int(salary * 20 / 100 + salary))  # %20 artış
# Çıktı: 1200, 2400, 3600, 4800, 6000

for salary in salaries:
    print(int(salary * 30 / 100 + salary))  # %30 artış
# Çıktı: 1300, 2600, 3900, 5200, 6500

for salary in salaries:
    print(int(salary * 50 / 100 + salary))  # %50 artış
# Çıktı: 1500, 3000, 4500, 6000, 7500
```

**Fonksiyonla Yeniden Yazma:**

```python
def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)

for salary in salaries:
    print(new_salary(salary, 20))  # Çıktı: 1200, 2400, 3600, 4800, 6000
```

**Farklı Veri Seti:**

```python
salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 15))  # %15 artış
# Çıktı: 12305, 28750, 34960, 46345, 57730
```

### 2.3. Koşullu Döngüler

Döngü içinde koşullu ifadeler kullanarak farklı işlemler yapılabilir.

**Örnek: Maaşlara Koşullu Artış**

```python
for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))  # %10 artış
    else:
        print(new_salary(salary, 20))  # %20 artış
# Çıktı: 1200, 2400, 3300, 4400, 5500
```

**Açıklama:** 3000 ve üzeri maaşlara %10, diğerlerine %20 artış uygulanır.

### 2.4. String Manipülasyonu

**Örnek: Alternating String**

Amaç: Bir string'in çift indeksli karakterlerini büyük, tek indeksli karakterlerini küçük harfe çevirmek.

```python
def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("Semih Bekdas")
# Çıktı: SeMiH BeKdAs
```

**Açıklama:** `range(len(string))`, string'in indekslerinde gezinmeyi sağlar. Çift indekslerde `upper()`, tek indekslerde `lower()` uygulanır.

---

## 3. Döngü Kontrol İfadeleri: `break` ve `continue`

Döngülerin akışını kontrol etmek için `break` ve `continue` kullanılır.

### 3.1. `break`

`break`, döngüyü tamamen sonlandırır.

**Örnek:**

```python
salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)
# Çıktı:
# 1000
# 2000
```

**Açıklama:** `salary == 3000` olduğunda döngü sonlanır.

### 3.2. `continue`

`continue`, mevcut iterasyonu atlar ve döngüye devam eder.

**Örnek:**

```python
for salary in salaries:
    if salary == 3000:
        continue
    print(salary)
# Çıktı:
# 1000
# 2000
# 4000
# 5000
```

**Açıklama:** `salary == 3000` olduğunda bu iterasyon atlanır, ancak döngü devam eder.

---

## 4. `while` Döngüsü

`while` döngüsü, bir koşul doğru olduğu sürece çalışır.

**Örnek:**

```python
number = 1
while number < 5:
    print(number)
    number += 1
# Çıktı:
# 1
# 2
# 3
# 4
```

**Açıklama:** `number` 5'e ulaştığında koşul `False` olur ve döngü sonlanır.

**Dikkat:** Sonsuz döngülerden kaçınmak için koşulun sonunda `False` olacağından emin olun.

**Örnek: Sonsuz Döngüden Kaçınma**

```python
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1
# Çıktı: 0, 1, 2, 3, 4
```

---

## 5. `enumerate`: İndeks ile Döngü

`enumerate`, bir veri yapısında gezinirken hem elemanları hem de indekslerini sağlar.

**Örnek:**

```python
students = ["John", "Mark", "Venessa", "Mariam"]

for index, student in enumerate(students):
    print(index, student)
# Çıktı:
# 0 John
# 1 Mark
# 2 Venessa
# 3 Mariam
```

**Başlangıç İndeksi Belirtme:**

```python
for index, student in enumerate(students, start=1):
    print(index, student)
# Çıktı:
# 1 John
# 2 Mark
# 3 Venessa
# 4 Mariam
```

**Örnek: Öğrencileri Gruplama**

```python
A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print(A)  # ['John', 'Venessa']
print(B)  # ['Mark', 'Mariam']
```

**Fonksiyonla Yeniden Yazma:**

```python
def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    return groups

st = divide_students(students)
print(st)  # [['John', 'Venessa'], ['Mark', 'Mariam']]
```

**Açıklama:** `enumerate`, indeks tabanlı işlemler için kullanışlıdır.

---

## 6. `zip`: Birden Fazla Listeyi Eşleştirme

`zip`, birden fazla veri yapısındaki elemanları eşleştirerek birleştirir.

**Örnek:**

```python
students = ["John", "Mark", "Venessa", "Mariam"]
departments = ["mathematics", "statistics", "physics", "astronomy"]
ages = [23, 30, 26, 22]

print(list(zip(students, departments, ages)))
# Çıktı: [('John', 'mathematics', 23), ('Mark', 'statistics', 30), ('Venessa', 'physics', 26), ('Mariam', 'astronomy', 22)]
```

**Döngü ile Kullanım:**

```python
for student, dept, age in zip(students, departments, ages):
    print(f"{student} studies {dept} and is {age} years old")
# Çıktı:
# John studies mathematics and is 23 years old
# Mark studies statistics and is 30 years old
# Venessa studies physics and is 26 years old
# Mariam studies astronomy and is 22 years old
```

**Veri Biliminde Kullanım:** `zip`, veri setlerinde birden fazla sütunu eşleştirerek işlemek için kullanılır (örneğin, özellik ve etiket eşleştirmesi).

---

## 7. Fonksiyonel Programlama: `lambda`, `map`, `filter`, `reduce`

Bu yapılar, döngülerin daha kısa ve fonksiyonel bir şekilde yazılmasını sağlar.

### 7.1. `lambda` Fonksiyonları

`lambda`, tek satırlık anonim fonksiyonlar tanımlamak için kullanılır.

**Örnek:**

```python
def summer(a, b):
    return a + b

print(summer(1, 3) * 9)  # Çıktı: 36

new_sum = lambda a, b: a + b
print(new_sum(4, 5))  # Çıktı: 9
```

**Not:** `lambda` fonksiyonları genellikle `map`, `filter`, veya `reduce` ile birlikte kullanılır. Atama yaparak kullanmak önerilmez.

### 7.2. `map`

`map`, bir fonksiyonu bir veri yapısındaki tüm elemanlara uygular.

**Örnek:**

```python
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

# Klasik döngü
for salary in salaries:
    print(new_salary(salary))

# map ile
print(list(map(new_salary, salaries)))  # Çıktı: [1200.0, 2400.0, 3600.0, 4800.0, 6000.0]

# lambda ile
print(list(map(lambda x: x * 20 / 100 + x, salaries)))  # Çıktı: [1200.0, 2400.0, 3600.0, 4800.0, 6000.0]
print(list(map(lambda x: x ** 2, salaries)))  # Çıktı: [1000000, 4000000, 9000000, 16000000, 25000000]
```

**Açıklama:** `map`, döngü yazmadan her elemana bir fonksiyon uygular ve bir `map` nesnesi döndürür. `list()` ile liste haline getirilir.

### 7.3. `filter`

`filter`, bir veri yapısındaki elemanları bir koşula göre filtreler.

**Örnek:**

```python
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, list_store)))  # Çıktı: [2, 4, 6, 8, 10]
```

**Açıklama:** `filter`, yalnızca `True` döndüren elemanları seçer.

### 7.4. `reduce`

`reduce`, bir veri yapısındaki elemanları birleştirerek tek bir sonuç üretir (örneğin, toplama).

**Örnek:**

```python
from functools import reduce

list_store = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, list_store))  # Çıktı: 10
```

**Açıklama:** `reduce`, sırayla elemanları birleştirir: `1 + 2 = 3`, `3 + 3 = 6`, `6 + 4 = 10`.

**Veri Biliminde Kullanım:** `map`, `filter`, ve `reduce`, veri ön işleme ve dönüştürme işlemlerinde sıkça kullanılır. Örneğin, bir veri setindeki sayısal değerleri dönüştürmek veya filtrelemek.

---

## 8. Veri Biliminde Pratik Örnek: Veri Ön İşleme

Aşağıda, döngüler ve ilgili yapıları kullanarak bir veri bilimi örneği verilmiştir:

```python
def preprocess_salaries(salaries, min_salary=2000, rate=15):
    """
    Maaşları filtreler ve artış uygular.

    Args:
        salaries (list): Maaş listesi.
        min_salary (int): Minimum maaş eşiği.
        rate (int): Artış oranı (%).

    Returns:
        list: İşlenmiş maaşlar.
    """
    # Minimum eşiğin üzerindeki maaşları filtrele
    filtered = list(filter(lambda x: x >= min_salary, salaries))
    
    # Artış uygula
    increased = list(map(lambda x: int(x * rate / 100 + x), filtered))
    
    # Toplam maaş
    total = reduce(lambda a, b: a + b, increased, 0)
    
    return {"filtered_salaries": filtered, "increased_salaries": increased, "total": total}

# Örnek kullanım
salaries = [1000, 2000, 3000, 4000, 5000]
result = preprocess_salaries(salaries)
print(result)
# Çıktı:
# {
#     'filtered_salaries': [2000, 3000, 4000, 5000],
#     'increased_salaries': [2300, 3450, 4600, 5750],
#     'total': 16100
# }
```

**Açıklama:** Bu fonksiyon, maaşları filtreler, artış uygular ve toplamı hesaplar. `filter`, `map`, ve `reduce` kullanımı, döngülerin fonksiyonel alternatiflerini gösterir.

---

## 9. Yaygın Hatalar ve Çözümleri

- **Hata:** Sonsuz `while` Döngüsü

  - **Sebep:** Koşul hiçbir zaman `False` olmuyor.
  - **Çözüm:** Koşulun değiştiğinden emin olun veya `break` kullanın.

    ```python
    count = 0
    while True:
        if count >= 5:
            break
        print(count)
        count += 1
    ```

- **Hata:** `map` veya `filter` Sonuçlarının Kullanılmaması

  - **Sebep:** `map` ve `filter` bir nesne döndürür, doğrudan yazdırılmaz.
  - **Çözüm:** `list()` ile liste haline getirin.

    ```python
    result = map(lambda x: x * 2, [1, 2, 3])
    print(list(result))  # Çıktı: [2, 4, 6]
    ```

- **Hata:** Yanlış İndeks Kullanımı

  - **Sebep:** `range` veya `enumerate` ile indeksler doğru hesaplanmamış.
  - **Çözüm:** İndeks aralığını kontrol edin.

    ```python
    for i in range(len("abc")):  # Doğru: 0, 1, 2
        print(i)
    ```

---

## 10. En İyi Uygulamalar ve İpuçları

- **Okunabilir Kod Yazın:** Döngülerde anlamlı değişken isimleri kullanın (örneğin, `salary` yerine `s` kullanmaktan kaçının).
- **Fonksiyonel Alternatifler Kullanın:** Mümkünse `map`, `filter`, veya liste comprehensions ile döngüleri değiştirin.
- **Erken Çıkış:** Gereksiz iterasyonları önlemek için `break` veya `continue` kullanın.
- **Veri Biliminde Kullanım:** Döngüleri veri ön işleme, filtreleme ve dönüştürme için optimize edin.

  ```python
  # Liste comprehension ile daha kısa
  salaries = [1000, 2000, 3000]
  increased = [int(s * 20 / 100 + s) for s in salaries]
  ```

- **Performans İyileştirmesi:** Büyük veri setlerinde döngüler yerine `numpy` veya `pandas` gibi kütüphaneleri kullanın.

---

## 11. Sonuç

Döngüler, Python'da veri yapıları üzerinde yinelemeli işlemler yapmak için temel bir yapıdır. `for` ve `while` döngüleri, veri işleme ve analizde sıkça kullanılırken; `enumerate`, `zip`, `lambda`, `map`, `filter`, ve `reduce` gibi yapılar, döngülerin daha kısa ve etkili bir şekilde yazılmasını sağlar. Veri bilimi ve makine öğrenmesi projelerinde bu yapılar, veri ön işleme, filtreleme, dönüştürme ve modelleme gibi görevlerde kritik rol oynar. Bu notlar, döngülerin ve ilgili yapıların temel kullanımlarını, en iyi uygulamalarını ve pratik örneklerini kapsamaktadır.

### 11.1. Öneri

Bir sonraki adım olarak, döngüleri ve ilgili yapıları bir veri bilimi projesinde kullanarak pratik yapabilirsiniz. Örneğin:
- Bir veri setindeki sayısal değerleri filtreleyin ve dönüştürün.
- Birden fazla veri setini `zip` ile birleştirerek analiz edin.
- `map` ve `filter` kullanarak veri ön işleme görevlerini optimize edin.
