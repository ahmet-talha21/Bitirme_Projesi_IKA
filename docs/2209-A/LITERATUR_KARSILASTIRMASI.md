# Literatür karşılaştırması — ilk inceleme

Kontrol tarihi: 21 Ekim 2026. Bu belge sınırlı bir ilk karşılaştırmadır; kapsamlı veya sistematik literatür taraması olduğu iddia edilmiyor. Kaynakların okunan kısmı ve doğrulama düzeyi ayrı belirtilmiştir.

## İçeriği incelenen ilgili çalışmalar

| Kaynak | İncelenen sistem / yöntem | Projemiz açısından çıkarım ve fark |
| --- | --- | --- |
| Iqbal vd. (2023) | BIM verilerinden çıkarılan koordinatları, masaüstü uygulaması ve bulut bağlantısıyla ESP32 tabanlı bir zemin çizim robotuna aktarır. İki NEMA 17 adım motoru ve DRV8825 sürücüleri kullanılır. Deneysel değerlendirmede çizim konum/açı doğruluğu ele alınır. | Kullanıcı/uygulama koordinatlarının fiziksel mobil robot hareketine aktarılmasına ilişkin gerçek bir örnektir. Bizim planımızda temel değerlendirme görevi, sabit engelden kaçınma ve rotaya yeniden katılmadır. Bu çalışmanın çizim doğruluğu bizim aracımızın beklenen veya ölçülmüş doğruluğu olarak kullanılamaz. |
| Rodrigues vd. (2026) | Küçük diferansiyel sürüşlü robotta yüksek düzey rota kontrolü ve düşük düzey LQG motor hız kontrolünü birleştirir. Enkoderler ve üstten kamera temelli konum bilgisi kullanılır; ESP32 gömülü kontrol katmanında yer alır. Dairesel ve sekiz biçimli yörüngelerde ileri/geri hareket deneyleri gerçekleştirilir. | Rota takibi, motor hız kontrolü ve konum bilgisinin ayrı ele alınmasının önemini gösterir. Bu mimarinin dış kamera/merkezi kontrol olanakları, yalnızca enkoder ve yerel sensörlerle yürütülmesi düşünülen bizim araca eşdeğer varsayılamaz. Engel kaçınma için bu makaleden doğrudan başarı garantisi çıkarılmaz. |
| Hauser, Bölüm 9 | Yerel engel bilgisi kullanan Bug yöntemlerini ve robot geometrisinin planlamaya etkisini açıklayan akademik ders kitabı bölümüdür. | Bug 2 yaklaşımı, hedef doğrultusuna yeniden katılma mantığı nedeniyle algoritma adayıdır. Noktasal robot, konum bilgisi ve algılama varsayımları gerçek araçta ayrıca ele alınmalıdır. |
| Dellaert ve Hutchinson, Bölüm 5.2 | Diferansiyel sürüşte tekerlek hareketleri ile doğrusal/açısal araç hareketi arasındaki kinematik ilişkiyi açıklar. | Enkoderli iki tahrik tekeri önerisinin modelleme temelidir. Kayma olmaması gibi model varsayımları, gerçek parkurda kontrol edilmelidir. |

**Okuma durumu:** İki makalenin yayıncı üzerindeki tam metnine erişildi; özet, platform/mimari, ilgili deney ve sonuç bölümleri incelendi. Yazar, yıl, dergi, cilt/sayı ve DOI bilgileri Crossref kayıtlarıyla ayrıca kontrol edildi. Ders kitaplarının ilgili bölümleri yazarların GitHub depolarından okundu. Makale sonuçları bağımsız olarak yeniden üretilmedi.

## Taslakta kullanılabilecek bilimsel çerçeve

- ESP32 kullanımı ve koordinat tabanlı mobil robot hareketi mevcut çalışmalarla gösterilmiş alanlardır. Projenin katkısı yalnızca kontrolcü seçimine dayandırılmayacak.
- Önerilen çalışma, kullanıcı tanımlı rota ile yerel sabit engelden kaçınma ve rotaya dönüşün tek prototipte bütünleştirilmesini, sınırları tanımlı koşullarda tekrarlı deneylerle değerlendirecek.
- Özellikle engel algılama, kaçınma ve rotaya yeniden katılma ayrı başarı ölçütleri olarak tutulacak. Böylece görev başarısızlığının hangi aşamada oluştuğu incelenebilecek.
- Beklenen çıktı, belirli donanım ve deney koşullarına ait performans verisi ve yeniden uygulanabilir bir prototip tasarımıdır. Evrensel üstünlük, ilk kez yapılma, düşük maliyet veya yeni algoritma iddiası bu incelemeyle kurulmuş değildir.
- Benzer engelden kaçınma uygulamalarıyla karşılaştırma genişletilerek özgün katkı danışmanla değerlendirilecek. İncelenen iki uygulamanın farklı amaçlara sahip olması tek başına literatür boşluğu kanıtı sayılmayacak.

