# 2. Yöntem — ilk bölüm taslağı

Durum: Kullanıcının ve danışmanın incelemesine açık çalışma taslağı. İki motorlu enkoderli şasi ve Bug 2 mantığından yararlanan kaçınma yaklaşımı kullanıcı tarafından seçildi; uygulama parametreleri henüz kesinleşmedi. Kullanıcı [deney protokolündeki](DENEY_PROTOKOLU_ONERISI.md) 40 deneme ve engelli koşul başına en az 8/10 birleşik görev hedefini uygun buldu. Kalan sayısal parametreler, sensör modelleri ve referans ölçüm düzeni tamamlanmadan bu metin nihai TYBS içeriği olarak aktarılmayacak. Deney gerçekleştirilmiş değildir.

## 2.1. Araştırma tasarımı

Araştırma, küçük ölçekli bir kara aracı prototipinin geliştirilmesi ve kontrollü koşullarda tekrarlı deneylerle değerlendirilmesi biçiminde planlanmaktadır. Kullanıcı arayüzünde tanımlanan waypoint rotasının izlenmesi, sabit engellerin algılanması, çarpışmasız kaçınma ve rotaya yeniden katılma davranışları bütünleşik olarak ele alınacaktır. Deneyler, düz zeminde yaklaşık 3 × 3 metre olarak planlanan alanda gerçekleştirilecektir. Şasi boyutları ve gerekli geçiş açıklıkları belirlendikten sonra alanın yeterliliği kontrol edilecektir.

Koordinat tabanlı uygulama verilerinin ESP32 tabanlı mobil robota aktarılmasına ilişkin bir örnek Iqbal vd. (2023) tarafından sunulmuştur. Rodrigues vd. (2026) ise enkoder geri bildirimi, konum bilgisi ve gömülü motor kontrolünü bir araya getiren küçük ölçekli diferansiyel sürüşlü bir platformu deneysel olarak değerlendirmiştir. Bu çalışmalar, arayüz/rota tanımı, konum bilgisi ve hareket kontrolünün ayrı işlevler olarak tasarlanması için dayanak oluşturmaktadır; bu yayınların donanım ve başarı sonuçları geliştirilecek araç için doğrudan geçerli sayılmayacaktır.

Yöntemin uygulanması [çalışma takvimi taslağındaki](CALISMA_TAKVIMI_TASLAGI.md) beş iş paketine bağlanmıştır: donanım/sensör kalibrasyonu İP1, arayüz/haberleşme İP2, konum kestirimi ve rota takibi İP3, kaçınma/rotaya dönüş İP4, kontrollü deney ve analiz İP5 kapsamında ele alınacaktır. Haziran 2027 akademik teslim hedefi için önerilen dönemler, başvuruda seçilecek resmî toplam süre ve ay aralıklarıyla ayrıca uyumlandırılacaktır.

## 2.2. Donanım ve konum kestirimi önerisi

Platform, iki tahrik tekerinin bağımsız kontrol edildiği küçük bir şasi ve enkoderli motorlar üzerine kurulacaktır. ESP32, motor sürücüsü, mesafe sensörleri ve uygun güç altyapısının bütünleştirilmesi planlanmaktadır. Tekerlek dönüşlerinden göreli hareketin hesaplanması için diferansiyel sürüş kinematiği kullanılabilecektir (Dellaert ve Hutchinson, t.y.). Motor, sürücü ve besleme modelleri elektriksel gereksinimler birlikte kontrol edilerek seçilecektir. Engel algılama için ön orta, iki ön çapraz ve iki yan yönünde beş sabit mesafe sensörü kullanılacak şekilde plan yapılmıştır. Mesafe sensörü seçiminde uçuş süresi (ToF) tabanlı taşıyıcılar önceliklendirilecektir. Kesin taşıyıcı modeli, montaj yüksekliği ve açıları; algılama mesafesi, yüzey davranışı, güncelleme hızı ve kaçınma sırasında gerekli ön/yan kapsama göre seçilecektir. Algılama kapsaması gerçek düzenekte kontrol edilecek; sensör sayısından kesintisiz çevre taraması sonucu çıkarılmayacaktır.

