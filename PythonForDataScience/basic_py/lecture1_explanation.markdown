# Python Ders 1: Sanal Ortam (Virtual Environment) ve Paket Yönetimi

Bu notlar, Python'da sanal ortamların ve paket yönetiminin temellerini açıklamaktadır. Sanal ortamlar, projeler arasında bağımlılık çakışmalarını önlemek ve düzenli bir geliştirme ortamı sağlamak için kullanılır. Paket yönetimi ise Python kütüphanelerini yüklemek, güncellemek ve yönetmek için gerekli araçları içerir.

---

## 1. Sanal Ortam Nedir ve Neden Kullanılır?

Sanal ortam, bir Python projesi için izole bir çalışma alanı oluşturur. Her sanal ortam, kendi Python yorumlayıcısına ve kütüphanelerine sahip olur. Bu, farklı projelerde farklı kütüphane versiyonlarını kullanmayı mümkün kılar.

### Avantajları:

- **Bağımsızlık:** Farklı projeler için farklı kütüphane versiyonları kullanılabilir.
- **Temizlik:** Sistem genelindeki Python kurulumunu etkilemez.
- **Çakışma Önleme:** Aynı kütüphanenin farklı versiyonlarının çakışmasını engeller.
- **Taşınabilirlik:** Ortamın bağımlılıkları başka bir bilgisayarda kolayca yeniden oluşturulabilir.

### Örnek Senaryo:

Bir veri analizi projesinde `pandas==1.4.0` kullanıyorsunuz, ancak bir makine öğrenimi projesinde `pandas==1.5.0` ve `tensorflow==2.8.0` gerekiyor. Sanal ortamlar sayesinde bu iki proje birbirinden bağımsız çalışabilir.

---

## 2. Paket Yöneticileri ve Sanal Ortam Yöneticileri

Python'da paket yönetimi ve sanal ortamlar için çeşitli araçlar bulunur. Aşağıda en yaygın kullanılan araçlar özetlenmiştir:

### Paket Yöneticileri:

- **pip:** Python'un varsayılan paket yöneticisi. PyPI (Python Package Index) deposundan paket indirir.
- **pipenv:** Hem paket hem de sanal ortam yöneticisi. `Pipfile` ile bağımlılıkları takip eder.
- **conda:** Anaconda/Miniconda ile gelen güçlü bir yönetici. Python dışı bağımlılıkları da destekler (örneğin, C kütüphaneleri).

### Sanal Ortam Yöneticileri:

- **venv:** Python 3.3+ ile gelen hafif bir modül. Sadece Python projeleri için uygundur.
- **virtualenv:** Daha eski ama daha fazla özellik sunar (örneğin, Python 2 desteği).
- **pipenv ve conda:** Hem sanal ortam hem de paket yönetimi sağlar.

### Hem Paket Hem Sanal Ortam Yöneticisi:

- **pipenv:** Modern, geliştirici dostu bir araç. Python projelerine odaklanır.
- **conda:** Veri bilimi ve büyük ekosistemler için uygundur.

---

## 3. Sanal Ortam İşlemleri (Conda ile)

Conda, hem sanal ortam hem de paket yönetimi için kullanılan güçlü bir araçtır. Aşağıda conda ile sanal ortam işlemlerinin detayları yer alıyor.

### 3.1. Sanal Ortamların Listelenmesi

Mevcut sanal ortamları görmek için:

```bash
conda env list
```

- Çıktıda, aktif olan ortam bir yıldız (`*`) ile işaretlenir.
- Örnek çıktı:

  ```
  base                  * /home/user/anaconda3
  myenv                   /home/user/anaconda3/envs/myenv
  ```

### 3.2. Sanal Ortam Oluşturma

Yeni bir sanal ortam oluşturmak için:

```bash
conda create -n ortam_adi
```

- Örnek: `myenv` adında bir ortam oluşturma:

  ```bash
  conda create -n myenv
  ```
- Belirli bir Python sürümü ile oluşturma:

  ```bash
  conda create -n myenv python=3.8
  ```

