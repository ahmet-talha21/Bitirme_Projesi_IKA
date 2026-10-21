# TÜBİTAK 2209-A — Araştırma Önerisi

**İlk birleşik metin taslağı · 22 Ekim 2026**

**Proje adı önerisi:** Kullanıcı Tanımlı Rota Takibi ve Engelden Kaçınma Özellikli Otonom Kara Aracının Geliştirilmesi

Bu belge planlanan araştırmanın ilk birleşik taslağıdır. Prototip ve deneyler henüz yapılmamıştır. Deney yeri belli değildir; açık bilgiler son bölümde toplanmıştır.

## Genel bilgiler

| Alan | Bilgi |
| --- | --- |
| Proje yürütücüsü | Ahmet Talha Arslan |
| Üniversite / bölüm | Konya Teknik Üniversitesi / Elektrik-Elektronik Mühendisliği |
| Öğrenim durumu | Lisans, 4. sınıf |
| Akademik danışman | Prof. Dr. Murat Ceylan |
| Proje ekibi | Tek öğrenci yürütücü |
| Akademik teslim hedefi | Haziran 2027; kesin gün henüz belli değil. |
| Resmî proje süresi | Henüz belirlenmedi. |
| Talep edilecek destek | Nihai bütçe henüz belirlenmedi. |

## Özet

Bu araştırmada, kullanıcı tarafından arayüzde tanımlanan bir rotayı izleyen, karşılaştığı sabit engelleri algılayarak çarpışmadan kaçınan ve ardından rotasına yeniden katılan küçük ölçekli bir otonom kara aracı geliştirilmesi amaçlanmaktadır. Araştırma, farklı engel yerleşimlerinin algılama, kaçınma, rotaya dönüş ve görev tamamlama davranışına etkisini kontrollü deneylerle inceleyecektir.

Prototip, ESP32 kontrol birimi, bağımsız sürülen iki enkoderli motor ve ön orta, iki ön çapraz ile iki yan yönünde yerleştirilecek beş sabit mesafe sensörü üzerine kurulacaktır. Kullanıcı, bilgisayar öncelikli ve telefondan erişimi de hedeflenen arayüzde yerel koordinatlarla ara rota noktaları belirleyecektir. Enkoder geri bildirimiyle göreli konum kestirimi ve mesafe ölçümlerine dayalı kaçınma davranışı bütünleştirilecektir. Kaçınma için Bug 2 mantığından yararlanan bir durum makinesi, taslak yöntem olarak değerlendirilmektedir.

Düz zeminde yaklaşık 3 × 3 metre olarak planlanan alanda engelsiz referans ve üç sabit engel yerleşimi karşılaştırılacaktır. Her koşul 10 kez tekrarlanarak toplam 40 geçerli değerlendirme denemesi yapılacaktır. Her engelli koşulda en az 8/10 denemede temas öncesi algılama, çarpışmasız kaçınma, rotaya dönüş ve hedefe ulaşmanın birlikte sağlanması hedeflenmektedir. Aracın hareketinin bağımsız değerlendirilmesinde, mevcut telefonla sabit görüntü kaydı ve kalibrasyon düzeni kurulması planlanmaktadır.

Çalışma; donanım ve sensör entegrasyonu, arayüz ve haberleşme, rota izleme, kaçınma ve kontrollü deneyler olmak üzere beş iş paketinde yürütülecektir. Beklenen çıktılar bir araç prototipi, rota arayüzü, deney kayıt kümesi ve performans değerlendirmesiyle birlikte sürümlenmiş teknik dokümantasyondur.

**Anahtar kelimeler:** Otonom kara aracı, rota takibi, engelden kaçınma, enkoder, gömülü kontrol.

## 1. Bilimsel nitelik

### 1.1. Konunun önemi ve araştırma önerisinin bilimsel niteliği

Otonom kara araçlarında rota takibi, aracın konum ve yön bilgisinin hareket kontrolüyle birlikte değerlendirilmesini gerektirir. İki tekeri bağımsız sürülen mobil robotların kinematik modeli, tekerleklerin hareketi ile aracın doğrusal ve açısal hareketi arasındaki ilişkiyi tanımlar. Bu nedenle kullanıcı tarafından belirlenen bir rotanın fiziksel ortamda izlenmesi, yalnızca hareket komutlarının gönderilmesine değil, aracın yöneliminin ve hareketinin uygun biçimde izlenmesine de bağlıdır (Dellaert ve Hutchinson, t.y.). Rota üzerinde engel bulunması durumunda ise aracın engeli algılaması, çarpışmadan kaçınacak bir hareket üretmesi ve hedefe ilerleyişini sürdürebilmesi gerekir.