Başlangıç konumu ve yönü tanımlanacak; enkoder verileriyle göreli konum/yön kestirimi yapılması değerlendirilecektir. Gerekirse IMU desteği kullanılacaktır. Tekerlek ölçekleri ve dönüş davranışı kalibre edilecek; kayma ve ölçüm hatalarının rota takibine etkisi incelenecektir. Seçilen yaklaşım yeterli doğruluğu sağlamazsa ek konum düzeltme yöntemi, hedefleri değiştirmeyen bir B planı olarak ayrıca tanımlanacaktır. Bağımsız ölçümde kullanılan kameranın konum kestirimine de veri sağlaması seçilirse, bu değişiklik açıkça belirtilecektir.

## 2.3. Arayüz ve veri akışı önerisi

Bilgisayar öncelikli, telefondan da erişilebilir bir web arayüzünde alan ölçeği, başlangıç yönü ve waypoint sırası tanımlanacaktır. Rota ve komutların yerel Wi-Fi üzerinden araca aktarılması; sensör, konum kestirimi ve görev durumunun arayüzde gösterilmesi planlanmaktadır. ESP-IDF'nin HTTP sunucusunda WebSocket desteği bulunması bu haberleşme seçeneği için teknik dayanak sağlamaktadır (Espressif Systems, t.y.). Rota yüklendikten sonra algılama ve hareket kararlarının ESP32 üzerinde yürütülmesi önerilmektedir. Bağlantı kaybı, sensör hatası ve durdurma komutu davranışları uygulama öncesinde belirlenecektir.

## 2.4. Engel kaçınma ve rotaya dönüş

Engelden kaçınma, Bug 2 yaklaşımının engel çevresini takip etme ve hedef doğrultusuna yeniden katılma mantığından yararlanan bir durum makinesiyle gerçekleştirilecektir (Hauser, t.y.-a). Her iki ardışık waypoint arasında bir referans rota parçası tanımlanacaktır. Engel algılandığında araç, algılama ve durma mesafesine uygun biçimde yavaşlayacak veya duracak; temas öncesinde kaçınma durumuna geçecektir. Ardından yerel mesafe ölçümlerine göre engelin kenarı izlenecek, seçilen izleme yönü ve engelle araç arasındaki açıklık korunacaktır.

Arayüzden yüklenen waypoint sırası kaçınma boyunca korunacaktır. Engel algılandığında kaçınmaya başlama konumu ve etkin hedefe uzaklık kaydedilecektir. Araç, etkin hedefe tanımlanan tolerans içinde ulaşıncaya kadar aynı hedefi izleyecektir. Her denemede başlangıç konumu ve yönü işaretli referansa göre ayarlanacak, enkoder başlangıç değerleri kaydedilecektir.

Rotaya dönüş kararı için aracın etkin **sonlu rota parçasına** tanımlanan tolerans içinde ulaşması, hedefe uzaklığının kaçınma başlangıcına göre ölçüm belirsizliğini aşan bir miktarda azalması, engelin geride kalması ve araç gövdesinin ilerleyebileceği açıklığın bulunması birlikte aranacaktır. Kenar izleme yönündeki değişiklikler önceden tanımlanmış durum geçişlerine bağlanacaktır. Rotaya dönüş, yalnızca rota çizgisinin kesilmesiyle değil, aracın belirlenen bant içinde kalarak hedefe doğru ilerlemesini sürdürmesiyle doğrulanacaktır. Açıklık, süre ve ilerleme eşikleri ölçüm duyarlılığı ve kalibrasyon sonuçlarıyla gerekçelendirilecektir.

Bug 2 yaklaşımı; araç genişliği, dönüş kabiliyeti, sınırlı sensör kapsaması ve konum hatası dikkate alınarak fiziksel düzeneğe uyarlanacaktır. Bu nedenle ideal algoritmaya ait teorik tamlık özellikleri prototip için garanti edilmeyecektir. Aynı bölgede ilerleyememe, döngü şüphesi, geçersiz sensör verisi, alan sınırına yaklaşma veya süre aşımı durumunda deneme durdurulacak ve neden kaydedilecektir. Bu kayıt, görevin ilgili düzenekte tamamlanamadığını gösterecektir; ortamda geçerli bir yol bulunmadığı sonucuna dayanak oluşturmayacaktır.

