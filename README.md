# İKA — otonom kara aracı ve TÜBİTAK 2209-A hazırlığı

**Yürütücü:** Ahmet Talha Arslan — Konya Teknik Üniversitesi, Elektrik-Elektronik Mühendisliği, 4. sınıf.

**Akademik danışman:** Prof. Dr. Murat Ceylan.

Proje, arayüzde tanımlanan waypoint rotasını izleyen küçük bir ESP32 tabanlı kara aracının sabit engelleri algılama, çarpışmasız kaçınma ve rotaya yeniden katılma davranışlarını geliştirmeyi ve değerlendirmeyi amaçlar. İlk deney alanı düz zeminde yaklaşık 3 × 3 metre olarak planlanmaktadır.

**TÜBİTAK 2209-A araştırma önerisi:** [Rapor metni](docs/2209-A/ARASTIRMA_ONERISI.md) · [PDF](docs/2209-A/ARASTIRMA_ONERISI.pdf) · [Düzenlenebilir Word](docs/2209-A/ARASTIRMA_ONERISI.docx)

Kapak, genel bilgiler, özet, bilimsel nitelik, hedefler, yöntem, takvim, risk yönetimi, olanaklar, yaygın etki, üç tasarım/deney planı şekli ve bir mantıksal ön çalışma grafiği, ayrıntılı 11.500 TL bütçe ve kaynakça aynı raporda birleştirildi. Başarı değerleri planlanan hedeflerdir; fiziksel prototip ve deneyler proje kapsamında gerçekleştirilecektir. Bu belge danışman kontrolüne sunulur; TYBS başvurusunun gönderildiği anlamına gelmez. Önceki birleşik taslaklar çalışma geçmişi olarak korunmuştur.

## Çalışma durumu

2026 yılı 2209-A araştırma önerisinin danışmana sunulacak sürümü hazırlandı. Önceki bölüm taslakları ve kaynak/fiyat araştırma kayıtları çalışma geçmişi olarak tutulmaktadır. Enkoderli iki motorlu hareket mimarisi ve beş sabit mesafe sensörü düzeni seçildi: ön orta, iki ön çapraz ve iki yan. Kullanıcı dört koşulda 10'ar tekrar, toplam 40 değerlendirme denemesini ve her engelli koşulda en az 8/10 birleşik görev başarısı hedefini uygun buldu. Bug 2 mantığından yararlanan kaçınma yaklaşımı, ToF önceliği, 6 aylık plan, 10 cm waypoint/rotaya dönüş hedefleri ve 120 saniye deneme sınırı seçildi. Kullanıcı 11.500 TL planlama bütçesini de seçti. Rapor, işlevsel donanım gereksinimleri, sensör yerleşimi, arayüz/ağ düzeni ve sayısal deney protokolüyle tamamlandı. Satın alınan ürünlerin giriş kontrolü ve fiziksel kalibrasyon proje faaliyetleridir; sonuçları elde edilmiş gibi sunulmaz. Fiziksel prototip geliştirme ve deneyler henüz yapılmadı. Altı sentetik senaryoyla durum makinesinin mantıksal ön doğrulaması çalıştırıldı; kod ve kayıtlar ayrı bir ön çalışma klasöründedir.

Kullanıcı Haziran 2027 hedefinin bitirme projesi teslimi olduğunu, kesin günün henüz belli olmadığını açıkladı. Mayısta deney/analiz, Haziranda inceleme/teslim hedefi önerildi. Kullanıcı daha sonra 6 aylık planı açıkça seçti; 1–6. ay dağılımı rapora işlendi. Resmî başlangıç günü sonuç ilanına göre belli olacak.

**Bütçe önerisini incele:** [11.500 TL planlama tablosu](docs/2209-A/BASVURU_BUTCE_ONERISI.md) · [PDF](docs/2209-A/BASVURU_BUTCE_ONERISI.pdf) · [Word](docs/2209-A/BASVURU_BUTCE_ONERISI.docx) · [CSV](docs/2209-A/BASVURU_BUTCE_ONERISI.csv)

Kullanıcı toplam 11.500 TL planlanan destek talebini seçti. Birim bedeller KDV dahil planlama tahminleridir; teklif veya onaylanmış destek tutarı değildir. Kaynaklı satış fiyatı gözlemleri ayrı tutulmuştur.

## Başvuru bölümleri