Hareket planlama literatüründe yerel engel bilgisini kullanan Bug türü yöntemler, önceden tüm engellerin haritası bilinmeden hedefe yönelik hareketin ele alınabildiği yaklaşımlar arasındadır. Bu yöntemlerin incelenmesinde robotun konumuna, engel geometrisine ve algılama biçimine ilişkin varsayımlar önem taşır. Ayrıca robotun fiziksel boyutlarının dikkate alınması, noktasal bir modelle bulunan yolun gerçek bir araçta uygulanabilirliğinin değerlendirilmesi açısından gereklidir (Hauser, t.y.-a).

İlgili uygulamalarda Iqbal vd. (2023), yapı modelinden çıkarılan koordinatların masaüstü uygulaması ve bulut bağlantısı üzerinden ESP32 tabanlı bir mobil robota aktarılmasıyla zemin çizimi gerçekleştiren bir sistem sunmuştur. Rodrigues vd. (2026) ise enkoderler, dış kamera temelli konum bilgisi ve ESP32 gömülü kontrol katmanını içeren küçük bir diferansiyel sürüşlü robotta yörünge takibini deneysel olarak değerlendirmiştir. Bu örnekler, koordinat aktarımı, konum bilgisi ve motor kontrolünün farklı mimarilerle bütünleştirilebildiğini göstermektedir. Önerilen projede ele alınacak değerlendirme görevi, kullanıcının tanımladığı rota üzerinde yerel algıyla engelden kaçınma ve rotaya yeniden katılmadır. Çalışmanın bilimsel çerçevesi, bu davranışın seçilen donanım ve sınırlı deney koşullarında hangi aşamalarda başarılı veya başarısız olduğunun tekrarlı ölçümlerle incelenmesine dayanmaktadır.

Bu projede ele alınacak problem, kullanıcı tarafından belirlenen waypoint rotasında ilerleyen mikrodenetleyici tabanlı bir kara aracının, farklı yerleşimlerdeki sabit engelleri algılayarak çarpışmasız kaçınma hareketi gerçekleştirmesi ve ardından rotasına yeniden katılmasıdır. Çalışma, düz zeminde yaklaşık 3 × 3 metre olarak planlanan kontrollü bir deney alanıyla sınırlandırılacaktır. Rota, bilgisayar öncelikli ve telefondan erişimi de hedeflenen kullanıcı arayüzündeki ölçülü kareli alan üzerinde tanımlanacaktır. Deneylerde engellerin yerleşimleri değiştirilecek; algılama, çarpışmasız kaçınma, rotaya dönüş ve görev tamamlama davranışları ayrı ayrı değerlendirilecektir.

Çalışmanın araştırma sorusu, “Sabit engellerin yerleşimi, kullanıcı tanımlı waypoint rotalarını izleyen küçük ölçekli bir kara aracında engel algılama, çarpışmasız kaçınma ve rotaya yeniden katılma başarısını nasıl etkiler?” biçiminde ele alınmaktadır. Geliştirilecek prototip üzerinde tekrarlanabilir deneyler gerçekleştirilmesi, başarılı ve başarısız durumların kaydedilmesi ve performansın ölçülebilir göstergelerle açıklanması amaçlanmaktadır. Kalibrasyon ve değerlendirmede güvenilir referans ölçümleri kullanılması, sensör çıktıları ile fiziksel hareket arasındaki ilişkinin incelenmesine dayanak sağlayacaktır (Hauser, t.y.-b). Bu kapsamda beklenen katkı; kullanıcı arayüzü, gömülü kontrol ve engelden kaçınma davranışının bütünleştirildiği bir prototip ile sınırları tanımlı deney koşullarına ait performans verilerinin oluşturulmasıdır.

### 1.2. Amaç ve hedefler

Projenin amacı, kullanıcı tanımlı waypoint rotasını izleyen küçük ölçekli bir kara aracında sabit engelin temas öncesinde algılanmasını, çarpışmasız kaçınma hareketinin gerçekleştirilmesini ve rotaya yeniden katılarak görevin sürdürülmesini sağlayan bir prototip geliştirmek; bu davranışın başarısını sınırları tanımlanmış deney koşullarında değerlendirmektir. Arayüz tasarımı, gömülü kontrol yazılımı ve donanım entegrasyonu proje yürütücüsü tarafından gerçekleştirilecektir.

