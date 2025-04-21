# Python Ders 3: Fonksiyonlar, Koşullar, Döngüler ve Comprehensions

Bu notlar, Python'da **fonksiyonlar**, **koşullar**, **döngüler** ve **comprehensions** konularını ayrıntılı bir şekilde açıklamaktadır. Fonksiyonlar, tekrar eden işlemleri otomatikleştirmek için kullanılırken; koşullar, program akışını kontrol eder; döngüler, veri yapıları üzerinde yinelemeli işlemler yapar; comprehensions ise daha kısa ve okunabilir kod yazmayı sağlar. Notlar, veri bilimi ve makine öğrenmesi projelerine yönelik pratik örneklerle zenginleştirilmiştir. Eksik noktalar tamamlanmış ve her bölümün kullanım senaryoları netleştirilmiştir.

---

## 1. Fonksiyonlar (Functions)

Fonksiyonlar, tekrar eden görevleri otomatikleştirmek ve kodu modüler hale getirmek için kullanılır. Python'da fonksiyonlar `def` anahtar kelimesiyle tanımlanır ve parametreler alarak çeşitli işlemler gerçekleştirebilir.

### 1.1. Fonksiyon Okuryazarlığı

Python'daki yerleşik fonksiyonların (örneğin, `print()`) nasıl çalıştığını öğrenmek için `help()` veya `?` kullanılabilir.

```python
# Fonksiyonun belgelerini görüntüleme
help(print)
# veya Jupyter Notebook'ta: ?print
```

**Örnek:** `print()` fonksiyonunun `sep` parametresi

```python
print("a", "b")  # Çıktı: a b
print("a", "b", sep="__")  # Çıktı: a__b
```

**Açıklama:** `sep` parametresi, birden fazla argüman arasında kullanılacak ayırıcıyı belirler. Varsayılan değeri bir boşluktur (`" "`).

### 1.2. Fonksiyon Tanımlama

Fonksiyonlar, `def` anahtar kelimesiyle tanımlanır ve bir isim, parametreler (isteğe bağlı) ve gövde (body) içerir.

**Basit Fonksiyon:**

```python
def calculate(x):
    print(x * 2)

calculate(5)  # Çıktı: 10
```

**İki Parametreli Fonksiyon:**

```python
def summer(arg1, arg2):
    print(arg1 + arg2)

summer(7, 8)  # Çıktı: 15
summer(arg2=8, arg1=7)  # Çıktı: 15
```

**Açıklama:** Parametreler sırayla veya isimle (keyword arguments) geçirilebilir.

### 1.3. Docstring

Docstring, fonksiyonun ne yaptığını, parametrelerini ve dönüş değerini açıklayan bir belgedir. Üç tırnak (`"""`) kullanılarak yazılır.

```python
def summer(arg1, arg2):
    """
    Sum of two numbers.

    Args:
        arg1 (int, float): First number.
        arg2 (int, float): Second number.

    Returns:
        int, float: Sum of the two numbers.
    """
    print(arg1 + arg2)

summer(1, 3)  # Çıktı: 4
```

**Açıklama:** Docstring, kodun okunabilirliğini artırır ve diğer geliştiricilerin fonksiyonu anlamasını kolaylaştırır. `numpydoc` veya `Google` docstring formatları yaygın olarak kullanılır.

### 1.4. Fonksiyon Gövdesi (Statements/Body)

Fonksiyonun gövdesi, fonksiyonun gerçekleştireceği işlemleri içerir.

```python
def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi()  # Çıktı: Merhaba\nHi\nHello
say_hi("semih")  # Çıktı: semih\nHi\nHello
```

**Örnek: Liste ile Çalışan Fonksiyon**

```python
list_store = []

def add_element(a, b):
    """
    Multiplies two numbers, appends the result to a global list, and prints the list.

    Args:
        a (int): First number.
        b (int): Second number.
    """
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 8)   # Çıktı: [8]
add_element(18, 8)  # Çıktı: [8, 144]
add_element(180, 10)  # Çıktı: [8, 144, 1800]
```

