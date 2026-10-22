# İKA — 2209-A hazırlık notları

Güncelleme: 22 Ekim 2026. Bu belge başvuru metni değil, kullanıcı tarafından doğrulanan bilgiler ve açık soruların kaydıdır.

## Kullanıcının belirttiği bilgiler

- Kullanıcının seçtiği proje başlığı (22 Ekim 2026): Kullanıcı tarafından belirlenen rota bilgisine göre hareket eden otonom araç tasarımı.
- Araç ESP32 ile geliştirilecek.
- Kullanıcı, iki motoru bağımsız kontrol edilen küçük bir şasi ve her iki tahrik tekerinin dönüşünü ölçen enkoderlerle ilerlemeyi seçti. Şasi ölçüleri, motor/enkoder modelleri ve taşıyıcı teker düzeni henüz belirlenmedi.
- Kullanıcı arayüzü proje sahibi tarafından tasarlanacak; araç bu arayüz üzerinden kontrol edilecek.
- Kullanıcı rotayı arayüzden tanımlayacak; araç rotayı otonom takip edecek.
- Engel algılandığında engelden kaçınma davranışı devreye girecek; araç daha sonra rotasına dönerek ilerleyecek. Algoritma henüz seçilmedi.
- Kullanıcı temel amacın engeli algılamak ve başarılı bir kaçınma hareketi gerçekleştirmek olduğunu netleştirdi. Rota takibi ve rotaya dönüş, bu davranışın görev içindeki değerlendirme çerçevesidir; eşya taşıma gibi ek görev belirlenmedi.
- İlk sürüm için ölçülü kareli alan üzerinde waypoint (ara rota noktaları) seçimi kullanıcı tarafından uygun bulundu. Sonraki aşamada isteğe bağlı ölçekli mekân krokisi ekleme yaklaşımı da uygun bulundu; bu ek özellik ilk sürüm için zorunlu teslim olarak belirlenmedi.
- Kullanıcı ev, okul ve iş yeri gibi farklı yerlerde kullanılabilirlik istiyor. Küçük Arduino/RC araçları boyutunda bir prototip ve düz zeminde kullanım belirtildi. İlk deneyler için yaklaşık 3 × 3 metre alan planlanıyor; bu, ölçülmüş veya üzerinde test yapılmış bir alan değil. Kesin araç ölçüleri ve kullanılacak fiziksel yer henüz belirlenmedi.
- Kullanıcı 22 Ekim 2026 tarihinde deney yerinin henüz belli olmadığını açıkça bildirdi ve rapor metninin yazılmasını istedi. Yer seçimi veya diğer açık teknik bilgiler ilk birleşik metnin hazırlanmasını durdurmayacak; bilinmeyenler açıkça işaretlenecek.
- Arayüzde öncelik bilgisayar kullanımı; telefonda da çalışması isteniyor. Her iki cihazda açılabilen tarayıcı arayüzü teknik seçenek olarak değerlendiriliyor; yazılım teknolojisi ve haberleşme yöntemi seçilmedi.
- Gerçek coğrafi harita ilk sürüm kapsamına alınmadı; yerel rota ekranı seçildi.
- ESP32 dışındaki malzemeler birlikte seçilecek; donanım listesi henüz kesinleşmedi.
- Kullanıcı beş sabit mesafe sensörüyle ilerlemeyi seçti: ön orta, iki ön çapraz ve iki yan. Bu karar sensör sayısı ve genel yerleşim düzenine aittir; VL53L0X/ToF modeli, kesin montaj açıları ve çoklayıcı ürünü henüz kesinleşmedi. Gerçek algılama kapsaması deneyle kontrol edilecek.
- Kullanıcı 22 Ekim 2026 tarihinde dört koşulda 10'ar tekrar, toplam 40 değerlendirme denemesini ve her engelli koşulda en az 8/10 denemede algılama, çarpışmasız kaçınma, rotaya dönüş ve hedefe ulaşmayı birlikte başarma hedefini uygun buldu. Bu yanıt 10 cm tolerans, 120 saniye, ek 9/10 hedefleri, hız, kesin geometri veya tüm protokol için onay sayılmadı. Sonuç değil, gelecekteki deney planı/hedefidir; danışman incelemesi ve uygulanabilirlik açık.
- Kullanıcının elinde henüz ESP32 yok; satın almayı planlıyor. Diğer araç bileşenlerinin mevcut olduğu bildirilmedi. Yaklaşık bütçe henüz bilinmiyor.
- Kullanıcının lehim ekipmanı var ve araç montajında sorun yaşayacağını düşünmüyor. Bu bilgi kişisel olanaktır; üniversite laboratuvarı, 3D yazıcı veya başka kurum altyapısının mevcut olduğu henüz doğrulanmadı.
- Kullanıcı, deneylerde kullanabileceği bir telefonu olduğunu 22 Ekim 2026 tarihinde doğruladı. Telefon kişisel ölçüm olanağı olarak planlanacak; yeni kamera satın alımı eklenmeyecek. Alanın tamamını görme, sabitleme, kayıt özellikleri ve kalibrasyon henüz kontrol edilmedi; bağımsız ölçüm düzeni kurulmuş sayılmayacak.
- TÜBİTAK 2209-A başvurusu hazırlanacak.
- Başvuru tek öğrenciyle yapılacak; proje ortağı bulunmayacak.
- Başvuru sahibi, adını Ahmet Talha Arslan olarak bildirdi; Konya Teknik Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü 4. sınıf öğrencisi olduğunu belirtti.
- Akademik danışman, kullanıcının bildirdiği üzere Prof. Dr. Murat Ceylan.
- Teknik ayrıntılar kullanıcıya sorularak netleştirilecek; bilinmeyen özellikler ve sonuçlar yazılmayacak.
- Kullanıcı projeye henüz başlamadığını belirtti. Şu an başvuru hazırlığı ve tasarım planlama aşamasındayız; çalışan araç, kurulmuş deney düzeneği veya tamamlanmış ön deney bulunmuş gibi yazılmayacak.
- Süre sorusuna kullanıcı “haziran ayına kadar sürücek” yanıtını verdi. Ardından Haziran 2027 hedefinin bitirme projesi teslimi olduğunu ve kesin günün henüz belli olmadığını açıkladı. Altı aylık süre veya Ocak başlangıcı onaylanmış sayılmayacak. Resmî TÜBİTAK süresi, sonuç ilanı ve başlangıç koşullarıyla ayrıca belirlenecek.
- Kullanıcı deney kapsamının uygulanabilir ve güçlü bir başvuru sağlayacak şekilde seçilmesini istedi. Bu kapsamda ilk deneyler için sabit engeller seçildi: engeller denemeler sırasında hareketsiz olacak, yerleşimleri denemeler arasında değiştirilebilecek. Hareketli engeller ana başvuru kapsamına eklenmedi. Bu bir çalışma planıdır; deney sonucu değildir.