## 2.5. Deney koşulları ve değişkenler

Geliştirme aşamasında önce engelsiz rota takibi, ardından sabit engelli kaçınma davranışı kontrol edilecektir. Nihai değerlendirmede ise engelsiz referans ve farklı sabit engel yerleşimleri aynı protokolle, aşağıdaki blok düzeninde karşılaştırılacaktır. Engel boyutları ve yüzeyleri, sensörlerin doğrulanmış algılama koşullarına göre tanımlanacak; geçişler araç geometrisine uygun seçilecektir. Her deney koşulu birden çok kez uygulanacaktır. Başlangıç pozu, rota, hız ayarı, zemin ve kontrol parametreleri mümkün olduğunca sabit tutulacak; pil durumu ve değişen koşullar kaydedilecektir.

Kullanıcının uygun bulduğu tekrar planı, dört koşulda 10'ar, toplam 40 geçerli değerlendirme denemesidir. Koşullar, engelsiz referans ile düz bölüm, dönüş öncesi ve dönüş sonrası tek engel yerleşimi olarak planlanmaktadır; aynı L biçimli 3 m rota ve kesin koordinatlar hâlen geometri önerisidir. Geliştirme/ayar denemeleri 40 denemeye dahil edilmeyecek. Koşulların 10 blokta, her blokta dördü de birer kez ve önceden rastgeleleştirilmiş sırayla uygulanması önerilmektedir. Koordinatlar, kabul ölçütleri ve uygulama ayrıntıları [protokol taslağında](DENEY_PROTOKOLU_ONERISI.md) verilmiştir. Donanım, ölçüm düzeni ve danışman incelemesiyle kalan ayrıntılar tamamlanacaktır.

- **Temel bağımsız değişken:** Sabit engellerin parkurdaki yerleşimi. Engel sayısı/boyutu da değiştirilecekse bunlar ayrı deney faktörleri olarak tanımlanacaktır.
- **Bağımlı değişkenler:** Temas öncesi algılama, çarpışmasız kaçınma, rotaya dönüş ve görev tamamlama sonuçları; tamamlanma süresi ve tanımlı referansa göre rota hatası.
- **Kontrol edilen koşullar:** Başlangıç pozu, referans rota, hız ayarı, zemin ve sabit deney parametreleri. Kontrol edilemeyen değişimler kayıtlarda belirtilecektir.

## 2.6. Ölçüm ve değerlendirme

Her deneme için engelin temas öncesinde algılanıp algılanmadığı, kaçınmanın temas olmadan tamamlanıp tamamlanmadığı, rotaya yeniden katılım ve hedefe varış ayrı ayrı kaydedilecektir. Engelsiz referans koşulunda oluşan yanlış engel uyarıları da kaydedilecektir. Bu ayrım, algılama hatası ile kaçınma veya konum kestirimi sorunlarının birbirinden ayrılmasını amaçlamaktadır. Geçerli denemelerin tamamı ilgili koşulun paydasında tutulacak; başarısız denemeler sonuçları iyileştirmek için çıkarılmayacaktır. Yalnızca önceden tanımlanmış kayıt/düzenek hataları geçersiz sayılacak ve gerekçeleri ayrıca bildirilecektir.

Başarı oranları başarılı deneme sayısının ilgili koşuldaki geçerli deneme sayısına bölünmesiyle hesaplanacaktır. Süreler ve rota sapması için uygun özet istatistikler verilecek; tamamlanamayan denemeler süre sınırı/başarısızlık kaydıyla ayrıca gösterilecektir. Rota izleme sırasında referans doğru parçasına uzaklık, kaçınma sırasındaki geçici sapma ve rotaya katılma sonrası izleme hatası ayrı değerlendirilecektir. Böylece engelden dolaşmanın gerektirdiği geçici rota değişimi doğrudan başarısız izleme olarak etiketlenmeyecektir. Kullanıcının seçtiği ana hedef, her engelli koşulda en az 8/10 denemede temas öncesi algılama, çarpışmasız kaçınma, rotaya dönüş ve hedefe erişimin birlikte sağlanmasıdır. Bu, elde edilmiş sonuç veya başarı vaadi değildir. Ek öneriler; her engelli koşulda 9/10 temas öncesi algılama, engelsiz koşulda 9/10 görev başarısı, waypoint/rotaya dönüş bandı için 10 cm ve süre sınırı için 120 saniyedir. Bu ek değerler henüz seçilmedi; bağımsız ölçüm/donanım uygulanabilirliği ve danışman incelemesiyle başvurudan önce kararlaştırılacaktır. Bu tekrar sayısından istatistiksel anlamlılık veya tüm ortamlara genellenen başarı sonucu çıkarılmayacaktır.