Bu amaç doğrultusunda aşağıdaki hedefler izlenecektir:

1. Bilgisayar öncelikli ve telefondan da erişilebilir bir arayüzde yerel koordinatlarla rota tanımlama, rotayı araca aktarma, başlatma/durdurma ve görev durumunu izleme işlevlerini geliştirmek.
2. İki enkoderli motorun geri bildirimiyle rota izleme altyapısını kurmak; beş sabit mesafe sensörünün ön ve yan kapsamasını kalibrasyonla değerlendirmek.
3. Engel algılama, çarpışmasız kaçınma ve rotaya dönüşü açık durum/geçiş kurallarıyla bütünleştirmek.
4. Engelsiz referans ve üç sabit engel yerleşiminde koşul başına 10, toplam 40 geçerli değerlendirme denemesi yürütmek.
5. Her engelli koşulda en az 8/10 denemede temas öncesi algılama, çarpışmasız kaçınma, rotaya dönüş ve hedefe ulaşmayı birlikte sağlamak; tüm geçerli başarısızlıkları da değerlendirmeye katmak.
6. Algılama, kaçınma, rotaya dönüş ve görev sonuçlarını ayrı kaydetmek; tamamlanma süresi ve bağımsız referansla ölçülebilen rota hatasını raporlamak.

Tekrar sayısı ve koşul başına ana başarı hedefi yürütücü tarafından uygun bulunmuştur. Kesin toleranslar, süre sınırı ve ek başarı eşikleri; ölçüm düzeni, donanımın uygulanabilirliği ve danışman değerlendirmesiyle sonlandırılacaktır. Bu hedefler gelecekte yapılacak çalışmaya aittir.

## 2. Yöntem

### 2.1. Araştırma tasarımı

Araştırma, bir kara aracı prototipinin geliştirilmesi ve kontrollü koşullarda tekrarlı deneylerle değerlendirilmesi biçiminde yürütülecektir. Temel bağımsız değişken, aynı referans rota üzerindeki sabit engelin yerleşimidir. Engel boyutu, yüzeyi ve sayısı engelli koşullar arasında sabit tutulacak; birden çok değişkenin etkisi tek bir etki gibi yorumlanmayacaktır. Bağımlı değişkenler temas öncesi algılama, çarpışmasız kaçınma, rotaya dönüş ve görev tamamlama sonuçları ile süre ve rota sapmasıdır.

Başlangıç konumu/yönü, referans rota, zemin, hız ayarı ve kontrol parametreleri koşullar arasında aynı tutulmaya çalışılacaktır. Pil gerilimi, aydınlatma ve kontrol edilemeyen değişimler kayıt altına alınacaktır. İlk deney alanı düz zeminde yaklaşık 3 × 3 metre olarak planlanmaktadır. Alanın fiziksel yeri henüz belirlenmemiş olup şasi ve geçiş açıklıkları seçildikten sonra geometrik yeterliliği kontrol edilecektir.

### 2.2. Donanım ve konum kestirimi

Araç, iki tahrik tekerinin bağımsız kontrol edildiği enkoderli bir diferansiyel sürüş mimarisine sahip olacaktır. ESP32; motor sürücüsü, enkoderler ve mesafe sensörleriyle bütünleştirilecektir. Tekerlek dönüşlerinden göreli doğrusal/açısal hareketin hesaplanmasında diferansiyel sürüş kinematiğinden yararlanılacaktır (Dellaert ve Hutchinson, t.y.). Başlangıç pozu tanımlanacak; tekerlek ölçekleri ve dönüş davranışı kalibre edilecektir. Kayma ve biriken konum hatası ayrıca incelenecek, gerekirse IMU desteği veya ek konum düzeltmesi değerlendirilecektir.

Engel algılamada ön orta, iki ön çapraz ve iki yan yönünde beş sabit mesafe sensörü kullanılacaktır. Sensör modeli, montaj yüksekliği ve açıları; ölçüm aralığı, yüzey davranışı, güncelleme hızı ve kaçınmanın gerektirdiği kapsama göre seçilecektir. Sensör sayısı kesintisiz çevre taraması sağlandığı anlamına gelmez; gerçek kapsama düzenekte kontrol edilecektir. Motor, sürücü, batarya ve regülasyon bileşenleri elektriksel ve mekanik uyum birlikte değerlendirilerek belirlenecektir.

