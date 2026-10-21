# İKA — otonom kara aracı ve TÜBİTAK 2209-A hazırlığı

**Yürütücü:** Ahmet Talha Arslan — Konya Teknik Üniversitesi, Elektrik-Elektronik Mühendisliği, 4. sınıf.

**Akademik danışman:** Prof. Dr. Murat Ceylan.

Proje, arayüzde tanımlanan waypoint rotasını izleyen küçük bir ESP32 tabanlı kara aracının sabit engelleri algılama, çarpışmasız kaçınma ve rotaya yeniden katılma davranışlarını geliştirmeyi ve değerlendirmeyi amaçlar. İlk deney alanı düz zeminde yaklaşık 3 × 3 metre olarak planlanmaktadır.

## Çalışma durumu

Şu an 2026 yılı 2209-A araştırma önerisi hazırlanıyor. Belgeler çalışma taslağıdır. Enkoderli iki motorlu hareket mimarisi ve beş sabit mesafe sensörü düzeni seçildi: ön orta, iki ön çapraz ve iki yan. Parça modelleri, kesin sensör açıları, algoritma, sayısal deney hedefleri, süre ve bütçe kesinleştirilecek. Fiziksel prototip geliştirme ve deneyler henüz yapılmadı.

Kullanıcı Haziran 2027 hedefinin bitirme projesi teslimi olduğunu, kesin günün henüz belli olmadığını açıkladı. Mayısta deney/analiz, Haziranda inceleme/teslim hedefi önerildi. Resmî TÜBİTAK başlangıcı belli olmadığı için toplam süre otomatik olarak altı ay kabul edilmedi.

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