## Netleştirilecek konular

İlk donanım mimarisi, arayüz/haberleşme seçenekleri, kaçınma yaklaşımı ve deney önerileri [yöntem ve deney planında](YONTEM_VE_DENEY_PLANI.md) hazırlandı. Bu teknik öneriler parça satın alma kararı veya kullanıcı tarafından onaylanmış nihai yöntem değildir.

Mevcut ekipman durumu ve teklif alınacak kalemler [malzeme ve bütçe ön listesinde](MALZEME_VE_BUTCE_ON_LISTESI.md) tutuluyor. Fiyatlar doğrulanmadan başvuru bütçesi oluşturulmayacak.

Kullanıcının malzeme listesini oluşturma isteği üzerine [donanım adayı ve uyumluluk değerlendirmesi](DONANIM_SECENEKLERI_VE_UYUMLULUK.md) hazırlandı: WROOM-32E modüllü DevKitC, düşük akımlı enkoderli N20 motorlar, koşullu TB6612FNG, beş sabit VL53L0X ve TCA9548A, regüle beslemeli 2S paket başlangıç önerileri. Kullanıcı sonrasında beş sabit sensörlü düzenle ilerlemeyi seçti; bu yanıt belirli ürün modellerini veya kesin montaj açılarını onaylamış sayılmıyor. İlk aşamada motor/batarya ürünleri ve fiyatlar doğrulanmamıştı. [Teklif tablosu](MALZEME_TEKLIF_FORMU.csv) oluşturuldu; sonraki incelemeyle referanslar ve bazı fiyatlar eklendi.