![Şekil 1 — Sistem mimarisi](gorseller/sekil_1_sistem_mimarisi.png)

**Şekil 1.** Arayüz, algılama, ESP32 ve motor sürme işlevleri arasındaki planlanan veri akışı. Simgeler temsilidir; çizim ÜYZ desteğiyle hazırlanmış tasarım şemasıdır.

### 2.3. Kullanıcı arayüzü ve haberleşme

Kullanıcı, ölçülü kareli bir ekran üzerinde başlangıç noktası/yönünü ve sıralı waypoint'leri belirleyecektir. Bilgisayardan kullanım öncelikli olacak, telefondan erişim de hedeflenecektir. Rota aktarımı ve telemetri için yerel Wi-Fi üzerinden HTTP/WebSocket bağlantısı değerlendirilmektedir. ESP-IDF HTTP sunucusunun WebSocket desteği, bu haberleşme seçeneğinin teknik dayanağını oluşturmaktadır (Espressif Systems, t.y.).

Rota araca yüklendikten sonra algılama ve hareket kararlarının araç üzerinde yürütülmesi planlanmaktadır. Arayüzde tahmini konum, sensör geçerlilik bilgisi ve görev durumu gösterilecektir. Bağlantı kesilmesi, sensör hatası, durdurma komutu ve ilerleyememe durumlarının davranışları uygulama öncesinde tanımlanacak ve denenecektir. Kesin arayüz teknolojisi ve ağ çalışma modu henüz seçilmemiştir.

### 2.4. Engel kaçınma ve rotaya yeniden katılma

Taslak yöntem önerisi, Bug 2 yaklaşımının hedef doğrultusunu izleme, engel çevresini takip etme ve uygun koşullarda doğrultuya yeniden katılma mantığını bir durum makinesine uyarlamaktır (Hauser, t.y.-a). Kesin algoritma kararı henüz verilmemiştir. Her ardışık waypoint çifti için aktif bir rota parçası tanımlanacak; rota izleme, engel tespiti, kaçınma ve rotaya katılma durumları ayrı yürütülecektir.

Engel algılandığında araç, toplam algılama/karar gecikmesi ve ölçülmüş durma mesafesi dikkate alınarak yavaşlatılacak veya durdurulacaktır. Ardından mesafe ölçümleriyle engel çevresini takip ederek geçiş açıklığını korumaya çalışacaktır. Rotaya katılmada aktif rota parçasına uzaklık, hedefe yaklaşma, engelin geride bırakılması ve ilerleme yönündeki açıklık birlikte değerlendirilecektir. Rota çizgisinin bir kez kesilmesi tek başına başarılı dönüş sayılmayacaktır.

Aracın gövde boyutları, dönüşte kapladığı alan ve sensörlerin gövdeye göre konumu dikkate alınacaktır. Teorik noktasal robot varsayımlarından gerçek araç için koşulsuz başarı sonucu çıkarılmayacaktır. Aynı bölgede ilerleyememe, geçersiz veri, alan sınırına yaklaşma ve süre aşımı durdurma/başarısızlık nedeni olarak kaydedilecektir.

![Şekil 2 — Kontrol akışı](gorseller/sekil_2_calisma_akisi.png)

**Şekil 2.** Rota izleme, engel algılama, kaçınma ve rotaya dönüş için önerilen kontrol akışı. “A” bağlantıları yeni kontrol döngüsüne dönüşü gösterir. Çizim ÜYZ desteğiyle hazırlanmıştır.

### 2.5. Deney koşulları ve tekrarlar

Geliştirme aşamasında önce engelsiz hareket ve rota takibi, ardından engelli kaçınma davranışı kontrol edilecektir. Kalibrasyon ve algoritma ayarı için kullanılan denemeler nihai değerlendirme verilerine dahil edilmeyecektir. Son değerlendirmede aşağıdaki dört koşul, aynı rota ve sabitlenmiş yazılım/parametrelerle uygulanacaktır.

| Koşul | Planlanan yerleşim | Geçerli tekrar |
| --- | --- | --- |
| K0 | Engelsiz referans rotası. | 10 |
| K1 | Rotanın düz bölümünde tek sabit engel. | 10 |
| K2 | Dönüş öncesi bölümde aynı sabit engel. | 10 |
| K3 | Dönüş sonrası bölümde aynı sabit engel. | 10 |

