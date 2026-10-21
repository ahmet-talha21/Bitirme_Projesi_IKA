# 2. Yöntem — ilk bölüm taslağı

Durum: Kullanıcının ve danışmanın incelemesine açık çalışma taslağı. İki motorlu enkoderli şasi kullanıcı tarafından seçildi; Bug 2 tabanlı yaklaşım öneri durumunda. Sayısal hedefler, sensör modelleri ve referans ölçüm düzeni seçilmeden bu metin nihai TYBS içeriği olarak aktarılmayacak. Deney gerçekleştirilmiş değildir.

## 2.1. Araştırma tasarımı

Araştırma, küçük ölçekli bir kara aracı prototipinin geliştirilmesi ve kontrollü koşullarda tekrarlı deneylerle değerlendirilmesi biçiminde planlanmaktadır. Kullanıcı arayüzünde tanımlanan waypoint rotasının izlenmesi, sabit engellerin algılanması, çarpışmasız kaçınma ve rotaya yeniden katılma davranışları bütünleşik olarak ele alınacaktır. Deneyler, düz zeminde yaklaşık 3 × 3 metre olarak planlanan alanda gerçekleştirilecektir. Şasi boyutları ve gerekli geçiş açıklıkları belirlendikten sonra alanın yeterliliği kontrol edilecektir.

Koordinat tabanlı uygulama verilerinin ESP32 tabanlı mobil robota aktarılmasına ilişkin bir örnek Iqbal vd. (2023) tarafından sunulmuştur. Rodrigues vd. (2026) ise enkoder geri bildirimi, konum bilgisi ve gömülü motor kontrolünü bir araya getiren küçük ölçekli diferansiyel sürüşlü bir platformu deneysel olarak değerlendirmiştir. Bu çalışmalar, arayüz/rota tanımı, konum bilgisi ve hareket kontrolünün ayrı işlevler olarak tasarlanması için dayanak oluşturmaktadır; bu yayınların donanım ve başarı sonuçları geliştirilecek araç için doğrudan geçerli sayılmayacaktır.

## 2.2. Donanım ve konum kestirimi önerisi

Platform, iki tahrik tekerinin bağımsız kontrol edildiği küçük bir şasi ve enkoderli motorlar üzerine kurulacaktır. ESP32, motor sürücüsü, mesafe sensörleri ve uygun güç altyapısının bütünleştirilmesi planlanmaktadır. Tekerlek dönüşlerinden göreli hareketin hesaplanması için diferansiyel sürüş kinematiği kullanılabilecektir (Dellaert ve Hutchinson, t.y.). Motor, sürücü ve besleme modelleri elektriksel gereksinimler birlikte kontrol edilerek seçilecektir. Engel sensörlerinin türü, sayısı ve yerleşimi; algılama mesafesi, yüzey davranışı, güncelleme hızı ve kaçınma sırasında gerekli ön/yan kapsama göre seçilecektir.

Başlangıç konumu ve yönü tanımlanacak; enkoder verileriyle göreli konum/yön kestirimi yapılması değerlendirilecektir. Gerekirse IMU desteği kullanılacaktır. Tekerlek ölçekleri ve dönüş davranışı kalibre edilecek; kayma ve ölçüm hatalarının rota takibine etkisi incelenecektir. Seçilen yaklaşım yeterli doğruluğu sağlamazsa ek konum düzeltme yöntemi, hedefleri değiştirmeyen bir B planı olarak ayrıca tanımlanacaktır. Bağımsız ölçümde kullanılan kameranın konum kestirimine de veri sağlaması seçilirse, bu değişiklik açıkça belirtilecektir.

## 2.3. Arayüz ve veri akışı önerisi

