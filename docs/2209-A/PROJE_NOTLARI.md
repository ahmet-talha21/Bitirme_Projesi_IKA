# İKA — 2209-A hazırlık notları

Güncelleme: 21 Ekim 2026. Bu belge başvuru metni değil, kullanıcı tarafından doğrulanan bilgiler ve açık soruların kaydıdır.

## Kullanıcının belirttiği bilgiler

- Geçici başlık: Kullanıcı tarafından belirlenen rota bilgisine göre hareket eden otonom araç tasarımı.
- Araç ESP32 ile geliştirilecek.
- Kullanıcı arayüzü proje sahibi tarafından tasarlanacak; araç bu arayüz üzerinden kontrol edilecek.
- Kullanıcı rotayı arayüzden tanımlayacak; araç rotayı otonom takip edecek.
- Engel algılandığında engelden kaçınma davranışı devreye girecek; araç daha sonra rotasına dönerek ilerleyecek. Algoritma henüz seçilmedi.
- Kullanıcı temel amacın engeli algılamak ve başarılı bir kaçınma hareketi gerçekleştirmek olduğunu netleştirdi. Rota takibi ve rotaya dönüş, bu davranışın görev içindeki değerlendirme çerçevesidir; eşya taşıma gibi ek görev belirlenmedi.
- İlk sürüm için ölçülü kareli alan üzerinde waypoint (ara rota noktaları) seçimi kullanıcı tarafından uygun bulundu. Sonraki aşamada isteğe bağlı ölçekli mekân krokisi ekleme yaklaşımı da uygun bulundu; bu ek özellik ilk sürüm için zorunlu teslim olarak belirlenmedi.
- Kullanıcı ev, okul ve iş yeri gibi farklı yerlerde kullanılabilirlik istiyor. Küçük Arduino/RC araçları boyutunda bir prototip ve düz zeminde kullanım belirtildi. İlk deneyler için yaklaşık 3 × 3 metre alan planlanıyor; bu, ölçülmüş veya üzerinde test yapılmış bir alan değil. Kesin araç ölçüleri ve kullanılacak fiziksel yer henüz belirlenmedi.
- Arayüzde öncelik bilgisayar kullanımı; telefonda da çalışması isteniyor. Her iki cihazda açılabilen tarayıcı arayüzü teknik seçenek olarak değerlendiriliyor; yazılım teknolojisi ve haberleşme yöntemi seçilmedi.
- Gerçek coğrafi harita ilk sürüm kapsamına alınmadı; yerel rota ekranı seçildi.
- ESP32 dışındaki malzemeler birlikte seçilecek; donanım listesi henüz kesinleşmedi.
- Kullanıcının elinde henüz ESP32 yok; satın almayı planlıyor. Diğer araç bileşenlerinin mevcut olduğu bildirilmedi. Yaklaşık bütçe henüz bilinmiyor.
- Kullanıcının lehim ekipmanı var ve araç montajında sorun yaşayacağını düşünmüyor. Bu bilgi kişisel olanaktır; üniversite laboratuvarı, 3D yazıcı veya başka kurum altyapısının mevcut olduğu henüz doğrulanmadı.
- TÜBİTAK 2209-A başvurusu hazırlanacak.
- Başvuru tek öğrenciyle yapılacak; proje ortağı bulunmayacak.
- Başvuru sahibi, adını Ahmet Talha Arslan olarak bildirdi; Konya Teknik Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü 4. sınıf öğrencisi olduğunu belirtti.
- Akademik danışman, kullanıcının bildirdiği üzere Prof. Dr. Murat Ceylan.
- Teknik ayrıntılar kullanıcıya sorularak netleştirilecek; bilinmeyen özellikler ve sonuçlar yazılmayacak.
- Kullanıcı projeye henüz başlamadığını belirtti. Şu an başvuru hazırlığı ve tasarım planlama aşamasındayız; çalışan araç, kurulmuş deney düzeneği veya tamamlanmış ön deney bulunmuş gibi yazılmayacak.
- Kullanıcı deney kapsamının uygulanabilir ve güçlü bir başvuru sağlayacak şekilde seçilmesini istedi. Bu kapsamda ilk deneyler için sabit engeller seçildi: engeller denemeler sırasında hareketsiz olacak, yerleşimleri denemeler arasında değiştirilebilecek. Hareketli engeller ana başvuru kapsamına eklenmedi. Bu bir çalışma planıdır; deney sonucu değildir.

