# Donanım seçeneği ve uyumluluk değerlendirmesi

Tarih: 21 Ekim 2026. Bu belge, birlikte değerlendirilecek ilk somut donanım önerisidir. ESP32 ve iki enkoderli motor mimarisi kullanıcı tarafından seçildi. Aşağıdaki kart/modül modelleri, sensör sayısı, ölçüler ve besleme düzeni henüz kullanıcı kararı veya kesin satın alma listesi değildir. Ürünlerin stok, fiyat ve tüm elektriksel özellikleri doğrulanmış değildir.

## 1. Önerilen başlangıç düzeni

| İşlev | Önerilen aday | Gerekçe / seçimi tamamlayacak koşul |
| --- | --- | --- |
| Ana kontrol | Bir ESP32-DevKitC V4, ESP32-WROOM-32E modüllü sürüm. | Wi-Fi, motor kontrolü ve enkoder/sensör bağlantıları için aday. Gerçek kartın pinleri ve besleme şeması kontrol edilecek. Farklı ESP32 kartları aynı pin düzenine sahip varsayılmayacak. |
| Hareket | İki aynı model, enkoderli N20 sınıfı düşük akımlı 6 V redüktörlü DC motor; yaklaşık 100 d/d çıkış hızı bir arama ölçütü. | Küçük araç için başlangıç adayı. Sıkışma akımı, tork, enkoder beslemesi/çıkışı ve çözünürlük tanımı alınmadan ürün seçilmeyecek. Bu öneri belirli bir N20 ürününün bu şartları karşıladığı iddiası değildir. |
| Mekanik | Yaklaşık 20 × 15 cm sınıfında şasi; motor miline uygun yaklaşık 60 mm iki tekerlek, iki motor bağlantısı ve bir serbest taşıyıcı teker. | Ölçüler tasarım önerisi. Batarya, motor ve sensörler yerleştirilince toplam kütle, tekerlek açıklığı ve dönüş sırasında taranan alan kontrol edilecek. Hazır kitte bulunan parçalar ayrıca iki kez bütçelenmeyecek. |
| Motor sürücüsü | Bir TB6612FNG çift kanallı modül, düşük akımlı motor şartıyla. | İki motor için bağımsız hız/yön kontrolü. Bu ön düzen için her motorun 6 V'daki sıkışma akımı en fazla 1 A olan model aranacak; seçilecek modülün sürekli akım/ısıl kapasitesi ayrıca doğrulanacak. Uygun motor bulunamazsa sürücü adayı değiştirilecek. |
| Engel mesafesi | Beş VL53L0X ToF taşıyıcı modül. | Ön orta, ön sol, ön sağ, sol yan ve sağ yan için öneriliyor. Modüllerin 3,3 V besleme ve I²C uyumluluğu belgeli olacak. |
| Sensör bağlantısı | Bir TCA9548A I²C çoklayıcı modül. | Aynı başlangıç adresindeki sensörleri ayrı kanallardan okumayı sağlar. Her işlemde yalnızca ilgili sensör kanalı etkinleştirilecek. |
| Güç | Hazır korumalı iki hücreli seri lityum pil paketi (2S), pakete uygun şarj cihazı; 5 V ve 3,3 V regülasyon dalları. | Kapasite, çıkış akımı ve gerçek ürün seçilmedi. Önerilen güç düzeni aşağıda açıklandı. |

### Motor ve sürücü birlikte nasıl seçilecek?

Motorun yalnızca boşta akımı yeterli değildir. Sürücü seçimi için çalışma akımı, kalkış/sıkışma akımı ve bunların süresi gerekir. SparkFun'ın TB6612FNG kart belgesi kanal başına 1,2 A sürekli ve 3,2 A tepe değerini bildiriyor [D2]. Tepe değer sürekli çalışma kapasitesi olarak kullanılmayacak; başka bir üreticinin modülü aynı ısıl kapasiteye sahip varsayılmayacak.