Sonraki [motor–sürücü–batarya incelemesinde](MOTOR_SURUCU_BATARYA_KARSILASTIRMASI.md) Pololu #5143 (MP 210:1, 6 V, 100 d/d) somut motor referansı, #5115 alternatif ve #713 TB6612FNG referans taşıyıcı olarak incelendi. Bunlar ürün satın alma/onay kararı değil. Yerel satıcı ve üretici erişimi HTTP 200 ile sağlandı; bazı gerçek fiyatlar ve stok etiketleri kaydedildi. Batarya koruma/şarj bilgileri, ithal motorun teslim maliyeti, gerçek araç yükü ve tam bütçe açık. Kaynak fiyatları TL ve USD ayrı tutulacak.

22 Ekim tarihli [fiyatlı bütçe taslağında](FIYATLI_BUTCE_TASLAGI.md) 13 yerel fiyat adayı için 3.189,41 TL, beş döviz kalemi için 177,35 USD ara toplam çıkarıldı. Aynı günün ilk saatlerindeki yeni kontrolde 21 Ekim TCMB USD döviz satış kuru 49,6015 TL olarak doğrulandı; iki ara toplamın planlama karşılığı 11.986,24 TL. Bu tutarlar tam proje maliyeti veya kullanıcı tarafından onaylanmış alım listesi değil. Şasi, bazı güç/bağlantı parçaları, telefon sabitleme ve ithalat giderleri açık; destek sınırına kalan 13,76 TL bu giderlerin karşılandığını göstermez. İki enkoderli motor ve beş sensör korunarak daha uygun fiyatlı belgeli yerel seçenekler değerlendirilecek. Beş sensör için belgeli Pololu taşıyıcı fiyatı referans alındı; daha ucuz CJMCU gözlemi ayrı tutuldu, 5 V/3,3 V ve stok farkları yok sayılmadı.

[Batarya ve şarj planı](BATARYA_VE_SARJ_PLANI.md), hazır 2S paket, uygun şarj ve gerekirse harici koruma üzerinden detaylandırıldı. Önceki taslak kaydının ardından 22 Ekim'deki yeni istekte Power-Xtra ana sayfası ve TCMB bülteni HTTP 200 ile açıldı. Üreticinin ürün bağlantısı verdiği Birikim Pilleri adresi ise ağ aracısında 403 döndürdü. Satıcı fotoğraflarında dört bağlantılı soket ve “1S 3.7V*2” etiketi görüldü; 2S1P satış tanımıyla birlikte pin/hücre bağlantısı açıklatılacak. Pilin şarj akımı hâlâ teyit bekliyor; A3 şarj eşleşmesi tamamlanmış sayılmayacak. Bilgi/bağlantı belgelenmezse başka hazır paket–şarj adayı seçilmesi önerildi; yeni model henüz belirlenmedi.

Başvuru sahibinin bildirdiği kurum, bölüm, sınıf, danışman ve tek yürütücülü görev dağılımı [genel bilgiler ve görevler taslağında](GENEL_BILGILER_VE_GOREVLER.md) tutuluyor. Üniversitedeki kayıt veya altyapı olanakları bağımsız olarak doğrulanmış değildir.

[Konunun önemi ve bilimsel niteliği taslağı](BILIMSEL_NITELIK_TASLAGI.md), DOI ve yayın bilgileri doğrulanan iki ilgili uygulama makalesiyle geliştirildi. Okunan içerik ve ilk karşılaştırma [literatür notunda](LITERATUR_KARSILASTIRMASI.md) kayıtlı. Bu ilk inceleme kapsamlı tarama veya literatürde boşluk kanıtı sayılmayacak.

[Yöntem bölümünün ilk metin taslağı](YONTEM_TASLAGI.md) hazırlandı. Enkoderli iki motorlu şasi kullanıcı tarafından seçildi. Bug 2 mantığıyla durum makinesi öneri durumunda; algoritma, ürün seçimi ve sayısal deney parametreleri henüz kesinleşmedi.