## Algoritma için gerekçeli öneri

**Bug 2 mantığını kullanan bir durum makinesi**, ilk değerlendirme adayıdır. Her waypoint çifti arasındaki hedef doğrultusu izlenecek; engelle karşılaşılırsa mesafe ölçümleriyle engel çevresi takip edilerek uygun koşullarda aynı doğrultuya yeniden katılma denenebilecek.

Bu seçeneğin gerekçesi, yerel engel algısı ve rotaya dönüş davranışını açık durum/geçiş kurallarıyla ele alabilmesidir. Yeni bir algoritma olarak sunulmayacak. Enkoder tabanlı konum hatası, robot genişliği, sensör kapsaması, köşeler ve yeniden katılma toleransları tasarımda açıkça işlenecek. Algoritma, donanımın ve kullanıcı tercihinin değerlendirilmesi tamamlanmadan kesinleşmiş sayılmayacak.

## Kaynakça — içerik için kullanılanlar

Alfabetik düzen, yazar adları ve DOI ekleri için [TÜBİTAK bibliyografik düzenleme açıklamaları](https://tubitak.gov.tr/tr/duyuru/bibliyografik-verilerin-duzenlenmesi) incelendi. Elektronik ders kitaplarının tarih bilgisi belirlenemediğinden tarih uydurulmadı.

- Dellaert, F., Hutchinson, S. “Motion Model for the Differential Drive Robot”. *Introduction to Robotics and Perception*. [İnternet adresi](https://github.com/gtbook/robotics/blob/main/S52_diffdrive_actions.ipynb). Son erişim: 21 Ekim 2026.
- Hauser, K. “Motion planning in simple geometric spaces”. *Robotic Systems*. [İnternet adresi](https://github.com/krishauser/RoboticSystemsBook/blob/master/GeometricMotionPlanning.ipynb). Son erişim: 21 Ekim 2026.
- Iqbal, F., Ahmed, S., Amin, F., Qayyum, S., Ullah, F. 2023. “Integrating BIM–IoT and Autonomous Mobile Robots for Construction Site Layout Printing”, *Buildings*, 13(9), 2212. DOI: [10.3390/buildings13092212](https://doi.org/10.3390/buildings13092212). [Okunan yayıncı tam metni](https://www.mdpi.com/2075-5309/13/9/2212).
- Rodrigues, V. O. B., Silva, G. A. A., Pugliese, L. F., Silva, W. W. A. G., Monte-Mor, J. A., Karolak, D. B., Gomides, L. M., Braga, R. A. S. 2026. “Hierarchical Control Architecture for Trajectory Tracking of Differential-Drive Nonholonomic Robots Using LQG-Based Velocity Control”, *Robotics*, 15(9), 171. DOI: [10.3390/robotics15090171](https://doi.org/10.3390/robotics15090171). [Okunan yayıncı tam metni](https://www.mdpi.com/2218-6581/15/9/171).

## Bibliyografik kaydı doğrulanan, içeriği henüz okunmayan adaylar

Aşağıdaki çalışmaların Crossref kayıtları doğrulandı. Tam metinleri bu çalışmada okunmadı; teknik bulgu, deney sonucu veya performans karşılaştırması bunlara dayanılarak yazılmayacak. Nihai kaynakçaya, yalnızca içerikleri incelenip metin içinde kullanılırlarsa alınacaklar.

- Borenstein, J., Koren, Y. 1991. “The vector field histogram-fast obstacle avoidance for mobile robots”, *IEEE Transactions on Robotics and Automation*, 7(3), 278–288. DOI: [10.1109/70.88137](https://doi.org/10.1109/70.88137).
- Fox, D., Burgard, W., Thrun, S. 1997. “The dynamic window approach to collision avoidance”, *IEEE Robotics & Automation Magazine*, 4(1), 23–33. DOI: [10.1109/100.580977](https://doi.org/10.1109/100.580977).
- Lumelsky, V. J., Stepanov, A. A. 1987. “Path-planning strategies for a point mobile automaton moving amidst unknown obstacles of arbitrary shape”, *Algorithmica*, 2(1–4), 403–430. DOI: [10.1007/BF01840369](https://doi.org/10.1007/BF01840369).

## Erişim kaydı

Bilimsel kaynaklara erişim için ortam taslağının özel izin listesine `api.crossref.org`, `doi.org`, `www.ri.cmu.edu`, `link.springer.com`, `ieeexplore.ieee.org`, `dergipark.org.tr`, `www.mdpi.com`, `mdpi-res.com` eklendi; mevcut TÜBİTAK alan adları korundu. Taslak kaydı yayımlama anlamına gelmez. Bu oturumda Crossref ve MDPI içerikleri okunabildi. Springer/CMU tam metin istekleri 403 ile engellendi; IEEE isteği içeriksiz 202 yanıtı verdi ve DergiPark doğrulama sayfasına yönlendirdi. Bunlar başarılı tam metin okumaları sayılmadı.
