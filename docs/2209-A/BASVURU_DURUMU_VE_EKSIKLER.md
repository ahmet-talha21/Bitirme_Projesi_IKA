# Başvuru durumu ve kalan işler

Güncelleme: 22 Ekim 2026. Bu liste hazırlık durumunu gösterir; başvurunun gönderildiği veya onaylandığı anlamına gelmez.

[İlk birleşik başvuru metni](ARASTIRMA_ONERISI_BIRLESIK_TASLAK.md), [PDF](ARASTIRMA_ONERISI_BIRLESIK_TASLAK.pdf) ve [Word](ARASTIRMA_ONERISI_BIRLESIK_TASLAK.docx) biçiminde hazırlandı. Bölümler ve mevcut üç görsel aynı belgede okunabilir. Dil ve anlatım düzenlemesi tamamlandı; Bug 2 yaklaşımı için kullanıcı seçimi metne işlendi. Başvuru öncesinde tamamlanacak bilgiler [ayrı hazırlık notunda](BASVURU_METNI_HAZIRLIK_NOTLARI.md) tutuluyor.

## Hazırlanan bölümler

| Bölüm | Durum | Tamamlanması için gereken |
| --- | --- | --- |
| Genel bilgiler | Yürütücü, kurum/bölüm, danışman ve Haziran 2027 bitirme teslim hedefi alındı. Kullanıcı ilk proje başlığını korumayı seçti. | Kesin teslim günü; seçilen 6 ay ve 11.500 TL bütçenin danışman incelemesi ve güncel fiyat kontrolü. |
| 1.1 Bilimsel nitelik | Kaynak destekli metin ve ilgili çalışma karşılaştırması hazır; üçüncü örnek incelenerek problem/literatür/katkı ara başlıkları eklendi. | Yöntemle tutarlılık, katkının son ifadesi ve danışman incelemesi. |
| 1.2 Amaç ve hedefler | Kullanıcı dört koşul × 10 tekrar = 40 denemeyi ve her engelli koşulda en az 8/10 birleşik görev başarısı hedefini seçti. | Kalan ek hedefler, uygulanabilirlik gerekçesi ve danışman incelemesi. |
| 2 Yöntem | Seçilen Bug 2 uyarlaması, tekrar planı ve ana hedef metne işlendi. Kullanıcı 10 cm waypoint erişimi, 10 cm rotaya dönüş bandı ve 120 saniye deneme sınırını da seçti; birleşik rapora işlendi. Geometri ve diğer sayısal öneriler açık. Boş kayıt şablonu hazır. | Parça modelleri, sensör açıları, algoritma parametreleri, deney alanı, bağımsız ölçüm ve kalan parametrelerin kesinleştirilmesi; danışman incelemesi. |
| Görseller | Üç yenilenmiş şema PNG ve PDF olarak hazır. | Son yöntem ve parça seçiminden sonra etiket kontrolü; TYBS önizlemesinde okunabilirlik. |
| 3.1 Çalışma takvimi | Kullanıcı 6 aylık toplam süreyi seçti. Beş iş paketi 1–6. ay aralıklarıyla birleşik rapora işlendi; katkılar toplamı %100. Akademik hedef planı ayrı tutuldu. | Danışman incelemesi, akademik hedefle ilişki, kesin teslim günü ve kalan sayısal deney eşikleri. |
| 3.2 Risk yönetimi | Temel hedefleri koruyan önlem ve B planları taslak olarak hazır. | Nihai donanım, algoritma ve ölçüm düzenine göre somutlaştırma. |
| 3.3 Araştırma olanakları | Kişisel lehim ekipmanı ve deneyde kullanılabilecek telefon doğrulandı; taslak hazır. | Kurum altyapısı, deney yeri, sabitleme/kalibrasyon ve diğer ölçüm araçları doğrulanacak. |
| 4 Yaygın etki | Prototip, arayüz, deney kayıtları ve dokümantasyon çıktıları önerildi. | Süre ve kapsamla son uyum; danışman incelemesi. |
| Malzeme / bütçe | Tüm ihtiyaç gruplarını kapsayan 22 kalemli **11.500 TL tahmini bütçe önerisi** Markdown, PDF, Word ve ayrı CSV olarak hazırlandı. Güncel fiyat dayanakları ile tahmini ödenekler ayrıldı. | Kullanıcı 11.500 TL toplamı seçti; danışman incelemesi, teknik model/uyum ve teslim fiyatı kontrolü açık. |
| Kaynakça | Mevcut bilimsel nitelik/yöntem metinlerinde kullanılan yedi kaynak tek alfabetik listede birleştirildi; atıf eşleştirmesi ve DOI'ler kaydedildi. | Nihai metin değişikliklerinde listeyi ve atıfları güncellemek; danışman incelemesi. |
| Özet | Birleşik metnin diğer bölümleri toplandıktan sonra ilk özet yazıldı; dil düzenlemesinde seçilen Bug 2 yaklaşımına göre güncellendi. | Son yöntem, kapsam ve süre kararlarıyla yeniden eşleştirmek. |

## Görsellerin son durumu

Kullanıcının kabul almış örnek olarak sunduğu iki PDF'nin 5–6. sayfalarındaki şemalar ve şekil yerleşimleri incelendi. Mevcut projeye özgü sistem mimarisi, kontrol akışı ve deney alanı şeması bu incelemenin ardından yenilendi. Ayrıntı ve üretim kaydı [görsel yenileme notlarında](gorseller/kaynaklar/yenileme_notlari.md).