Toplam 40 geçerli değerlendirme denemesi yapılacaktır. Koşulların 10 blokta uygulanması, her blokta dört koşulun birer kez ve önceden rastgeleleştirilmiş sırayla yürütülmesi önerilmektedir. Böylece koşulların yalnızca pilin belirli bir durumuna veya tek bir uygulama sırasına denk gelmesi azaltılacaktır. Nihai rota, engel koordinatları ve geçiş açıklıkları araç geometrisiyle birlikte sonlandırılacaktır. L biçimli 3 metre rota, mevcut protokolde başlangıç önerisidir.

![Şekil 3 — Deney düzeni](gorseller/sekil_3_deney_alani.png)

**Şekil 3.** Planlanan yaklaşık 3 × 3 metre alanda örnek rota ve kaçınma davranışının temsili gösterimi. Şekil nihai engel koordinatlarını veya ölçülmüş yolu göstermez; kaçınma eğrisi deney/simülasyon verisi değildir. Çizim ÜYZ desteğiyle hazırlanmıştır.

### 2.6. Bağımsız ölçüm ve başarı tanımı

Aracın hareketi, mevcut telefonla sabit görüntü kaydı üzerinden bağımsız olarak değerlendirilecektir. Bu düzenek henüz kurulmamıştır; tüm alanın görülmesi, sabitleme, görüntü–metre dönüşümü, lens bozulması ve izleme işaretinin yüksekliğine bağlı perspektif hatası kontrol edilecektir. Kalibrasyonda kullanılmayan kontrol noktalarıyla ölçüm doğruluğu değerlendirilecektir. Güvenilir referansla kalibrasyon gereksinimi, Hauser'in (t.y.-b) yaklaşımıyla uyumludur. Rota hatası aracın kendi konum tahmininin yine kendisiyle karşılaştırılmasıyla doğrulanmayacaktır.

Sensör günlüğü ve kamera kaydı ortak bir başlangıç olayıyla zaman bakımından eşleştirilecektir. Temas öncesi algılama, çarpışmasız kaçınma, rotaya dönüş ve hedefe varış ayrı ayrı işaretlenecektir. Her engelli koşulda en az 8/10 geçerli denemede bu aşamaların birlikte tamamlanması ana başarı hedefidir. Yalnızca engel önünde durmak veya insan müdahalesiyle devam etmek başarılı otonom görev sayılmayacaktır.

Waypoint toleransı, rotaya dönüş bandı ve süre sınırı, ölçüm duyarlılığı ve donanım davranışıyla gerekçelendirilecektir. Mevcut çalışma notlarındaki 10 cm bant ve 120 saniye sınırı henüz seçilmiş değerler değildir. Bu değerler ile ek hedefler başvuru metni sonlandırılmadan önce değerlendirilecektir.

### 2.7. Veri analizi ve başarısız denemeler

Her koşul için başarı oranları, ilgili aşamada başarılı deneme sayısının o koşuldaki tüm geçerli denemelere bölünmesiyle hesaplanacaktır. Birleşik görev hedefi her engelli koşul için ayrı aranacak; yalnız toplam engelli başarı oranının yeterli görünmesi, bir koşuldaki yetersizliği gizlemeyecektir. Engelsiz koşulda yanlış engel uyarıları ayrıca sayılacaktır.

Tamamlanan denemelerin süreleri medyan ve en küçük–en büyük değerlerle özetlenecek; tamamlanamayan denemeler ve süre aşımları ayrıca gösterilecektir. Ölçüm kapsamı uygunsa rota izleme bölümlerinde RMSE ve en büyük sapma değerlendirilecektir. Kaçınma sırasındaki gerekli geçici sapma ile rotaya dönüşten sonraki izleme hatası ayrılacaktır. Görüntü kaybı ve ölçülemeyen aralıklar raporlanacaktır.

Çarpışma, kontrol kesintisi, ilerleyememe ve süre aşımı gibi geçerli başarısızlıklar paydada tutulacaktır. Yalnızca önceden tanımlanmış, araç davranışından bağımsız kayıt/düzenek hataları nedeniyle değerlendirilemeyen denemeler gerekçeleriyle ayrılabilecektir. Yazılım veya donanım değişirse sürüm ve neden kaydedilecek; karşılaştırılan koşullar aynı son sürümle değerlendirilecektir. Bu tekrar planından bütün kullanım ortamlarına başarı veya istatistiksel anlamlılık sonucu çıkarılmayacaktır.

