# Başvuru için hazırlanan tasarım görselleri

Bu çizimler, 21 Ekim 2026 tarihli proje kararları ve teknik öneriler temel alınarak özgün biçimde hazırlandı. Fotoğraf, çalışır prototip görüntüsü veya deney sonucu değildir. Şekiller ChatGPT/Codex desteğiyle Graphviz ve Python/Matplotlib kullanılarak oluşturuldu; bu destek başvurunun ÜYZ kullanım beyanına dahil edilecek.

TYBS'ye eklemek için PNG dosyaları; düzenleme ve yüksek çözünürlüklü dışa aktarım için SVG/PDF dosyaları bulunuyor. Yerleştirmeden sonra görünürlük, boyut ve sayfa taşmaları ön izlemeyle kontrol edilecek. Nihai şekil numaraları metindeki sıraya göre ayarlanacak.

## Şekil 1 — planlanan sistem mimarisi

![Planlanan sistem mimarisi](sekil_1_sistem_mimarisi.png)

**Önerilen açıklama:** Kullanıcı arayüzü, ESP32 kontrol birimi, mesafe algılama, enkoder geri bildirimi ve iki motorun sürülmesi arasındaki planlanan veri akışı. Kesik çizgili IMU bloğu henüz seçilmemiş bir seçenektir. Parça modelleri ve güç altyapısı ayrıca belirlenecektir. Çizim ChatGPT/Codex desteğiyle hazırlanmıştır.

[PNG](sekil_1_sistem_mimarisi.png) · [SVG](sekil_1_sistem_mimarisi.svg) · [PDF](sekil_1_sistem_mimarisi.pdf)

## Şekil 2 — önerilen kontrol akışı

![Önerilen çalışma akışı](sekil_2_calisma_akisi.png)

**Önerilen açıklama:** Rota takibi, engel algılama, kaçınma ve rotaya katılma durumlarının Bug 2 yaklaşımı temelinde önerilen akışı. Algoritma, eşikler ve sensör düzeni henüz kesinleşmemiştir. Akış şeması, uygulanmış veya test edilmiş yazılım sonucu değildir. Çizim ChatGPT/Codex desteğiyle hazırlanmıştır.

[PNG](sekil_2_calisma_akisi.png) · [SVG](sekil_2_calisma_akisi.svg) · [PDF](sekil_2_calisma_akisi.pdf)

## Şekil 3 — örnek deney alanı planı

![Planlanan deney alanı](sekil_3_deney_alani.png)

**Önerilen açıklama:** Yaklaşık 3 × 3 metre olarak planlanan düz zeminli deney alanına ait örnek waypoint rotası ve sabit engel yerleşimi. Noktalar, engel sayısı, boyutları ve konumları anlatım amaçlı seçilmiştir; nihai deney düzeni değildir. Kesik mavi çizgi kullanıcı tarafından tanımlanabilecek referans rotayı temsil eder. Çizgi engellerden geçebilir; kaçınma sırasında araç bu referanstan geçici olarak ayrılacaktır. Ölçülmüş veya simülasyonla elde edilmiş bir kaçınma yolu gösterilmemektedir. Çizim ChatGPT/Codex desteğiyle hazırlanmıştır.

[PNG](sekil_3_deney_alani.png) · [SVG](sekil_3_deney_alani.svg) · [PDF](sekil_3_deney_alani.pdf)

## Çizim ile deney kaydı arasındaki fark

- Bu şekiller başvuruya planlanan sistemi ve yöntemi açıklamak için hazırlanmıştır.
- Araç geliştirildiğinde gerçek hareketin ölçülmesi ayrı bir iştir. Sabit kamera, o aşamada bağımsız referans ölçümü için değerlendirilen seçeneklerden biridir; kullanıcının kamera erişimi henüz doğrulanmadı.
- Şekilleri hazırlamak için kullanıcının şu anda araç kurması, fotoğraf veya video çekmesi gerekmiyor.

## Yeniden oluşturma

Gereksinimler: Python 3, Matplotlib ve Graphviz `dot`. Bu ortamda mevcut araçlarla çizimler oluşturuldu ve PNG çıktıları görsel olarak kontrol edildi.

Depo kökünden:

```sh
python docs/2209-A/gorseller/kaynaklar/olustur.py
```

İlk iki şeklin düzenlenebilir kaynakları `kaynaklar/*.dot`, üçüncü şeklin çizim kodu `kaynaklar/olustur.py` içindedir. Şekiller dış kaynak görseli kopyalanarak üretilmedi. Yöntemin kavramsal kaynakları ilgili [yöntem taslağında](../YONTEM_TASLAGI.md) belirtilmiştir.
