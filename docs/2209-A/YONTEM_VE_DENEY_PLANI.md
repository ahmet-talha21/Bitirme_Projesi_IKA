# Yöntem ve deney planı — teknik öneri

Durum: Görüşülmek üzere hazırlanmış tasarım önerisi. Kullanıcının bildirdiği kapsamı temel alır; kesin satın alma listesi, tamamlanmış yöntem bölümü veya deney sonucu değildir. ESP32 dışında parça modelleri seçilmedi. ESP32 henüz satın alınmadı; kullanıcının lehim ekipmanı var. Yaklaşık bütçe, diğer parçaların mevcudiyeti ve kurum olanakları henüz bilinmiyor.

## 1. Kesinleşen kapsam

- Küçük ölçekli, ESP32 tabanlı bir kara aracı.
- Kullanıcı tarafından seçilen hareket mimarisi: iki bağımsız tahrik motoru ve tekerlek dönüşlerini ölçen enkoderler.
- Bilgisayar öncelikli, telefondan da erişilebilir arayüz.
- Ölçülü kareli ekranda tanımlanan waypoint rotası.
- Engel algılama, çarpışmasız kaçınma ve rotaya yeniden katılmanın değerlendirilmesi.
- Beş sabit mesafe sensörü: ön orta, iki ön çapraz ve iki yan. Model ve kesin montaj açıları henüz seçilmedi.
- Düz zeminde, yaklaşık 3 × 3 metre olarak planlanan deney alanı; uygunluğu şasi seçilince kontrol edilecek.
- İlk deneylerde sabit engeller; yerleşimler denemeler arasında değiştirilebilecek.

## 2. Önerilen donanım mimarisi

| Bileşen | Öneri ve gerekçe | Seçim durumu |
| --- | --- | --- |
| Kontrolcü | ESP32; rota, sensör okuma ve hareket kontrolü araç üzerinde yürütülebilir. | Kullanıcı tarafından seçildi; kart modeli belirsiz. |
| Şasi ve hareket | İki motorun ayrı kontrol edildiği küçük diferansiyel sürüşlü şasi. | İki motorlu enkoderli mimari seçildi; şasi boyutu, taşıyıcı teker düzeni ve motor modelleri seçilmedi. |
| Hareket geri bildirimi | Her tahrik tekeri için enkoder; dönüş miktarı ve hız ölçümünden göreli konum kestirimi. ESP32 PCNT birimi quadrature sinyal çözümlemeyi destekliyor [T1]. | Enkoder kullanımı seçildi; model, çözünürlük ve elektriksel uyumluluk kontrol edilecek. |
| Yön/hareket ölçümü | IMU ile yön değişimi ölçümünün enkoder bilgisiyle birlikte değerlendirilmesi. Kalibrasyon ve sürüklenme incelenecek. | İhtiyaç ve model belirsiz; yalnızca IMU ile kesin konum varsayılmayacak. |
| Engel algılama | Ön orta, iki ön çapraz ve iki yana bakan beş sabit mesafe sensörü. ToF adayı; algılama alanı, minimum mesafe, yüzey davranışı, güncelleme hızı ve bütçeyle değerlendirilecek. | Beş sensör ve genel yönleri kullanıcı tarafından seçildi. Tür/model, kesin açılar ve gerçek kapsama kontrol edilecek. |
| Motor sürücüsü | Seçilecek motorların beslemesine ve kalkış/sıkışma akımına uygun çift kanallı sürücü. | Motor seçilmeden model seçilmeyecek. |
| Güç | Motorlar ve elektronik için uygun besleme, regülasyon ve açma/kapama düzeni. | Pil ve şarj çözümü seçilmedi; bütçeye ayrıca yazılacak. |

Enkoder ve IMU ile konum kestiriminde hata birikebilir. Parkur uzunluğu, zemin ve kabul edilecek hata birlikte değerlendirilecek; gerekirse ek konum düzeltmesi planlanacak. Sensör görüş alanı ve aracın fiziksel genişliği kaçınma kararında dikkate alınacak.

Malzeme planını somutlaştırmak için [ayrı bir donanım adayı](DONANIM_SECENEKLERI_VE_UYUMLULUK.md) hazırlandı. Kullanıcı beş sabit sensörlü düzenle ilerlemeyi seçti. ToF modeli ve I²C çoklayıcı hâlen adaydır. Ürünlerin fiyatı, motor/sürücü/güç uyumu ve gerçek sensör kapsaması doğrulandıktan sonra yöntemle birlikte güncellenecek.

