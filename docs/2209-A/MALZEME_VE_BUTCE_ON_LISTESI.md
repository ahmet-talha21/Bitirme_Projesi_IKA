# Malzeme ve bütçe ön listesi

Güncelleme: 22 Ekim 2026. Tek prototip için miktar ve uyumluluk önerisi. Kesin satın alma listesi veya TYBS bütçesi değildir. ESP32, enkoderli iki motor mimarisi ve beş sabit mesafe sensörü düzeni kullanıcı tarafından seçildi. Model önerileri, kesin montaj açıları ve diğer parça miktarları birlikte değerlendirilecek. Fiyatı bulunan kalemlerin ara toplamları [fiyatlı bütçe taslağında](FIYATLI_BUTCE_TASLAGI.md); tam proje toplamı henüz yok.

Adayların gerekçeleri ve elektriksel koşulları [donanım uyumluluk değerlendirmesinde](DONANIM_SECENEKLERI_VE_UYUMLULUK.md); fiyat/ürün bilgisi girilecek tablo [teklif formunda](MALZEME_TEKLIF_FORMU.csv). CSV, noktalı virgülle ayrılmış UTF-8 tablodur. Boş fiyat alanları sıfır maliyet anlamına gelmez.

Motor için #5143 ve #5115 referansları, TB6612FNG taşıyıcısı ve yerelde bulunan batarya/şarj adayları [karşılaştırma dosyasında](MOTOR_SURUCU_BATARYA_KARSILASTIRMASI.md). CSV'de kaynak para birimi ayrıca tutuluyor; gerçek TL teklifi olmayan USD satırlarının TL hücreleri boş bırakıldı. Resmî kurla ayrı hesaplanan referans karşılık 11.986,24 TL; eksik kalemler dahil olmadan destek üst sınırına 13,76 TL fark kaldığından daha uygun fiyatlı belgeli seçenekler değerlendirilecek. Fiyatı bulunan adayın uyum kontrolü bitmiş sayılmayacak.

## Mevcut olanaklar

- ESP32 henüz mevcut değil; kullanıcı satın almayı planlıyor.
- Kullanıcı lehim ekipmanına sahip ve montajda sorun beklemiyor. Araç henüz monte edilmedi.
- Diğer parçaların mevcut olduğu bildirilmedi.
- Kullanıcı 22 Ekim 2026 tarihinde telefonunu deneylerde kullanabileceğini doğruladı. Yeni kamera alımı planlanmıyor; uygun görüş alanı, sabitleme ve kalibrasyon düzeni kontrol edilecek.
- Üniversite laboratuvarı ve 3D yazıcıya erişim henüz doğrulanmadı. Bunlar başvuruda mevcut kurum altyapısı olarak gösterilmeyecek.

## Temel mimari için teklif alınacak kalemler

Seçilen başlangıç düzeni: küçük iki tekerlekli diferansiyel sürüşlü şasi ve beş sabit mesafe sensörü (ön orta, iki ön çapraz, iki yan). ToF tipi ve I²C çoklayıcı hâlen adaydır. Yaklaşık 100 d/d, 6 V motor için Pololu #5143 somut referans olarak incelendi; bu, satın alma/model onayı değildir. Şasi ölçüleri ve taşıyıcı teker yüksekliği kesinleşmedi.

| Kalem | Önerilen miktar | Seçimde kontrol edilecek özellik |
| --- | --- | --- |
| ESP32 geliştirme kartı | 1 | Yerel fiyat adayı ESP32-WROOM CP2102 Type-C kartı. Önceki DevKitC referansıyla aynı pin/güç devresine sahip varsayılmayacak. |
| Enkoderli redüktörlü DC motor | 2 | Pololu #5143, 6 V / MP 210:1 / 100 d/d ve belgeli eşdeğerleri aday. Üretici teknik verileri okundu; 5 V yük davranışı, gerçek kütle, temin ve teslim maliyeti açık. |
| Motorlarla uyumlu tekerlek | 2, bir çift | Pololu #1420 60×8 mm / 3 mm D mil referansı; yükseklik ve şasi yerleşimi kontrol edilecek. CSV'de bir çift olarak fiyatlandı. |
| Şasi | 1 | Yaklaşık 20 × 15 cm sınıfı öneri; toplam kütle, dönüş alanı ve parça yerleşimi kontrol edilecek. |
| Motor bağlantı aparatı | 2, bir çift | Pololu #1089 referans çift; şasi delik düzeni ve dahil vidalar kontrol edilecek. |
| Serbest taşıyıcı teker | İhtiyaç 1 | Yerel fiyat adayı iki adetlik paket satılıyor; paketin tam bedeli alındı. Gerekli yükseklik/spacer kontrol edilecek. |
| Çift kanallı motor sürücüsü | 1 | TB6612FNG aday; düşük akımlı motor koşulu ve modülün sürekli akım/ısıl sınırları doğrulanacak. |
| Sabit mesafe sensörü | 5 | Sayı ve yönler seçildi. Bütçe örneğinde 3,3 V arayüzü belgeli Pololu #2490 referansı var; daha ucuz 5 V kart gözlemi ayrı tutuldu. Model, açı ve kapsama nihai değil. |
| I²C çoklayıcı | 1 | TCA9548A aday; aynı adresli sensörler ayrı kanallara bağlanacak. |
| Hazır batarya paketi | 1 | 2S / 1000 mAh Power-Xtra fiyat adayı. Paket koruması, şarj akımı ve soketler teyit edilecek. |
| Gerekirse harici koruma modülü | 1 | 2S BMS fiyat adayı ayrı gösterildi; paket korumalı gelirse ayrıca alınmayacak. |
| Pakete uygun şarj cihazı | 1 | Batarya kimyası ve hücre sayısıyla uyumlu olacak; paketteki koruma devresiyle aynı parça sayılmayacak. |
| 5 V regülatör modülü | 1 | Seçilen bataryanın giriş aralığında gerçek sürekli akım kapasitesi doğrulanacak; ilk arama ölçütü en az 3 A. |
| 3,3 V regülatör modülü | 1 | Sensör/çoklayıcı/sürücü mantığı için; toplam tüketim ve ısıl hesap yapılacak. |
| Ana güç anahtarı | 1 | Hesaplanan akıma uygun. |
| Sigorta ve yuvası | 1 takım | Değer/tip, motor kalkışı ve kablo kapasitesiyle seçilecek. |
| Devre montaj kartı | 1 | Boyut, bağlantı ve akım yollarına uygun. |
| USB veri kablosu | 1 | Seçilecek kartın konektörüyle uyumlu; mevcutsa yeni alım olmayacak. |
| Motor/enkoder bağlantı kablosu | 2 | Referans Pololu motorlara dahil değil; altı pinli JST SH tarzı #4763 aday. Genel konnektör satırıyla mükerrer sayılmayacak. |
| Sinyal jumper seti | 1 paket, 40 hat | Yerel fiyat adayı. Motorların ana güç kablosu yerine sayılmayacak. |
| Kablo, konnektör, bağlantı elemanları ve süzme parçaları | Adetler çıkarılacak | Son bağlantı şemasına göre ayrı kalemler halinde fiyatlandırılacak; belirsiz toplu fiyat girilmeyecek. |