22 Ekim'de [sayısal deney protokolü](DENEY_PROTOKOLU_ONERISI.md) hazırlandı ve kullanıcının 40 deneme/koşul başına en az 8/10 ana hedef seçimiyle 0.3 sürümüne güncellendi. Aynı 3 m L rotası, kesin engel yerleşimleri, ek 9/10 algılama/engelsiz başarı hedefleri, 10 cm tolerans ve 120 saniye süre hâlen öneridir. Kullanıcı deney yerinin henüz belli olmadığını bildirdi. [Kayıt şablonu](DENEY_KAYIT_SABLONU.csv) yalnız başlıklardan oluşuyor; deney sonucu yok. Bağımsız görüntü ölçümü, perspektif/işaret yüksekliği, kontrol noktaları, zaman eşleme, başarısızlık paydası ve ayar/son değerlendirme ayrımı açıklandı.

Bilimsel nitelik ve yöntem taslaklarında atıf yapılan ilk altı kaynak [tek alfabetik kaynakçada](KAYNAKCA_TASLAGI.md) birleştirildi. Mevcut metin içi eşleşmeler ve iki makalenin DOI'leri korundu; içeriği okunmayan bibliyografik adaylar listeye alınmadı. Elektronik kaynakların gerçek erişim tarihleri değiştirilmedi. Nihai metin değişirse kaynakça yeniden kontrol edilecek.

[İlk birleşik araştırma önerisi](ARASTIRMA_ONERISI_BIRLESIK_TASLAK.md), kullanıcının rapor metnini birlikte görme isteği üzerine hazırlandı. Genel bilgiler, bilimsel nitelik, amaç/hedefler, yöntem, yönetim, yaygın etki, üç görsel ve kaynakça aynı metne alındı; diğer bölümler toplandıktan sonra 211 kelimelik ilk özet yazıldı. Word/PDF inceleme sürümleri oluşturuldu. Deney yerinin henüz belli olmadığı kaydedildi; ilk metin için bu bilgi beklenmedi. Başlık, resmî süre, nihai bütçe ve diğer açık bilgiler son bölümde toplandı. Bu, gönderilmiş başvuru veya gerçekleşmiş deney raporu değildir.

[Risk yönetimi](RISK_YONETIMI_TASLAGI.md) ve [yaygın etki](YAYGIN_ETKI_TASLAGI.md) için ilk taslaklar hazırlandı. Önlemler ve çıktı miktarları plan önerileridir; kullanıcı tarafından kesinleştirilmiş donanım, yeni ekipman erişimi veya gerçekleşmiş başarı olarak sunulmayacak. [Başvuru durumu ve kalan işler](BASVURU_DURUMU_VE_EKSIKLER.md) bölüm bazında izleniyor.

[Araştırma olanakları taslağı](ARASTIRMA_OLANAKLARI_TASLAGI.md) mevcut kişisel lehim ekipmanı ve telefonla hazırlandı. Kurum laboratuvarı, kesin deney yeri ve diğer ölçüm araçları mevcut sayılmadı; multimetre ve metre/cetvel erişimi soruldu.

Haziran hedefi için [çalışma takvimi taslağı](CALISMA_TAKVIMI_TASLAGI.md) hazırlandı: beş iş paketi, bağımlılıklar ve %20/%15/%20/%30/%15 katkı önerisi. Kasım–Mayıs teknik çalışma, Haziran inceleme/teslim planı akademik hedef önerisidir. Resmî TÜBİTAK başlangıcı ve toplam süre bu akademik takvimden varsayılmayacak.

[Başvuru görselleri](gorseller/README.md), kullanıcının daha açıklayıcı ve görsel olarak özenli tasarım isteğiyle yenilendi: simgeli sistem mimarisi, dış dönüş oku yerine “A” bağlantıları kullanan iki kollu kontrol akışı ve temsili kaçınma yolunu da gösteren deney şeması. İlk sürüm arşivlendi. Yeni şekiller ÜYZ destekli tasarım çizimleridir; fotoğraf, gerçek deney kaydı veya simülasyon sonucu değildir. Kullanıcıdan şu anda çekim yapması beklenmiyor. İleride deney ölçümünde kamera kullanımı ayrı bir seçenek olarak açık kalıyor.