**Açıklama:** Fonksiyon, global bir listeyi (`list_store`) günceller ve her çağrıda yeni bir eleman ekler.

### 1.5. Ön Tanımlı Parametreler (Default Parameters)

Fonksiyon parametrelerine varsayılan değerler atanabilir.

```python
def divide(a, b=1):
    print(a / b)

divide(10)  # Çıktı: 10.0
divide(10, 2)  # Çıktı: 5.0
```

**Örnek:**

```python
def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi()  # Çıktı: Merhaba\nHi\nHello
say_hi("mrb")  # Çıktı: mrb\nHi\nHello
```

**Açıklama:** Varsayılan parametreler, fonksiyon çağrısında değer belirtilmezse kullanılır.

### 1.6. Ne Zaman Fonksiyon Yazılmalı?

Fonksiyonlar, **DRY (Don't Repeat Yourself)** ilkesine uygun olarak tekrar eden işlemleri otomatikleştirmek için yazılır.

**Örnek: Tekrar Eden İşlem**

```python
# Tekrar eden işlem
print((56 + 15) / 80)  # Çıktı: 0.8875
print((17 + 45) / 70)  # Çıktı: 0.8857142857142857
print((52 + 45) / 80)  # Çıktı: 1.2125
```

**Fonksiyonla Çözüm:**

```python
def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)

calculate(98, 12, 78)  # Çıktı: 1.4102564102564104
```

**Açıklama:** Fonksiyon, aynı işlemi tekrar tekrar yazmayı önler ve kodu daha düzenli hale getirir.

### 1.7. `return` ile Fonksiyon Çıktılarını Kullanma

`return`, fonksiyonun sonucunu dış dünyaya döndürmesini sağlar. `print()` yalnızca ekrana yazdırır, ancak `return` ile değer başka işlemlerde kullanılabilir.

```python
def calculate(varm, moisture, charge):
    return (varm + moisture) / charge

result = calculate(98, 12, 78) * 10
print(result)  # Çıktı: 14.102564102564102
```

**Çoklu Değer Döndürme:**

```python
def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output  # Tuple olarak döner

# Değerleri ayırma
varma, moisturea, chargea, outputa = calculate(98, 12, 78)
print(f"Varm: {varma}, Moisture: {moisturea}, Charge: {chargea}, Output: {outputa}")
# Çıktı: Varm: 196, Moisture: 24, Charge: 156, Output: 1.4102564102564104
```

**Açıklama:** `return` ile birden fazla değer döndürülebilir ve bunlar tuple olarak alınabilir.

### 1.8. Fonksiyon İçinden Fonksiyon Çağırma

Fonksiyonlar, başka fonksiyonları çağırabilir. Bu, modüler ve karmaşık işlemleri basitleştirir.

```python
def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

def standardization(a, p):
    return a * 10 / 100 * p * p

def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 12)  # Çıktı: 172.8
```

**Açıklama:** `all_calculation`, `calculate` ve `standardization` fonksiyonlarını çağırarak karmaşık bir işlemi adım adım gerçekleştirir.

### 1.9. Lokal ve Global Değişkenler

- **Lokal Değişkenler:** Fonksiyon içinde tanımlanır ve sadece fonksiyon kapsamında erişilebilir.
- **Global Değişkenler:** Fonksiyon dışında tanımlanır ve her yerden erişilebilir.

```python
list_store = [1, 2]  # Global değişken

def add_element(a, b):
    c = a * b  # Lokal değişken
    list_store.append(c)  # Global listeye erişim
    print(list_store)

add_element(1, 9)  # Çıktı: [1, 2, 9]
```

**Açıklama:** Lokal bir değişken (`c`), global bir veri yapısına (`list_store`) eklenebilir.

**Not:** Global değişkenleri değiştirmek için `global` anahtar kelimesi kullanılabilir, ancak bu genellikle önerilmez.

### 1.10. Veri Biliminde Fonksiyon Kullanımı

Fonksiyonlar, veri bilimi projelerinde veri ön işleme, model eğitimi ve değerlendirme gibi tekrar eden görevleri otomatikleştirmek için kullanılır. Örnek:

```python
def preprocess_data(data, threshold):
    """
    Veriyi filtreler ve eksik değerleri doldurur.

    Args:
        data (list): Sayısal veri listesi.
        threshold (float): Filtreleme eşiği.

    Returns:
        list: İşlenmiş veri.
    """
    # Eksik değerleri 0 ile doldur
    data = [x if x is not None else 0 for x in data]
    # Eşik değerin üzerindeki verileri filtrele
    return [x for x in data if x > threshold]

data = [1, None, 5, 3, None, 8]
processed = preprocess_data(data, 2)
print(processed)  # Çıktı: [5, 3, 8]
```

---

## 2. Koşullar (Conditions)

Koşullu ifadeler, programın akışını belirli koşullara göre kontrol etmek için kullanılır. Python'da `if`, `elif`, ve `else` anahtar kelimeleri kullanılır.

### 2.1. Temel Söz Dizimi

```python
def check_number(num):
    if num > 0:
        print("Pozitif")
    elif num == 0:
        print("Sıfır")
    else:
        print("Negatif")

check_number(5)   # Çıktı: Pozitif
check_number(0)   # Çıktı: Sıfır
check_number(-3)  # Çıktı: Negatif
```

### 2.2. Mantıksal Operatörler

- `and`: Her iki koşul da doğruysa `True`.
- `or`: Koşullardan biri doğruysa `True`.
- `not`: Koşulu tersine çevirir.

```python
def check_range(num):
    if num > 0 and num < 10:
        print("0-10 arasında")
    elif num >= 10 or num <= 0:
        print("0-10 dışında")

check_range(5)  # Çıktı: 0-10 arasında
check_range(15)  # Çıktı: 0-10 dışında
```

### 2.3. İç İçe Koşullar

```python
def classify_age(age):
    if age >= 0:
        if age < 18:
            print("Çocuk")
        elif age < 65:
            print("Yetişkin")
        else:
            print("Yaşlı")
    else:
        print("Geçersiz yaş")

classify_age(25)  # Çıktı: Yetişkin
classify_age(70)  # Çıktı: Yaşlı
classify_age(-5)  # Çıktı: Geçersiz yaş
```

### 2.4. Veri Biliminde Koşullu İfadeler

Koşullu ifadeler, veri filtreleme ve kategorizasyon için sıkça kullanılır.

```python
def categorize_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

scores = [95, 82, 75, 60]
grades = [categorize_score(score) for score in scores]
print(grades)  # Çıktı: ['A', 'B', 'C', 'D']
```

---

## 3. Döngüler (Loops)

Döngüler, veri yapıları üzerinde yinelemeli işlemler yapmak için kullanılır. Python'da `for` ve `while` döngüleri bulunur.

### 3.1. `for` Döngüsü

`for` döngüsü, bir veri yapısında (örneğin, liste, string) sırayla elemanlar üzerinde gezinir.

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)  # Çıktı: 2, 4, 6, 8, 10
```

**`range()` ile Kullanım:**

```python
for i in range(5):
    print(i)  # Çıktı: 0, 1, 2, 3, 4
