# Deney protokolü — sayısal plan önerisi

**Çalışma geçmişi:** Bu dosya önceki 0.5 önerisidir. Kullanıcının raporu tamamlama talebiyle sayısal yöntem güncellendi; uygulama ve danışman değerlendirmesi için [güncel araştırma önerisinin 2. bölümü](ARASTIRMA_ONERISI.md) esas alınacaktır.

Sürüm: 0.5 — 22 Ekim 2026. **Kullanıcı dört koşulda 10'ar tekrar, toplam 40 değerlendirme denemesini ve her engelli koşulda en az 8/10 birleşik otonom görev başarısı hedefini uygun buldu.** Kullanıcı ayrıca waypoint/hedef erişimi için 10 cm, rotaya dönüş bandı için 10 cm ve deneme başına 120 saniye sınırını planlanan hedefler olarak seçti. Bu seçimler diğer sayısal önerilerin veya tüm protokolün kesinleştiği anlamına gelmez. Sayılar yapılmış deney veya kanıtlanmış araç performansı değildir. Donanım seçimi, deney alanına erişim ve ölçüm uygulanabilirliği henüz tamamlanmadı. Danışman incelemesi ve kalan parametreler sonrasında, nihai değerlendirmeden önce protokol ve yazılım sürümü sabitlenecek.

## 1. Araştırma sorusu ve karşılaştırma

Sabit bir waypoint rotasında engelin bulunduğu bölüm, aracın temas öncesi algılama, çarpışmasız kaçınma, rotaya yeniden katılma ve görevi tamamlama başarısını nasıl etkiler?

Tek bir kaçınma yaklaşımının farklı engel yerleşimlerindeki davranışı değerlendirilecek. Engelsiz koşul rota takibinin referansıdır; engelden kaçınma yöntemleri arasında üstünlük karşılaştırması yapılmış sayılmaz. İki enkoderli motor ve beş sabit mesafe sensörü korunacak. Kullanıcının seçtiği Bug 2 mantığından yararlanan durum makinesi esas alınacak; sensör seçiminde ToF taşıyıcıları önceliklendirilecek. Kesin taşıyıcı/model ve uygulama parametreleri henüz seçilmedi. Deneyler, seçilen altı aylık planda kaçınma entegrasyonundan sonra 6. ayda yürütülecek.

## 2. Alan ve rota geometrisi önerisi

- Alan: yaklaşık **3 × 3 m**, düz ve kuru zemin; fiziksel yer ve erişim henüz doğrulanmadı.
- Yerel koordinatlar metre biriminde tanımlanacak; aynı köşe `(0, 0)` başlangıç referansı olacak.
- Önerilen L biçimli rota: **A = (0,75; 0,75) → B = (2,25; 0,75) → C = (2,25; 2,25)**. Noktalı virgül, x ve y bileşenlerini ayırır. Toplam referans yol uzunluğu **3,00 m**'dir. Başlangıç yönü A'dan B'ye doğrudur.
- Başlangıç ve rota, tekerlek temas noktaları yerine önceden tanımlanacak araç referans noktasına göre kurulacak. Görüntüde izlenen işaretin bu noktaya göre ofseti ölçülecek.
- Engelli koşullarda aynı **tek, opak, mat yüzeyli dikdörtgen prizma** kullanılacak. Başlangıç boyut önerisi **30 × 30 cm taban, 30 cm yükseklik**; sensör yüksekliği ve algılama kontrolünden sonra kesinleştirilecek.
- Araç dış ölçüleri, dönüşte kapladığı alan, sensörlerin konumu ve gerekli açıklıklar bilinmeden bu yerleşimin uygulanabilir olduğu kabul edilmeyecek. Engel, waypoint'i veya gerekli geçişi kapatmayacak; sınırlar ve serbest yol, aracın tüm gövdesi dikkate alınarak kontrol edilecek.

