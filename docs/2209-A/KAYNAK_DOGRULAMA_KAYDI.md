# Kaynak ve DOI doğrulama kaydı

Tarih: 22 Ekim 2026. Bu kayıt bilimsel metnin dışında tutulur. DOI doğrulaması eserin kimliğine ve bağlantı çözümlemesine ilişkindir; tam metnin okunması ayrı bir erişim kaydıdır.

| Kaynak | DOI yönlendirmesi | Crossref kaydı |
| --- | --- | --- |
| Path-planning strategies for a point mobile automaton moving amidst unknown obstacles of arbitrary shape | HTTP 302; https://doi.org/10.1007/BF01840369 | HTTP 200; başlık/yazar/yıl eşleşti. |
| Robotics, Vision and Control | HTTP 302; https://doi.org/10.1007/978-3-319-54413-7 | HTTP 200; başlık/yazar/yıl eşleşti. |
| Probable Inference, the Law of Succession, and Statistical Inference | HTTP 302; https://doi.org/10.1080/01621459.1927.10502953 | HTTP 200; başlık/yazar/yıl eşleşti. |
| An Optimal and Energy Efficient Multi-Sensor Collision-Free Path Planning Algorithm for a Mobile Robot in Dynamic Environments | HTTP 302; https://doi.org/10.3390/robotics6020007 | HTTP 200; başlık/yazar/yıl eşleşti. |
| Integrating BIM–IoT and Autonomous Mobile Robots for Construction Site Layout Printing | HTTP 302; https://doi.org/10.3390/buildings13092212 | HTTP 200; başlık/yazar/yıl eşleşti. |
| Hierarchical Control Architecture for Trajectory Tracking of Differential-Drive Nonholonomic Robots Using LQG-Based Velocity Control | HTTP 302; https://doi.org/10.3390/robotics15090171 | HTTP 200; başlık/yazar/yıl eşleşti. |

## Okuma ve erişim kapsamı

- Alajlan vd. (2017), Iqbal vd. (2023) ve Rodrigues vd. (2026) için önceki incelemede alınan yayınevi içerikleri ve bu revizyonda makalelerin amaç/deney karşılaştırmaları kullanıldı. Kesin biçimde “bu kaynaklarda bu işlev yoktur” iddiası kurulmadı; araştırma boşluğu seçilen mimaride aşama bazlı, bağımsız ölçümlü deneysel veri ihtiyacı olarak tanımlandı.
- Lumelsky ve Stepanov (1987): DOI ve makale kimliği Crossref ile eşleşti. Yayınevinin tam metin adresi ağ aracısında 403 ile engellendi. Bug 2 kenar izleme ve hedefe daha yakın M-line noktasından ayrılma mantığı için kitabın yazarına ait açık `Bug2.m` açıklaması/uygulaması da okundu: https://github.com/petercorke/robotics-toolbox-matlab/blob/master/Bug2.m. Makalenin tam metni okunmuş sayılmadı.
- Corke (2017): Kitabın DOI, yazar, yıl ve ISBN kayıtları doğrulandı. Yazarın eşlik eden araç kutusunun README ve `Vehicle.m` / `Bug2.m` açıklamaları incelendi. README, 2017 ikinci baskının bu sürümü kullandığını açıklıyor. Kitabın tüm bölümlerinin tam metin incelemesi yapıldığı iddia edilmiyor.
- Wilson (1927): Özgün skor aralığı kaynağının DOI ve eser kimliği doğrulandı. Yayıncı tam metni erişime kapalıydı. Wilson skor aralığı, raporda gelecekte uygulanacak bir analiz yöntemi olarak belirtildi; bu aşamada fiziksel denemelere ait oran veya aralık üretilmedi.
- STMicroelectronics (2024): Resmî veri sayfası PDF'si HTTP 200 ile indirildi. Kapaktaki DS11555 Rev. 6 / Haziran 2024 ve özellikle s. 21–24 üzerindeki koşul, menzil, doğruluk ve zamanlama tabloları doğrudan okundu. Bu teknik kaynağa DOI atanmadığından DOI uydurulmadı. https://www.st.com/resource/en/datasheet/vl53l0x.pdf
- Eski tarihsiz ders notu/GitHub kaynakları ana kaynakçadan çıkarıldı. Teknik çalışma geçmişindeki kayıtlar korunmuştur.

## Doğrulamanın sınırı

Bazı DOI adresleri HTTP 302 ile yayınevine yönlendirildi; yönlendirme sonrasındaki sayfalarda 403 veya boş HTTP 202 yanıtları görüldü. Bu yanıtlar başarılı tam metin erişimi olarak raporlanmadı. Kaynak künyeleri Crossref kayıtlarıyla karşılaştırıldı. Ham doğrulama özeti `tedarik/kaynak_dogrulama_2026-10-22.json` dosyasındadır.
