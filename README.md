# 🔐 Basit Port Tarayıcı

Bu proje, Python kullanarak yazdığım basit bir port tarama aracıdır.
Amacım hem siber güvenliğe giriş yapmak hem de ağ (network) mantığını daha iyi anlamaktı.

## 🚀 Ne İşe Yarar?

Bu araç sayesinde bir IP adresinde hangi portların açık olduğunu görebilirsiniz.
Ayrıca bazı portlar için basit güvenlik uyarıları da verir.

Örnek:

* 21 → FTP (güvensiz olabilir)
* 23 → Telnet (şifrelenmemiş)
* 3389 → RDP (uzaktan erişim)

## ⚙️ Nasıl Çalışır?

Program, belirlediğim bazı yaygın portlara sırayla bağlanmayı dener.
Eğer bağlantı kurulursa o portun açık olduğunu anlar.

Mantık tamamen şu:

> "Bağlanabiliyorsam port açıktır"

## ▶️ Nasıl Kullanılır?

1. Python kurulu olmalı (Python 3 önerilir)
2. Dosyayı indir
3. Terminalden çalıştır:

```bash id="run1"
python scan.py
```

4. IP adresini gir ve sonucu bekle

## ⚠️ Uyarı

Bu proje sadece eğitim amaçlıdır.
Lütfen izinsiz sistemlerde kullanmayın.

## 🧠 Neden Yazdım?

Siber güvenliğe yeni başladım ve teoriden ziyade pratik yapmak istedim.
Bu yüzden basit ama işe yarar bir şey yapmak istedim.

## 🔧 Geliştirme Fikirleri

İleride şunları eklemeyi düşünüyorum:

* Daha hızlı tarama (multi-thread)
* Servis bilgisi çekme
* Basit arayüz (GUI)
* Daha fazla port desteği

## 👨‍💻 Not

Kod olabildiğince sade yazıldı.
Yeni başlayan biri bile okuyup anlayabilir.

Geliştirmek isteyen olursa PR atabilir 👍