## Netleştirilecek konular

İlk donanım mimarisi, arayüz/haberleşme seçenekleri, kaçınma yaklaşımı ve deney önerileri [yöntem ve deney planında](YONTEM_VE_DENEY_PLANI.md) hazırlandı. Bu teknik öneriler parça satın alma kararı veya kullanıcı tarafından onaylanmış nihai yöntem değildir.

Mevcut ekipman durumu ve teklif alınacak kalemler [malzeme ve bütçe ön listesinde](MALZEME_VE_BUTCE_ON_LISTESI.md) tutuluyor. Fiyatlar doğrulanmadan başvuru bütçesi oluşturulmayacak.

Başvuru sahibinin bildirdiği kurum, bölüm, sınıf, danışman ve tek yürütücülü görev dağılımı [genel bilgiler ve görevler taslağında](GENEL_BILGILER_VE_GOREVLER.md) tutuluyor. Üniversitedeki kayıt veya altyapı olanakları bağımsız olarak doğrulanmış değildir.

[Konunun önemi ve bilimsel niteliği taslağı](BILIMSEL_NITELIK_TASLAGI.md), DOI ve yayın bilgileri doğrulanan iki ilgili uygulama makalesiyle geliştirildi. Okunan içerik ve ilk karşılaştırma [literatür notunda](LITERATUR_KARSILASTIRMASI.md) kayıtlı. Bu ilk inceleme kapsamlı tarama veya literatürde boşluk kanıtı sayılmayacak.

[Yöntem bölümünün ilk metin taslağı](YONTEM_TASLAGI.md) hazırlandı. Enkoderli iki motorlu şasi ve Bug 2 mantığıyla durum makinesi öneri durumunda; kullanıcı tercihi, ürün seçimi ve sayısal deney parametreleri henüz kesinleşmedi.

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
- Mesafe sensörleriyle yerel engelden kaçınma ve ardından rotaya katılma değerlendirilecek. Sensör tipi, sayısı, görüş alanı ve algoritma seçilmedi; her engelin aşılabileceği iddia edilmeyecek.
- Basit süreye bağlı hareket komutları ilk hareket deneyi için kullanılabilir; engel etrafından dolaştıktan sonra rotaya doğru dönüşü güvenilir biçimde göstermek için konum/yön geri bildirimi gerekir.
- Rota sapması, hedefe ulaşma oranı, engelden sonra rotaya dönüş ve tamamlanma süresi olası ölçütlerdir. Karşılaştırma yöntemi, tekrar sayıları ve hedef değerler henüz belirlenmedi. Gerçek rota hatası, yalnızca aracın kendi kestiriminden hesaplanmayacak; bağımsız referans ölçüm yöntemi seçilecek.
- Seçilen ilk deney kapsamı: sabit engellerle engel algılama, çarpışmasız kaçınma ve rotaya dönüş başarısını incelemek. Engel yerleşimleri denemeler arasında değiştirilerek performans değerlendirilecek. Algoritma, tekrar sayıları ve araştırma sorusunun son biçimi literatür ve uygulanabilirlik incelemesiyle belirlenecek; özgünlük iddiası henüz yok.

## Başvuru dili ve ön çalışma

- 2026 Başvuru İçeriği Bilgi Notu, Yöntem bölümünde “Araştırma önerisinde herhangi bir ön çalışma veya fizibilite yapıldıysa bunların sunulması beklenir.” diyor. Bu ifade, önceden tamamlanmış prototipi başvuru şartı olarak tanımlamıyor.
- Yapılacak çalışma gelecek zamanla; gerçekten yapılmış hazırlık/deney varsa yalnızca kanıtlanabilir kısmı geçmiş zamanla anlatılacak. Denenmemiş bir tasarım için başarı oranı veya elde edilmiş sonuç yazılmayacak.
- Ön deney yapılmış olması uygulanabilirliğe dayanak sağlayabilir; ön deney yoksa seçilen yaklaşımın gerekçesi, doğrulanmış kaynaklar, donanım gereksinimleri, bütçe, takvim ve risk planı başvurudan önce somutlaştırılacak.