Başlangıç için düşük akımlı motor arama koşulu konuldu. Motor bu koşulu karşılamıyorsa listede yalnızca adını değiştirmek yetmez; sürücü, regülatör ve batarya akım gereksinimi birlikte yeniden hesaplanacak. İki motor aynı anda yük altındayken gerekli toplam akım da dikkate alınacak.

Enkoderin A/B çıkışları ESP32'nin 3,3 V girişleriyle uyumlu olacak. Enkoderin motorla aynı beslemeyi kullandığı varsayılmayacak; gerekirse uygun seviye dönüştürme veya başka motor/enkoder ürünü seçilecek. Çözünürlük, motor mili/çıkış mili ayrımı ve sayılan kenarlar belirtilerek kaydedilecek.

## 2. Neden beş sabit sensör öneriliyor?

Öndeki ölçüm engeli fark etmek için, yan ölçümler ise engelin kenarını izleyip açıklığı korumak için kullanılabilecek. Ön çapraz ölçümler, köşelere yaklaşırken ek bilgi sağlayabilecek. Açılar yaklaşık ön orta, ±45° ve ±90° olarak düşünülebilir; bunlar nihai montaj açıları değildir. Şasi ve sensör görüş alanına göre düzenlenecek.

VL53L0X taşıyıcısı için Adafruit dar algılama alanını ve taşıyıcı üzerindeki regülatör/seviye dönüştürmeyi açıklıyor [D3]. Bu özellikler tüm benzer görünümlü modüllerde var kabul edilmeyecek. Dar görüş alanı nedeniyle beş sensör dahi aracın çevresinde kesintisiz tarama sağlamaz. Engel boyutu/yüzeyi, sensör yüksekliği, kör bölgeler ve durma mesafesi gerçek düzenekte sınanacak; her tür engeli algılama iddiası kurulmayacak.

| Düzen | Katkısı | Sınırlılığı / karar durumu |
| --- | --- | --- |
| Beş sabit ToF sensörü + çoklayıcı | Ön, ön çaprazlar ve iki yandan ölçüm; hareketli tarama mekanizması gerektirmez. | Bu belgedeki başlangıç önerisi. Ürün maliyeti ve gerçek kapsama doğrulanacak. |
| Üç sabit ToF sensörü: ön, sol, sağ | Daha az modül ve bağlantı kullanır. | Ön çaprazlarda daha az bilgi sağlar; parça sayısının azalması tek başına kaçınma için yeterli olduğunu göstermez. Ancak deneyle yeterliliği doğrulanırsa değerlendirilecek. |
| Ultrasonik sensör düzeni | Başka bir mesafe algılama seçeneği. | Gerçek modülün yankı sinyali seviyesi, yüzey/açı davranışı ve çoklu sensörlerin birbirini etkilemesi kontrol edilmeli. Güncel fiyatlarla karşılaştırma henüz yapılamadı. |

Çoklayıcı zorunlu olan tek bağlantı yöntemi değildir. VL53L0X kütüphanesinde adres değiştirme işlevi, Adafruit örneğinde de XSHUT ile sensörleri sırayla başlatma yaklaşımı bulunuyor [D4–D5]. Çoklayıcı önerisi, beş sensörde ayrı adres atama ve çok sayıda XSHUT bağlantısını yönetme gereğini azaltmak içindir; hem çoklayıcı hem ayrı XSHUT düzeni birlikte zorunlu alım olarak yazılmadı.

Sensörler sırayla ölçülecekse tam taramanın süresi ve haberleşme gecikmesi durma mesafesi hesabına dahil edilecek. Aynı anda açık sensörlerin optik etkisi de kontrol edilecek. Ölçüm yapılamaması doğrudan “önü boş” sayılmayacak.

## 3. Önerilen güç ve bağlantı düzeni