| Belge | İçerik |
| --- | --- |
| [Genel bilgiler ve görevler](docs/2209-A/GENEL_BILGILER_VE_GOREVLER.md) | Yürütücü, danışman, kurum ve tek öğrencili görev dağılımı. |
| [1.1 Bilimsel nitelik taslağı](docs/2209-A/BILIMSEL_NITELIK_TASLAGI.md) | Konunun önemi, ilgili çalışmalar, araştırma sorusu ve beklenen katkı. |
| [Amaç ve hedefler taslağı](docs/2209-A/AMAC_VE_KAPSAM_TASLAGI.md) | Projenin kapsamı ve geliştirilecek temel işlevler. |
| [2 Yöntem taslağı](docs/2209-A/YONTEM_TASLAGI.md) | Önerilen mimari, kaçınma yaklaşımı, deney değişkenleri ve ölçüm düzeni. |
| [3.1 Çalışma takvimi taslağı](docs/2209-A/CALISMA_TAKVIMI_TASLAGI.md) | Haziran hedefi, iş bağımlılıkları, başarı kontrolleri ve katkı dağılımı önerisi. |
| [3.2 Risk yönetimi taslağı](docs/2209-A/RISK_YONETIMI_TASLAGI.md) | Olası teknik sorunlar, önleyici kontroller ve temel hedefleri koruyan B planları. |
| [3.3 Araştırma olanakları taslağı](docs/2209-A/ARASTIRMA_OLANAKLARI_TASLAGI.md) | Doğrulanan kişisel ekipman ve kurumdan teyit edilecek altyapı. |
| [4 Yaygın etki taslağı](docs/2209-A/YAYGIN_ETKI_TASLAGI.md) | Beklenen prototip, arayüz, deney kayıtları ve teknik dokümantasyon çıktıları. |

## Hazırlık ve kaynak notları

- [Başvuru durumu, kalan işler ve önerilen tamamlama sırası](docs/2209-A/BASVURU_DURUMU_VE_EKSIKLER.md)
- [Başvuru görselleri: sistem şeması, çalışma akışı ve deney alanı](docs/2209-A/gorseller/README.md)
- [Literatür karşılaştırması ve okuma durumu](docs/2209-A/LITERATUR_KARSILASTIRMASI.md)
- [Başvuru metninde kullanılan kaynakların tek alfabetik listesi](docs/2209-A/KAYNAKCA_TASLAGI.md)
- [2026 başvuru kuralları ve resmî kaynaklar](docs/2209-A/2026_BASVURU_KURALLARI.md)
- [Proje kararları ve açık bilgiler](docs/2209-A/PROJE_NOTLARI.md)
- [Teknik yöntem ve deney planı](docs/2209-A/YONTEM_VE_DENEY_PLANI.md)
- [Sayısal deney protokolü önerisi ve boş kayıt şablonu](docs/2209-A/DENEY_PROTOKOLU_ONERISI.md)
- [Malzeme ve bütçe ön listesi](docs/2209-A/MALZEME_VE_BUTCE_ON_LISTESI.md)
- [Fiyatlı bütçe taslağı ve para birimi başına ara toplamlar](docs/2209-A/FIYATLI_BUTCE_TASLAGI.md)
- [Batarya–şarj–güç dağıtımı taslağı](docs/2209-A/BATARYA_VE_SARJ_PLANI.md)
- [Eksik ürün bilgileri ve Türkiye teslim fiyatı için teklif metni](docs/2209-A/TEKLIF_ICIN_GEREKEN_BILGILER.md)
- [Donanım adayları ve uyumluluk koşulları](docs/2209-A/DONANIM_SECENEKLERI_VE_UYUMLULUK.md)
- [Motor–sürücü–batarya karşılaştırması ve bulunan fiyatlar](docs/2209-A/MOTOR_SURUCU_BATARYA_KARSILASTIRMASI.md)
- [Ürün ve fiyat teklifi tablosu (CSV)](docs/2209-A/MALZEME_TEKLIF_FORMU.csv)

Nihai metin, güncel TYBS alanlarına aktarılmadan önce yürütücü ve akademik danışman tarafından kontrol edilecek. Kaynaklar, deney sonuçları ve mevcut olanaklar doğrulanmış bilgilere dayanacak.

## Araştırma gerekçesi ve ön çalışma revizyonu

Güncel başlık: **Kullanıcı tanımlı rotada sabit engelden kaçınma ve rotaya yeniden katılma: küçük ölçekli bir kara aracında deneysel değerlendirme**. Ana kaynakça, özgün Bug çalışması, robotik ders kitabı, ToF veri sayfası ve Wilson skor aralığı kaynağıyla yenilendi. Deney yeri üniversitede bölüm kullanımına izin verilecek bir derslik olarak planlandı; varsayımsal oda numarası veya tahsis bilgisi eklenmedi. İP5, 5–6. ayda analiz ve sonuç raporlamasını kapsıyor.

[Çalıştırılmış mantıksal ön çalışma](docs/2209-A/on_calisma/README.md) · [DOI ve okuma kapsamı](docs/2209-A/KAYNAK_DOGRULAMA_KAYDI.md) · [Revizyon kontrol listesi](docs/2209-A/REVIZYON_KONTROLU_2026-10-22.md)