### 3.3. Sanal Ortamı Aktif Etme

Sanal ortamı kullanmak için:

```bash
conda activate ortam_adi
```

- Örnek:

  ```bash
  conda activate myenv
  ```
- Aktif olduktan sonra terminalde ortam adı parantez içinde görünür: `(myenv)`.

### 3.4. Sanal Ortamı Deaktif Etme

Sanal ortamdan çıkmak için:

```bash
conda deactivate
```

- Bu komut, sizi base ortamına veya sistem ortamına geri döndürür.

### 3.5. Sanal Ortamı Silme

Bir sanal ortamı tamamen silmek için:

```bash
conda env remove -n ortam_adi
```

- Örnek:

  ```bash
  conda env remove -n myenv
  ```

### 3.6. Yüklü Paketleri Listeleme

Sanal ortamdaki yüklü paketleri görmek için:

```bash
conda list
```

- Örnek çıktı:

  ```
  # Name                    Version                   Build  Channel
  numpy                     1.21.2                   py38    conda-forge
  pandas                    1.4.0                    py38    conda-forge
  ```

### 3.7. Paket Yükleme

Bir paketi sanal ortama yüklemek için:

```bash
conda install paket_adi
```

- Örnek: `numpy` yükleme:

  ```bash
  conda install numpy
  ```

### 3.8. Birden Fazla Paket Yükleme

Aynı anda birden fazla paket yüklemek için:

```bash
conda install paket_adi1 paket_adi2 paket_adi3
```

- Örnek:

  ```bash
  conda install numpy scipy pandas
  ```

### 3.9. Paket Silme

Bir paketi sanal ortamdan kaldırmak için:

```bash
conda remove paket_adi
```

- Örnek:

  ```bash
  conda remove numpy
  ```

### 3.10. Belirli Versiyona Göre Paket Yükleme

Bir paketin belirli bir versiyonunu yüklemek için:

```bash
conda install paket_adi=versiyon
```

- Örnek: `numpy` 1.20.1 versiyonunu yükleme:

  ```bash
  conda install numpy=1.20.1
  ```

### 3.11. Paket Güncelleme

Bir paketi güncellemek için:

```bash
conda upgrade paket_adi
```

- Örnek:

  ```bash
  conda upgrade numpy
  ```

### 3.12. Tüm Paketleri Güncelleme

Sanal ortamdaki tüm paketleri güncellemek için:

```bash
conda upgrade -all
```

---

## 4. Paket Yönetimi (pip ile)

`pip`, Python'un varsayılan paket yöneticisidir ve PyPI deposundan paket indirir. `venv` veya `virtualenv` ile oluşturulan sanal ortamlarda sıkça kullanılır.

### 4.1. Paket Yükleme

Bir paketi yüklemek için:

```bash
pip install paket_adi
```

- Örnek: `pandas` yükleme:

  ```bash
  pip install pandas
  ```

### 4.2. Belirli Versiyona Göre Paket Yükleme

Bir paketin belirli bir versiyonunu yüklemek için:

```bash
pip install paket_adi==versiyon
```

- Örnek: `pandas` 1.2.1 versiyonunu yükleme:

  ```bash
  pip install pandas==1.2.1
  ```

### 4.3. Yüklü Paketleri Listeleme

Sanal ortamdaki yüklü paketleri görmek için:

```bash
pip list
```

- Örnek çıktı:

  ```
  Package    Version
  ---------- -------
  numpy      1.21.2
  pandas     1.4.0
  ```

### 4.4. Paket Güncelleme

Bir paketi güncellemek için:

```bash
pip install --upgrade paket_adi
```

- Örnek:

  ```bash
  pip install --upgrade pandas
  ```

---

## 5. Sanal Ortamın Paylaşımı (YAML Dosyaları ile)

Sanal ortamın bağımlılıklarını başka bir kullanıcıyla ya da başka bir bilgisayarda paylaşmak için YAML dosyaları kullanılır.