- **Batarya:** 2S hazır paket, yaygın 4,2 V/hücre şarj sonu gerilimine sahip kimya seçilirse nominal 7,4 V ve tam doluyken 8,4 V. Paket kimyası, kapasitesi, koruması ve izin verilen akımı ürün belgesiyle doğrulanacak. Koruma devresi şarj cihazının yerine geçmez; uygun şarj cihazı ayrıca listelendi.
- **5 V dalı:** Bataryadan düşürücü regülatörle 5 V elde edilmesi; gerçek giriş aralığında en az 3 A sürekli çıkış sağlayabilen bir modülün aday olarak incelenmesi. Regülatörün üzerinde yazan tepe akımı yeterli kanıt sayılmayacak. Motor sürücüsünün güç girişi ile ESP32'nin 5 V girişi ayrı kablo dallarıyla beslenecek; güç dönüşleri ve yerel süzme elemanları düzenlenecek.
- **Motor gerilimi:** Bu ilk düzende 6 V anma değerli motorun 5 V ile çalıştırılması öneriliyor. 6 V için verilen hız/torkun 5 V'ta aynen elde edileceği varsayılmayacak. Yük altında gereken hareket sağlanamazsa motor/redüksiyon veya güç düzeni birlikte değiştirilecek. Bataryanın ham 8,4 V çıkışı 6 V motora bağlanmayacak.
- **3,3 V dalı:** Beş sensör, çoklayıcı ve sürücü mantığı için ayrı regülasyon öneriliyor; toplam tüketim ve ısıl hesap ürünlere göre yapılacak. Böylece sensör yükünün ESP32 kartındaki regülatöre uygun olduğu varsayılmayacak. I²C hatlarının çekme dirençleri 3,3 V ile uyumlu olacak.
- **Ortak referans:** Bütün denetim/sensör devreleri ortak GND referansı kullanacak. Motorlar ESP32 GPIO veya 3,3 V çıkışından beslenmeyecek. Sürücünün STBY/PWM başlangıç davranışı, enerji verildiğinde istenmeyen hareket üretmeyecek biçimde tasarlanacak.
- **Programlama:** DevKitC kılavuzu USB, 5 V pini ve 3,3 V pininden beslemeyi birbirini dışlayan seçenekler olarak tanımlıyor [D1]. Programlama sırasında batarya beslemesi ayrılacak veya gerçek kart için uygun güç ayırma düzeni kurulacak; iki kaynağın birlikte güvenle kullanılabildiği varsayılmayacak.

Batarya kapasitesinden çalışma süresi henüz hesaplanmadı. Motor yükü, elektronik tüketimi ve dönüştürücü verimi belirlenince enerji bütçesi çıkarılacak. Sigorta, anahtar, konnektör ve kablo kapasiteleri de bu hesaba göre seçilecek.

## 4. Ek parça ve ölçüm ihtiyaçları

- Altı eksenli IMU, enkoderle yapılan yön/konum kestiriminin gereksinimine göre değerlendirilecek; şu anda zorunlu alım değil ve tek başına mutlak konum referansı sağlamaz.
- Motor gürültüsünü sınırlayacak ve beslemeyi süzecek elemanların değer/adetleri, seçilen motor ve sürücü belgesine göre çıkarılacak.
- Multimetre, metre ve deney alanı işaretleme malzemesine erişim doğrulanacak. Kullanıcının lehim ekipmanı mevcut; diğer araçlar mevcut sayılmıyor.
- Bağımsız referans ölçümü için kamera/düzenek henüz seçilmedi. Kamera kullanımı veya alımı bu listeyle kesinleştirilmedi; ölçüm planı ve varsa ek maliyeti ayrıca tamamlanacak.

## 5. Teklif alınmadan önce gerekli ürün bilgileri

1. Motorun tam kodu; anma gerilimi, redüksiyonu, hızı, torku, yük/kalkış/sıkışma akımları; enkoderin besleme, çıkış ve çözünürlük bilgisi.
2. Sürücü modülünün gerçek devresi, akım/ısıl sınırları ve 3,3 V kontrol uyumu.
3. Sensör/çoklayıcı taşıyıcılarının regülatör, seviye dönüştürme ve çekme dirençleri; beş sensörün toplam tüketimi.
4. Şasi boyutları ve toplam kütle; motor mili, tekerlek, bağlantı ve batarya yerleşim uyumu.
5. Batarya/şarj cihazı ve regülatörlerin tam kodları, giriş/çıkış sınırları ve doğrulanmış sürekli akım kapasiteleri.
6. Adet, tarihli fiyat, KDV durumu, stok ve teslim koşulları. Doğrulanmış fiyat gelmeden toplam bütçe yazılmayacak.