- Ölçülü waypoint ekranının fiziksel alanla eşleştirilmesi ve başlangıç noktası/yönünün tanımlanması.
- Planlanan 3 × 3 metre alanın fiziksel yeri, kesin araç ölçüleri ve donanım seçildikten sonra parkurun yeterliliğinin değerlendirilmesi.
- Manuel kontrolün ayrıca gerekip gerekmediği.
- Konum/yön ölçümü, sensörler, motorlar, sürücü ve mevcut donanım.
- Bilgisayar öncelikli ve telefonda da çalışan arayüzün uygulama teknolojisi, haberleşme yöntemi ve engelden kaçınma algoritması.
- Araştırma sorusu, karşılaştırma yöntemi ve ölçülebilir başarı ölçütleri.
- Sabit engellerin boyutları, malzemeleri, geçiş açıklıkları ve yerleşimleri; algılama mesafesi, hız ve başarının sayısal eşikleri.
- Kullanılabilecek kurum olanakları, proje süresi ve bütçe. Yürütücü adı/soyadı, tek yürütücülü başvuru, üniversite/bölüm/sınıf ve danışman bilgisi kullanıcı tarafından belirtildi.

## Belgeler ve doğrulama durumu

- Kullanıcı tarafından kabul almış örnekler olarak sunulan iki PDF incelendi. İç kapaklarında 2025 yılı belirtiliyor. Bunlar araştırma önerisi formu niteliğinde; güncel resmî şablon veya sonuç raporu olarak kullanılmayacak.
- Örneklerde bilimsel nitelik, amaç/hedefler, yöntem, proje yönetimi, yaygın etki ve kaynaklar bulunuyor. Güncel şartlar resmî 2026 belgeleriyle ayrıca kontrol edildi; ayrıntılar [2026 başvuru kurallarında](2026_BASVURU_KURALLARI.md).
- Örnek metinler kopyalanmayacak; içlerindeki kaynaklar bağımsız doğrulama yapılmadan kullanılmayacak. Örnek PDF'ler ve bu örneklerdeki diğer başvuru sahiplerinin kişisel bilgileri bu depoya aktarılmadı. Mevcut başvuru sahibinin bu çalışma için bildirdiği bilgiler ayrı taslakta tutuluyor.
- Öğretim üyesinin paylaşılan uyarıları: güncel yönergeleri izlemek, eksik/uydurma kaynak kullanmamak, kaynak metinleri aynen aktarmamak ve yüklemeden önce öğretim üyesi kontrolünü sağlamak.
- Resmî sayfa: https://tubitak.gov.tr/tr/burslar/lisans-onlisans/destek-programlari/2209-universite-ogrencileri-arastirma-projeleri-destekleme-programi
- Önceki 403 erişim hatasının ardından 21 Ekim 2026 tarihinde yeniden denendi: program sayfası, 2026 çağrı duyurusu, 2026 başvuru içeriği bilgi notu ve ÜYZ rehberi HTTP 200 ile indirildi. Kullanıcının yüklediği bilgi notunun SHA-256 değeri resmî dosyayla aynı: `d5bf5477971b5924fe079970bab156057378afa1c2bff07df0a0d78614aba0e6`.

## Teknik değerlendirme ve görüşülecek öneriler