```

**İç İçe Döngü:**

```python
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for elem in row:
        print(elem)  # Çıktı: 1, 2, 3, 4, 5, 6
```

### 3.2. `while` Döngüsü

`while` döngüsü, bir koşul doğru olduğu sürece çalışır.

```python
count = 0
while count < 5:
    print(count)
    count += 1  # Çıktı: 0, 1, 2, 3, 4
```

**Dikkat:** Sonsuz döngülerden kaçınmak için koşulun sonunda yanlış olacağından emin olun.

### 3.3. Döngü Kontrol İfadeleri

- `break`: Döngüyü sonlandırır.
- `continue`: Mevcut iterasyonu atlar, döngüye devam eder.

```python
for i in range(10):
    if i == 3:
        continue  # 3'ü atla
    if i == 7:
        break  # 7'de döngüyü sonlandır
    print(i)  # Çıktı: 0, 1, 2, 4, 5, 6
```

### 3.4. Veri Biliminde Döngüler

Döngüler, veri işleme ve modelleme sırasında sıkça kullanılır.

```python
# Veriyi normalizasyon
data = [10, 20, 30, 40, 50]
max_val = max(data)
normalized = []
for x in data:
    normalized.append(x / max_val)
print(normalized)  # Çıktı: [0.2, 0.4, 0.6, 0.8, 1.0]
```

---

## 4. Comprehensions

Comprehensions, döngülerin daha kısa ve okunabilir bir alternatifidir. Liste, sözlük ve set comprehensions bulunur.

### 4.1. Liste Comprehension

```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Çıktı: [1, 4, 9, 16, 25]
```

**Koşullu Liste Comprehension:**

```python
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # Çıktı: [4, 16]
```

### 4.2. Sözlük Comprehension

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)  # Çıktı: {'a': 1, 'b': 2, 'c': 3}
```