## İncelenen üretici / taşıyıcı üreticisi kaynakları

21 Ekim 2026 tarihinde aşağıdaki içerikler doğrudan okundu. Bunlar her marka eşdeğer modülün uyumluluğunu veya stok/fiyatını doğrulamaz. Kütüphane dokümanı, seçilecek ürünün veri sayfasının yerini tutmaz.

- **[D1]** Espressif, *ESP32-DevKitC V4 Getting Started Guide*, ESP-IDF v4.4 deposu: [resmî kaynak](https://github.com/espressif/esp-idf/blob/v4.4/docs/en/hw-reference/esp32/get-started-devkitc.rst). Kart sürümleri, pinler ve besleme seçenekleri okundu. Bu, proje yazılım sürümü seçimi değildir.
- **[D2]** SparkFun, *Motor Driver — Dual TB6612FNG*: [üretici kaynak deposu](https://github.com/sparkfun/Motor_Driver-Dual_TB6612FNG). İki kanal, akım değerleri, PWM ve STBY açıklamaları okundu.
- **[D3]** Adafruit, *VL53L0X ToF Distance Sensor PCB*: [taşıyıcı kaynak deposu](https://github.com/adafruit/Adafruit-VL53L0X-ToF-Distance-Sensor-PCB). Algılama alanı ve taşıyıcı arayüzü açıklaması okundu; ürünün pazarlama niteliğindeki üstünlük ifadeleri proje başarısına aktarılmadı.
- **[D4]** Pololu, *VL53L0X Arduino Library*: [üretici kaynak deposu](https://github.com/pololu/vl53l0x-arduino). 3,3 V bağlantı örneği, I²C, adres değiştirme, ölçüm zamanlaması ve zaman aşımı işlevleri okundu.
- **[D5]** Adafruit, *vl53l0x_dual* örneği: [kaynak](https://github.com/adafruit/Adafruit_VL53L0X/blob/master/examples/vl53l0x_dual/vl53l0x_dual.ino). XSHUT ile sıralı başlatma ve ayrı adresler incelendi; bu proje kodu olarak denenmedi.
- **[D6]** Adafruit, *TCA9548A I2C Multiplexer PCB*: [taşıyıcı kaynak deposu](https://github.com/adafruit/Adafruit-TCA9548A-I2C-Multiplexer-PCB). Sekiz kanal ve kanal seçimi açıklaması okundu.

Motor ve batarya için henüz seçilmiş ürün veri sayfası yok. Ürün düzeyindeki uyumluluk kontrolü bu nedenle tamamlanmış sayılmıyor.

## Erişim ve fiyat durumu

Robotistan, Robolink Market ve Direnc.net sayfaları ile Pololu, ST, TI ve Espressif'in doğrudan doküman sitelerine istekler ağ aracısında 403 ile engellendi. İlgili GitHub kaynakları okunabildi. Fiyat karşılaştırması veya toplam maliyet elde edilemedi.

Gerekli alan adları, önceki izinler korunarak ortam yapılandırma taslağına eklendi. Araç `saved` ve `requires_publish: true` döndürdü. Bu kayıt ağı etkinleştirmedi; kayıttan sonraki denemelerde de 403 sürdü. Ortam ayarlarında değişikliklerin kaydedilip ortamın yayımlanması gerekiyor. Eklenen alan adları: `www.robotistan.com`, `www.robolinkmarket.com`, `www.direnc.net`, `www.pololu.com`, `www.st.com`, `www.ti.com`, `docs.espressif.com`, `www.espressif.com`.
