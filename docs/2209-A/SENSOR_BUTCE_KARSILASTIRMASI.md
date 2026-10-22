# Beş sabit sensör için teknik ve bütçe karşılaştırması

Tarih: 22 Ekim 2026. Kullanıcının seçtiği beş sabit sensör ve Bug 2 mantığından yararlanan kaçınma yaklaşımı korunmuştur. Kullanıcı ToF sensörlerini önceliklendirmeyi seçti; kesin taşıyıcı/model henüz seçilmedi. Bu dosya satın alma listesi veya nihai bütçe değildir.

## Fiyat ve temin gözlemleri

| Seçenek | Bir adet için görülen fiyat | Beş adet karşılığı | Temin / fiyat kaydının sınırı |
| --- | --- | --- | --- |
| [Pololu #2490 VL53L0X](https://www.pololu.com/product/2490) | 19,95 USD | 99,75 USD | Önceki belgeli taşıyıcı referansı; Türkiye teslim giderleri dahil değil. |
| [GY-VL53L0XV2 / Direnc.net](https://www.direnc.net/gy-vl53l0xv2-lazer-mesafe-modulu) | 435,88 TL, KDV dahil etiketi | 2.179,40 TL | Yapılandırılmış sayfa verisinde **OutOfStock**. Beş adet temin edilebilir sayılmadı. |
| [GY-53 siyah / Robotistan 25505](https://www.robotistan.com/vl53l0x-lazer-tof-sensor-modul-i2c-pwm-serial-siyah) | Güncel KDV dahil etiketinde 352,42 TL | Bu etikete göre 1.762,10 TL | Sayfada ayrıca aynı tutarla “+ KDV” etiketi var. Fiyat etiketleri tutarsız; kesin teslim teklifi değildir. Gerçek kartın I²C seviyeleri açık. |
| [HC-SR04 / Direnc.net](https://www.direnc.net/arduino-ultrasonic-sensor-hc-sr04) | 58,12 TL, KDV dahil | 290,60 TL | Yapılandırılmış veri InStock; beş adet stok ve teslim bedeli teyit edilmedi. |
| [HC-SR04 / Robolink Market](https://www.robolinkmarket.com/hc-sr04-arduino-ultrasonic-mesafe-sensoru) | 45,00 TL + KDV; gösterilen son fiyat 54,00 TL | 270,00 TL | Yapılandırılmış veri InStock; beş adet stok ve teslim bedeli teyit edilmedi. |

Direnc.net [HC-SR04 tutucusu](https://www.direnc.net/hcsr-04-ultrasonic-sensor-tutucu) 23,25 TL/adet, beş adet için 116,25 TL olarak listeleniyor. Hazır tutucu yalnızca bir montaj seçeneğidir. Beş Direnc.net sensörü ve beş bu tutucunun toplamı **406,85 TL** olur; seviye uyarlama, kablolama ve teslim bedeli bu toplama dahil değildir. ToF sensörlerinin de montaj giderleri ayrıca belirlenecektir.

Robotistan siyah sensörün önceki kısa fiyat özetinde, ikinci “KDV Dahil Fiyat” alanındaki güncel 352,42 TL gösterimi yer almıyordu. Kaynak HTML yeniden incelenerek bu alan kayda eklendi. Aynı sayfadaki “+ KDV” yazımı nedeniyle tutarsızlık bütçe varsayımıyla giderilmedi.

## Hareket kontrolüne etkisi

| Konu | Küçük ToF taşıyıcısı | HC-SR04 sınıfı ultrasonik modül |
| --- | --- | --- |
| Şasiye yerleşim | Küçük taşıyıcılar ön ve yan yönlere yerleştirmeye elverişli bir adaydır; gerçek kart ölçüsü/modeli doğrulanacak. | Okunan belgede 45 × 20 × 15 mm. Beş modülün şasi, tekerlek ve birbirleriyle çakışmaması kontrol edilecek. |
| Engel kenarını izleme | Ölçüm alanı, köşeler ve yüzey davranışı gerçek kartla sınanacak. | Yüzey açısı ve yansımalar ölçümü etkileyebilir. Engel kenarında doğru yüzeyin ölçüldüğü deneyle kontrol edilecek. |
| ESP32 bağlantısı | I²C taşıyıcısının regülatör/seviye devresi ve çekme gerilimleri gerekli. Aynı adresli sensörler için çoklayıcı veya sıralı adres atama değerlendiriliyor. | 5 V besleme ve Trig/Echo arayüzü. Echo için ESP32'ye uygun seviye uyarlama, tetik giriş eşiği ve GPIO planı gerekli. Doğrudan bağlantı uyumu varsayılmayacak. |
| Beşli ölçüm zamanlaması | Ardışık okuma süresi ve olası optik etkileşim kontrol edilecek. | Bir modülün sesinin diğerinde ölçüm oluşturmasını önleyen sıralama ve bekleme gerekir. |
| Maliyet | Taşıyıcı modeline göre değişiyor. Stokta olmayan ürünün fiyatı durumuyla birlikte referans tutulabilir; temin planı ve tutarlı fiyat gerekçesi ayrıca hazırlanmalı. | Sensörlerin görünen fiyatı daha düşük; bağlantı ve mekanik ekler toplamda ayrıca hesaplanmalı. |

Robotistan'ın bağladığı [HC-SR04 veri sayfasının](https://www.robotistan.com/Data/EditorFiles/HCSR04-datasheet-version-1.pdf) üç sayfası okundu. Belgede 5 V, 15 mA, en az 10 µs tetik, 2–400 cm aralık ve 15° nominal ölçüm açısı belirtiliyor. Zaman diyagramında 40 kHz ses darbesi ve 60 ms'den uzun ölçüm çevrimi öneriliyor. Bazı ürün açıklamalarındaki “40 Hz” alanı ses taşıyıcı frekansı olarak aktarılmadı.

Beş modülü tek tek tetikleyip her tetikleme arasında 60 ms'den fazla beklemek, örnek bir muhafazakâr tasarımda tam taramayı 300 ms'nin üzerine çıkarır. Bu, beş modül için üretici tarafından doğrulanmış bir tarama hızı veya seçilmiş proje parametresi değildir. Hız ve durma mesafesi seçilirken ölçümün en kötü durum gecikmesi ile frenleme mesafesi birlikte ele alınacaktır. Zaman aşımı veya geçersiz yankı “önü boş” olarak yorumlanmayacaktır.

Belgenin 3. sayfasında düzgün yüzey ve en az 0,5 m² hedef alanı koşulu anılıyor. Küçük deney engellerinde katalogdaki milimetre düzeyindeki doğruluk varsayılmayacak; algılama ve kenar takibi gerçek düzenekte sınanacaktır. Aynı şekilde ToF ürün sayfasındaki “±3 mm” ifadesi proje için sağlanmış doğruluk olarak kullanılmayacaktır.

## Bütçe ve seçim durumu

İlk önerim, küçük şasi ve engel kenarı takibi için **ToF taşıyıcılarını önceliklendirmek**, ultrasoniği teknik/maliyet alternatifi olarak tutmaktır. Kullanıcı “ToF sensörlerini önceliklendirelim.” yanıtıyla bu önceliği seçti. Bu karar belirli bir ürünün satın alınmasını veya uyumunun doğrulandığını ifade etmez. GY-VL53L0XV2 fiyatı stokta bir ürünün fiyatı gibi sunulmayacaktır. Uygun fiyatlı ToF adayında kart devresi, 3,3 V bağlantısı, gerçek temin ve KDV dahil teslim bedeli doğrulanmalıdır.

[Mevcut referans bütçe](FIYATLI_BUTCE_TASLAGI.md) değiştirilmedi: yerel ara toplam 3.189,41 TL, yabancı referanslar 177,35 USD. Önceki kurla 11.986,24 TL karşılık, şasi ve diğer eksik giderleri içermiyor. Bu dosyadaki alternatifler aynı anda alınacak kalemler olarak CSV'ye eklenmedi; mükerrer sensör maliyeti oluşturulmadı. Yerel motorun eksik sıkışma akımı/enkoder bilgileri de giderilmiş sayılmadı.

Kaynak URL'leri, HTML özetleri, stok verisi ve doküman okuma kapsamı [22 Ekim sensör kaydında](tedarik/sensor_secenekleri_2026-10-22.json) tutulmaktadır. Satıcıya mesaj gönderilmedi, sipariş oluşturulmadı.

## Başvuruda stok zorunluluğu

Güncel çağrı ve bilgi notunda, başvuru anında tüm ürünlerin stokta olmasına ilişkin bir şart bulunmadı. Stokta olmayan ToF adayı teknik/fiyat karşılaştırmasında kalabilir; bu durum rapor yazımını durdurmaz. Temin araştırması, eşdeğer alternatif ve gerçekçi bütçe hazırlamak içindir. Ayrıntılı ayrım [başvuru hazırlık notlarında](BASVURU_METNI_HAZIRLIK_NOTLARI.md) kayıtlıdır.
