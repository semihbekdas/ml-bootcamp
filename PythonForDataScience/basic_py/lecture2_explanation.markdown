# Python Ders 2: Veri Yapıları (Data Structures)

Bu notlar, Python'daki temel veri yapılarını (sayılar, karakter dizileri, boolean, liste, sözlük, demet, set) ayrıntılı bir şekilde açıklamaktadır. Her veri yapısının özellikleri, metodları ve kullanım senaryoları ele alınmıştır. Eksik noktalar tamamlanmış ve veri bilimi/makine öğrenmesi projelerine yönelik pratik örnekler eklenmiştir. Python'daki veri yapıları, veri analizi, makine öğrenmesi modelleri ve algoritma geliştirme gibi alanlarda temel yapı taşlarıdır.

---

## 1. Veri Yapılarına Giriş ve Hızlı Özet

Python'daki veri yapıları, verileri organize etmek ve işlemek için kullanılır. Her veri yapısının kendine özgü özellikleri vardır ve farklı senaryolarda avantaj sağlar. Python'daki temel veri yapıları şunlardır:

- **Sayılar (Numbers):** `int`, `float`, `complex`
- **Karakter Dizileri (Strings):** `str`
- **Boolean (True/False):** `bool`
- **Liste (List):** Değiştirilebilir, sıralı, kapsayıcı
- **Sözlük (Dictionary):** Değiştirilebilir, key-value çiftleri, sıralı (Python 3.7+)
- **Demet (Tuple):** Değiştirilemez, sıralı, kapsayıcı
- **Set (Küme):** Değiştirilebilir, sırasız, eşsiz elemanlar, kapsayıcı

**Not:** Liste, sözlük, demet ve set, aynı zamanda Python'da **Collections (Arrays)** olarak sınıflandırılır.

### 1.1. Veri Yapılarının Özellikleri

| Veri Yapısı | Değiştirilebilir mi? | Sıralı mı? | Kapsayıcı mı? | Örnek Kullanım |
| --- | --- | --- | --- | --- |
| Sayılar | Hayır | \- | Hayır | Matematiksel işlemler |
| String | Hayır | Evet | Hayır | Metin işleme |
| Boolean | Hayır | \- | Hayır | Koşullu ifadeler |
| Liste | Evet | Evet | Evet | Veri toplama, sıralama |
| Sözlük | Evet | Evet (3.7+) | Evet | Key-value tabanlı veri saklama |
| Demet | Hayır | Evet | Evet | Sabit veri saklama |
| Set | Evet | Hayır | Evet | Küme işlemleri, eşsiz elemanlar |

### 1.2. Veri Yapılarının Veri Bilimindeki Rolü

- **Sayılar:** Veri analizinde matematiksel hesaplamalar için kullanılır (örneğin, ortalama, standart sapma).
- **String:** Veri ön işleme sırasında metin verilerini temizlemek veya işlemek için kullanılır.
- **Liste:** Veri setlerini veya özellik vektörlerini saklamak için idealdir.
- **Sözlük:** Veri setlerinde sütun-etiket eşleştirmeleri veya model parametreleri için kullanılır.
- **Demet:** Sabit veri yapıları (örneğin, koordinatlar) için tercih edilir.
- **Set:** Eşsiz veri noktalarını bulmak veya veri temizliği için kullanılır.

---

## 2. Sayılar (Numbers): `int`, `float`, `complex`

Sayılar, Python'daki temel veri tiplerinden biridir ve matematiksel işlemler için kullanılır.

### 2.1. Türler

- **Integer (**`int`**):** Tam sayılar (örneğin, `5`, `-10`).
- **Float (**`float`**):** Ondalık sayılar (örneğin, `3.14`, `-0.001`).
- **Complex (**`complex`**):** Karmaşık sayılar (örneğin, `2 + 3j`).

### 2.2. Örnekler

```python
# Integer
x = 46
print(type(x))  # <class 'int'>

# Float
x = 10.3
print(type(x))  # <class 'float'>

# Complex
x = 2j + 1
print(type(x))  # <class 'complex'>
```

### 2.3. Matematiksel İşlemler

```python
a = 5
b = 10.5

# Çarpma
print(a * 3)  # 15

# Bölme (float sonuç)
print(a / 7)  # 0.7142857142857143

# Çarpma ve bölme
print(a * b / 10)  # 5.25

# Üs alma (kare)
print(a ** 2)  # 25

# Mod alma
print(a % 3)  # 2

# Tam sayı bölmesi
print(7 // 3)  # 2

# Normal bölme
print(7 / 3)  # 2.3333333333333335
```

