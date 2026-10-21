# Malzeme ve bütçe ön listesi

Güncelleme: 21 Ekim 2026. Tek prototip için miktar ve uyumluluk önerisi. Kesin satın alma listesi veya TYBS bütçesi değildir. ESP32, enkoderli iki motor mimarisi ve beş sabit mesafe sensörü düzeni kullanıcı tarafından seçildi. Model önerileri, kesin montaj açıları ve diğer parça miktarları birlikte değerlendirilecek. Bazı ürün fiyatları doğrulandı; tam proje toplamı henüz yok.

Adayların gerekçeleri ve elektriksel koşulları [donanım uyumluluk değerlendirmesinde](DONANIM_SECENEKLERI_VE_UYUMLULUK.md); fiyat/ürün bilgisi girilecek tablo [teklif formunda](MALZEME_TEKLIF_FORMU.csv). CSV, noktalı virgülle ayrılmış UTF-8 tablodur. Boş fiyat alanları sıfır maliyet anlamına gelmez.

Motor için #5143 ve #5115 referansları, TB6612FNG taşıyıcısı ve yerelde bulunan batarya/şarj adayları [karşılaştırma dosyasında](MOTOR_SURUCU_BATARYA_KARSILASTIRMASI.md). CSV'de kaynak para birimi ayrıca tutuluyor; USD fiyatı için TL hücresi dönüştürülmeden boş bırakıldı. Fiyatı bulunan adayın uyum kontrolü bitmiş sayılmayacak.

## Mevcut olanaklar

- ESP32 henüz mevcut değil; kullanıcı satın almayı planlıyor.
- Kullanıcı lehim ekipmanına sahip ve montajda sorun beklemiyor. Araç henüz monte edilmedi.
- Diğer parçaların mevcut olduğu bildirilmedi.
- Üniversite laboratuvarı, 3D yazıcı ve referans ölçüm kamerasına erişim henüz doğrulanmadı. Bunlar başvuruda mevcut altyapı olarak gösterilmeyecek.

## Temel mimari için teklif alınacak kalemler

Seçilen başlangıç düzeni: küçük iki tekerlekli diferansiyel sürüşlü şasi ve beş sabit mesafe sensörü (ön orta, iki ön çapraz, iki yan). ToF tipi ve I²C çoklayıcı hâlen adaydır. Enkoderli motorlar seçildi; N20 sınıfı, yaklaşık 100 d/d ve 6 V önerisi ise henüz tam ürün koduna dönüştürülmedi. Şasi ölçüleri ve destek tekeri düzeni kesinleşmedi.

| Kalem | Önerilen miktar | Seçimde kontrol edilecek özellik |
| --- | --- | --- |
| ESP32 geliştirme kartı | 1 | ESP32-DevKitC V4 / WROOM-32E sürümü aday; satılan kartın pin ve besleme düzeni doğrulanacak. |
| Enkoderli redüktörlü DC motor | 2 | Pololu #5143, 6 V / MP 210:1 / 100 d/d ve belgeli eşdeğerleri aday. Üretici teknik verileri okundu; 5 V yük davranışı, gerçek kütle, temin ve teslim maliyeti açık. |
| Motorlarla uyumlu tekerlek | 2 | Yaklaşık 60 mm çap önerisi; mil bağlantısı ve zemin tutuşu kontrol edilecek. |
| Şasi | 1 | Yaklaşık 20 × 15 cm sınıfı öneri; toplam kütle, dönüş alanı ve parça yerleşimi kontrol edilecek. |
| Motor bağlantı aparatı | 2 | Seçilecek motor ve şasiye uyumlu; kitte varsa ayrıca alınmayacak. |
| Serbest taşıyıcı teker | 1 | Tahrik tekerleriyle uygun yükseklik ve küçük alanda dönme. |
| Çift kanallı motor sürücüsü | 1 | TB6612FNG aday; düşük akımlı motor koşulu ve modülün sürekli akım/ısıl sınırları doğrulanacak. |
| Sabit mesafe sensörü | 5 | Sayı ve ön orta, iki ön çapraz, iki yan düzeni seçildi. VL53L0X/ToF model adayı; kesin açılar, 3,3 V besleme/I²C ve algılama kapsaması kontrol edilecek. |
| I²C çoklayıcı | 1 | TCA9548A aday; aynı adresli sensörler ayrı kanallara bağlanacak. |
| Hazır korumalı batarya paketi | 1 | 2S paket önerisi; kimya, kapasite ve akım gereksinimleri doğrulanacak. |
| Pakete uygun şarj cihazı | 1 | Batarya kimyası ve hücre sayısıyla uyumlu olacak; paketteki koruma devresiyle aynı parça sayılmayacak. |
| 5 V regülatör modülü | 1 | Seçilen bataryanın giriş aralığında gerçek sürekli akım kapasitesi doğrulanacak; ilk arama ölçütü en az 3 A. |
| 3,3 V regülatör modülü | 1 | Sensör/çoklayıcı/sürücü mantığı için; toplam tüketim ve ısıl hesap yapılacak. |
| Ana güç anahtarı | 1 | Hesaplanan akıma uygun. |
| Sigorta ve yuvası | 1 takım | Değer/tip, motor kalkışı ve kablo kapasitesiyle seçilecek. |
| Devre montaj kartı | 1 | Boyut, bağlantı ve akım yollarına uygun. |
| USB veri kablosu | 1 | Seçilecek kartın konektörüyle uyumlu; mevcutsa yeni alım olmayacak. |
| Motor/enkoder bağlantı kablosu | 2 | Referans Pololu motorlara dahil değil; altı pinli JST SH tarzı #4763 aday. Genel konnektör satırıyla mükerrer sayılmayacak. |
| Kablo, konnektör, bağlantı elemanları ve süzme parçaları | Adetler çıkarılacak | Son bağlantı şemasına göre ayrı kalemler halinde fiyatlandırılacak; belirsiz toplu fiyat girilmeyecek. |