- İlk sürümde seçilen ölçülü ızgara üzerinde yerel (x, y) waypoint'ler kullanılacak. Waypoint kullanmak GPS kullanmayı zorunlu kılmaz; serbest çizimi noktalara dönüştürme ayrıca değerlendirilebilecek bir özelliktir.
- Sonraki aşama için isteğe bağlı ölçekli kroki görünümü değerlendirilebilir. Planın fiziksel ölçüsü, başlangıç noktası ve yönüyle eşleştirilmesi gerekir; görüntü yüklemek tek başına konumlandırma sağlamaz.
- Gerçek coğrafi haritayı görüntülemek ile araç konumunu harita koordinatlarıyla eşleştirmek ayrı işlerdir. Küçük araçla kısa mesafeli kapalı alan deneylerinde standart GPS uygun bir hassas konumlandırma çözümü olarak varsayılmayacak. Harita veya kroki seçimi, fiziksel konum takibi ihtiyacını ortadan kaldırmaz.
- Planlanan yaklaşık 3 × 3 metre deney alanında başlangıç noktası ve yönü bilinen kısa parkurlar öneriliyor. Parkurun boyutu ve engel açıklıkları, şasi ölçüleri ve hareket kabiliyeti seçilince kontrol edilecek; mevcut planın yeterli olduğu henüz deneyle doğrulanmadı.
- Motor enkoderleri ve IMU ile göreli konum/yön kestirimi değerlendirilebilir. Kayma ve ölçüm hataları zamanla birikir; bu yaklaşım tek başına kesin veya sınırsız konum doğruluğu sağlamaz. Parkur boyutu ve hata hedeflerine göre ek konum düzeltmesi gerekebilir.
- Mesafe sensörleriyle yerel engelden kaçınma ve ardından rotaya katılma değerlendirilecek. Beş sabit sensör ve genel yönleri seçildi; sensör tipi/modeli, kesin açılar, görüş alanı ve algoritma henüz kesinleşmedi. Her engelin aşılabileceği iddia edilmeyecek.
- Basit süreye bağlı hareket komutları ilk hareket deneyi için kullanılabilir; engel etrafından dolaştıktan sonra rotaya doğru dönüşü güvenilir biçimde göstermek için konum/yön geri bildirimi gerekir.
- Rota sapması, hedefe ulaşma oranı, engelden sonra rotaya dönüş ve tamamlanma süresi olası ölçütlerdir. Karşılaştırma yöntemi, tekrar sayıları ve hedef değerler henüz belirlenmedi. Gerçek rota hatası, yalnızca aracın kendi kestiriminden hesaplanmayacak; bağımsız referans ölçüm yöntemi seçilecek.
- Seçilen ilk deney kapsamı: sabit engellerle engel algılama, çarpışmasız kaçınma ve rotaya dönüş başarısını incelemek. Engel yerleşimleri denemeler arasında değiştirilerek performans değerlendirilecek. Algoritma, tekrar sayıları ve araştırma sorusunun son biçimi literatür ve uygulanabilirlik incelemesiyle belirlenecek; özgünlük iddiası henüz yok.

## Başvuru dili ve ön çalışma

- 2026 Başvuru İçeriği Bilgi Notu, Yöntem bölümünde “Araştırma önerisinde herhangi bir ön çalışma veya fizibilite yapıldıysa bunların sunulması beklenir.” diyor. Bu ifade, önceden tamamlanmış prototipi başvuru şartı olarak tanımlamıyor.
- Yapılacak çalışma gelecek zamanla; gerçekten yapılmış hazırlık/deney varsa yalnızca kanıtlanabilir kısmı geçmiş zamanla anlatılacak. Denenmemiş bir tasarım için başarı oranı veya elde edilmiş sonuç yazılmayacak.
- Ön deney yapılmış olması uygulanabilirliğe dayanak sağlayabilir; ön deney yoksa seçilen yaklaşımın gerekçesi, doğrulanmış kaynaklar, donanım gereksinimleri, bütçe, takvim ve risk planı başvurudan önce somutlaştırılacak.

## 22 Ekim — yöntem ve kaynakça devam güncellemesi

Alajlan, Elleithy, Almasri ve Sobh'un (2017) engelden kaçınmaya ilişkin deneysel çalışmasının ilgili yayıncı bölümleri okundu; DOI ve künyesi Crossref ile kontrol edildi. Bilimsel nitelik karşılaştırmasına eklendi ve birleşik kaynakça yedi kaynağa çıktı. Çalışmanın enerji/yol sonuçları veya sensör altyapısı projeye aktarılmış başarı olarak sunulmadı.

Yöntem ve birleşik metinde waypoint sırasının korunması, aynı etkin hedefe kaçınma sonrası ilerleme, sonlu rota parçasına dönüş ve belirsizlikten büyük ilerleme koşulu açıklandı. Bağımsız ölçülen rota hatası ve RMSE tanımı eklendi. Bug 2 mantığı ana yöntem önerisi olarak kullanıcıya soruldu; henüz yanıt alınmadı. Önceden seçilen 40 deneme ve koşul başına en az 8/10 ana hedef değişmedi; diğer sayısal değerler öneri olarak kaldı.

Yerel motor ve sensör devam kontrolü kaynak URL/özetleriyle ayrı tedarik kaydına işlendi. GY-53 kılavuzunun UART/I²C mod seçimi okundu; kartın I²C gerilimi, motor akımları ve kesin KDV/teslim bilgileri tamamlanmış sayılmadı. Referans bütçe ara toplamları bu adaylarla değiştirilmedi; satıcıya ileti gönderilmedi.

## 22 Ekim — kaçınma yaklaşımı seçimi ve metin düzenleme