**Not:** İşlemler arasında boşluk bırakmak, kod okunabilirliğini artırır.

### 2.4. Tür Dönüşümleri

Sayı türleri arasında dönüşüm yapmak için `int()`, `float()`, ve `complex()` fonksiyonları kullanılır.

```python
a = 5
b = 10.5

# Float'ı integer'a çevirme
print(int(b))  # 10

# Integer'ı float'a çevirme
print(float(a))  # 5.0

# İşlem sonucu dönüşüm
c = a * b / 10  # 5.25
print(int(c))  # 5
```

**Veri Biliminde Kullanım:**

- `int` ve `float`, veri analizi sırasında sayısal sütunlarla çalışırken sıkça kullanılır.
- `complex`, sinyal işleme veya bilimsel hesaplamalarda kullanılır (örneğin, Fourier dönüşümleri).

---

## 3. Karakter Dizileri (Strings): `str`

Karakter dizileri, metin verilerini saklamak ve işlemek için kullanılır. Değiştirilemez (immutable) ve sıralıdır.

### 3.1. Tanımlama

```python
name = "John"
print(name)  # John

name = 'John'
print(name)  # John

# Çok satırlı string
long_str = """Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizileri (Strings): str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""
print(long_str)
```

**Not:** Tek (`'`) veya çift (`"`) tırnak kullanımı arasında fark yoktur. Çok satırlı stringler için üç tırnak (`"""`) kullanılır.

### 3.2. Elemanlara Erişim

```python
name = "John"

# İlk karakter
print(name[0])  # J

# Son karakter
print(name[-1])  # n

# 3. karakter
print(name[2])  # h
```

### 3.3. Dilimleme (Slicing)

```python
# İlk iki karakter
print(name[0:2])  # Jo

# İlk 10 karakter (long_str)
print(long_str[0:10])  # Veri Yapıl
```

### 3.4. İçerik Sorgulama

```python
# Küçük harf duyarlılığı
print("veri" in long_str)  # False
print("Veri" in long_str)  # True

print("bool" in long_str)  # True
```

### 3.5. String Metodları

String'ler, metin işleme için birçok yerleşik metoda sahiptir. Tüm metodları görmek için:

```python
print(dir(str))  # String metodlarının listesi
```

#### 3.5.1. `len()`: Uzunluk

```python
name = "john"
print(len(name))  # 4

print(len("semihbekdas"))  # 11
```

**Not:** `len()`, bir Python yerleşik fonksiyonudur, metod değildir.

#### 3.5.2. `upper()` ve `lower()`: Büyük/Küçük Harf Dönüşümü

```python
print("machine".upper())  # MACHINE
print("LEARNING".lower())  # learning
```

#### 3.5.3. `replace()`: Karakter Değiştirme

```python
hi = "Hello AI Era"
print(hi.replace("l", "p"))  # Heppo AI Era
```

#### 3.5.4. `split()`: Bölme

```python
print("Hello AI Era".split())  # ['Hello', 'AI', 'Era']
print("a,b,c".split(","))  # ['a', 'b', 'c']
```

#### 3.5.5. `strip()`: Kırpma

```python
print(" ofofo ".strip())  # ofofo
print("ofofo".strip("o"))  # f
```

#### 3.5.6. `capitalize()`: İlk Harfi Büyütme

```python
print("foo".capitalize())  # Foo
```

#### 3.5.7. `startswith()` ve `endswith()`: Başlangıç/Bitiş Kontrolü

```python
print("foo".startswith("f"))  # True
print("foo".endswith("o"))  # True
```

**Veri Biliminde Kullanım:**

- String metodları, veri temizleme sırasında sıkça kullanılır (örneğin, metin verilerinde büyük/küçük harf uyumu, boşluk temizleme).
- `split()` ve `replace()`, doğal dil işleme (NLP) projelerinde metin tokenizasyonu için önemlidir.

---

## 4. Boolean (True/False): `bool`

Boolean, yalnızca `True` veya `False` değerlerini alır ve koşullu ifadelerde kullanılır.

### 4.1. Örnekler

```python
print(type(True))  # <class 'bool'>

# Karşılaştırma işlemleri
print(5 == 4)  # False
print(3 == 2)  # False
print(1 == 1)  # True
print(type(3 == 2))  # <class 'bool'>
```

**Veri Biliminde Kullanım:**

- Boolean değerler, veri filtreleme (örneğin, `df[df['age'] > 30]`) ve koşullu işlemler için kullanılır.

---

## 5. Liste (List)

