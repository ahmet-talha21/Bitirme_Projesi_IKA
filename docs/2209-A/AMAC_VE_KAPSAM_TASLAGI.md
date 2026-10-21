# Amaç ve kapsam — ilk çalışma taslağı

Durum: Kullanıcının ve danışmanın incelemesine açık çalışma taslağı. Nihai başvuru metni değildir. Kullanıcı 40 denemelik planı ve her engelli koşulda en az 8/10 birleşik görev başarısı hedefini uygun buldu. Teknik yöntem, araştırma sorusunun son biçimi ve diğer sayısal parametreler henüz kesinleşmedi.

## Başlık önerisi — henüz onaylanmadı

Kullanıcı Tanımlı Rota Takibi ve Engelden Kaçınma Özellikli Otonom Kara Aracının Geliştirilmesi

## Kullanıcının belirttiği kapsamdan oluşturulan amaç taslağı

Bu projenin amacı, kullanıcı tarafından belirlenen bir rotada ilerlerken sabit engelleri algılayıp çarpışmadan kaçınma hareketi gerçekleştirmesi ve ardından rotasına dönmesi hedeflenen mikrodenetleyici tabanlı bir kara aracı prototipi geliştirmek ve bu davranışın başarısını kontrollü deneylerle değerlendirmektir. Rota, kullanıcı arayüzünde ölçülü kareli alan üzerinde seçilen ara noktalarla tanımlanacaktır. Çalışma kapsamında kullanıcı arayüzü, araç kontrol yazılımı ve gerekli donanım birlikte tasarlanacak; engel yerleşimlerinin değiştirildiği deneylerde algılama, kaçınma ve rotaya dönüş performansı incelenecektir. Arayüzün tasarımı proje sahibi tarafından gerçekleştirilecek; konum takibi ve engelden kaçınma yaklaşımı teknik seçenekler değerlendirilerek belirlenecektir.

Kullanıcı arayüzünde bilgisayardan kullanım öncelikli olacak, telefondan erişim de hedeflenecektir. Prototipin küçük RC araç ölçeğinde ve düz zeminde kullanılması planlanmaktadır. İlk deneyler için yaklaşık 3 × 3 metre alan düşünülmektedir; alanın uygunluğu araç ölçüleri ve hareket kabiliyeti belirlendikten sonra değerlendirilecektir. İlk rota ekranı ölçülü ızgara olacak; ölçekli mekân krokisi sonraki aşamada isteğe bağlı olarak değerlendirilebilecektir.

Hareket altyapısı, iki motorun bağımsız kontrol edildiği ve tekerlek dönüşlerinin enkoderlerle ölçüldüğü bir şasi üzerine kurulacaktır. Motor, sürücü ve sensör modelleri ayrıca seçilecektir.

Henüz fiziksel geliştirme veya deney yapılmamıştır. Bu metin planlanan çalışmayı tanımlar.

## Araştırma sorusu adayı — kullanıcı ve literatür değerlendirmesi gerekiyor

Kullanıcı tanımlı waypoint rotalarını izleyen küçük ölçekli bir otonom kara aracında, sabit engellerin yerleşimi; engel algılama, çarpışmasız kaçınma ve rotaya yeniden katılma başarısını nasıl etkiler?

Bu soru bir öneridir. Sabit engeller ilk deney kapsamı olarak seçildi; hareketli engeller kapsamda değil. Deney koşulları, kontrol/kaçınma yöntemleri, karşılaştırma düzeni ve bağımsız referans ölçümü seçilmeden yöntem bölümü tamamlanmış sayılmaz.

## Hedeflerin çalışma taslağı

1. Bilgisayar öncelikli ve telefondan da erişilebilir bir arayüz üzerinden waypoint rotası tanımlanmasını sağlamak.
2. Küçük ölçekli kara aracında, belirlenen test koşullarındaki sabit engellerin temas öncesinde algılanmasını ve kaçınma hareketinin uygulanmasını sağlamak.
3. Kaçınma sonrasında tanımlı rotaya yeniden katılmayı ve hedefe ilerlemeyi sağlamak.
4. Engel yerleşimleri değiştirilerek tekrarlanacak denemelerde algılama, çarpışmasız kaçınma ve rotaya dönüş oranlarını; görev tamamlama süresini ve uygun referans ölçümüyle rota sapmasını değerlendirmek.

Kullanıcı [deney protokolündeki](DENEY_PROTOKOLU_ONERISI.md) şu tekrar planı ve ana başarı hedefini uygun buldu:

- Engelsiz referans ve üç sabit engel yerleşiminde koşul başına 10, toplam 40 geçerli değerlendirme denemesi yapmak.
- Engelli koşulların her birinde en az 8/10 denemede temas öncesi algılama, çarpışmasız kaçınma, rotaya dönüş ve süre içinde sıralı waypoint'ler/hedefe erişimi birlikte sağlamak.

Ek sayısal öneriler henüz kesinleşmedi:

- Engelsiz koşulda en az 9/10 görev tamamlama; engelli koşulların her birinde en az 9/10 temas öncesi algılama hedeflemek.
- 10 cm waypoint/rotaya dönüş bandını, 120 saniye süre sınırını ve bunların bağımsız ölçüm gereksinimlerini uygulanabilirlik incelemesiyle kararlaştırmak.

Bunlar gelecekteki çalışma için planlanan hedeflerdir; gerçekleşmiş performans veya kabul garantisi değildir. Seçilen iki karar korunarak kalan parametreler, donanım ve ölçüm düzeni netleştirilecek; danışman incelemesiyle amaç/hedefler metnine nihai biçimi verilecek.

## Bu metnin tamamlanması için gerekenler

- Yaklaşık 3 × 3 metre deney alanının fiziksel yerinin ve bilgisayar/telefon erişimi için uygulama teknolojisinin seçilmesi; alanın araç boyutlarına uygunluğunun kontrol edilmesi.
- Waypoint'lerin fiziksel alanla eşleştirilmesi ve aracın konumunu/yönünü belirleme yönteminin netleştirilmesi.
- Prototip geliştirme işini ölçülebilir bir araştırmaya dönüştürecek sorunun ve karşılaştırma düzeninin seçilmesi.
- Donanım, kontrol/kaçınma yöntemleri, bağımsız referans ölçümü ve kalan sayısal parametrelerin kararlaştırılması; seçilen tekrar planı ve ana hedefin uygulanabilirlik/danışman incelemesi.
- Kaynaklarla desteklenen gerekçe ve yöntem bölümlerinin yazılması; ardından amaç/hedefler metninin bu kararlara göre yeniden düzenlenmesi.

Bu aşamada her ortamda çalışma, özgün algoritma, belirli doğruluk oranı, belirli maliyet veya tamamlanmış deney iddiası bulunmuyor.