[Motor–sürücü–batarya karşılaştırmasında](MOTOR_SURUCU_BATARYA_KARSILASTIRMASI.md) somut referans motorların üretici verileri, enkoder sinyal seviyeleri ve bir TB6612FNG taşıyıcısının besleme/akım sınırları incelendi. Bu çalışma, parça önerisini destekler; 5 V altında yük deneyi, kurulmuş prototip veya kesin ürün seçimi değildir. Batarya/şarj/koruma ve toplam maliyet ayrıca tamamlanacak.

## 3. Arayüz ve haberleşme önerisi

- Bilgisayar ve telefon tarayıcısından açılabilen bir web arayüzü.
- Arayüzde alan ölçeği, başlangıç noktası/yönü ve waypoint sırası tanımlanması; başlatma/durdurma ve durum görüntüleme.
- ESP32 ile yerel Wi-Fi üzerinden rota aktarımı ve telemetri için HTTP/WebSocket değerlendirilmesi. Espressif'in HTTP sunucusu WebSocket desteği sunuyor [T2].
- Rota yüklendikten sonra engel algılama ve motor kontrol kararlarının araç üzerinde yürütülmesi öneriliyor. Anlık kontrolün tarayıcıdaki bağlantı gecikmesine bağımlı olmaması amaçlanıyor.
- Ağ modu, iletişim kesildiğinde davranış, kayıt sıklığı ve arayüz teknolojisi henüz kararlaştırılmadı.

## 4. Kaçınma ve rotaya dönüş yaklaşımı

Önerilen durumlar: rota izleme → engel tespiti ve yavaşlama/durma → engelden dolaşma → rotaya katılma → rota izleme. Hedefe varış, sensör hatası ve ilerleyememe durumları ayrıca ele alınacak.

Yerel sensör bilgisiyle engel çevresini izleyen Bug türü yöntemler, incelenecek algoritma adaylarıdır. Hauser'in açık ders kitabında bu yöntemlerin yerel engel bilgisiyle çalışabildiği ve Bug 2'nin hedef doğrultusuna dönüş mantığı açıklanıyor [T3]. PythonRobotics'te Bug 0/1/2 için simülasyon örnekleri bulunuyor [T4]. Bunlar uygulanmış proje kodumuz veya deney sonucumuz değil, teknik inceleme kaynaklarıdır.

Kesin algoritma henüz seçilmedi. İdeal noktasal robot veya hatasız konum varsayımlarına dayanan teorik özellikler, sonlu boyutlu ve ölçüm hatalı gerçek araç için doğrudan başarı garantisi olarak yazılmayacak. Temaslı algılama içeren ders örnekleri, çarpışmasız algılama hedefimize doğrudan kopyalanmayacak; uygun mesafe algısı ve açıklık kontrolü gerekecek.

## 5. Deney düzeni önerisi

1. Önce şasi boyutu, motor yönleri, enkoder ölçeği, sensör davranışı ve durma mesafesi kalibre edilecek.
2. Geliştirme aşamasında aynı rota engelsiz durumda çalıştırılarak temel hareket ve rota takibi kontrol edilecek. Son değerlendirmedeki engelsiz referans denemeleri geliştirme denemelerinden ayrı tutulacak.
3. Rotaya sabit engeller farklı yerleşimlerle konulacak. Engel çevresinde araç için geçiş alanı bırakılacak; açıklıklar şasi ve sensör seçimine göre belirlenecek.
4. Her koşul birden çok kez tekrarlanacak. Başlangıç pozu, rota, hız ayarı ve zemin mümkün olduğunca aynı tutulacak; pil durumu ve başarısız denemeler kaydedilecek.
5. Algılama, çarpışmasız kaçınma, rotaya dönüş ve görev tamamlama ayrı sonuçlar olarak raporlanacak. Tamamlanamayan denemeler analizden çıkarılmayacak; seçilen 120 saniye sınırı kullanılacak ve başarısızlık kayıtları deney öncesinde tanımlanacak.