Listeler, değiştirilebilir, sıralı ve kapsayıcı veri yapılarıdır. Farklı veri tiplerini içerebilir.

### 5.1. Tanımlama ve Özellikler

```python
notes = [1, 2, 3, 4]
print(type(notes))  # <class 'list'>

names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]  # Kapsayıcı
```

### 5.2. Elemanlara Erişim

```python
print(not_nam[0])  # 1
print(not_nam[5])  # True
print(not_nam[6])  # [1, 2, 3]
print(not_nam[6][1])  # 2 (İç içe liste)

print(type(not_nam[6]))  # <class 'list'>
print(type(not_nam[6][1]))  # <class 'int'>
```

### 5.3. Eleman Değiştirme

```python
notes[0] = 99
print(notes)  # [99, 2, 3, 4]
```

### 5.4. Dilimleme

```python
print(not_nam[0:4])  # [1, 2, 3, 'a']
```

### 5.5. Liste Metodları

Tüm metodları görmek için:

```python
print(dir(list))
```

#### 5.5.1. `len()`: Uzunluk

```python
print(len(notes))  # 4
print(len(not_nam))  # 7
```

#### 5.5.2. `append()`: Eleman Ekleme

```python
notes.append(100)
print(notes)  # [99, 2, 3, 4, 100]
```

#### 5.5.3. `pop()`: Eleman Silme

```python
notes.pop(0)  # İlk elemanı siler
print(notes)  # [2, 3, 4, 100]
```

#### 5.5.4. `insert()`: Belirli İndekse Ekleme

```python
notes.insert(2, 99)  # 2. indekse 99 ekler
print(notes)  # [2, 3, 99, 4, 100]
```

**Veri Biliminde Kullanım:**

- Listeler, veri setlerindeki satırları veya özellikleri saklamak için kullanılır (örneğin, `[age, salary, experience]`).
- Makine öğrenmesi modellerinde özellik vektörleri genellikle liste olarak temsil edilir.

---

## 6. Sözlük (Dictionary)

Sözlükler, key-value çiftleriyle veri saklar. Değiştirilebilir ve Python 3.7+ ile sıralıdır.

### 6.1. Tanımlama

```python
dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}
print(dictionary["REG"])  # Regression

# İç içe sözlük
dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}
print(dictionary["CART"][1])  # 30
```

### 6.2. Metodlar ve İşlemler

#### 6.2.1. Key Sorgulama

```python
print("REG" in dictionary)  # True
print("YSA" in dictionary)  # False
```

#### 6.2.2. Value Sorgulama

```python
print("RMSE" in dictionary.values())  # False (doğru sorgulama için iç listeye bakılmalı)
```

#### 6.2.3. Key ile Value'ya Erişim

```python
print(dictionary["REG"])  # ['RMSE', 10]
print(dictionary.get("REG"))  # ['RMSE', 10]
```

**Not:** `get()` metodu, key yoksa hata yerine `None` döndürür.

#### 6.2.4. Value Değiştirme

```python
dictionary["REG"] = ["YSA", 10]
print(dictionary["REG"])  # ['YSA', 10]
```

#### 6.2.5. Tüm Key'ler ve Value'lar

```python
print(dictionary.keys())  # dict_keys(['REG', 'LOG', 'CART'])
print(dictionary.values())  # dict_values([['YSA', 10], ['MSE', 20], ['SSE', 30]])
```

#### 6.2.6. Key-Value Çiftlerini Listeleme

```python
print(dictionary.items())  # dict_items([('REG', ['YSA', 10]), ('LOG', ['MSE', 20]), ('CART', ['SSE', 30])])
```

#### 6.2.7. Güncelleme

```python
dictionary.update({"REG": 11})
print(dictionary["REG"])  # 11

dictionary.update({"RF": 10})  # Yeni key-value ekleme
print(dictionary)  # {'REG': 11, 'LOG': ['MSE', 20], 'CART': ['SSE', 30], 'RF': 10}
```

#### 6.2.8. Key Silme

```python
dictionary = {"name": "Ali", "age": 25, "city": "Istanbul"}
del dictionary["age"]
print(dictionary)  # {'name': 'Ali', 'city': 'Istanbul'}
```

**Veri Biliminde Kullanım:**

- Sözlükler, veri setlerinde sütun-etiket eşleştirmeleri (örneğin, `{"age": "Yaş", "salary": "Maaş"}`) veya model hiperparametreleri için kullanılır.

---

## 7. Demet (Tuple)

Demetler, değiştirilemez, sıralı ve kapsayıcı veri yapılarıdır.

### 7.1. Tanımlama ve Özellikler

