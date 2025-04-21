# Python Ders 4: Koşullu İfadeler (Conditions) - Ayrıntılı Notlar

Bu notlar, Python'da **koşullu ifadeler (conditions)** konusunu ayrıntılı bir şekilde açıklamaktadır. Koşullu ifadeler, programın akışını belirli koşullara göre kontrol etmek için kullanılır ve `if`, `else`, `elif` anahtar kelimeleriyle tanımlanır. Notlar, temel kullanımları, mantıksal operatörleri, iç içe koşulları ve veri bilimi/makine öğrenmesi projelerine yönelik pratik örnekleri kapsamaktadır. Eksik noktalar tamamlanmış ve her bölümün kullanım senaryoları netleştirilmiştir.

---

## 1. Koşullu İfadeler Nedir?

Koşullu ifadeler, bir programın belirli koşullara bağlı olarak farklı yollar izlemesini sağlar. Python'da koşullu ifadeler, `if`, `else`, ve `elif` anahtar kelimeleriyle yazılır. Koşullar, genellikle **boolean** ifadelerle (`True` veya `False`) değerlendirilir ve programın hangi kod bloğunun çalıştırılacağını belirler.

### 1.1. Neden Kullanılır?

- **Karar Verme:** Programın farklı durumlara göre farklı işlemler yapmasını sağlar (örneğin, bir sayının pozitif mi, negatif mi olduğunu kontrol etme).
- **Veri Filtreleme:** Veri bilimi projelerinde veri setlerini koşullara göre filtrelemek için kullanılır.
- **Hata Kontrolü:** Giriş verilerinin doğruluğunu kontrol etmek için kullanılır.

### 1.2. Veri Biliminde Koşullu İfadeler

Veri bilimi ve makine öğrenmesi projelerinde koşullu ifadeler, veri ön işleme, kategorizasyon, ve model değerlendirme gibi alanlarda sıkça kullanılır. Örneğin:
- Bir veri setindeki eksik değerleri kontrol etme.
- Bir modelin tahminlerini belirli bir eşik değere göre sınıflandırma.

---

## 2. Koşullu İfadelerin Temel Yapısı

Python'da koşullu ifadeler aşağıdaki yapıya sahiptir:

```python
if koşul:
    # Koşul doğruysa çalışacak kod
elif başka_koşul:
    # Başka bir koşul doğruysa çalışacak kod
else:
    # Hiçbir koşul doğru değilse çalışacak kod
```

**Not:** Python'da girintiler (indentation) önemlidir. Koşullu ifadelerin gövdesi, 4 boşluk veya bir sekme (tab) ile girintilendirilir.

### 2.1. `if` İfadesi

`if` ifadesi, bir koşulun doğru (`True`) olması durumunda belirli bir kod bloğunu çalıştırır.

**Örnek:**

```python
if 1 == 1:
    print("eşit")  # Çıktı: eşit

if 1 == 2:
    print("eşit")  # Çalışmaz, çünkü koşul yanlış
```

**Fonksiyonla Kullanım:**

```python
def number_check(number):
    if number == 10:
        print("number is 10")

number_check(12)  # Çıktı: (Hiçbir şey yazdırmaz)
number_check(10)  # Çıktı: number is 10
```

**Açıklama:** Koşul doğruysa (`number == 10`), ilgili kod bloğu çalışır. Yanlışsa, hiçbir şey olmaz.

### 2.2. `else` İfadesi

`else`, `if` koşulu yanlış olduğunda çalışacak alternatif bir kod bloğu tanımlar.

**Örnek:**

```python
def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)  # Çıktı: number is not 10
number_check(10)  # Çıktı: number is 10
```

**Açıklama:** `else`, `if` koşulunun karşılanmadığı tüm durumları kapsar.

### 2.3. `elif` İfadesi

`elif` (else if), birden fazla koşulu kontrol etmek için kullanılır. İlk doğru koşul bulunana kadar kontrol edilir.

**Örnek:**

```python
def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(6)   # Çıktı: less than 10
number_check(12)  # Çıktı: greater than 10
number_check(10)  # Çıktı: equal to 10
```

**Açıklama:** `elif`, birden fazla koşulu sırayla kontrol eder ve sadece ilk doğru koşulun kod bloğu çalışır.

---

## 3. Mantıksal Operatörler

Koşullu ifadelerde birden fazla koşulu birleştirmek için mantıksal operatörler kullanılır:

- `and`: Her iki koşul da doğruysa `True`.
- `or`: Koşullardan biri doğruysa `True`.
- `not`: Koşulu tersine çevirir.

**Örnek:**

```python
def check_range(number):
    if number > 0 and number < 10:
        print("0 ile 10 arasında")
    elif number <= 0 or number >= 10:
        print("0 ile 10 dışında")
    else:
        print("Tanımsız")

check_range(5)   # Çıktı: 0 ile 10 arasında
check_range(15)  # Çıktı: 0 ile 10 dışında
```