| Koşul | Engel durumu / merkez koordinatı | Amaç | Seçilen geçerli tekrar |
| --- | --- | --- | --- |
| K0 | Engel yok. | Temel rota takibi, süre ve yanlış engel uyarılarını görmek. | 10 |
| K1 | İlk düz parçada `(1,40; 0,75)`. | Düz bölümde algılama, kaçınma ve aynı parçaya dönüşü incelemek. | 10 |
| K2 | Dönüş öncesinde `(1,75; 0,75)`. | B waypoint'ine yaklaşırken kaçınma ve sonrasında dönüşü incelemek. | 10 |
| K3 | Dönüşten sonraki parçada `(2,25; 1,50)`. | İkinci parçada kaçınma ve rotaya dönüşü incelemek. | 10 |

Bu koordinatlar alanı hazırlamak için öneridir; nihai şasiyle geometrik kontrol yapılacak. Engel boyutu, sayısı ve malzemesi K1–K3 arasında değiştirilmeyecek. Böylece temel değişken engel yerleşimi olacak. Daha karmaşık şekiller, hareketli engeller ve dar/kapalı geçitler bu ilk deney grubuna eklenmedi.

## 3. Ayar denemeleri ve son değerlendirme

Önce motor/enkoder ölçeği, sensör kapsaması, dönüşler, frenleme ve kamera ölçümü için geliştirme denemeleri yapılacak. Bunlar aşağıdaki **40 geçerli değerlendirme denemesine dahil edilmeyecek**. Alan yeterli olmazsa geometri, gerekçesiyle birlikte son değerlendirme başlamadan değiştirilecek.

Önerilen uygulama, **10 blok × 4 koşul** biçimindedir. Her blokta K0, K1, K2 ve K3 birer kez, sırası önceden rastgeleleştirilerek uygulanacak. Böylece tüm engelli koşulların pilin yalnızca başlangıç veya bitiş durumuna denk gelmesi azaltılacak. Koşulların sırası, pil gerilimi, zemin, aydınlatma ve önemli değişiklikler kaydedilecek. Çalışma aralığı dışındaki pil geriliminde deneme başlatılmayacak; gerilim sınırları seçilen paketin belgesi ve besleme testleriyle belirlenecek.

Son değerlendirmede algoritma, rota, hız hedefi, sensör eşikleri ve yazılım sürümü koşullar arasında değiştirilmeyecek. Değişiklik gerekirse eski kayıtlar korunacak, yeni sürüm açıkça ayrılacak ve karşılaştırılan koşullar yeni sürümle tamamlanacak. Başarısızlığı gördükten sonra kabul eşiği veya deney koşulu gevşetilmeyecek.

## 4. Seçilen hedefler ve ek sayısal öneriler