```python
t = ("john", "mark", 1, 2)
print(type(t))  # <class 'tuple'>

print(t[0])  # john
print(t[0:3])  # ('john', 'mark', 1)
```

### 7.2. Değiştirilemezlik

```python
# Hata: t[0] = 99  # TypeError: 'tuple' object does not support item assignment

# Çözüm: Listeye çevirip değiştirme
t = list(t)
t[0] = 99
t = tuple(t)
print(t)  # (99, 'mark', 1, 2)
```

**Veri Biliminde Kullanım:**

- Demetler, sabit veri yapıları (örneğin, koordinatlar: `(x, y)`) veya fonksiyonlardan birden fazla değer döndürmek için kullanılır.

---

## 8. Set (Küme)

Set'ler, sırasız, eşsiz elemanlar içeren ve değiştirilebilir veri yapılarıdır. Küme işlemleri için idealdir.

### 8.1. Tanımlama

```python
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
print(type(set1))  # <class 'set'>
```

### 8.2. Küme İşlemleri

#### 8.2.1. `difference()`: Fark

```python
print(set1.difference(set2))  # {5}
print(set1 - set2)  # {5}

print(set2.difference(set1))  # {2}
```

#### 8.2.2. `symmetric_difference()`: Simetrik Fark

```python
print(set1.symmetric_difference(set2))  # {2, 5}
```

#### 8.2.3. `intersection()`: Kesişim

```python
print(set1.intersection(set2))  # {1, 3}
print(set1 & set2)  # {1, 3}
```

#### 8.2.4. `union()`: Birleşim

```python
print(set1.union(set2))  # {1, 2, 3, 5}
```

#### 8.2.5. `isdisjoint()`: Kesişim Boş mu?

```python
set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])
print(set1.isdisjoint(set2))  # False
```

#### 8.2.6. `issubset()`: Alt Küme mi?

```python
print(set1.issubset(set2))  # True
```

#### 8.2.7. `issuperset()`: Üst Küme mi?

```python
print(set2.issuperset(set1))  # True
```

**Veri Biliminde Kullanım:**

- Set'ler, veri temizleme sırasında eşsiz değerleri bulmak (örneğin, bir sütundaki benzersiz kategoriler) veya küme tabanlı analizler için kullanılır.

---

## 9. Veri Biliminde Pratik Örnek: Veri Temizleme

Aşağıda, veri bilimi projelerinde veri yapılarının nasıl kullanıldığına dair bir örnek verilmiştir:

```python
# Veri seti simülasyonu
data = {
    "names": ["John", "Jane", "John", "Alice"],
    "ages": [25, 30, 25, 28],
    "cities": ["Istanbul", "Ankara", "Istanbul", "Izmir"]
}

# Eşsiz isimleri bulma (Set)
unique_names = set(data["names"])
print(unique_names)  # {'John', 'Jane', 'Alice'}

# Yaş ortalaması hesaplama (Liste ve Sayılar)
average_age = sum(data["ages"]) / len(data["ages"])
print(average_age)  # 27.0

# Şehir isimlerini büyük harfe çevirme (String)
data["cities"] = [city.upper() for city in data["cities"]]
print(data["cities"])  # ['ISTANBUL', 'ANKARA', 'ISTANBUL', 'IZMIR']
```

## 10. Yaygın Hatalar ve Çözümleri

- **Hata:** `TypeError: 'tuple' object does not support item assignment`

  - **Çözüm:** Demeti listeye çevirip değiştirin: `t = list(t)`.

- **Hata:** `KeyError` (Sözlükte olmayan bir key'e erişim)

  - **Çözüm:** `get()` metodu kullanın: `dictionary.get("key", default_value)`.

- **Hata:** Set'lerde indeksleme

  - **Çözüm:** Set'ler sırasızdır; indeksleme yerine döngü veya küme işlemleri kullanın.

## 11. Sonuç

Python'daki veri yapıları, veri bilimi ve makine öğrenmesi projelerinde temel yapı taşlarıdır. Sayılar matematiksel hesaplamalar, string'ler metin işleme, boolean'lar koşullu ifadeler, listeler veri toplama, sözlükler key-value eşleştirmeleri, demetler sabit veriler ve set'ler eşsiz elemanlar için kullanılır. Bu notlar, her veri yapısının özelliklerini, metodlarını ve pratik örneklerini kapsamaktadır. Bir sonraki adım olarak, bu veri yapılarını bir veri bilimi projesinde (örneğin, veri temizleme veya model eğitimi) kullanarak pratik yapabilirsiniz.
