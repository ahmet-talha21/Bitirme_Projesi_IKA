# Malzeme ve bütçe ön listesi

Durum: Tek prototip için miktar ve uyumluluk planı. Kesin satın alma listesi veya TYBS bütçesi değildir. Kullanıcıdan yaklaşık bütçe henüz alınmadı; fiyatlar ve toplam tutar doğrulanmış değildir.

## Mevcut olanaklar

- ESP32 henüz mevcut değil; kullanıcı satın almayı planlıyor.
- Kullanıcı lehim ekipmanına sahip ve montajda sorun beklemiyor. Araç henüz monte edilmedi.
- Diğer parçaların mevcut olduğu bildirilmedi.
- Üniversite laboratuvarı, 3D yazıcı ve referans ölçüm kamerasına erişim henüz doğrulanmadı. Bunlar başvuruda mevcut altyapı olarak gösterilmeyecek.

## Temel mimari için teklif alınacak kalemler

Bu miktarlar iki tahrik tekerli diferansiyel sürüş önerisine aittir; kullanıcı bu şasiyi henüz seçmedi.

| Kalem | Önerilen miktar | Seçimde kontrol edilecek özellik |
| --- | --- | --- |
| ESP32 geliştirme kartı | 1 | Kesin kart modeli, kullanılabilir pinler, sensör ve enkoder bağlantıları, USB bağlantısı. |
| Enkoderli redüktörlü DC motor | 2 | Aynı model iki motor; besleme, kalkış/sıkışma akımı, redüksiyon, enkoder çıkışı ve çözünürlüğü. |
| Motorlarla uyumlu tekerlek | 2 | Mil bağlantısı, çap, zemin tutuşu ve konum hesabında kullanılacak çevre ölçüsü. |
| Şasi, motor bağlantıları ve taşıyıcı teker | 1 set | İki motoru ayrı kontrol etmeye ve sensör yerleşimine uygunluk; küçük alan içindeki dönüş ve geçiş açıklıkları. |
| Çift kanallı motor sürücüsü | 1 | Motorların besleme/akım gereksinimleri, ESP32 kontrol sinyalleriyle uyumluluk ve ısıl kapasite. |
| Mesafe algılama düzeni | Sayı belirlenecek | Ön ve yan açıklıklar için kapsama; minimum mesafe, algılama alanı, güncelleme hızı, yüzey ve elektriksel uyumluluk. Ultrasonik/ToF seçilmedi. |
| Batarya ve uygun şarj çözümü | 1 set | Motor ve elektronik beslemesi, beklenen çalışma süresi ve seçilen pil türüne uygun şarj. |
| Gerilim regülasyonu ve güç dağıtımı | 1 set | Seçilen batarya, motor ve kartın gerektirdiği gerilim/akımlara uygunluk. |
| Anahtar, kablo, konnektör, montaj ve devre malzemesi | İhtiyaca göre | Kesin devre ve şasiye göre miktarlandırılacak; set adıyla belirsiz toplu tutar yerine başvuru için gerekirse ayrı kalemler çıkarılacak. |

Basit bir araç kitinde enkoder bulunması otomatik olarak varsayılmayacak. Motor, sürücü ve güç bileşenleri birlikte kontrol edilmeden ürün listesi kesinleştirilmeyecek.

## İhtiyaca göre ayrıca değerlendirilecekler

- IMU: yön ölçümü ve konum kestirimine katkısı, kalibrasyon ihtiyacı ve bütçeyle değerlendirilecek; model seçilmedi.
- İlave mesafe sensörü veya tarama mekanizması: kaçınma algoritmasının istediği kapsama göre belirlenecek.
- Gövde/muhafaza: hazır bağlantı parçaları yeterliyse özel üretim gerekmeyebilir; 3D yazıcı erişimi varsayılmayacak.
- Deney ölçümü: metre, zemin işaretleri, uygun referans kamera ve sabitleme olanağı incelenecek. Rota sapmasını bağımsız ölçmek yöntem için gereklidir; kamera kullanımı ve satın alımı henüz kararlaştırılmadı.

## Bütçeyi kesinleştirme yöntemi

1. Önce motor-enkoder-şasi seçeneği ve hareket gereksinimleri netleştirilecek.
2. Motor sürücüsü ve güç bileşenleri bu seçime göre eşleştirilecek; sensör kapsaması kaçınma yöntemine göre belirlenecek.
3. Uyumlu ürünler için tarihli fiyat, adet, KDV durumu, stok ve teslim koşulları kaydedilecek. Varsa kargo ve yan giderlerin destek kapsamı ayrıca kontrol edilecek.
4. Yeni alınacak ve kişisel olarak zaten mevcut parçalar ayrılacak. Mevcut lehim ekipmanı yeni alım kalemi olarak varsayılmayacak.
5. Adet × birim fiyat üzerinden toplam çıkarılacak; program sınırı ve danışman görüşüyle son bütçe oluşturulacak. Kontrol edilen program sayfasındaki destek üst sınırı 12.000 TL; bu tutar projenin belirlenmiş bütçesi veya destek alma garantisi değildir.

21 Ekim 2026 tarihinde üç satıcının ESP32 sayfasına erişim denemeleri ağ aracısı tarafından 403 ile engellendi. Bu nedenle bu belgede güncel fiyat, doğrulanmış ürün modeli veya toplam maliyet verilmedi. Resmî bütçeye doğrulanmamış tahmin eklenmeyecek.