Rota sapması için, işaretlenmiş deney alanını gören sabit bir kameradan bağımsız referans yol ölçümü değerlendirilmektedir. Kullanıcı deneylerde kullanabileceği telefonunun olduğunu bildirmiştir; alanın tamamını gören yerleşim, sabitleme ve görüntü kalibrasyonu henüz doğrulanmamıştır. Ölçümün güvenilir referansla ilişkilendirilmesi ve kalibrasyon gereksinimi Hauser'in kalibrasyon çerçevesiyle uyumludur (Hauser, t.y.-b). Rota hatası, yalnızca aracın kendi konum tahmini yine kendisiyle karşılaştırılarak doğrulanmayacaktır.

Bağımsız değerlendirmede aktif rota parçası, waypoint'lere sıralı erişimin görüntüden doğrulanmasına göre belirlenecektir. Ölçülen araç referans noktasının bu sonlu parçadaki en yakın noktaya uzaklığı rota hatası olarak alınacaktır; parçanın sonsuz uzantısına uzaklık yeterli sayılmayacaktır. Geçerli ve eşit zaman aralığına getirilmiş izleme örneklerinde kök ortalama karesel hata (RMSE) hesaplanacaktır:

$$\operatorname{RMSE}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}e_i^2}$$

Burada $e_i$ bağımsız ölçülen konumun referans parçaya uzaklığı, $N$ değerlendirilen konum örneği sayısıdır. Örnekleme aralığı ve veri kapsamı raporlanacak; kayıp görüntü aralıkları sonuç iyileştirmek için doldurulmayacaktır. Temas ve algılama olaylarının sırası zaman eşleme belirsizliği nedeniyle ayırt edilemiyorsa olay başarılı algılama diye işaretlenmeyecektir.

## Kesinleştirilecek parametreler

| Parametre | Mevcut durum |
| --- | --- |
| Şasi, motor/enkoder ve sensör modelleri | Enkoderli iki motorlu hareket ve beş sabit mesafe sensörü düzeni seçildi; ToF taşıyıcıları öncelikli. Ölçüler, kesin açılar ve ürünler seçilmedi. |
| Hız, algılama/durma ve yan açıklık mesafeleri | Donanım/kalibrasyonla gerekçelendirilecek. |
| Waypoint ve rotaya katılma toleransları | 10 cm bant ve rotaya dönüş için süre/ilerleme koşulları önerildi; ölçüm doğruluğuyla birlikte kesinleştirilecek. |
| Engel düzenleri ve tekrar sayıları | Dört koşul × 10 tekrar = 40 değerlendirme denemesi kullanıcı tarafından uygun bulundu; kesin geometri ve danışman incelemesi açık. |
| Başarı eşikleri ve süre sınırı | Her engelli koşulda en az 8/10 birleşik görev hedefi kullanıcı tarafından seçildi; diğer hedefler ve 120 saniye süre önerisi kesinleşmedi. |
| Bağımsız referans ölçümü | Kullanıcının telefonu mevcut; alanı gören sabitleme düzeni ve ölçüm doğruluğu doğrulanacak. |

## Kaynaklar

Bu bölümde ve bilimsel nitelik taslağında atıf yapılan yedi kaynağın tam künyeleri [tek alfabetik kaynakçada](KAYNAKCA_TASLAGI.md) birleştirildi. Hauser'in planlama ve kalibrasyon bölümleri sırasıyla t.y.-a ve t.y.-b olarak korunmuştur. DOI bulunan üç makalenin DOI'leri künyelerinin sonundadır. Okuma kapsamı [literatür karşılaştırmasında](LITERATUR_KARSILASTIRMASI.md) kayıtlıdır. Nihai metinde kaynak eklenir veya çıkarılırsa atıf eşleştirmesi yeniden kontrol edilecek.