### 4.3. Set Comprehension

```python
numbers = [1, 1, 2, 3, 3, 4]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # Çıktı: {16, 1, 4, 9}
```

### 4.4. Veri Biliminde Comprehensions

Comprehensions, veri ön işleme ve dönüştürme için sıkça kullanılır.

```python
# Veriyi z-skor normalizasyonu
data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)
std = (sum([(x - mean)**2 for x in data]) / len(data))**0.5
z_scores = [(x - mean) / std for x in data]
print(z_scores)  # Çıktı: [-1.414, -0.707, 0.0, 0.707, 1.414]
```

---

## 5. Veri Biliminde Pratik Örnek: Veri Ön İşleme

Aşağıda, fonksiyonlar, koşullar, döngüler ve comprehensions kullanarak bir veri ön işleme örneği verilmiştir:

```python
def preprocess_dataset(data, threshold=0):
    """
    Veriyi filtreler, eksik değerleri doldurur ve normalleştirir.

    Args:
        data (list): Sayısal veri listesi.
        threshold (float): Filtreleme eşiği.

    Returns:
        list: Normalleştirilmiş veri.
    """
    # Eksik değerleri doldur
    data = [0 if x is None else x for x in data]
    
    # Eşik değerin altındaki verileri filtrele
    filtered = [x for x in data if x >= threshold]
    
    # Normalizasyon
    if filtered:
        max_val = max(filtered)
        normalized = [x / max_val for x in filtered]
        return normalized
    return []

# Örnek veri
data = [10, None, 5, 20, None, 15]
result = preprocess_dataset(data, threshold=10)
print(result)  # Çıktı: [0.5, 1.0, 0.75]
```

## 6. Yaygın Hatalar ve Çözümleri

- **Hata:** `ZeroDivisionError` (Sıfıra bölme)

  - **Çözüm:** Fonksiyonda sıfıra bölme kontrolü yapın:

    ```python
    def divide(a, b):
        if b == 0:
            return "Sıfıra bölme hatası"
        return a / b
    ```

- **Hata:** Sonsuz `while` döngüsü

  - **Çözüm:** Koşulun sonunda `False` olacağından emin olun veya `break` kullanın.

- **Hata:** Global değişkenlerin yanlış kullanımı

  - **Çözüm:** Global değişkenleri dikkatli kullanın veya parametre olarak geçirin.

## 7. Sonuç

Fonksiyonlar, koşullar, döngüler ve comprehensions, Python'da programlamanın temel taşlarıdır. Fonksiyonlar kodu modüler hale getirir, koşullar akışı kontrol eder, döngüler yinelemeli işlemler yapar ve comprehensions kısa, okunabilir kod yazmayı sağlar. Veri bilimi ve makine öğrenmesi projelerinde bu yapılar, veri ön işleme, model eğitimi ve değerlendirme gibi görevlerde kritik rol oynar. Bir sonraki adım olarak, bu yapıları bir veri bilimi projesinde (örneğin, bir veri setini temizleme ve analiz etme) kullanarak pratik yapabilirsiniz.