Önerilen ilk güç düzeninde motor sürücüsü ve ESP32 ayrı kablo dallarından regüle 5 V ile beslenecek; sensör/mantık için 3,3 V dalı kullanılacak. 6 V anma değerli motorun 5 V'taki yük davranışı ayrıca kontrol edilecek. Bataryanın ham çıkışı doğrudan motora veya ESP32'ye bağlanacakmış gibi planlanmadı. Ayrıntılar [uyumluluk değerlendirmesinde](DONANIM_SECENEKLERI_VE_UYUMLULUK.md).

Basit bir araç kitinde enkoder bulunması otomatik olarak varsayılmayacak. Motor, sürücü ve güç bileşenleri birlikte kontrol edilmeden ürün listesi kesinleştirilmeyecek. Kitteki şasi, motor aparatı veya tekerlekler ayrı alımlarla mükerrer bütçelenmeyecek.

## İhtiyaca göre ayrıca değerlendirilecekler

- IMU: yön ölçümü ve konum kestirimine katkısı, kalibrasyon ihtiyacı ve bütçeyle değerlendirilecek; model seçilmedi, zorunlu alım değil.
- Sensör türü/modeli: beş sabit sensörlü düzen seçildi. VL53L0X/ToF adayı, gerçek kapsama ve fiyatla birlikte değerlendirilecek. Kesin montaj açıları seçilmedi; servo bu düzende zorunlu parça değil.
- Gövde/muhafaza: hazır bağlantı parçaları yeterliyse özel üretim gerekmeyebilir; 3D yazıcı erişimi varsayılmayacak.
- Deney ölçümü: metre, zemin işaretleri, uygun referans kamera ve sabitleme olanağı incelenecek. Rota sapmasını bağımsız ölçmek yöntem için gereklidir; kamera kullanımı ve satın alımı henüz kararlaştırılmadı.

## Bütçeyi kesinleştirme yöntemi

1. Önce motor-enkoder-şasi seçeneği ve hareket gereksinimleri netleştirilecek.
2. Motor sürücüsü ve güç bileşenleri bu seçime göre eşleştirilecek; sensör kapsaması kaçınma yöntemine göre belirlenecek.
3. Uyumlu ürünler için tarihli fiyat, adet, KDV durumu, stok ve teslim koşulları kaydedilecek. Varsa kargo ve yan giderlerin destek kapsamı ayrıca kontrol edilecek.
4. Yeni alınacak ve kişisel olarak zaten mevcut parçalar ayrılacak. Mevcut lehim ekipmanı yeni alım kalemi olarak varsayılmayacak.
5. Adet × birim fiyat üzerinden toplam çıkarılacak; program sınırı ve danışman görüşüyle son bütçe oluşturulacak. Kontrol edilen program sayfasındaki destek üst sınırı 12.000 TL; bu tutar projenin belirlenmiş bütçesi veya destek alma garantisi değildir.

İlk denemelerde ağ aracısında 403 görülmüştü. 21 Ekim 2026 tarihli son incelemede Pololu ve üç yerel satıcıya HTTP 200 ile erişildi; bazı fiyatlar KDV ve stok etiketleriyle kaydedildi. Tamamlanan gözlemler [karşılaştırma dosyasında](MOTOR_SURUCU_BATARYA_KARSILASTIRMASI.md). Fiyatı bulunan tüm ürünler teknik açıdan seçilmiş değildir; tam bütçe oluşturulmadı.

**Teklif formu doldurma:** Her kaleme tam ürün kodu, satıcı bağlantısı, teklif tarihi, KDV durumu, stok, adet ve birim fiyat yazılacak. Şimdilik boş olan fiyat/tutar hücreleri sıfır kabul edilmeyecek. İsteğe bağlı ve mevcut ekipman satırları kesin alım toplamına otomatik dahil edilmeyecek. Toplam ancak temel parçalar ve bağımsız deney ölçümü için gereken kaynaklar tamamlandığında oluşturulacak.