### 2.8. Ön hazırlık durumu

Başvuru hazırlığında güncel program belgeleri, ilgili yayınlar ve teknik dokümanlar incelenmiş; mimari, deney protokolü, kaynaklı malzeme adayları ve tasarım şemaları hazırlanmıştır. Fiziksel prototip üretilmemiş, sensör/motor kalibrasyonu veya performans deneyi yapılmamıştır. Dolayısıyla araç için elde edilmiş doğruluk, başarı oranı veya çalışma süresi bildirilmemektedir.

## 3. Proje yönetimi

### 3.1. Çalışma takvimi

Çalışma beş iş paketinde yürütülecektir. Aşağıdaki dönemler Haziran 2027 bitirme teslim hedefine göre hazırlanmış **akademik plan önerisidir**; resmî TÜBİTAK başlangıcı veya TYBS ay aralıkları değildir. Başvuruya girilecek toplam ay sayısı ve resmî iş paketi aralıkları başvuru öncesinde belirlenecektir. Her iş paketinin uygulama sorumlusu Ahmet Talha Arslan'dır.

| İP | Faaliyet ve başarı kontrolü | Akademik hedef dönemi | Katkı |
| --- | --- | --- | --- |
| 1 | Donanım/sensör entegrasyonu ve kalibrasyon: iki motor, iki enkoder, beş sensör ve besleme davranışının kontrolü. | Kasım–Aralık 2026; donanıma erişime bağlı. | %20 |
| 2 | Arayüz/haberleşme: rota tanımlama, aktarım, başlatma/durdurma ve durum izlemenin doğrulanması. | Ocak 2027 | %15 |
| 3 | Konum kestirimi/rota izleme: engelsiz waypoint takibi ve bağımsız referansla hata değerlendirmesi. | Şubat 2027 | %20 |
| 4 | Engel algılama, kaçınma ve rotaya dönüş: davranışların bütünleştirilmesi ve ayar denemeleri. | Mart–Nisan 2027 | %30 |
| 5 | Kontrollü deney ve analiz: seçilen 40 deneme, koşul başına ana başarı hedefi ve başarısızlıklar dahil değerlendirme. | Mayıs 2027 | %15 |

Katkı değerleri toplamı %100'dür; bunlar deney başarı yüzdeleri değildir. Donanım erişimi beklenirken arayüz ve yazılım hazırlığı öne alınabilecektir. Mayıs içinde deney/analiz, Haziran içinde danışman incelemesi ve bitirme teslimi hedeflenmektedir. Literatür incelemesi, malzeme alımı ve rapor hazırlığı ayrı iş paketi olarak gösterilmemiştir. Haziran teslim günü henüz belli değildir.

### 3.2. Risk yönetimi

| Risk | Önleyici çalışma | Temel hedefi koruyan B planı | İP |
| --- | --- | --- | --- |
| Enkoder ölçeği, kayma veya dönüşlerde biriken konum hatası. | Düz ilerleme/dönüş kalibrasyonu ve engelsiz referans kontrolü. | Mekanik tutuş ve kalibrasyonu düzeltmek; gerekirse IMU/ek konum düzeltmesini maliyet ve bağımsız doğrulamayla değerlendirmek. | 1, 3, 4 |
| Engel yüzeyi veya sensör kapsaması nedeniyle geç algılama. | Gerçek engel yüzeylerinde ön/yan kapsama ve durma mesafesi kontrolü. | Yerleşim/süzmeyi düzenlemek; gerekli algılamayı koruyan uyumlu sensör seçeneğini değerlendirmek. | 1, 4 |
| Kaçınmada döngüye girme veya rotaya katılamama. | Durum geçişlerini, ilerlemeyi ve kaçınma başlangıç noktasını kaydetmek. | Sınır izleme/katılma koşullarını ayar denemelerinde düzeltip son sürümle değerlendirmeyi yenilemek; kabul eşiklerini sonuçtan sonra gevşetmemek. | 4, 5 |
| Besleme düşümü veya motor akımı nedeniyle kontrol kesintisi. | Motor–sürücü–pil uyumu, kalkış/dönüş ve güç dağıtımı kontrolü. | Uygun besleme ve bağlantıları yeniden seçmek; değişiklik sonrası durdurma davranışını doğrulamak. | 1, 4 |
| Bağımsız görüntü ölçümünün kurulamaması veya yetersizliği. | Alan görüşü, sabitleme ve kalibrasyonun uygulanabilirliğini kontrol etmek. | Başka erişilebilir sabit görüntüleme düzeni veya açıkça tanımlanmış bağımsız kontrol noktası ölçümü seçmek; sürekli yörünge ölçülmüş gibi sonuç vermemek. | 1, 5 |
| Temin sorunu veya bütçenin yetersizliği. | Kaynaklı fiyat, stok ve teknik uyumu birlikte incelemek. | İki motorun enkoderini ve beş sensörlü temel düzeni koruyan alternatifleri değerlendirmek; zorunlu olmayan ekleri ertelemek. | 1–5 |