Bilgisayar öncelikli, telefondan da erişilebilir bir web arayüzünde alan ölçeği, başlangıç yönü ve waypoint sırası tanımlanacaktır. Rota ve komutların yerel Wi-Fi üzerinden araca aktarılması; sensör, konum kestirimi ve görev durumunun arayüzde gösterilmesi planlanmaktadır. ESP-IDF'nin HTTP sunucusunda WebSocket desteği bulunması bu haberleşme seçeneği için teknik dayanak sağlamaktadır (Espressif Systems, t.y.). Rota yüklendikten sonra algılama ve hareket kararlarının ESP32 üzerinde yürütülmesi önerilmektedir. Bağlantı kaybı, sensör hatası ve durdurma komutu davranışları uygulama öncesinde belirlenecektir.

## 2.4. Engel kaçınma ve rotaya dönüş önerisi

Algoritma adayı, Bug 2 yaklaşımının rota izleme, engel çevresini takip etme ve hedef doğrultusuna yeniden katılma mantığını durum makinesiyle uygulamaktır (Hauser, t.y.-a). Her iki ardışık waypoint arasında bir başlangıç–hedef doğrultusu tanımlanacaktır. Engel tespit edildiğinde araç, algılama ve durma mesafesine uygun biçimde yavaşlatılacak veya durdurulacak; temas gerçekleşmeden kaçınma durumuna geçilecektir. Yerel mesafe ölçümlerine göre engel çevresi izlenirken seçilen izleme yönü ve açıklık korunmaya çalışılacaktır.

Rotaya katılma için aracın hedef doğrultusuna belirlenen tolerans içinde ulaşması, hedefe uzaklığının kaçınmaya başladığı noktaya göre azalması ve ilerleme yönündeki algılanan açıklığın yeterli olması birlikte değerlendirilecektir. Aynı bölgede ilerleyememe, geçersiz sensör verisi, alan sınırına yaklaşma veya süre sınırının aşılması durumlarında deneme durdurulup nedeni kaydedilecektir. Teorik noktasal robot varsayımları yerine gerçek aracın genişliği, dönüş kabiliyeti ve ölçüm belirsizliği tasarımda dikkate alınacaktır. Bu nedenle teorik yöntemden gerçek araç için koşulsuz başarı garantisi çıkarılmayacaktır.

## 2.5. Deney koşulları ve değişkenler

Önce engelsiz referans parkuru çalıştırılacak; ardından aynı rota farklı sabit engel yerleşimleriyle tekrarlanacaktır. Engel boyutları ve yüzeyleri, sensörlerin doğrulanmış algılama koşullarına göre tanımlanacak; geçişler araç geometrisine uygun seçilecektir. Her deney koşulu birden çok kez uygulanacaktır. Başlangıç pozu, rota, hız ayarı, zemin ve kontrol parametreleri mümkün olduğunca sabit tutulacak; pil durumu ve değişen koşullar kaydedilecektir.

- **Temel bağımsız değişken:** Sabit engellerin parkurdaki yerleşimi. Engel sayısı/boyutu da değiştirilecekse bunlar ayrı deney faktörleri olarak tanımlanacaktır.
- **Bağımlı değişkenler:** Temas öncesi algılama, çarpışmasız kaçınma, rotaya dönüş ve görev tamamlama sonuçları; tamamlanma süresi ve tanımlı referansa göre rota hatası.
- **Kontrol edilen koşullar:** Başlangıç pozu, referans rota, hız ayarı, zemin ve sabit deney parametreleri. Kontrol edilemeyen değişimler kayıtlarda belirtilecektir.

## 2.6. Ölçüm ve değerlendirme

Her deneme için engelin temas öncesinde algılanıp algılanmadığı, kaçınmanın temas olmadan tamamlanıp tamamlanmadığı, rotaya yeniden katılım ve hedefe varış ayrı ayrı kaydedilecektir. Engelsiz referans koşulunda oluşan yanlış engel uyarıları da kaydedilecektir. Bu ayrım, algılama hatası ile kaçınma veya konum kestirimi sorunlarının birbirinden ayrılmasını amaçlamaktadır. Geçerli denemelerin tamamı ilgili koşulun paydasında tutulacak; başarısız denemeler sonuçları iyileştirmek için çıkarılmayacaktır. Yalnızca önceden tanımlanmış kayıt/düzenek hataları geçersiz sayılacak ve gerekçeleri ayrıca bildirilecektir.