Önerilen ilk güç düzeninde motor sürücüsü ve ESP32 ayrı kablo dallarından regüle 5 V ile beslenecek; referans sensör/mantık için 3,3 V dalı kullanılacak. 6 V motorun 5 V'taki yük davranışı ayrıca kontrol edilecek. [Batarya–şarj–güç planı](BATARYA_VE_SARJ_PLANI.md), paket/koruma ve şarj akımıyla ilgili açık kontrolleri gösteriyor.

Basit bir araç kitinde enkoder bulunması otomatik olarak varsayılmayacak. Motor, sürücü ve güç bileşenleri birlikte kontrol edilmeden ürün listesi kesinleştirilmeyecek. Kitteki şasi, motor aparatı veya tekerlekler ayrı alımlarla mükerrer bütçelenmeyecek.

## İhtiyaca göre ayrıca değerlendirilecekler

- IMU: yön ölçümü ve konum kestirimine katkısı, kalibrasyon ihtiyacı ve bütçeyle değerlendirilecek; model seçilmedi, zorunlu alım değil.
- Sensör türü/modeli: beş sabit sensörlü düzen seçildi. VL53L0X/ToF adayı, gerçek kapsama ve fiyatla birlikte değerlendirilecek. Kesin montaj açıları seçilmedi; servo bu düzende zorunlu parça değil.
- Gövde/muhafaza: hazır bağlantı parçaları yeterliyse özel üretim gerekmeyebilir; 3D yazıcı erişimi varsayılmayacak.
- Deney ölçümü: kullanıcının mevcut telefonu, metre, zemin işaretleri ve uygun sabitleme düzeni değerlendirilecek. Yeni kamera alımı planlanmıyor. Telefon erişimi, rota sapmasının bağımsız ve yeterli doğrulukta ölçüldüğü anlamına gelmez; görüş alanı ve kalibrasyon kontrol edilecek.

## Bütçeyi kesinleştirme yöntemi

1. Önce motor-enkoder-şasi seçeneği ve hareket gereksinimleri netleştirilecek.
2. Motor sürücüsü ve güç bileşenleri bu seçime göre eşleştirilecek; sensör kapsaması kaçınma yöntemine göre belirlenecek.
3. Uyumlu ürünler için tarihli fiyat, adet, KDV durumu, stok ve teslim koşulları kaydedilecek. Varsa kargo ve yan giderlerin destek kapsamı ayrıca kontrol edilecek.
4. Yeni alınacak ve kişisel olarak zaten mevcut parçalar ayrılacak. Mevcut lehim ekipmanı yeni alım kalemi olarak varsayılmayacak.
5. Adet × birim fiyat üzerinden toplam çıkarılacak; program sınırı ve danışman görüşüyle son bütçe oluşturulacak. Kontrol edilen program sayfasındaki destek üst sınırı 12.000 TL; bu tutar projenin belirlenmiş bütçesi veya destek alma garantisi değildir.

İlk denemelerde ağ aracısında 403 görülmüştü. 21 Ekim 2026 tarihli son incelemede Pololu ve üç yerel satıcıya HTTP 200 ile erişildi; bazı fiyatlar KDV ve stok etiketleriyle kaydedildi. Tamamlanan gözlemler [karşılaştırma dosyasında](MOTOR_SURUCU_BATARYA_KARSILASTIRMASI.md). Fiyatı bulunan tüm ürünler teknik açıdan seçilmiş değildir; tam bütçe oluşturulmadı.

**Teklif formu doldurma:** Her kaleme tam ürün kodu, satıcı bağlantısı, teklif tarihi, KDV durumu, stok, adet ve birim fiyat yazılacak. Şimdilik boş olan fiyat/tutar hücreleri sıfır kabul edilmeyecek. İsteğe bağlı ve mevcut ekipman satırları kesin alım toplamına otomatik dahil edilmeyecek. Toplam ancak temel parçalar ve bağımsız deney ölçümü için gereken kaynaklar tamamlandığında oluşturulacak.