**Örnek: `not` Kullanımı**

```python
def is_not_zero(number):
    if not number == 0:
        print("Sıfır değil")
    else:
        print("Sıfır")

is_not_zero(5)  # Çıktı: Sıfır değil
is_not_zero(0)  # Çıktı: Sıfır
```

---

## 4. İç İçe Koşullar (Nested Conditions)

Koşullu ifadeler, başka koşulların içinde kullanılabilir. Bu, daha karmaşık karar yapıları oluşturmak için faydalıdır.

**Örnek:**

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

**Açıklama:** İç içe koşullar, bir koşulun doğru olması durumunda daha spesifik kontroller yapılmasını sağlar.

---

## 5. Koşullu İfadelerde Kısa Yazım (Ternary Operator)

Python, basit koşullu ifadeleri tek satırda yazmak için **ternary operator** sunar.

**Söz Dizimi:**

```python
değer = sonuç1 if koşul else sonuç2
```

**Örnek:**

```python
number = 15
result = "Büyük" if number > 10 else "Küçük"
print(result)  # Çıktı: Büyük
```

**Açıklama:** Ternary operator, kısa ve okunabilir kod yazmak için kullanışlıdır, ancak karmaşık koşullarda okunabilirliği azaltabilir.

---

## 6. Veri Biliminde Koşullu İfadeler

Koşullu ifadeler, veri bilimi ve makine öğrenmesi projelerinde şu alanlarda sıkça kullanılır:

- **Veri Filtreleme:** Veri setindeki belirli koşullara uyan satırları seçme.
- **Kategorizasyon:** Sayısal verileri kategorilere ayırma (örneğin, yaş grupları).
- **Hata Kontrolü:** Eksik veya geçersiz verileri tespit etme.
- **Model Değerlendirme:** Tahmin sonuçlarını eşik değerlere göre sınıflandırma.

### 6.1. Örnek: Veri Kategorizasyonu

```python
def categorize_score(score):
    """
    Puanı harf notuna çevirir.

    Args:
        score (int): Öğrencinin puanı (0-100).

    Returns:
        str: Harf notu (A, B, C, D, F).
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Örnek kullanım
scores = [95, 82, 75, 55, 90]
grades = [categorize_score(score) for score in scores]
print(grades)  # Çıktı: ['A', 'B', 'C', 'F', 'A']
```

**Açıklama:** Bu fonksiyon, bir öğrencinin puanını harf notuna çevirir ve veri bilimi projelerinde sıkça kullanılan bir kategorizasyon örneğidir.

### 6.2. Örnek: Eksik Veri Kontrolü

```python
def check_missing(data):
    """
    Verideki eksik değerleri kontrol eder.

    Args:
        data (list): Kontrol edilecek veri listesi.

    Returns:
        bool: Eksik veri varsa True, yoksa False.
    """
    for item in data:
        if item is None:
            return True
    return False

# Örnek kullanım
data = [1, 2, None, 4, 5]
print(check_missing(data))  # Çıktı: True

data = [1, 2, 3, 4, 5]
print(check_missing(data))  # Çıktı: False
```

**Açıklama:** Eksik veri kontrolü, veri ön işleme sırasında sıkça kullanılan bir işlemdir.

### 6.3. Örnek: Model Tahminlerini Sınıflandırma

```python
def classify_prediction(probability, threshold=0.5):
    """
    Modelin tahmin olasılığını sınıflandırır.

    Args:
        probability (float): Modelin tahmin olasılığı (0-1).
        threshold (float): Sınıflandırma eşiği.

    Returns:
        str: 'Positive' veya 'Negative'.
    """
    if probability >= threshold:
        return "Positive"
    else:
        return "Negative"

# Örnek kullanım
predictions = [0.75, 0.45, 0.90, 0.30]
results = [classify_prediction(p) for p in predictions]
print(results)  # Çıktı: ['Positive', 'Negative', 'Positive', 'Negative']
```

**Açıklama:** Bu örnek, makine öğrenmesi modellerinin olasılıksal çıktılarını sınıflandırmak için koşullu ifadelerin nasıl kullanıldığını gösterir.

---

## 7. Yaygın Hatalar ve Çözümleri

- **Hata:** Girinti Hatası (`IndentationError`)

  - **Sebep:** Koşullu ifadelerin gövdesi doğru şekilde girintilendirilmemiş.
  - **Çözüm:** Her koşul bloğunun 4 boşluk veya bir sekme ile girintilendiğinden emin olun.

    ```python
    # Yanlış
    if True:
    print("Hata")  # IndentationError

    # Doğru
    if True:
        print("Doğru")
    ```