Başarı oranları başarılı deneme sayısının ilgili koşuldaki geçerli deneme sayısına bölünmesiyle hesaplanacaktır. Süreler ve rota sapması için uygun özet istatistikler verilecek; tamamlanamayan denemeler süre sınırı/başarısızlık kaydıyla ayrıca gösterilecektir. Rota izleme sırasında referans doğru parçasına uzaklık, kaçınma sırasındaki geçici sapma ve rotaya katılma sonrası izleme hatası ayrı değerlendirilecektir. Böylece engelden dolaşmanın gerektirdiği geçici rota değişimi doğrudan başarısız izleme olarak etiketlenmeyecektir. Bu aşamada istatistiksel anlamlılık veya belirli bir başarı yüzdesi vaat edilmemektedir. Tekrar sayıları ve karşılaştırma yöntemi son deney planında belirlenecektir.

Rota sapması için, işaretlenmiş deney alanını gören sabit bir kameradan bağımsız referans yol ölçümü değerlendirilmekte; kamera ve görüntü kalibrasyonu olanakları henüz doğrulanmamıştır. Ölçümün güvenilir referansla ilişkilendirilmesi ve kalibrasyon gereksinimi Hauser'in kalibrasyon çerçevesiyle uyumludur (Hauser, t.y.-b). Rota hatası, yalnızca aracın kendi konum tahmini yine kendisiyle karşılaştırılarak doğrulanmayacaktır.

## Kesinleştirilecek parametreler

| Parametre | Mevcut durum |
| --- | --- |
| Şasi, motor/enkoder ve sensör modelleri | Enkoderli iki motorlu hareket mimarisi seçildi; ölçüler ve ürünler seçilmedi. |
| Hız, algılama/durma ve yan açıklık mesafeleri | Donanım/kalibrasyonla gerekçelendirilecek. |
| Waypoint ve rotaya katılma toleransları | Konum ölçümü doğruluğuyla birlikte seçilecek. |
| Engel düzenleri ve tekrar sayıları | İlk tasarım belirlendi; sayısal deney planı hazırlanacak. |
| Başarı eşikleri ve süre sınırı | Henüz seçilmedi. |
| Bağımsız referans ölçümü | Kamera erişimi ve alanı görebilen düzenek doğrulanacak. |

## Kaynaklar

Iqbal vd. (2023), Rodrigues vd. (2026), Dellaert ve Hutchinson ile Hauser'in planlama bölümünün tam künyeleri [literatür karşılaştırmasında](LITERATUR_KARSILASTIRMASI.md) verildi. Bu bölümde ayrıca kullanılanlar:

- Espressif Systems. “HTTP Server”. ESP-IDF v5.5.1 Documentation. [Resmî kaynak deposu](https://github.com/espressif/esp-idf/blob/v5.5.1/docs/en/api-reference/protocols/esp_http_server.rst). Son erişim: 21 Ekim 2026.
- Hauser, K. “Calibration”. *Robotic Systems*, Bölüm 22. [Yazarın kaynak deposu](https://github.com/krishauser/RoboticSystemsBook/blob/master/Calibration.ipynb). Son erişim: 21 Ekim 2026.

Hauser'in planlama ve kalibrasyon bölümleri metin içinde sırasıyla t.y.-a ve t.y.-b olarak ayrılmıştır. Nihai TYBS başvurusunda tüm kullanılan kaynaklar tek bir alfabetik kaynakçada birleştirilecek ve DOI bulunan makalelerin DOI'leri korunacaktır.
