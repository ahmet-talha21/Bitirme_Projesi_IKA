# TÜBİTAK 2209-A — ayrıntılı uygunluk incelemesi

**Kontrol tarihi:** 23 Ekim 2026 (Türkiye). **İncelenen dosya:** kullanıcının yüklediği `Ahmet_Talha_Arslan_2209A.pdf`; depodaki `ARASTIRMA_ONERISI.pdf` ile SHA-256 düzeyinde aynıdır. **İncelenen rapor sürümü:** `fe9357a228b2ecd43da0c7dd72fa7d449c9c1132`, 14 sayfa. Bu kayıt bir değerlendirmedir; aşağıdaki öneriler rapora uygulanmış gibi sunulmamaktadır. Ana PDF/Word değiştirilmemiştir.

**Sonuç:** Ana bölüm yapısı, metin uzunlukları, Türkçe dil, atıf düzeni, bütçe ve proje süresi temel şartlarla örtüşmektedir. Bununla birlikte takvimdeki paralel iş paketlerinin süre hesabı resmî bilgi notunun ifadesiyle netleştirilmeli; kaynakçadaki bir kitap künyesi tamamlanmalıdır. Yöntemde temas sonrası durdurma açıklığı, derslik/kamera erişimi ve başvuru sistemindeki zorunlu işlemler de tamamlanmadan “başvuruya bütünüyle hazır” sonucu verilmez. Bilimsel kabul veya belirli bir değerlendirme puanı öngörülmez.

## 1. Yeniden erişilen resmî kaynaklar