Kullanıcı, önceki mesajda önerilen Bug 2 mantığından yararlanan engel kenarı takibi ve rotaya dönüş yaklaşımını “tamam uygunudur” diyerek uygun buldu. Bu seçim ana yaklaşımı belirler; sensör modelleri, sayısal eşikler ve uygulamanın deneysel başarısı onaylanmış veya doğrulanmış sayılmaz. Önceki “henüz yanıt alınmadı” kaydı bu yanıtla güncellenmiştir.

Kullanıcı, taslak cümlelerinin başvuru metninde nasıl düzenleneceğini sordu. Taslak son metnin temelidir; anlatım, tutarlılık, bölüm uyumu ve kaynak bağlantıları düzenlenecek. Yeni teknik kararlar veya hedefler kullanıcıya sorulacak; yapılmamış deneyler sonuç olarak yazılmayacaktır.

## 22 Ekim — birleşik metnin dil ve anlatım düzenlemesi

Birleşik araştırma önerisinde tekrarlar azaltıldı; özet, bilimsel gerekçe, kaçınma ve bağımsız ölçüm anlatımı düzenlendi. Kullanıcının seçtiği Bug 2 uyarlaması özet ve yönteme işlendi. Başvuruya aktarılmayacak çalışma açıklamaları, seçilmemiş sayısal öneriler ve ÜYZ hazırlık kaydı ayrı hazırlık notuna taşındı. Donanım mimarisi, dört koşulda toplam 40 deneme ve her engelli koşulda en az 8/10 birleşik görev hedefi korundu. Yeni teknik karar, kaynak veya deney sonucu eklenmedi. Eksik süre, bütçe, deney yeri ve toleranslar tamamlanmış sayılmadı.

## 22 Ekim — sensör maliyeti ve yerel seçenekler

Beş sabit sensör için ToF ve ultrasonik alternatifler kaynaklı karşılaştırma dosyasında toplandı. GY-VL53L0XV2 için 435,88 TL/adet görülüyor ancak yapılandırılmış stok verisi OutOfStock; satın alınabilir set olarak sunulmadı. HC-SR04 için iki yerel satıcı fiyatı ve üç sayfalık veri sayfası incelendi; seviye uyarlama, sıralı ölçüm, yüzey ve montaj gereksinimleri kaydedildi. Robotistan siyah sensörünün önceki özetinde yer almayan ikinci güncel KDV dahil fiyat alanı da not edildi; sayfadaki çelişkili +KDV etiketi nedeniyle bağlayıcı teslim fiyatı çıkarılmadı. Kullanıcı “ToF sensörlerini önceliklendirelim.” yanıtıyla ToF önceliğini seçti. Kesin sensör taşıyıcısı/modeli, motor bilgileri ve nihai bütçe tamamlanmış sayılmadı; CSV ve ana rapor değiştirilmedi.

## 22 Ekim — stok şartının açıklanması ve yönteme ToF önceliğinin işlenmesi

Kullanıcı stokta olmanın rapor için zorunlu olup olmadığını sordu. Güncel çağrı ve bilgi notu yeniden okunarak başvuru anında bütün parçaların stokta olmasına ilişkin bir şart bulunmadığı açıklandı. Stok araştırmasının temin ve bütçe planı için yapıldığı, rapor yazımını durdurmayacağı belirtildi. Kullanıcının “tamam” yanıtı sonrasında bu ayrım hazırlık ve kural notlarına kaydedildi.

Önceden seçilen ToF önceliği birleşik yöntem ve ilgili taslaklara işlendi. Belirli bir sensör modeli, yeni sayısal hedef veya deney sonucu eklenmedi. Beş sensör, iki enkoderli motor, 40 değerlendirme denemesi ve her engelli koşulda en az 8/10 birleşik başarı hedefi korundu. Başlık tercihi ayrıca kullanıcıya soruldu; yanıt gelene kadar öneri başlığı korunacak.

## 22 Ekim — kullanıcının ilk proje başlığını koruma kararı

Kullanıcı, önerilen yeni başlık yerine ilk başlığının aynen kalmasını seçti: “Kullanıcı tarafından belirlenen rota bilgisine göre hareket eden otonom araç tasarımı”. Seçim birleşik rapora, genel bilgilere, amaç/kapsam ve durum notlarına işlendi; başlığın öneri veya yanıt bekleyen alan olduğu yönündeki güncel işaretler kaldırıldı. Önceki başlık sorusu bu yanıtla sonuçlandı. Danışman incelemesi ve TYBS başvurusu tamamlanmış sayılmadı; teknik kapsam ve deney hedefleri değiştirilmedi.

