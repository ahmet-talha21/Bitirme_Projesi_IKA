# 3.1. Çalışma takvimi — Haziran hedefi için taslak

Güncelleme: 21 Ekim 2026. Kullanıcı Haziran 2027 hedefinin okulun bitirme projesi teslimi olduğunu, kesin günün henüz belli olmadığını açıkladı. Önceden önerilen altı aylık süre kullanıcı tarafından onaylanmış sayılmayacak. Aşağıdaki Kasım–Haziran planı akademik teslim hedefi için öneridir; resmî TÜBİTAK başlangıcı/süresi değildir.

## Süreyi belirleme dayanağı

[2026 çağrı duyurusunun 6.1 maddesi](https://tubitak.gov.tr/sites/default/files/2026-10/2209-A_2026_Yili_Cagri_Duyurusu.pdf), proje süresini değerlendirme sonuçlarının ilan edildiği tarihten itibaren en fazla 12 ay olarak tanımlıyor. İlan tarihi ve projenin fiilî çalışma başlangıcı henüz belli değil. Bu yüzden Ocak 2027'yi resmî başlangıç varsayıp “Ocak–Haziran, altı ay” yazılmayacak.

Haziran hedefi çalışma planına kaydedildi. TYBS'ye girilecek toplam süre ve iş paketlerinin ay aralıkları, bu hedef ile resmî süre hesabı birlikte değerlendirilerek belirlenecek. Geliştirme için gerekli donanıma ne zaman erişilebileceği de dikkate alınacak; destek/ödeme tarihi veya kişisel harcama taahhüdü varsayılmadı.

Başvurudaki toplam süre, başvuru tamamlanmadan önce planlanan ay sayısı olarak seçilmelidir; sonuç ilanı beklenerek süre alanı boş bırakılmayacak. Henüz bilinmeyen ilan tarihi, Haziran akademik teslimiyle resmî destek takviminin kesin olarak çakıştığı varsayımını kurmamıza izin vermiyor. Planlanan süre ve bu ilişki danışmanla başvuru öncesinde değerlendirilecek.

## Bitirme projesi hedef takvimi — öneri

| Hedef dönem | Geliştirme odağı |
| --- | --- |
| Kasım–Aralık 2026 | İP1: donanım/sensör düzenini netleştirme; parçalar erişilebilir olduğunda montaj, besleme, enkoder ve mesafe ölçümü kalibrasyonları. |
| Ocak 2027 | İP2: rota arayüzü, araçla haberleşme ve komut/durum akışı. |
| Şubat 2027 | İP3: konum kestirimi ve engelsiz waypoint rotası takibi. |
| Mart–Nisan 2027 | İP4: engel algılama, kaçınma ve rotaya dönüşün bütünleştirilmesi/ayar denemeleri. |
| Mayıs 2027 | İP5: sabitlenmiş sürümle kontrollü deneyler ve performans analizi. |
| Haziran 2027 | Tamamlanan teknik çalışmanın danışman incelemesi, gerekli düzeltmeler ve bitirme projesi teslimi; kesin güne göre zaman payı ayrılacak. |

Kasım başlangıcı ve dönem dağılımı planlama önerisidir. Donanım alım tarihi veya bu dönemlerde yapılacak harcamaların destek kapsamında olduğu iddia edilmiyor. Donanım beklenirken arayüz ve yazılım hazırlığı öne alınabilir. Haziran satırı, resmî çalışma takvimine ayrı “rapor yazma/yaygınlaştırma” iş paketi olarak taşınmayacak. Akademik hedef takvimi, TYBS'nin resmî süre hesabının yerine kullanılmayacak.

## İş paketleri, bağımlılıklar ve katkı önerisi

Aşağıdaki katkı değerleri planlama önerisidir; toplamları %100'dür. Bunlar deney başarı yüzdeleri değildir. Her iş paketinin uygulama sorumlusu Ahmet Talha Arslan'dır; danışmanın bilimsel yönlendirmesi ve incelemesi süreç boyunca sürecektir.

| İş paketi | Ön koşul / sıra | Planlanan başarı kontrolü | Araştırmanın başarısına katkı önerisi |
| --- | --- | --- | --- |
| İP1 — Donanım ve sensör entegrasyonu, kalibrasyon | Ürün uyumluluğu ve donanım erişimi netleşince. | İki motorun yön/hız komutları ve iki enkoderin sayımı doğrulanacak; beş sensörün ölçüm/geçerlilik bilgisi kaydedilecek. Besleme, tekerlek ölçeği ve durma davranışı kontrol edilecek. | %20 |
| İP2 — Kullanıcı arayüzü ve haberleşme | Rota koordinatları ve komut biçimi tanımlanınca; ilk yazılım çalışmaları İP1'e kısmen paralel yapılabilir. | Bilgisayar öncelikli ve telefondan erişilebilir arayüzde waypoint rotası tanımlama, rota aktarımı, durum gösterimi ve başlatma/durdurma akışı doğrulanacak. | %15 |
| İP3 — Rota izleme ve konum kestirimi | İP1'in hareket/enkoder kalibrasyonu ve İP2'nin rota aktarımı. | Engelsiz referans parkurunda rota takibi, başlangıç pozu ve waypoint sırası kontrol edilecek. Rota hatası seçilecek bağımsız referans yöntemiyle değerlendirilecek; sayısal kabul eşiği deney planında belirlenecek. | %20 |
| İP4 — Engel algılama, kaçınma ve rotaya dönüş | İP1'in mesafe ölçümleri ve İP3'ün temel rota takibi. | Sabit engelin temas öncesinde algılanması, çarpışmasız kaçınma ve rotaya yeniden katılma ayrı sonuçlar olarak doğrulanacak. İlerleyememe/hata durumları kaydedilecek. | %30 |
| İP5 — Kontrollü deneyler ve performans analizi | İP4 tamamlandıktan ve son değerlendirme sürümü sabitlendikten sonra. | Önceden tanımlanacak koşul ve tekrar sayılarıyla denemeler yürütülecek. Geçerli başarısız denemeler de dahil edilerek oranlar, süreler ve uygun referansla rota hatası değerlendirilecek. | %15 |

## Haziran hedefine göre planlama ilkeleri

- Donanım gelmeden yapılabilecek arayüz tasarımı, koordinat/komut tanımı ve kontrol yazılımının hazırlığı ilerletilebilir. Bunlar tamamlanmış araç deneyi olarak gösterilmeyecek.
- Nihai performans deneyleri için geliştirme/ayar denemelerinden ayrı zaman ayrılacak. Son değerlendirme başladıktan sonra sürüm değişirse etkilenen koşullar aynı son sürümle yeniden çalıştırılacak.
- Deney ve analizin Mayıs içinde tamamlanması, Haziranın danışman incelemesi ve olası düzeltmelere ayrılması öneriliyor. Bu tarihler gerçekleşmiş ilerleme değildir; kesin teslim günü ve başlangıç koşullarına göre gözden geçirilecek.
- Literatür incelemesi, malzeme alımı, sonuç raporu hazırlığı ve paylaşım çalışmaları yürütülecek; 2026 bilgi notuna uygun biçimde ayrı iş paketleri yapılmayacak.

## Nihai takvim için tamamlanacak bilgiler

1. Haziran içindeki kesin teslim günü ve okulun ayrıntılı teslim takvimi.
2. Çalışmaya ve donanıma erişime ilişkin gerçek başlangıç koşulları; resmî proje süresiyle ilişki.
3. Beş iş paketinin ay aralıkları; birbirine bağımlı adımların sırası ve tek yürütücünün iş yükü.
4. Deney tekrar sayıları, ölçüm doğruluğu, rota/katılma toleransları ve sayısal hedefler.

Bu belge, akademik hedef takvimi, başarı kontrolleri ve katkı dağılımı önerisini hazırlar. Resmî başlangıç/süre ve TYBS ay aralıkları tamamlanmadığı için nihai TYBS çalışma takvimi olarak aktarılmaya hazır değildir.
