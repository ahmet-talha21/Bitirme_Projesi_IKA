# 1.1. Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği — ilk taslak

Durum: Kullanıcının ve danışmanın incelemesine açık çalışma metni. Nihai TYBS metni değildir. Akademik ders kitabı bölümlerine ek olarak iki ilgili uygulama makalesi incelendi; karşılaştırmanın kapsamı [literatür notunda](LITERATUR_KARSILASTIRMASI.md) açıklanıyor. Özgün katkının daha geniş literatürde konumlandırılması henüz tamamlanmadı. Teknik seçimler ve deney planı kesinleştikçe metin yeniden düzenlenecek.

## Bölüm metni

Otonom kara araçlarında rota takibi, aracın konum ve yön bilgisinin hareket kontrolüyle birlikte değerlendirilmesini gerektirir. İki tekeri bağımsız sürülen mobil robotların kinematik modeli, tekerleklerin hareketi ile aracın doğrusal ve açısal hareketi arasındaki ilişkiyi tanımlar. Bu nedenle kullanıcı tarafından belirlenen bir rotanın fiziksel ortamda izlenmesi, yalnızca hareket komutlarının gönderilmesine değil, aracın yöneliminin ve hareketinin uygun biçimde izlenmesine de bağlıdır (Dellaert ve Hutchinson, t.y.). Rota üzerinde engel bulunması durumunda ise aracın engeli algılaması, çarpışmadan kaçınacak bir hareket üretmesi ve hedefe ilerleyişini sürdürebilmesi gerekir.

Hareket planlama literatüründe yerel engel bilgisini kullanan Bug türü yöntemler, önceden tüm engellerin haritası bilinmeden hedefe yönelik hareketin ele alınabildiği yaklaşımlar arasındadır. Bu yöntemlerin incelenmesinde robotun konumuna, engel geometrisine ve algılama biçimine ilişkin varsayımlar önem taşır. Ayrıca robotun fiziksel boyutlarının dikkate alınması, noktasal bir modelle bulunan yolun gerçek bir araçta uygulanabilirliğinin değerlendirilmesi açısından gereklidir (Hauser, t.y.-a).

İlgili uygulamalarda Iqbal vd. (2023), yapı modelinden çıkarılan koordinatların masaüstü uygulaması ve bulut bağlantısı üzerinden ESP32 tabanlı bir mobil robota aktarılmasıyla zemin çizimi gerçekleştiren bir sistem sunmuştur. Rodrigues vd. (2026) ise enkoderler, dış kamera temelli konum bilgisi ve ESP32 gömülü kontrol katmanını içeren küçük bir diferansiyel sürüşlü robotta yörünge takibini deneysel olarak değerlendirmiştir. Bu örnekler, koordinat aktarımı, konum bilgisi ve motor kontrolünün farklı mimarilerle bütünleştirilebildiğini göstermektedir. Önerilen projede ele alınacak değerlendirme görevi, kullanıcının tanımladığı rota üzerinde yerel algıyla engelden kaçınma ve rotaya yeniden katılmadır. Çalışmanın bilimsel çerçevesi, bu davranışın seçilen donanım ve sınırlı deney koşullarında hangi aşamalarda başarılı veya başarısız olduğunun tekrarlı ölçümlerle incelenmesine dayanmaktadır.

Bu projede ele alınacak problem, kullanıcı tarafından belirlenen waypoint rotasında ilerleyen mikrodenetleyici tabanlı bir kara aracının, farklı yerleşimlerdeki sabit engelleri algılayarak çarpışmasız kaçınma hareketi gerçekleştirmesi ve ardından rotasına yeniden katılmasıdır. Çalışma, düz zeminde yaklaşık 3 × 3 metre olarak planlanan kontrollü bir deney alanıyla sınırlandırılacaktır. Rota, bilgisayar öncelikli ve telefondan erişimi de hedeflenen kullanıcı arayüzündeki ölçülü kareli alan üzerinde tanımlanacaktır. Deneylerde engellerin yerleşimleri değiştirilecek; algılama, çarpışmasız kaçınma, rotaya dönüş ve görev tamamlama davranışları ayrı ayrı değerlendirilecektir.

Çalışmanın araştırma sorusu, “Sabit engellerin yerleşimi, kullanıcı tanımlı waypoint rotalarını izleyen küçük ölçekli bir kara aracında engel algılama, çarpışmasız kaçınma ve rotaya yeniden katılma başarısını nasıl etkiler?” biçiminde ele alınmaktadır. Geliştirilecek prototip üzerinde tekrarlanabilir deneyler gerçekleştirilmesi, başarılı ve başarısız durumların kaydedilmesi ve performansın ölçülebilir göstergelerle açıklanması amaçlanmaktadır. Kalibrasyon ve değerlendirmede güvenilir referans ölçümleri kullanılması, sensör çıktıları ile fiziksel hareket arasındaki ilişkinin incelenmesine dayanak sağlayacaktır (Hauser, t.y.-b). Bu kapsamda beklenen katkı; kullanıcı arayüzü, gömülü kontrol ve engelden kaçınma davranışının bütünleştirildiği bir prototip ile sınırları tanımlı deney koşullarına ait performans verilerinin oluşturulmasıdır.

## Bu taslakta kullanılan kaynaklar

Bu bölümün beş kaynağı ile yöntemde kullanılan Espressif dokümanı [tek alfabetik kaynakçada](KAYNAKCA_TASLAGI.md) birleştirildi. Metin içi atıf eşleştirmesi, erişim tarihleri ve doğrulanmış DOI'ler aynı dosyadadır. Ders kitabı bölümlerine doğrulanmamış yayın yılı veya DOI eklenmedi. Kaynak metinler veya görseller depoya kopyalanmadı; bölüm metni proje kapsamında özgün biçimde yazıldı.

## Tamamlanacak bilimsel gerekçe

- İlk karşılaştırmanın benzer engelden kaçınma çalışmalarına genişletilmesi; iki ilgili uygulama ile sınırlı incelemenin tamamlanmış sistematik tarama gibi sunulmaması.
- Bu karşılaştırma üzerinden projenin somut katkısının daraltılması; henüz doğrulanmamış “ilk”, “üstün”, “daha ucuz” veya “literatürde yok” iddiaları eklenmemesi.
- Kesinleşen algılama, konum kestirimi ve kaçınma yönteminin ilgili akademik çalışmalarla desteklenmesi.
- Kullanıcının seçtiği 40 deneme ve koşul başına en az 8/10 birleşik başarı hedefiyle uyum; kalan hata/süre toleransları ve bağımsız referans ölçüm yönteminin belirlenmesi.
- Araştırma sorusu ve bölüm metninin kullanıcı ile danışman görüşleri doğrultusunda son hâline getirilmesi.