## 22 Ekim — altı aylık resmî takvim önerisi

Beş iş paketi 1–6. ay aralıklarına yerleştirilerek somut süre önerisi hazırlandı: donanım ve arayüz 1–2. ay, engelsiz rota takibi 3. ay, kaçınma/rotaya dönüş 4–5. ay, nihai deney/analiz 6. ay. Mevcut %20/%15/%20/%30/%15 katkılar, 40 deneme ve koşul başına en az 8/10 ana hedef korundu. Haziran 2027 akademik teslim hedefi ile sonuç ilanından başlayan resmî sürenin ilişkisi açıklandı; Ocak başlangıcı, kesin Haziran resmî bitişi veya kullanıcı süre seçimi varsayılmadı. Birleşik rapor ve bütçe değiştirilmedi.

## 22 Ekim — altı aylık planın kullanıcı tarafından seçilmesi

Kullanıcı açık süre sorusuna “6 aylık planı kullanalım.” yanıtını verdi. Planlanan toplam süre 6 ay olarak birleşik rapora ve genel bilgilere işlendi. İP1/İP2 1–2. ay, İP3 3. ay, İP4 4–5. ay ve İP5 6. ay dağılımı kullanıldı; %20/%15/%20/%30/%15 katkılar korundu. Özet ve yöntem içindeki takvim açıklamaları bu seçime göre güncellendi.

Önceki “süre seçilmedi” kayıtları tarihsel hazırlık aşamasını gösterir; bu yanıtla süre tercihi tamamlandı. Haziran 2027 akademik teslim hedefi korunur. Sonuç ilan tarihi bilinmediği için Ocak başlangıcı veya Haziran resmî bitişi varsayılmadı. Danışman incelemesi, bütçe, deney yeri ve kalan teknik eşikler tamamlanmış sayılmadı. Donanım kapsamı, 40 deneme ve koşul başına en az 8/10 ana başarı hedefi değiştirilmedi.

## 22 Ekim — deney ölçütleri sorusu ve TYBS hazırlık kontrolü

Waypoint erişimi için 10 cm, rotaya dönüş bandı için 10 cm ve her deneme için 120 saniye sınırı planlanan hedefler olarak kullanıcıya soruldu. Yanıt gelene kadar bu değerler seçilmiş sayılmadı; ek 9/10 hedefleri, 0,10 m/s hız, 1/2 saniyelik süreler ve 2 cm ölçüm kontrol hedefi ayrıca öneri olarak kaldı. Protokol 0.4 sürümünde önceden seçilen Bug 2, ToF önceliği ve altı aylık planla uyumlandırıldı. Birleşik raporun özet kelime sayısı, üç bölümün karakter sayıları ve deney CSV dosyasının sonuç içermemesi kontrol edilerek durum notuna kaydedildi.

## 22 Ekim — mesafe ve deneme süresi hedeflerinin seçilmesi

Kullanıcı açık ölçüt sorusuna “Bu planlanan hedefleri kullanalım.” yanıtını verdi. Waypoint/hedef erişimi için en çok 10 cm, kaçınma sonrası etkin sonlu rota parçasına dönüş için en çok 10 cm ve her deneme için hareket başlangıcından itibaren en çok 120 saniye planlanan değerlendirme hedefleri olarak rapora işlendi. Protokol 0.5 sürümüne güncellendi.

Bu seçim, 10 cm'nin tüm hareket boyunca azami izleme hatası olduğu veya ölçülmüş doğruluk sağlandığı anlamına gelmez. Son hedefte 2 saniye durma, bantta 1 saniye kalma, hedef yönünde 10 cm ek ilerleme, 0,10 m/s hız, 2 cm bağımsız ölçüm kontrol hedefi ve ek 9/10 başarı hedefleri seçilmiş sayılmadı. Başarısız denemelerin paydada tutulması, 40 değerlendirme denemesi ve koşul başına en az 8/10 ana hedef korundu. Ölçüm/donanım uygulanabilirliği, danışman incelemesi ve bütçe tamamlanmış sayılmadı.
