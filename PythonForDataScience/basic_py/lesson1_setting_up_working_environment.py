
###############################################
# Virtual Environment (Sanal Ortam)  ve (Package Managment) Paket Yönetimi
###############################################


"""
paket yöneticileri: pip pipenv conda
sanal ortam yöneticileri:  venv  virtualenv (venv ve virtualenv paket yönetim aracı olarak pip kullanır) pipenv conda
hem sanal hem paket yöneticisi: pipenv conda

sanal ortamların listelenmesi: (içinde bulunduğun yıldızla gözükür)
conda env list

sanal ortam oluşturma:
conda create -name ortamadı

sanal ortamı aktif etme:
conda activate ortamadı

sanal ortamı deaktif etme:
conda deactivate

sanal ortamı silme:
conda env remove -n ortamadı

yüklü paketleri gösterme:
conda list

sanal ortama paket yükleme:
conda install paketadı

aynı anda birden fazla paket yüklerken
conda install paketadı1 paketadı2 paketadı3

paket silme:
conda remove paketadı

paketin versiyonunu belirterek yükleme:
conda install paketadı=versiyon (pipte iki = kullanılır)

paket güncelleme:
conda upgrade paketadı
conda upgrade -all (tüm paketleri günceller)



pip  paket yüklemek için kullanılır

paketi yükleme:
pip install paketadı

paket yüklerken versiyon belirtme:
pip install paketadı==versiyon


paketi arkadaşa atmak için yaml oluşturma

conda env export > enviroment.yaml

başka ortamdan gelen yaml dosyasını yükleme
conda env create -f enviroment.yaml




"""




# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create –n myenv

# Sanal ortamı aktif etme:
# conda activate myenv

# Yüklü paketlerin listelenmesi:
# conda list

# Paket yükleme:
# conda install numpy

# Aynı anda birden fazla paket yükleme:
# conda install numpy scipy pandas

# Paket silme:
# conda remove package_name

# Belirli bir versiyona göre paket yükleme:
# conda install numpy=1.20.1

# Paket yükseltme:
# conda upgrade numpy

# Tüm paketlerin yükseltilmesi:
# conda upgrade –all

# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme:
# pip install pandas

# Paket yükleme versiyona göre:
# pip install pandas==1.2.1



"""
**Ek Bilgiler:**

- **Sanal Ortam Nedir ve Neden Kullanılır?**
  Sanal ortam, Python projeleriniz için izole bir çalışma alanı oluşturur. Farklı projelerde farklı paket versiyonlarına ihtiyaç duyabilirsiniz; sanal ortamlar bu çakışmaları önler. Örneğin, bir projede `pandas` 1.2.1, başka bir projede 1.5.0 kullanabilirsiniz.
  - **Avantajları:**
    - Proje bazlı bağımsızlık sağlar.
    - Sistem genelindeki Python kurulumunu etkilemez.
    - Paket çakışmalarını engeller.
  - **Örnek Senaryo:** Bir makine öğrenimi projesinde `tensorflow` 2.8.0 gerekirken, başka bir veri analizi projesinde `pandas` 1.4.0 kullanıyorsunuz. Sanal ortamlar bu iki projeyi ayrı tutar.

- **Paket Yöneticileri Hakkında:**
  - **pip:** Python'un varsayılan paket yöneticisidir ve PyPI (Python Package Index) deposundan paket indirir. Hafif ve kullanımı kolaydır.
  - **pipenv:** Hem paket hem de sanal ortam yöneticisidir. `Pipfile` kullanarak bağımlılıkları takip eder, daha modern bir yaklaşımdır.
  - **conda:** Anaconda/Miniconda ile gelen güçlü bir yöneticidir. Python dışı bağımlılıkları (örneğin C kütüphaneleri) da yönetebilir. Veri bilimi projelerinde sık kullanılır.

- **Sanal Ortam Yöneticileri Hakkında:**
  - **venv:** Python 3.3+ ile gelen standart modüldür. Hafif ve sadece Python projeleri için uygundur.
  - **virtualenv:** `venv`'den daha eski ama daha fazla özellik sunar (örneğin, Python 2 desteği). Genelde `pip` ile kullanılır.
  - **pipenv ve conda:** Hem sanal ortam oluşturur hem de paketleri yönetir. `pipenv` daha çok Python projelerine odaklanırken, `conda` geniş bir ekosistemi destekler.
"""