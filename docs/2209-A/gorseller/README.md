# Başvuru görselleri — yenilenen sürüm

Güncelleme: 21 Ekim 2026. Üç şekil, kullanıcının daha açıklayıcı ve görsel olarak özenli tasarım isteğiyle yeniden hazırlandı. Paylaşılan kabul almış örneklerin kısa blok, simge ve aşamalı anlatımı incelendi; onların metinleri, şekilleri veya sonuçları kopyalanmadı.

Bu şekiller tasarım önerisidir; fotoğraf, uygulanmış devre, yapılmış deney veya simülasyon sonucu değildir. Sensör ve araç simgeleri belirli bir ürün modelini ya da satın alınmış donanımı göstermez. Çizimler image_gen aracıyla ÜYZ desteği kullanılarak yenilendi; [yenileme kaydı](kaynaklar/yenileme_notlari.md) bu kullanımın başvuruda beyan edilmesine yardımcı olacaktır.

TYBS için PNG dosyaları, birlikte incelemek için [PDF paketi](gorseller_toplu.pdf) bulunuyor. Güncel PDF'ler PNG'lerin belgeye yerleştirilmiş hâlidir; düzenlenebilir vektör çizim değildir. İlk sürümün PNG/SVG/PDF ve kaynakları [arşivde](arsiv/ilk_surum/README.md) korunuyor. Nihai şekil numaraları ve TYBS'deki okunaklılık ön izlemeyle kontrol edilecek.

## Şekil 1 — sistem mimarisi

![Sistem mimarisi](sekil_1_sistem_mimarisi.png)

**Önerilen açıklama:** Kullanıcı arayüzü, algılama, ESP32 kontrol birimi ve motor sürme işlevleri arasındaki planlanan veri akışı. Mesafe ölçümleri ve enkoder geri bildirimi kontrol birimine aktarılır; motor komutları sürücü üzerinden iki motora iletilir. Wi-Fi önerilen arayüz bağlantısıdır. Simgeler temsilidir; sensör türleri, parça modelleri ve güç altyapısı ayrıca belirlenecektir. Çizim ÜYZ desteğiyle hazırlanmıştır.

[PNG](sekil_1_sistem_mimarisi.png) · [PDF](sekil_1_sistem_mimarisi.pdf)

## Şekil 2 — önerilen çalışma akışı

![Önerilen çalışma akışı](sekil_2_calisma_akisi.png)

**Önerilen açıklama:** Rota izleme ve engelden kaçınma durumlarının iki kolda gösterildiği kontrol akışı önerisi. “A” bağlantıları sensör ve konum verilerinin güncellendiği yeni kontrol döngüsüne dönüşü gösterir. Kaçınma etkinken engel çevresi izlenir ve rotaya katılma koşulları değerlendirilir; etkin değilken waypoint takibi ve engel tespiti yürütülür. Geçersiz veri veya süre aşımında güvenli duruş öngörülür. Algoritma, eşikler ve sensör düzeni henüz kesinleşmemiştir. Çizim ÜYZ desteğiyle hazırlanmıştır.

Uzun dış dönüş oku kaldırıldı; karar dalları Evet/Hayır etiketleri ve kısa bağlantılarla düzenlendi. “A” işareti fiziksel kablo veya ek sensör anlamına gelmez.

[PNG](sekil_2_calisma_akisi.png) · [PDF](sekil_2_calisma_akisi.pdf)

## Şekil 3 — planlanan deney düzeni

![Planlanan deney düzeni](sekil_3_deney_alani.png)

**Önerilen açıklama:** Yaklaşık 3 × 3 metre olarak planlanan deney alanında örnek waypoint rotası, sabit engel ve kaçınma davranışının temsili gösterimi. Kesik mavi çizgi referans rotayı, turkuaz çizgi anlatım amacıyla çizilmiş olası bir kaçınma yolunu gösterir. Sağdaki aşamalar rota izleme, algılama, kaçınma ve rotaya katılma işlevlerini açıklar. Noktalar, engel boyutları ve konumu, algılama alanı ve kaçınma eğrisi nihai ölçülendirme değildir; çizimden sayısal açıklık veya performans sonucu çıkarılmayacaktır. Kaçınma eğrisi deney veya simülasyon verisi değildir; nihai algoritmanın tam olarak bu eğriyi izleyeceği iddia edilmemektedir. Çizim ÜYZ desteğiyle hazırlanmıştır.

[PNG](sekil_3_deney_alani.png) · [PDF](sekil_3_deney_alani.pdf)

## Dosyalar ve yeniden paketleme

Şekilleri hazırlamak için şu anda araç kurulması veya fotoğraf/video çekilmesi gerekmiyor. İleride gerçek hareketin bağımsız ölçülmesi ayrı bir iştir; kamera o aşama için değerlendirilen bir seçenektir.

Yeni PNG çıktıları görsel olarak kontrol edildi. Mevcut PNG'leri içeriklerini değiştirmeden PDF belgelere yerleştirmek için Python 3 ve ReportLab kullanılıyor. Depo kökünden:

```sh
python docs/2209-A/gorseller/kaynaklar/pdf_paketle.py
```

İlk sürümün Graphviz/Matplotlib kaynakları ve çıktıları [arşivde](arsiv/ilk_surum/README.md) bulunuyor; bunlar güncel görselleri yeniden üretmez. Yöntemin kavramsal kaynakları [yöntem taslağında](../YONTEM_TASLAGI.md) belirtilmiştir.