### 5.1. YAML Dosyası Oluşturma

Mevcut sanal ortamın bağımlılıklarını dışa aktarmak için:

```bash
conda env export > environment.yaml
```

- Bu komut, ortamın tüm paketlerini ve versiyonlarını `environment.yaml` dosyasına kaydeder.
- Örnek `environment.yaml` içeriği:

  ```yaml
  name: myenv
  channels:
    - defaults
  dependencies:
    - numpy=1.21.2
    - pandas=1.4.0
    - python=3.8
  ```

### 5.2. YAML Dosyasından Sanal Ortam Oluşturma

Başka bir bilgisayarda aynı ortamı oluşturmak için:

```bash
conda env create -f environment.yaml
```

- Bu komut, `environment.yaml` dosyasındaki bağımlılıkları kullanarak yeni bir sanal ortam oluşturur.

---

## 6. Ek Bilgiler ve İpuçları

### 6.1. `venv` ile Sanal Ortam Oluşturma

Python'un yerleşik `venv` modülü ile sanal ortam oluşturmak için:

```bash
python -m venv ortam_adi
```

- Örnek:

  ```bash
  python -m venv myenv
  ```
- Aktif etme (Windows):

  ```bash
  myenv\Scripts\activate
  ```
- Aktif etme (Linux/MacOS):

  ```bash
  source myenv/bin/activate
  ```
- Deaktif etme:

  ```bash
  deactivate
  ```

### 6.2. `pipenv` Kullanımı

`pipenv`, modern bir alternatif olarak hem sanal ortam hem de paket yönetimi sağlar. Örnek kullanım:

- Sanal ortam oluşturma ve paket yükleme:

  ```bash
  pipenv install pandas
  ```
- Sanal ortamı aktif etme:

  ```bash
  pipenv shell
  ```
- Bağımlılıkları `Pipfile` ile yönetir.

### 6.3. Conda ve pip Birlikte Kullanımı

Bazı paketler conda deposunda bulunmayabilir. Bu durumda, conda ortamında `pip` kullanılabilir:

```bash
conda activate myenv
pip install paket_adi
```

- **Not:** Önce conda ile yüklemeyi deneyin, çünkü conda bağımlılıkları daha iyi yönetir.

### 6.4. Yaygın Hatalar ve Çözümleri

- **Hata:** `conda: command not found`
  - **Çözüm:** Anaconda/Miniconda'nın doğru yüklendiğinden ve PATH'e eklendiğinden emin olun.
- **Hata:** Paket çakışmaları
  - **Çözüm:** Yeni bir sanal ortam oluşturun veya mevcut ortamı sıfırlayın.
- **Hata:** `pip` ile yüklenen paket çalışmıyor
  - **Çözüm:** Sanal ortamın aktif olduğundan emin olun (`pip list` ile kontrol edin).

---

## 7. Örnek Proje: Veri Analizi Ortamı Oluşturma

Bir veri analizi projesi için sanal ortam oluşturup gerekli paketleri yükleyelim:

```bash
# Sanal ortam oluşturma
conda create -n data_analysis python=3.9

# Sanal ortamı aktif etme
conda activate data_analysis

# Gerekli paketleri yükleme
conda install numpy pandas matplotlib seaborn

# Paketlerin yüklendiğini doğrulama
conda list

# Ortamı YAML olarak dışa aktarma
conda env export > data_analysis_env.yaml
```

Bu ortamı başka bir bilgisayarda yeniden oluşturmak için:

```bash
conda env create -f data_analysis_env.yaml
```

---

## 8. Sonuç

Sanal ortamlar ve paket yönetimi, Python projelerinde düzenli ve çakışmasız bir geliştirme ortamı sağlamak için kritik öneme sahiptir. `conda` ve `pip` gibi araçlar, farklı ihtiyaçlara uygun çözümler sunar. Bu notlar, temel işlemleri ve en iyi uygulamaları kapsamaktadır. Daha fazla pratik yaparak bu araçları rahatça kullanabilirsiniz!