| Parametre / ölçüt | Planlanan değer | Gerekçe ve sınırlama |
| --- | --- | --- |
| İlerleme hızı hedefi | **0,10 m/s**; dönüş ve kaçınmada daha düşük hız kullanılabilecek. | Küçük alanda gözlem ve kontrol için başlangıç ayarı. Seçilen motorların bu hızda kararlı çalıştığı henüz gösterilmedi. |
| Waypoint/hedefe erişim toleransı | Araç referans noktasının sıradaki noktaya Öklid uzaklığı **en çok 10 cm**. | Kullanıcı tarafından planlanan hedef olarak seçildi. Literatürden alınmış veya ölçülmüş doğruluk değildir. Noktalar A–B–C sırasıyla değerlendirilecek. |
| Son hedefte durma süresi | Son hedef bandında **2 saniye** durmuş olma önerisi. | Bu süre henüz seçilmedi; 10 cm erişim toleransının seçilmesi 2 saniyelik süreyi onaylamaz. |
| Rotaya yeniden katılma bandı | Aktif sonlu rota parçasına uzaklık **en çok 10 cm**. | Kullanıcı tarafından planlanan hedef olarak seçildi. Engel geride bırakılmış, gövde için geçiş açık ve hedefe uzaklık kaçınma başlangıcına göre azalmış olacak. Yalnızca çizgi kesişimi yeterli olmayacak. |
| Rotaya dönüşün süre/ilerleme kontrolü | Bantta **en az 1 saniye** kalma ve hedef yönünde **en az 10 cm** ilerleme önerisi. | Bu iki ek değer henüz seçilmedi. İlerleme mesafesi, seçilmiş olan 10 cm enine dönüş bandından farklı bir parametredir. |
| Deneme süre sınırı | Hareket başlangıcından görevin tamamlanmasına kadar **en çok 120 saniye**. | Kullanıcı tarafından planlanan hedef olarak seçildi. Önerilen 3 m rota ve 0,10 m/s hız için ideal düz ilerleme hesabı 30 saniyedir; hız ve gerçek tamamlama süresi doğrulanmış değildir. |
| Engelsiz görev başarısı | K0'da **en az 9/10** geçerli denemede sıralı waypoint'ler ve son hedef tamamlanacak. | Temel rota takibinin ayrı değerlendirilmesini sağlar. |
| Temas öncesi engel algılama | K1, K2 ve K3'ün **her birinde en az 9/10** geçerli denemede. | Bir yerleşimdeki düşük performansın toplam oran içinde gizlenmemesi amaçlanır. |
| Birleşik otonom görev başarısı | K1, K2 ve K3'ün **her birinde en az 8/10** geçerli denemede: temas öncesi algılama **ve** çarpışmasız kaçınma **ve** rotaya dönüş **ve** süre içinde sıralı waypoint'ler ve hedefe varış. | Kullanıcı bu ana hedefi uygun buldu. En az 24/30 engelli denemeye karşılık gelir; yalnız toplam 24/30 olması koşul başına hedefi karşılamaya yetmez. Algılama ve kaçınma aşamaları ayrıca raporlanacak. |
| Bağımsız konum ölçümü kontrolü | Değerlendirmede kullanılan alanı kapsayan, dönüşüm hesabında kullanılmamış kontrol noktalarında mutlak konum hatası hedefi **en çok 2 cm**. | 10 cm kabul bandına göre beşte bir kontrol hedefidir; sağlandığı henüz bilinmiyor. Tek başına tüm hareketli ölçümlerin belirsizliğini kanıtlamaz. |

40 denemelik tekrar planı, her engelli koşulda en az 8/10 birleşik başarı hedefi, 10 cm waypoint/hedef erişimi, 10 cm rotaya dönüş bandı ve 120 saniye deneme sınırı kullanıcı tarafından seçildi. Hız, 9/10 ek hedefleri, son hedefte 2 saniye durma, bantta 1 saniye kalma, 10 cm ileri hareket ve 2 cm bağımsız ölçüm kontrol değeri öneri durumunda. Tüm planın uygulanabilirliği ve danışman değerlendirmesi başvurudan önce tamamlanacak; bunlar kabul garantisi veya istatistiksel güç hesabı değildir. Kalibrasyonla seçilecek algılama/durma mesafesi, yan açıklık, örnekleme aralığı ve zaman eşleme doğruluğu ayrıca sayısallaştırılacak; şimdilik doğrulanmamış değer yazılmadı.

Algılama eşiğinde sensörün gövdeye göre konumu, toplam algılama/karar gecikmesindeki ilerleme, ölçülmüş durma mesafesi ve açıklık payı birlikte dikkate alınacak. Sensörün kendi referansından verdiği mesafe doğrudan araç gövdesinin açıklığı sayılmayacak.

## 5. Başarı ve başarısızlık kayıtları

1. **Algılama:** Sensör/durum kaydında, herhangi bir temastan önce engel olayı var mı? K0'da bu olaylar yanlış uyarı olarak ayrıca sayılacak; engel algılama başarı paydasına K0 eklenmeyecek.
2. **Çarpışmasız kaçınma:** Araç gövdesi ve tekerlekleri engele temas etmeden engeli geride bırakıp açık ilerleme alanına ulaşabildi mi? Engel yüzeyinin geride kalması ve tüm gövdenin açıklığı kamera kaydıyla kontrol edilecek. Yalnızca engel önünde durma başarılı kaçınma sayılmayacak.
3. **Rotaya dönüş:** Yukarıdaki mesafe, süre, ilerleme ve hedefe yaklaşma koşulları bağımsız referansla sağlandı mı? Aracın kendi yazılımındaki “rotaya döndüm” durumu tek başına kanıt olmayacak.
4. **Görev:** Önceki aşamalar ve sıralı waypoint'ler tamamlandıktan sonra son hedef toleransı süre sınırı içinde sağlandı mı? İnsan müdahalesiyle devam edilen deneme otonom başarı sayılmayacak.