| Kaynak | İncelenen hüküm / içerik |
| --- | --- |
| [Program sayfası](https://tubitak.gov.tr/tr/burslar/lisans-onlisans/destek-programlari/2209-universite-ogrencileri-arastirma-projeleri-destekleme-programi) | 2026 başvuru düzeni, süre, 12.000 TL üst sınır, başvuru/onay tarihleri |
| [2026 çağrı duyurusu](https://tubitak.gov.tr/sites/default/files/2026-10/2209-A_2026_Yili_Cagri_Duyurusu.pdf) | 2.1–2.2 destek kapsamı; 4.1.8 marka; 4.2–4.3 başvuru; 5.2 değerlendirme; 6.1 süre; 8.4–8.5 ÜYZ |
| [2026 başvuru içeriği bilgi notu](https://tubitak.gov.tr/sites/default/files/2026-10/2209-A_Basvuru_Icerigi_Bilgi_Notu.pdf) | Özet, 1.1–6, kaynakça, editör/görsel/önizleme talimatları |
| [Bibliyografik verilerin düzenlenmesi](https://tubitak.gov.tr/tr/duyuru/bibliyografik-verilerin-duzenlenmesi) | Metin içi yazar–yıl atıfları, alfabetik kaynakça, kitap künyesinde basım yeri, DOI |
| [ÜYZ kullanım rehberi](https://tubitak.gov.tr/sites/default/files/2026-01/UYZ_Rehberi_v04_TR.pdf) | Özellikle 1.2.1–1.2.2: önemli ölçüde kullanım ve özel sistem alanında beyan |
| [Program sayfasının bağladığı öncelikli alanlar listesi](https://tubitak.gov.tr/sites/default/files/2025-07/Oncelikli_Alanlar_2025-2.pdf) | “Robotik-mekatronik”; bu dosyaya güncel program sayfası bağlantı vermektedir |

Bütün bağlantılara bu incelemede HTTP 200 ile erişildi. Çağrı, bilgi notu ve ÜYZ rehberi önceki kontrol kopyalarıyla aynı SHA-256 değerindedir. Kaynaklar değişmemiş olsa da yeniden okunarak raporla karşılaştırıldı. Erişim ve sayısal kontrol özeti [kanıt dosyasındadır](tedarik/uygunluk_inceleme_2026-10-23.json).

## 2. Bölüm ve şart karşılaştırması

| Şart | Raporda bulunan içerik | Değerlendirme |
| --- | --- | --- |
| Türkçe, açık bilimsel başlık | Kapak ve genel bilgilerde rota, sabit engel, yeniden katılma ve deneysel değerlendirme | Uygun; başlıkta ticari ad yok |
| Özet 25–450 kelime | 249 kelime; soru, yöntem, yönetim, beklenen etki | Uygun |
| 1.1 en az 350 karakter | Yaklaşık 5.018 karakter; kapsam, literatür, araştırma boşluğu, soru, H1 | Asgari içerik mevcut; stratejik alan ilişkisi aşağıda ayrıca ele alındı |
| 1.2 en az 350 karakter | Yaklaşık 1.723 karakter; altı ölçülebilir hedef | Uygun; 8/10, 10 cm ve 120 s ölçülmüş sonuç değil hedef |
| Yöntem en az 350 karakter | Yaklaşık 24.957 karakter; donanım, kontrol, değişkenler, deney, analiz, ön çalışma | Asgari içerik mevcut; teknik açıklıklar aşağıda |
| Yöntem–takvim ilişkisi | İP1–5 eşleştirmesi | Mevcut |
| Ön çalışma, varsa sunulması | Altı sentetik durum makinesi senaryosu, tablo ve Şekil 4 | Gerçek kod çalışmasına dayanıyor; fiziksel doğrulama olarak sunulmuyor |
| Azami 12 aylık proje | Altı aylık takvim | Proje zaman aralığı uygun; paralel iş paketlerinin toplam süre ifadesi ayrıca netleştirilmeli |
| Çalışma takvimi, ölçütler, toplam %100 | Beş iş paketi; %20+%15+%20+%30+%15 | Katkı toplamı doğru; sonuç raporlaması ayrı iş adımı yapılmamış |
| Risk ve hedefi koruyan B planları | Altı risk, önlem ve ilişkili iş paketleri | Mevcut; eşiklerin sonuca göre gevşetilmemesi olumlu |
| Araştırma olanakları | Mevcut telefon/lehim ekipmanı; planlanan derslik; bütçeden alınacak parçalar ayrılmış | Bilgi dürüstçe ayrılmış; derslik ve montaj erişimi henüz doğrulanmış değil |
| Ölçülebilir yaygın etki | Bir prototip, arayüz, 40 kayıt, bir ulusal bildiri başvurusu, açık kaynak depo | Mevcut; yayın kabulü garanti edilmemiş |
| Atıf ve kaynakça birlikte | Yedi kaynağın tümü metinde; alfabetik liste | Yapı doğru; kitap künyesinde küçük eksik var |
| Varsa DOI | Altı DOI; üretici veri sayfasına DOI uydurulmamış | Altı DOI yönlendirme ve Crossref kimliğiyle yeniden doğrulandı |
| Bütçe | 22 kalem, 11.500 TL; KDV dahil planlama tahminleri | 12.000 TL sınırının altında; aritmetik doğru |
| Kapsam dışı harcamalar | Kongre katılımı/yayın/patent/konaklama/gündelik bütçelenmemiş | Uygun; bildiri hedefi bu giderleri destek kapsamına sokmaz |
| Görseller ve metin katmanı | Dört şekil; plan ve sentetik çıktı ayrımı; Türkçe başlıklar doğru | PDF içinde taşma görülmedi; TYBS'de yeniden önizleme gerekir |
| Başvuru yöntemi | İnceleme için PDF/Word hazırlanmış | 2026'da bağımsız öneri PDF'si yükleme adımı yok; asıl başvuru TYBS alanlarından oluşturulur |
| ÜYZ beyanı | Bölüm 5'te genel açıklama; ayrı gerçek kullanım kaydı | Raporda açıklama var; sistemdeki özel beyan alanının doldurulduğu doğrulanmış değil |

Karakter sayıları Pandoc düzyazı çıktısına göre yaklaşık değerlerdir; editörün sayımı farklılaşsa da asgari 350 sınırına yakın değildir.

## 3. Başvuru öncesi düzeltilmesi veya netleştirilmesi gerekenler

### 3.1. Takvimde paralel süre hesabı — s. 11, bölüm 3.1

Bilgi notunun doğrudan ifadesi: **“İş paketlerinin toplam süresi proje süresinden uzun olamaz.”** Mevcut tabloda 1–2, 1–2, 3, 4–5 ve 5–6. ay aralıkları vardır. Çakışan faaliyetleri ayrı ayrı topladığımızda 2+2+1+2+2=9 paket-ayı oluşur; takvimin başlangıcından bitişine kadar geçen süre ise altı aydır. Metin, paralel çalışmayı zaten açıklamaktadır.

Bu iki süre tanımını aynı kabul ederek koşulun kesin karşılandığını söylemek doğru olmaz. TYBS'nin paralel iş paketlerini nasıl hesapladığına erişilmeden “sistem reddeder” de denemez. Son düzenlemede bu belirsizlik giderilmelidir. Örneğin ilk iki ayın donanım/arayüz çalışmaları tek bütünleştirme paketinde toplanıp üçüncü ay rota takibi, dördüncü–beşinci ay kaçınma, altıncı ay değerlendirme olarak dört paket kurulabilir; katkılar %35/%20/%30/%15 olabilir. Bu yalnız bir düzenleme önerisidir; rapora uygulanmamıştır. Teknik hazırlık ve raporlama ilgili paketlere entegre kalmalıdır.

### 3.2. Çarpışma sonrası durdurma ve durum geçişlerinin ölçülmesi — s. 6, bölüm 2.5

Metin “Çarpışma ... durumunda görev durdurulacaktır” diyor. Ancak bileşenler arasında temas sensörü yok; telefon kamerası da çevrim içi denetleyiciye bağlı değil. Dolayısıyla gerçek temasın hangi sinyalle anlaşılacağı ve durdurmayı kimin/nasıl tetikleyeceği yeterince açık değildir. ToF sensörünün her fiziksel teması algılayacağı varsayılmamalıdır.

Kapsam ve bütçe korunarak, gözlemcinin temas halinde arayüz/ana güç anahtarıyla denemeyi durduracağı ve bunu müdahale içeren başarısız deneme olarak kaydedeceği açıkça yazılabilir. Otomatik temas algılama iddia edilecekse bunun ayrıca donanım/yöntem karşılığı gerekir. Sınır dışına çıkma için de araç içi odometri kontrolü ile bağımsız videoda saptanan ihlal ayrılmalıdır.

Ayrıca “engel geride” ve “gövde için açıklık” koşulları kontrol mantığında kullanılıyor; bu mantıksal koşulların beş sensörün hangi ölçümleri ve konum tahminiyle oluşturulacağı daha açık ifade edilebilir. Bunları sentetik benzetimde doğru vermek, fiziksel araçta güvenilir biçimde üretildiklerini kanıtlamaz. Bu bir genel başvuru biçimi kuralı değil, yöntem tekrarlanabilirliği önerisidir.

### 3.3. Mevcut araştırma olanağı ile planlanan erişim — s. 8 ve 12, bölümler 2.7/3.3

Üniversitede bir derslik seçilmiş fakat kullanım zamanı/erişim henüz doğrulanmamıştır. Yaklaşık üç metre yükseklikte telefon montajı ve bütün 3 × 3 metrelik alanın görüntülenmesi de plan niteliğindedir. Telefonun görüş açısı ve kullanılabilecek montaj yeri bilinmeden nominal yüksekliğin yeterli olduğu söylenemez.

Resmî 3.3 bölümü “var olan ve projede kullanılacak” altyapıyı istemektedir. Mevcut telefon ve lehim ekipmanı ile satın alınacak donanımın ayrı gösterilmiş olması doğrudur. Planlanan derslik ve sabitleme erişimi de danışman/bölümle doğrulanmalı; henüz alınmamış izin alınmış gibi yazılmamalıdır. Bilgi notunda oda numarasını yazma veya başvuru öncesinde kamera kalibrasyonu yapma zorunluluğu bulunmamıştır. Bu inceleme böyle ek şartlar üretmez.

### 3.4. Kaynakçada kitap basım yeri — s. 14

Bibliyografik düzenleme açıklamasındaki kitap düzeni **“Basım Yeri: Yayınevi”** içerir. Corke (2017) künyesinde yayınevi var, basım yeri yok. Crossref kitabın basım yerini **Cham** olarak veriyor. İlgili kısım “Cham: Springer International Publishing” biçiminde tamamlanmalıdır. DOI, yıl ve ISBN kayıtları eşleşmektedir.

Metin içi atıfları kaldırmak gerekmez. Bilgi notu, kaynakçadaki kaynakların tümüne başvuru metninde atıf yapılmasını açıkça istemektedir. Bu nedenle yalnız sonda kaynakça vermek mevcut düzenlemenin yerine geçmez.

### 3.5. Öncelikli alanla ilişkinin açıklanması — s. 2–3, bölüm 1.1

Güncel program sayfasının bağladığı listede **“Robotik-mekatronik”** yer almaktadır. Projenin algılama, gömülü hareket kontrolü ve otonom kara aracı değerlendirmesiyle bu alan arasındaki ilişki somuttur; 1.1'de kısa bir gerekçeyle belirtilmesi uygundur. Liste dosyasının adında 2025-2 bulunması, güncel sayfanın ona bağlantı verdiği gerçeğinden ayrı kaydedilmiştir.

Bilgi notu, konu 12. Kalkınma Planı/2030 Sanayi ve Teknoloji Stratejisi ile ilişkiliyse sebebin ve yararın açıklanmasını ister. Mevcut rapor bu belgelere özel madde atfı yapmamaktadır. Belirli bir politika maddesine uyum iddia edilecekse ilgili asıl bölüm ayrıca doğrulanıp atıf eklenmelidir. Yalnız “robot” sözcüğü üzerinden özel taban puanından yararlanılacağı veya kabul sağlanacağı sonucu çıkarılamaz. Yeni bir algoritma geliştirmek ya da yapay zekâ kullanmak da bu projeye sonradan zorunluluk olarak eklenmez.

### 3.6. Ticari adların görünürlüğü — s. 2–6 ve 12–14

Çağrı 4.1.8 **“öne çıkarılmamalıdır”** diyor; metindeki her kurum veya teknik bileşen adının mutlak biçimde yasaklandığını söylemiyor. Başlıkta marka yok; genel işlevsel gereksinimler verilmiş. Bununla birlikte ESP32 birçok yerde, GitHub çıktı metninde geçiyor. Özette/amaçta genellikle “kablosuz haberleşmeli mikrodenetleyici”, yaygın etkide “açık kaynak kod deposu” denilmesi, teknik referansın gerektiği yerde sınırlı tutulması daha ölçülü olur.

Bunu kesin bir ön inceleme eleme nedeni olarak göstermiyoruz. Bilimsel künyelerde yazar/kurum/yayınevi bilgilerini silmek, üniversite bilgisini kaldırmak veya ÜYZ özel beyanında gerçek araç adlarını saklamak önerilmez.

## 4. Uygun bulunan bilimsel ve teknik noktalar

- Araç henüz yapılmadığı için gelecek zaman kullanılması doğrudur. Çağrı/bilgi notu önceden bitmiş prototip istememektedir.
- Kullanıcının baştaki her ortamda kullanım düşüncesi, raporda ölçülebilir düz zemin ve sabit engel kapsamına daraltılmıştır. Sonuçlar kontrol edilen derslik koşullarıyla sınırlandırılmıştır.
- Nominal 0,10 m/s ve kaçınmada en çok 0,05 m/s, 3 m rota/120 s hedefiyle aritmetik olarak çelişmez. Bu, gerçek donanımda başarı kanıtı değildir.
- 5 × 33 + 35 = 200 ms tarama planı, 50 ms denetim periyodu ve 250/300 ms veri yaşı/tepki bütçeleri birbirleriyle açıklanmıştır. Sensör okumalarının 20 Hz denetimi bloke etmeyecek zamanlama düzeninde yürütülmesi gerçek uygulamada doğrulanmalıdır; rapor süreleri ölçülmüş olarak sunmamaktadır.
- A/B/C koordinatları, engel merkezleri ve Şekil 3 eşleşmektedir. K2 için 0,35 m kalan mesafe hesabı doğrudur.
- 10 cm tolerans, araç referans noktası ve ölçüm belirsizliğiyle birlikte tanımlanmıştır; bütün rota boyunca 10 cm hata garantisi verilmemiştir.
- Videonun denetleyiciye konum vermemesi bağımsız değerlendirme sağlar. Ayrı kalibrasyon/kontrol noktaları, zaman eşleme ve başarısız kayıt kuralları vardır.
- 40 nihai deneme ayar denemelerinden ayrıdır; başarısızlıklar paydadan çıkarılmamaktadır. Dört koşullu bloklu rastgele sıra planı vardır.
- Wilson aralıkları küçük örneklem belirsizliğini göstermeye uygundur. Koşul başına 8/10 bir başarı hedefidir; gerçek başarı olasılığının %95 güvenle en az %80 olduğunu kanıtlamaz. Raporda böyle bir kanıt iddiası yoktur.
- Altı sentetik senaryo incelemede dosyalar değiştirilmeden yeniden yürütülüp kayıtlarla karşılaştırılmıştır. Bunlar fiziksel deney sayısına eklenmemiştir. Boş fiziksel kayıt CSV'sine sonuç yazılmamıştır.
- Kaynak kimlikleri ve atıflar eşleşmektedir. Alajlan makalesinin özeti ve ilgili sensör açıklamaları bu incelemede yayınevi metninden, Iqbal/Rodrigues açıklamaları önceki yayınevi metinlerinden karşılaştırıldı. Bazı diğer eserlerin tam metin erişim sınırları [kaynak doğrulama kaydında](KAYNAK_DOGRULAMA_KAYDI.md) korunmaktadır; DOI doğrulaması bütün tam metinlerin okunduğu anlamına gelmez.
- Bilimsel katkı yeni bir Bug algoritması iddiası yerine, bu prototipte engel yerleşimine göre aşama bazlı deneysel değerlendirme olarak konumlandırılmıştır. 2209-A için yeni algoritma şartı bulunmamıştır. Katkının yeterliliğini bilimsel değerlendirici belirleyecektir.

## 5. On dört sayfanın görünüm kontrolü

| Sayfa | Kontrol sonucu |
| --- | --- |
| 1 | Kapak/kimlik/başlık okunaklı. Özel kapak, 2026 sistem formunun yerine geçmez; kapak zorunluluğu bulunmadı. |
| 2 | Genel bilgiler ve 249 kelimelik özet mevcut. Özetin dört boyutu içerdiği görüldü. |
| 3 | Literatür, araştırma boşluğu, soru/H1, amaç-hedefler. Amaçların ardından gelen kısa açıklama s. 4'e taşmış; içerik kaybı yok. |
| 4 | Donanım tablosu ve teknik gereksinimler okunaklı; güç uyumu açıklanmış. |
| 5 | Şekil 1, kinematik denklemleri ve veri yaşı açıklaması okunaklı. |
| 6 | Arayüz ve kaçınma koşulları mevcut; temas/durdurma belirsizliği yukarıda kaydedildi. |
| 7 | Akış şeması ve deney koşulları tablosu okunaklı. |
| 8 | Şekil 3 koordinatları ve Türkçe “Dönüş öncesi/sonrası” hem görüntüde hem metin katmanında doğru. |
| 9 | Başarı ölçütleri, payda kuralları, Wilson ve RMSE açıklanmış. |
| 10 | Ön çalışma tablosu ve Şekil 4 okunaklı; sentetik/fiziksel ayrımı açık. |
| 11 | Takvim ve risk tabloları sayfa sınırları içinde; paralel süre yorumu açık konu. |
| 12 | Olanaklar, yaygın etki ve genel ÜYZ açıklaması okunaklı. |
| 13 | 22 kalemlik bütçe tek sayfada; 11.500 TL toplamı doğru. |
| 14 | Yedi kaynak alfabetik; altı DOI bağlantısı doğru hedefe bağlı. Corke künyesinde basım yeri eksik. |

Metin bloklarında sayfa dışına taşma saptanmadı. Görsel ve tablo boyutları TYBS önizlemesinde farklılaşabileceğinden bu dosya kontrolü sistem önizlemesinin yerine geçmez. İncelenen 2026 bilgi notunda bu kapaklı inceleme PDF'sine özel bir sayfa üst sınırı saptanmadı; “14 sayfa olduğu için uygunsuz” sonucu çıkarılmadı.

## 6. PDF dışındaki zorunlu başvuru kontrolleri

Bunların tamamlandığı rapor dosyasından doğrulanamaz:

1. Öğrencilik/başvuru uygunluğu; aynı dönemde birden fazla veya devam eden 2209-A/B görevi olmaması; aynı projenin önceki TÜBİTAK desteği bulunmaması.
2. Yürütücü ARBİS bilgilerinin, danışmanın YÖKSİS/ARBİS bilgilerinin güncelliği; danışmanın aynı dönemde en fazla beş 2209-A görevi kuralı.
3. Yürütücüye ait IBAN ve sistemdeki diğer kimlik/kurum/bütçe bilgileri.
4. İçeriğin TYBS alanlarına eksiksiz aktarılması. Şekiller JPG/JPEG/PNG olarak eklenmeli; PDF/SVG kaynakları doğrudan editöre resim diye yüklenmemelidir. Tablolar, listeler ve denklemler bilgi notundaki editör talimatlarıyla kurulmalıdır.
5. ÜYZ rehberi 1.2.2 uyarınca özel alanda gerçek araç adları, görünen sürüm bilgisi ve kullanım aşaması/kapsamı beyanı. Bölüm 5'in genel ifadesi bu özel alanı doldurmanın yerine geçmez. Görünmeyen sürüm numarası üretilmez; [gerçek kullanım kaydı](UYZ_KULLANIM_BEYANI_KAYDI.md) temel alınır.
6. “Proje Önerisini Önizle” ile görseller, tablolar, Türkçe harfler, matematiksel ifadeler ve bütün metnin yeniden kontrolü.
7. Öğrenci ve akademik danışman onayı: **11 Kasım 2026, saat 17.30 (Türkiye)**. Kuruluş yetkilisi e-imza dönemi: **16–23 Kasım 2026**. PDF'nin danışmana iletilmesi sistem onayı sayılmaz.

Resmî süre sonuçların ilanından başlar; altı ayın okulun Haziran 2027 teslimine kesin olarak sığacağı henüz garanti edilemez. Nihai takvim sonuç tarihiyle birlikte izlenmelidir. Donanım satın alındığında fatura ve varsa üniversite envanter yükümlülükleri ayrıca geçerlidir; bu inceleme satın alma yapılmasını istememektedir.