Güncel görsel düzeni korunabilir. Teknik seçimler değişirse etiketler veya akış güncellenecek. Şekiller önerilen tasarımı anlatıyor; yapılmış deney, üretilmiş araç fotoğrafı veya simülasyon çıktısı göstermiyor. Deney alanındaki kaçınma yolu temsili. Yeni görsel gereksinimi, nihai yöntemin anlaşılmasına katkısına göre değerlendirilecek; deney yapılmadan sonuç grafiği hazırlanmayacak.

## Önerilen tamamlama sırası

1. Motor/enkoder, şasi, mesafe sensörleri, sürücü ve güç bileşenlerini uyumluluk ve fiyatlarla seçmek. Kaçınma yaklaşımının gerektirdiği algılama kapsamını bu seçimle birlikte kararlaştırmak.
2. Deney yeri ve bağımsız ölçüm imkânını doğrulamak; [hazırlanan protokol önerisini](DENEY_PROTOKOLU_ONERISI.md) kullanıcı/danışmanla gözden geçirmek ve kalibrasyona bağlı parametrelerle birlikte kesinleştirmek. Bunlar gelecek deneyler için planlanan ölçütler olacak.
3. Seçilen 6 aylık süre ve ay bazında çalışma takvimini danışmanla değerlendirmek; risk, bütçe ve çıktı taslaklarını aynı kapsamda sonlandırmak.
4. Başlık, bilimsel katkı, amaç ve yöntem metinlerini birlikte gözden geçirmek; birleşik kaynakçayı son metinle eşleştirmek ve ilk özeti son kararlara göre güncellemek.
5. Yürütücü ve danışman incelemesinden sonra metin, tablo ve PNG görselleri güncel TYBS alanlarına aktarmak; önizlemeyi, kaynakları ve gerekli ÜYZ beyanını kontrol ederek başvuru/onay adımlarını tamamlamak.

Son tarih ve biçim kuralları [2026 başvuru kuralları notunda](2026_BASVURU_KURALLARI.md) tutuluyor. Görsellerin hazır olması, yöntem ve bütçe kararlarının da tamamlandığı anlamına gelmiyor.

Sensör maliyeti devam incelemesi: [beşli ToF/ultrasonik karşılaştırması](SENSOR_BUTCE_KARSILASTIRMASI.md) hazırlandı. Kullanıcı ToF sensörlerini önceliklendirmeyi seçti. Kesin ürün seçimi açık; kullanıcı daha sonra 11.500 TL planlama bütçesini seçti. ToF önceliği birleşik yöntem metninde korunuyor. Stok durumu başvuru şartı veya rapor yazımına engel olarak kullanılmayacak.

Kullanıcı [altı aylık iş paketi planını](ALTI_AYLIK_RESMI_TAKVIM_ONERISI.md) seçti. Süre ve ay dağılımı birleşik rapora işlendi. Mevcut akademik hedef takvimi ayrı tutuldu; danışman incelemesi ve kesin takvim günleri hâlen açık.

## TYBS metin uzunluğu ve içerik kontrolü — 22 Ekim

Düzyazı çıktısında, boşluklar dahil karakterler sayıldı. Bu kontrol başvuru editöründeki son önizlemenin yerine geçmez; metin değişirse sayımlar yenilenecektir.

| Alan | Hazırlık kontrolü |
| --- | --- |
| Özet | 203 kelime; 25–450 kelime aralığında. |
| 1.1 Bilimsel nitelik | 4172 karakter; en az 350 karakter koşulunun üzerinde. |
| 1.2 Amaç ve hedefler | 1781 karakter; en az 350 karakter koşulunun üzerinde. |
| 2 Yöntem | 12870 karakter; en az 350 karakter koşulunun üzerinde. |
| Çalışma takvimi | Kullanıcının seçtiği 6 ay, beş iş paketi, toplam %100 katkı. |
| Deney kayıtları | CSV yalnız başlık içeriyor; sonuç satırı yok. |

Kullanıcı 10 cm waypoint erişimi, 10 cm rotaya dönüş bandı ve 120 saniye deneme sınırını planlanan hedefler olarak seçti; birleşik rapora işlendi. Ek sayısal öneriler seçilmiş sayılmadı. Danışman incelemesi, gerçek kurum olanakları ve nihai bütçe açık tutuldu.

Ekipman erişimi: Kullanıcı bu ayrıntıların düzenlenebileceğini belirterek yazımın sürmesini istedi. Ölçüm ve telefon sabitleme ekipmanına erişim çalışma hazırlığında planlanacak; mevcut sahiplik, kurum envanteri veya bedelsiz temin varsayılmadı. Başvuru yazımı için fiziksel ön ölçüm beklenmeyecek.

Güncel bütçe önerisi: [11.500 TL planlama tablosu](BASVURU_BUTCE_ONERISI.md) · [PDF](BASVURU_BUTCE_ONERISI.pdf) · [Word](BASVURU_BUTCE_ONERISI.docx). Bütçe 12.000 TL üst sınırının 500 TL altında; mevcut telefon ve lehim ekipmanı yeniden bütçelenmedi. Önceki kaynaklı fiyat CSV'si korunarak tahmini ödenekler ayrı CSV'ye yazıldı. Kullanıcı toplam tutarı seçti; 11.500 TL planlanan destek talebi birleşik rapora işlendi. Resmî gider türlerine aktarım öncesinde danışman ve güncel fiyat/ürün kontrolü yapılacak.

Üçüncü örnek: Kullanıcının sunduğu 2025 tarihli otonom yük taşıma robotu önerisi incelendi; inceleme kapsamı ve anlatıma uyarlanan noktalar [hazırlık notlarına](BASVURU_METNI_HAZIRLIK_NOTLARI.md) kaydedildi. Birleşik metinde bilimsel nitelik bölümünün okunabilirliği ve yöntem–iş paketi bağlantısı geliştirildi. Proje kapsamı, sayısal hedefler, seçilen süre ve tahmini bütçe korundu.