Hata nedeniyle durdurulan bir deneme başarılı kaçınma sayılmayacaktır. B planları, otonom kaçınma ve rotaya dönüşü elle yönlendirme veya yalnızca durmayla değiştirmeyecektir.

### 3.3. Araştırma olanakları

Deney alanının fiziksel yeri henüz belirlenmemiştir. Üniversitede kullanılacak belirli bir laboratuvar, cihaz veya imalat altyapısına erişim de doğrulanmamıştır. Kurum olanakları tablosu bu bilgiler alındığında tamamlanacaktır. Şu anda yürütücünün doğruladığı kişisel kaynaklar aşağıdadır; bunlar kurum envanteri olarak sunulmamaktadır.

| Kişisel kaynak | Planlanan kullanım | Tamamlanacak kontrol |
| --- | --- | --- |
| Mevcut lehim ekipmanı | Elektronik bağlantılar ve montaj. | Son bağlantı/imalat ihtiyaçları. |
| Mevcut telefon | Deney hareketinin bağımsız görüntü kaydı. | Tüm alanı görme, sabitleme, kalibrasyon ve kayıt kalitesi. |

Mevcut telefon ve lehim ekipmanı için yeniden alım planlanmamaktadır. Multimetre, uzunluk ölçümü, şasi imalatı ve telefon sabitleme olanakları ayrıca doğrulanacaktır. Planlanan ESP32, motor ve sensörler mevcut kurum ekipmanı gibi gösterilmeyecektir.

## 4. Araştırma önerisinin yaygın etkisi

Araştırma sonunda kullanıcı arayüzü, gömülü kontrol ve engelden kaçınmayı birlikte ele alan bir prototip ile sınırları tanımlanmış deney verilerinin oluşturulması hedeflenmektedir. Başarılı ve başarısız denemelerin ayrı aşamalarla kaydedilmesi, benzer öğrenci çalışmalarında tasarım kararlarının ve kısıtların anlaşılmasına yardımcı olabilecektir.

| Çıktı grubu | Hedeflenen somut çıktı | Beklenen kullanım / kontrol |
| --- | --- | --- |
| Teknolojik | Bir araç prototipi ve bir rota arayüzü. | Rota yükleme, algılama, kaçınma ve dönüşün tanımlı deneylerde değerlendirilmesi; gömülü kontrol/robotik eğitiminde örnek kullanım. |
| Bilimsel / yöntemsel | Bir deney protokolü, bir kayıt kümesi ve performans değerlendirmesi. | Koşullar, sürümler, başarılar ve başarısızlıkların ilişkilendirilmesi; gözlenen sınırların açıklanması. |
| Eğitsel / yeniden kullanım | Bir sürümlenmiş yazılım ve teknik dokümantasyon paketi. | GitHub'da bağlantı, kurulum, arayüz/araç yazılımı ve deney düzeninin incelenebilir biçimde tutulması. |
| Yeni araştırmalar | Sınırlılıklar ve geliştirme önerileri bölümü. | Sensör kapsaması, konum sürüklenmesi ve kaçınma davranışı hakkında bulguya dayalı sonraki araştırma önerileri. |

Yürütücünün gömülü sistem, arayüz geliştirme, sensör kalibrasyonu ve deneysel analiz becerilerini geliştirmesi beklenmektedir. Paylaşılabilir teknik çıktılar aynı GitHub deposunda düzenlenecektir. Yayın veya bilimsel sunum olanağı, elde edilecek bulguların niteliği ve danışman değerlendirmesine göre ele alınacaktır.

## 5. Belirtmek istenen diğer konular

