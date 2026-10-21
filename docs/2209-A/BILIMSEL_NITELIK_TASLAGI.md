# 1.1. Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği — ilk taslak

Durum: Kullanıcının ve danışmanın incelemesine açık ilk metin. Nihai TYBS metni değildir. Temel açıklamalar, aşağıda listelenen ve okunmuş akademik ders kitabı bölümlerine dayanıyor. Benzer deneysel çalışmalarla karşılaştırma ve özgün katkının literatürde konumlandırılması henüz tamamlanmadı. Teknik seçimler ve deney planı kesinleştikçe metin yeniden düzenlenecek.

## Bölüm metni

Otonom kara araçlarında rota takibi, aracın konum ve yön bilgisinin hareket kontrolüyle birlikte değerlendirilmesini gerektirir. İki tekeri bağımsız sürülen mobil robotların kinematik modeli, tekerleklerin hareketi ile aracın doğrusal ve açısal hareketi arasındaki ilişkiyi tanımlar. Bu nedenle kullanıcı tarafından belirlenen bir rotanın fiziksel ortamda izlenmesi, yalnızca hareket komutlarının gönderilmesine değil, aracın yöneliminin ve hareketinin uygun biçimde izlenmesine de bağlıdır (Dellaert ve Hutchinson, t.y.). Rota üzerinde engel bulunması durumunda ise aracın engeli algılaması, çarpışmadan kaçınacak bir hareket üretmesi ve hedefe ilerleyişini sürdürebilmesi gerekir.

Hareket planlama literatüründe yerel engel bilgisini kullanan Bug türü yöntemler, önceden tüm engellerin haritası bilinmeden hedefe yönelik hareketin ele alınabildiği yaklaşımlar arasındadır. Bu yöntemlerin incelenmesinde robotun konumuna, engel geometrisine ve algılama biçimine ilişkin varsayımlar önem taşır. Ayrıca robotun fiziksel boyutlarının dikkate alınması, noktasal bir modelle bulunan yolun gerçek bir araçta uygulanabilirliğinin değerlendirilmesi açısından gereklidir (Hauser, t.y.-a). Küçük ölçekli bir prototipte bu çerçeve, seçilen sensör düzeni, konum kestirimi ve kaçınma davranışının birlikte sınanmasını gerektiren somut bir tasarım ve ölçüm problemi oluşturmaktadır.

Bu projede ele alınacak problem, kullanıcı tarafından belirlenen waypoint rotasında ilerleyen mikrodenetleyici tabanlı bir kara aracının, farklı yerleşimlerdeki sabit engelleri algılayarak çarpışmasız kaçınma hareketi gerçekleştirmesi ve ardından rotasına yeniden katılmasıdır. Çalışma, düz zeminde yaklaşık 3 × 3 metre olarak planlanan kontrollü bir deney alanıyla sınırlandırılacaktır. Rota, bilgisayar öncelikli ve telefondan erişimi de hedeflenen kullanıcı arayüzündeki ölçülü kareli alan üzerinde tanımlanacaktır. Deneylerde engellerin yerleşimleri değiştirilecek; algılama, çarpışmasız kaçınma, rotaya dönüş ve görev tamamlama davranışları ayrı ayrı değerlendirilecektir.

Çalışmanın araştırma sorusu, “Sabit engellerin yerleşimi, kullanıcı tanımlı waypoint rotalarını izleyen küçük ölçekli bir kara aracında engel algılama, çarpışmasız kaçınma ve rotaya yeniden katılma başarısını nasıl etkiler?” biçiminde ele alınmaktadır. Geliştirilecek prototip üzerinde tekrarlanabilir deneyler gerçekleştirilmesi, başarılı ve başarısız durumların kaydedilmesi ve performansın ölçülebilir göstergelerle açıklanması amaçlanmaktadır. Kalibrasyon ve değerlendirmede güvenilir referans ölçümleri kullanılması, sensör çıktıları ile fiziksel hareket arasındaki ilişkinin incelenmesine dayanak sağlayacaktır (Hauser, t.y.-b). Bu kapsamda beklenen katkı; kullanıcı arayüzü, gömülü kontrol ve engelden kaçınma davranışının bütünleştirildiği bir prototip ile sınırları tanımlı deney koşullarına ait performans verilerinin oluşturulmasıdır.

## Bu taslakta kullanılan kaynaklar

1. Dellaert, F. ve Hutchinson, S. (t.y.). “Motion Model for the Differential Drive Robot.” *Introduction to Robotics and Perception*, Bölüm 5.2. [Yazarların kaynak deposundaki bölüm](https://github.com/gtbook/robotics/blob/main/S52_diffdrive_actions.ipynb). Erişim: 21 Ekim 2026.
2. Hauser, K. (t.y.-a). “Motion planning in simple geometric spaces.” *Robotic Systems*, Bölüm 9. [Yazarın kaynak deposundaki bölüm](https://github.com/krishauser/RoboticSystemsBook/blob/master/GeometricMotionPlanning.ipynb). Erişim: 21 Ekim 2026.
3. Hauser, K. (t.y.-b). “Calibration.” *Robotic Systems*, Bölüm 22. [Yazarın kaynak deposundaki bölüm](https://github.com/krishauser/RoboticSystemsBook/blob/master/Calibration.ipynb). Erişim: 21 Ekim 2026.

Bu elektronik ders kitabı bölümlerinin incelenen sayfalarında kesin yayın tarihi ve DOI bilgisi belirlenmedi; yıl veya DOI uydurulmadı. Kaynakların nihai bibliyografik biçimi başvuru öncesinde TÜBİTAK yönergesiyle yeniden kontrol edilecek. Kaynak metinler veya görseller depoya kopyalanmadı; bölüm metni proje kapsamında özgün biçimde yazıldı.

## Tamamlanacak bilimsel gerekçe

- Benzer küçük ölçekli araç ve engelden kaçınma çalışmalarının yöntem, donanım ve deney ölçütleri açısından karşılaştırılması.
- Bu karşılaştırma üzerinden projenin somut katkısının daraltılması; henüz doğrulanmamış “ilk”, “üstün”, “daha ucuz” veya “literatürde yok” iddiaları eklenmemesi.
- Kesinleşen algılama, konum kestirimi ve kaçınma yönteminin ilgili akademik çalışmalarla desteklenmesi.
- Deney sayılarının, başarı tanımlarının, hata toleranslarının ve referans ölçüm yönteminin belirlenmesi.
- Araştırma sorusu ve bölüm metninin kullanıcı ile danışman görüşleri doğrultusunda son hâline getirilmesi.