- **Hata:** Yanlış Koşul Sırası

  - **Sebep:** `elif` veya `else` kullanımlarında koşulların sırası mantıksız.
  - **Çözüm:** Daha spesifik koşulları önce, genel koşulları sonra yazın.

    ```python
    # Yanlış
    def check_number(num):
        if num > 0:
            print("Pozitif")
        elif num > 5:  # Hiçbir zaman çalışmaz
            print("5'ten büyük")

    # Doğru
    def check_number(num):
        if num > 5:
            print("5'ten büyük")
        elif num > 0:
            print("Pozitif")
    ```

- **Hata:** Karşılaştırma Operatörlerinin Yanlış Kullanımı

  - **Sebep:** `==` yerine `=` kullanılması.
  - **Çözüm:** Eşitlik kontrolü için `==` kullanın (`=` atama operatörüdür).

    ```python
    # Yanlış
    if number = 10:  # SyntaxError
        print("Hata")

    # Doğru
    if number == 10:
        print("Doğru")
    ```

---

## 8. En İyi Uygulamalar ve İpuçları

- **Okunabilir Koşullar Yazın:** Karmaşık koşulları parantezlerle gruplayın veya değişkenlere ayırın.

  ```python
  # Okunması zor
  if number > 0 and number < 10 or number == 15:
      print("Karmaşık")

  # Daha okunabilir
  is_valid_range = number > 0 and number < 10
  is_special = number == 15
  if is_valid_range or is_special:
      print("Daha iyi")
  ```

- **Ternary Operator Kullanımı:** Basit koşullarda ternary operator kullanarak kodu kısaltın.

  ```python
  status = "Yetişkin" if age >= 18 else "Çocuk"
  ```

- **Hata Kontrolü Ekleyin:** Geçersiz girişleri yakalamak için koşullu ifadeler kullanın.

  ```python
  def safe_divide(a, b):
      if b == 0:
          return "Sıfıra bölme hatası"
      return a / b
  ```

- **Veri Biliminde Kullanım:** Koşullu ifadeleri veri filtreleme ve kategorizasyon için döngüler veya comprehensions ile birleştirin.

  ```python
  data = [10, 20, None, 15]
  valid_data = [x for x in data if x is not None]
  print(valid_data)  # Çıktı: [10, 20, 15]
  ```

---

## 9. Pratik Örnek: Veri Bilimi Projesi

Aşağıda, koşullu ifadeleri kullanarak bir veri bilimi projesinde veri ön işleme ve kategorizasyon örneği verilmiştir:

```python
def preprocess_and_categorize(data, threshold=10, age_limit=18):
    """
    Veriyi temizler ve yaşa göre kategorize eder.

    Args:
        data (list): Yaş değerleri listesi (eksik değerler None olabilir).
        threshold (int): Minimum yaş eşiği.
        age_limit (int): Yetişkinlik sınırı.

    Returns:
        dict: Kategorize edilmiş veriler.
    """
    # Eksik değerleri 0 ile doldur
    cleaned_data = [0 if x is None else x for x in data]
    
    # Kategorizasyon
    categories = []
    for age in cleaned_data:
        if age < threshold:
            categories.append("Geçersiz")
        elif age < age_limit:
            categories.append("Çocuk")
        else:
            categories.append("Yetişkin")
    
    return {"ages": cleaned_data, "categories": categories}

# Örnek kullanım
data = [25, None, 15, 30, 10]
result = preprocess_and_categorize(data)
print(result)
# Çıktı: {'ages': [25, 0, 15, 30, 10], 'categories': ['Yetişkin', 'Geçersiz', 'Çocuk', 'Yetişkin', 'Geçersiz']}
```

**Açıklama:** Bu fonksiyon, bir yaş listesini temizler, eksik değerleri doldurur ve yaşlara göre kategorizasyon yapar. Veri bilimi projelerinde sıkça kullanılan bir ön işleme örneğidir.

---

## 10. Sonuç

Koşullu ifadeler, Python'da program akışını kontrol etmek için temel bir yapıdır. `if`, `else`, ve `elif` ifadeleri, farklı koşullara göre kararlar almayı sağlar. Mantıksal operatörler, iç içe koşullar ve ternary operator, daha karmaşık senaryoları ele almayı kolaylaştırır. Veri bilimi ve makine öğrenmesi projelerinde koşullu ifadeler, veri filtreleme, kategorizasyon, hata kontrolü ve model değerlendirme gibi görevlerde kritik rol oynar. Bu notlar, koşullu ifadelerin temel kullanımlarını, en iyi uygulamalarını ve pratik örneklerini kapsamaktadır.

### 10.1. Öneri

Bir sonraki adım olarak, koşullu ifadeleri bir veri bilimi projesinde kullanarak pratik yapabilirsiniz. Örneğin:
- Bir veri setindeki sayısal değerleri belirli eşiklere göre sınıflandırın.
- Eksik değerleri kontrol eden ve temizleyen bir fonksiyon yazın.
- Bir makine öğrenmesi modelinin tahminlerini eşik değerlere göre değerlendirin.