Çarpışma, alan dışına çıkma, denetleyici yeniden başlatması, ilerleyememe ve süre aşımı gerçekleşirse nedeni kaydedilecek ve deneme başarısız olarak paydada tutulacak. Önceki bir aşama sağlanmadığı için sonraki aşama gerçekleşmezse sonraki aşama da başarı sayılmayacak; olay kayıtlarında “ulaşılamadı” olarak açıklanabilecek.

Her koşul için payda **o koşuldaki tüm geçerli denemeler** olacak; örneğin rotaya dönüş oranı yalnız başarılı kaçınmalar üzerinden hesaplanmayacak. Bilinen araç başarısızlığı, eşzamanlı kayıt kaybı olduğu için veri setinden çıkarılmayacak. Yalnız önceden tanımlanan ve araç davranışından bağımsız düzeneğe/kayda ilişkin nedenlerle değerlendirilemeyen denemeler geçersiz olarak ayrılabilecek. Bu nedenler, yerine yapılan denemeler ve toplam başlatılan deneme sayısı raporda gösterilecek; sonuç belirsizse başarılı yazılmayacak.

## 6. Bağımsız görüntü ölçümü ve kayıt

**Sonlu parça üzerinden hata:** Değerlendirme tarafındaki aktif rota parçası, sıralı waypoint'lere görüntüyle doğrulanan erişime göre seçilecek. Araç referans noktası $P$, parça uçları $A$ ve $B$ için $u=((P-A)\cdot(B-A))/\lVert B-A\rVert^2$ hesaplanıp $[0,1]$ aralığına sınırlandırılacak; $Q=A+\operatorname{clip}(u,0,1)(B-A)$ ve $e=\lVert P-Q\rVert$ kullanılacak. Böylece rota parçasının ilerisindeki/gerisindeki bir konum, yalnız sonsuz doğruya yakın olduğu için doğru izleme sayılmayacak. Aynı noktanın iki kez girilmesiyle oluşan sıfır uzunluklu parça rota yüklenirken reddedilecek.

Kaçınma sırasında etkin hedef ve yüklenen waypoint sırası korunacak. Geri katılımda hedefe yaklaşma, engelin geride kalması ve açık geçiş de aranacak. Kayıtlardaki tek bir çizgi kesişimi yeterli olmayacak. Enkoder tabanlı kontrol kararı ile görüntüden verilen değerlendirme kararı ayrı kaydedilecek; uyuşmazlıklar ayrıca incelenecek.

Kullanıcının mevcut telefonu sabit görüntü kaydı için kullanılabilecek; tüm alanı kesintisiz gören yerleşim, sabitleme ve uygun görüntü kalitesi henüz doğrulanmadı. Kamera, son değerlendirmede kontrolcüye konum geri bildirimi vermeyen bağımsız ölçüm aracı olarak öneriliyor. Bu tercih değişirse yöntem ve bağımsız doğrulama yeniden tanımlanacak.

Alan üzerindeki ölçülmüş referanslarla görüntü–metre dönüşümü kurulacak. Lens bozulması ve araç üzerindeki izleme işaretinin yerden yüksekliğine bağlı perspektif hatası kontrol edilecek; yalnızca zemin köşeleriyle yapılan dönüşümün yüksek bir işaret için doğru olduğu varsayılmayacak. Dönüşümde kullanılmayan kontrol noktalarıyla hata ölçülecek. Kalibrasyon noktaları ve kontrol noktaları karıştırılmayacak.