Projenin ilk kapsamı düz zemindeki sabit engellerle sınırlandırılmıştır. Hareketli engeller, gerçek coğrafi harita, farklı zemin türleri ve her ortamda doğrulanmış çalışma bu deney planının hedefi değildir. Önceki yıllara ait örnek başvurular anlatım/yerleşim açısından incelenmiş; metinleri, sonuçları veya kişisel bilgileri bu öneriye aktarılmamıştır.

## 6. Ekler

Bu taslakta ayrı ölçek veya anket eki bulunmamaktadır. Üç tasarım şeması ilgili yöntem bölümlerinde yer almaktadır. Ayrıntılı deney protokolü, boş kayıt şablonu ve malzeme/fiyat kayıtları hazırlık dosyalarında tutulmaktadır; bunlar yapılmış deney sonucu değildir.

## Kaynakça

- Dellaert, F., Hutchinson, S. t.y. “Motion Model for the Differential Drive Robot”. *Introduction to Robotics and Perception*, Bölüm 5.2. İnternet adresi: https://github.com/gtbook/robotics/blob/main/S52_diffdrive_actions.ipynb. Son erişim tarihi: 21 Ekim 2026.

- Espressif Systems. t.y. “HTTP Server”. *ESP-IDF Programming Guide*, v5.5.1. İnternet adresi: https://github.com/espressif/esp-idf/blob/v5.5.1/docs/en/api-reference/protocols/esp_http_server.rst. Son erişim tarihi: 21 Ekim 2026.

- Hauser, K. t.y.-a. “Motion planning in simple geometric spaces”. *Robotic Systems*, Bölüm 9. İnternet adresi: https://github.com/krishauser/RoboticSystemsBook/blob/master/GeometricMotionPlanning.ipynb. Son erişim tarihi: 21 Ekim 2026.

- Hauser, K. t.y.-b. “Calibration”. *Robotic Systems*, Bölüm 22. İnternet adresi: https://github.com/krishauser/RoboticSystemsBook/blob/master/Calibration.ipynb. Son erişim tarihi: 21 Ekim 2026.

- Iqbal, F., Ahmed, S., Amin, F., Qayyum, S., Ullah, F. 2023. “Integrating BIM–IoT and Autonomous Mobile Robots for Construction Site Layout Printing”, *Buildings*, 13(9), 2212. DOI: https://doi.org/10.3390/buildings13092212.

- Rodrigues, V. O. B., Silva, G. A. A., Pugliese, L. F., Silva, W. W. A. G., Monte-Mor, J. A., Karolak, D. B., Gomides, L. M., Braga, R. A. S. 2026. “Hierarchical Control Architecture for Trajectory Tracking of Differential-Drive Nonholonomic Robots Using LQG-Based Velocity Control”, *Robotics*, 15(9), 171. DOI: https://doi.org/10.3390/robotics15090171.

## Son düzenlemede tamamlanacak alanlar — hazırlık notu

Bu bölüm çalışma takibi içindir; başvuru metninin bilimsel bölümüne aynen aktarılmayacaktır.

- Son proje başlığı ve danışmanın metin değerlendirmesi.
- Resmî proje süresi ve TYBS'ye uygun ay aralıkları; Haziran bitirme hedefiyle uyumu.
- Deney yerinin seçimi ve gerçekten kullanılacak kurum olanakları.
- Algoritma/ürün seçimleri, bağımsız ölçüm uygulanabilirliği ve kalan sayısal toleranslar.
- Türkiye teslim giderleri ve eksik kalemlerle tamamlanmış nihai TL bütçesi. Mevcut kaynaklı referans hesabı 11.986,24 TL'dir; şasi ve diğer eksikler dahil değildir, talep edilecek bütçe olarak yazılmamıştır.
- Özetin son metinle uyumu, atıflar, görsel etiketleri ve TYBS önizleme kontrolü.

2026 başvurusu TYBS alanlarına girilen bilgilerle oluşturulmaktadır. Bu belgenin PDF/Word sürümü birlikte inceleme içindir; ayrı bir araştırma önerisi PDF'si yükleme şartı olarak sunulmamaktadır.

**ÜYZ beyanı için hazırlık kaydı:** ChatGPT/Codex; kaynak inceleme desteği, taslakların hazırlanması/düzenlenmesi ve belge oluşturma için; image_gen üç tasarım şemasının üretilmesi için kullanılmıştır. Araç sürümü görünmüyorsa tahmin edilmeyecektir. Başvuru sistemindeki beyan alanı gerçek kullanım kapsamıyla doldurulacak; içerik yürütücü ve danışman tarafından kontrol edilecektir.
