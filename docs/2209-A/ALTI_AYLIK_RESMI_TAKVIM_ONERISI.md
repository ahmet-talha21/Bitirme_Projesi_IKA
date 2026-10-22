# Altı aylık çalışma takvimi — kullanıcının seçtiği plan

Güncelleme: 22 Ekim 2026. Kullanıcı “6 aylık planı kullanalım.” diyerek bu planı seçti. Danışman incelemesi henüz yapılmış sayılmıyor; takvim tarihleri ve destek sonucu ilan günü bilinmiyor.

**Proje:** Kullanıcı tarafından belirlenen rota bilgisine göre hareket eden otonom araç tasarımı

## Süre ve akademik teslim ilişkisi

[2026 çağrı duyurusunun 6.1 maddesi](https://tubitak.gov.tr/sites/default/files/2026-10/2209-A_2026_Yili_Cagri_Duyurusu.pdf), resmî proje süresini sonuçların ilan edildiği tarihten itibaren en fazla 12 ay olarak tanımlar. Kullanıcının seçtiği planlanan toplam süre **6 ay**dır. Başlangıç tarihi olarak Ocak 2027 varsayılmamıştır.

Kullanıcının **Haziran 2027 bitirme projesi teslim hedefi** korunur. Sonuçların hangi tarihte açıklanacağı bilinmediği için altı aylık resmî sürenin Haziran 2027'de biteceği söylenemez. Akademik hazırlık ve resmî destek takviminin ilişkisi danışmanla başvuru öncesinde değerlendirilecektir. Destek/ödeme tarihi, destekten önce yapılacak giderlerin uygunluğu veya kişisel harcama taahhüdü varsayılmamaktadır.

## Seçilen plandaki iş paketleri

Her iş paketinin uygulama sorumlusu **Ahmet Talha Arslan**'dır. Danışmanın bilimsel yönlendirme ve incelemesi süreç boyunca devam edecektir.

| İP | Faaliyet ve başarı kontrolü | Planlanan ay aralığı | Katkı |
| --- | --- | --- | --- |
| 1 | Donanım ve kalibrasyon: iki motorun kontrolü ve enkoder sayımı, beş sabit mesafe sensörünün ölçüm/geçerlilik kaydı, besleme ve tekerlek ölçeği kontrolleri. ToF taşıyıcıları öncelikli değerlendirilecek. | 1–2 | %20 |
| 2 | Arayüz ve haberleşme: yerel waypoint rotası tanımlama, rota aktarımı, başlatma/durdurma ve görev durumunu izlemenin doğrulanması. | 1–2 | %15 |
| 3 | Konum kestirimi ve rota takibi: başlangıç konumu/yönü ve waypoint sırasının kontrolü; engelsiz izleme hatasının bağımsız referansla değerlendirilmesi. | 3 | %20 |
| 4 | Engel algılama, kaçınma ve rotaya dönüş: seçilen Bug 2 uyarlamasının bütünleştirilmesi, durum geçişleri ve ayar denemelerinin kaydı. | 4–5 | %30 |
| 5 | Kontrollü deneyler ve analiz: aynı son sürümle dört koşulda 10'ar, toplam 40 geçerli deneme; her engelli koşulda en az 8/10 birleşik başarı hedefinin, sürelerin ve ölçülebilen rota hatasının değerlendirilmesi. | 6 | %15 |

Katkılar toplamı **%100**'dür. Bunlar iş paketlerinin araştırmanın başarısına katkısını gösterir; gerçekleşmiş performans oranı değildir.

## Uygulama sırası ve zaman gerekçesi

İlk iki ayda donanım/kalibrasyon ve arayüz çalışmaları birlikte ilerletilecektir. Tek yürütücünün işi bölümlere ayırması planlanmaktadır; eş zamanlı çalışan ayrı geliştirme ekipleri varsayılmamaktadır. Donanım beklenen günlerde arayüzün koordinat, rota doğrulama ve komut işlevleri üzerinde çalışılabilir.

Üçüncü ayın rota takibi çalışmaları, hareket/enkoder kalibrasyonu ile rota aktarımı tamamlandıktan sonra yürütülecektir. Dördüncü ve beşinci aylar, projenin temel amacı olan engelden kaçınma ve rotaya dönüşün bütünleştirilmesine ayrılmıştır. Son ayda geliştirme/ayar denemelerinden ayrı nihai değerlendirme ve analiz yapılacaktır. Sürüm değişikliği gerektiğinde etkilenen deney koşulları aynı son sürümle yeniden değerlendirilecektir.

Bu dağılım, mevcut beş iş paketini ve seçilen deney sayısını altı ay içine yerleştirir. Donanıma erişim ve bağımsız görüntü ölçümünün kurulabilirliği takvim açısından ayrıca kontrol edilecektir. Deney yeri hâlen bilinmiyor; belirli bir üniversite laboratuvarına erişim varsayılmadı.

Literatür incelemesi, malzeme alımı, sonuç raporu hazırlığı ve paylaşım çalışmaları ilgili teknik faaliyetlerle birlikte yürütülecektir; 2026 bilgi notuna uygun olarak ayrı iş paketleri yapılmamıştır. Nihai teslim hazırlığı için akademik takvimdeki Haziran hedefi ayrıca izlenecektir.

## Danışman incelemesinde ve uygulama hazırlığında açık kalanlar

- Seçilen altı aylık sürenin ve iş yükü dağılımının danışman tarafından değerlendirilmesi.
- Haziran 2027 tesliminin kesin günü ve destek takvimiyle ilişkisinin değerlendirilmesi.
- Donanıma erişim, seçilen 11.500 TL bütçenin güncel ürün/fiyat kontrolü, deney yeri ve bağımsız ölçüm düzeni.
- Kullanıcının seçtiği 10 cm waypoint/rotaya dönüş hedefleri ve 120 saniye deneme sınırının uygulanabilirliği; kalan teknik parametreler.

Kullanıcının seçtiği süre ve ay dağılımı [birleşik rapora](ARASTIRMA_ONERISI_BIRLESIK_TASLAK.md) işlendi. Mevcut [Kasım–Haziran akademik hedef planı](CALISMA_TAKVIMI_TASLAGI.md) ayrıca korunmuştur. Bu seçim başvurunun gönderildiği veya danışman tarafından onaylandığı anlamına gelmez.