Kayıt başlatıldıktan sonra görüntü ve araç günlüğünde görülen ortak bir başlangıç olayıyla zaman eşlemesi yapılacak; eşleme hatası ölçülecek. Görüntüde konumun izlenemediği aralıklar ve veri kapsamı açıklanacak. İstenen ölçüm doğruluğu sağlanamazsa risk planındaki alternatif ölçüm düzeni, başvurudan önce somutlaştırılacak; sürekli yörünge ölçülmüş gibi sonuç yazılmayacak.

Engelsiz ve kaçınma dışındaki rota izleme bölümleri için sonlu referans rota parçalarına uzaklık değerlendirilecek. Kaçınma aralığı, engel olayından başlayıp bağımsız ölçümle doğrulanmış rotaya dönüşe kadar tanımlanacak; yazılımın durum etiketi tek başına aralık seçmeye yetmeyecek. Kaçınmanın gerektirdiği geçici rota sapması ayrıca gösterilecek. Rotaya hiç dönülemeyen deneme için rota izleme hatası tek başına başarı göstergesi yapılmayacak.

## 7. Analiz ve veri dosyaları

- Her koşul için geçerli/başlatılan deneme sayıları, algılama, kaçınma, rotaya dönüş ve birleşik görev sonuçları **başarılı adet / payda ve yüzde** olarak verilecek.
- Süre, yol uzunluğu ve rota hatası için veri kapsamı belirtilerek özetler hazırlanacak. Tamamlanan denemelerin süreleri medyan ve en küçük–en büyük değerle verilebilecek; tamamlanmayan denemeler ve süre aşımları ayrıca gösterilecek. Bu özet yalnızca tamamlanan denemeler içinse açıkça yazılacak.
- Rota hatası için uygun kapsamda karesel ortalama kök hata (RMSE) ve en büyük sapma değerlendirilecek. Eksik görüntü aralıkları açıklanacak; yalnız seçilmiş iyi bölümler genel başarı gibi sunulmayacak.
- K1–K3 karşılaştırması bu koşullardaki gözlenen davranışı tanımlayacak. Bu tekrar planından bütün ortamlara başarı veya istatistiksel anlamlılık sonucu çıkarılmayacak.

[Boş deneme kayıt şablonu](DENEY_KAYIT_SABLONU.csv) sonuç satırları olmadan hazırlanmıştır. Dosya özet kaydı içindir; zaman damgalı ham sensör/konum verileri ve görüntüler ayrı dosyalarda, deneme kimliğiyle ilişkilendirilecek. Şablonda boş hücre, sıfır veya başarısızlık anlamına gelmez. `1/0` sonuç alanları yalnız gerçek gözlemden sonra doldurulacak; K0'ın engel aşamalarına `uygulanmaz` yazılabilecek. Birleşik görev alanı ise her geçerli deneme için değerlendirilecek.

## Kesinleştirme için açık bilgiler

1. Kullanıcı deney yerinin henüz belli olmadığını bildirdi. Yer/erişim seçilecek ve telefonun tüm alanı sabit görebilmesi kontrol edilecek.
2. Nihai gövde ölçüleri, engel ve sensör geometrisi; önerilen parkurda serbest yolun doğrulanması.
3. Seçilen Bug 2 uyarlamasının uygulama parametreleri, başlangıç/rotaya dönüş kuralları ve bağlantı/sensör hatası davranışı.
4. Seçilen tekrar planı ve ana hedefin danışman incelemesi; kalan sayısal önerilerin değerlendirilmesi, kalibrasyona bağlı eksik parametreler ve resmî takvimle uyum.

Yöntemin literatür dayanağı [yöntem taslağı](YONTEM_TASLAGI.md) ve [literatür karşılaştırmasında](LITERATUR_KARSILASTIRMASI.md) kayıtlıdır. Buradaki koşullar ve sayısal eşikler bu proje için tasarım önerisidir; anılan kaynakların elde ettiği sonuçlar olarak sunulmaz.