| Ölçüt | Planlanan tanım |
| --- | --- |
| Engel algılama | Engel bulunan denemelerde temas öncesi tespit sayısı / geçerli engelli deneme sayısı. Uygun sensör kayıtları ve gözlemle kontrol edilecek. |
| Çarpışmasız kaçınma | Temas olmadan kaçınma manevrasını tamamlayan denemelerin oranı. |
| Rotaya dönüş | Kaçınma sonrasında etkin sonlu rota parçasına en çok 10 cm uzaklıktaki banda, diğer katılma koşullarını da sağlayarak dönen denemelerin oranı. |
| Görev tamamlama | 120 saniye içinde sıralı waypoint'lere ve son hedefe en çok 10 cm uzaklığa ulaşarak görevi tamamlayan denemelerin oranı. |
| Süre ve rota sapması | Tamamlanma süresi ve bağımsız referans ölçümüne göre izlenen yolun tanımlı rotadan sapması. |

Rota sapması aracın kendi enkoder tahminini yine kendisiyle karşılaştırarak doğrulanmayacak. İşaretlenmiş alanı gören harici bir kamerayla referans yol ölçümü aday yöntemdir. Kullanıcı telefonunu deneylerde kullanabileceğini bildirdi; görüş alanı, sabitleme, ölçek kalibrasyonu ve ölçüm doğruluğu henüz doğrulanmadı. Bu telefon araç üstü algılama kamerası olarak seçilmedi.

Kullanıcı [deney protokolündeki](DENEY_PROTOKOLU_ONERISI.md) dört koşulda 10'ar tekrar, toplam 40 deneme ve her engelli koşulda en az 8/10 birleşik görev başarısı hedefini uygun buldu. Kullanıcı 10 cm waypoint erişimi, 10 cm rotaya dönüş bandı ve 120 saniye deneme sınırını da planlanan hedefler olarak seçti. Aynı 3 m L rotası ve bağımsız ölçüm kontrol değerleri hâlen öneridir. Donanım/alan, kalibrasyon gerektiren parametreler ve danışman incelemesi açık. [Deneme kayıt CSV'si](DENEY_KAYIT_SABLONU.csv) yalnız sütun başlıklarını içeriyor, deney sonucu yok. Mevcut kaynak incelemesi literatürde özgünlük veya üstünlük iddiası kurmak için yeterli değildir; ilgili akademik çalışmalar ayrıca incelenecek.

## 6. Açık bilgiler

- ESP32 dışındaki parçaların mevcudiyeti, yaklaşık bütçe ve kurum olanakları. Kullanıcının lehim ekipmanı olduğu doğrulandı; ESP32 satın alınacak.
- Şasi, enkoder, mesafe sensörü, motor sürücüsü ve güç bileşenleri.
- Referans ölçümü için kullanıcının telefonu mevcut; tüm alanı gören sabitleme ve kalibrasyonun uygulanabilirliği henüz doğrulanmadı.
- Kullanıcının teknik önerilere ilişkin tercihleri ve danışman görüşü.

## İncelenen teknik kaynaklar

Kontrol tarihi: 21 Ekim 2026. Doğrudan teknik dokümantasyon sitesine erişilemediği için Espressif belgelerinin resmî GitHub deposundaki v5.5.1 sürümü okundu. Bu sürüm, proje için seçilmiş yazılım sürümü değildir.

- **[T1]** Espressif Systems, ESP-IDF v5.5.1, “Pulse Count Controller (PCNT)”: [resmî kaynak](https://github.com/espressif/esp-idf/blob/v5.5.1/docs/en/api-reference/peripherals/pcnt.rst). Quadrature sinyal çözümleme ve enkoder örneği incelendi.
- **[T2]** Espressif Systems, ESP-IDF v5.5.1, “HTTP Server”: [resmî kaynak](https://github.com/espressif/esp-idf/blob/v5.5.1/docs/en/api-reference/protocols/esp_http_server.rst). WebSocket desteği ve yerel ağ örneği incelendi.
- **[T3]** Kris Hauser, *Robotic Systems*, “Motion planning in simple geometric spaces”: [yazarın açık ders kitabı](https://github.com/krishauser/RoboticSystemsBook/blob/master/GeometricMotionPlanning.ipynb). Bug algoritmaları ve model varsayımları incelendi. Taslak ders kitabıdır.
- **[T4]** PythonRobotics, “Bug Planning”: [kod örneği](https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/BugPlanning/bug.py). Bug 0/1/2 simülasyon uygulaması incelendi; bu çalışma kapsamında çalıştırılmadı.

Bu liste teknik hazırlık kaynaklarıdır; nihai başvuru kaynakçası biçimi ve akademik literatür listesi ayrıca düzenlenecektir.
