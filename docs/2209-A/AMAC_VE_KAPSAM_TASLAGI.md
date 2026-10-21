# Amaç ve kapsam — ilk çalışma taslağı

Durum: Kullanıcının incelemesine açık çalışma taslağı. Nihai başvuru metni değildir. Temel işlev ve sabit engelli deney kapsamı belirlendi; teknik yöntem, araştırma sorusunun son biçimi ve sayısal başarı eşikleri henüz seçilmemiştir.

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

Başarı tanımları, kabul edilecek rota sapması, deneme sayıları ve sayısal hedefler henüz kararlaştırılmadı. Bu liste, nihai ölçülebilir hedefler bölümünün yerine geçmez.

## Bu metnin tamamlanması için gerekenler

- Yaklaşık 3 × 3 metre deney alanının fiziksel yerinin ve bilgisayar/telefon erişimi için uygulama teknolojisinin seçilmesi; alanın araç boyutlarına uygunluğunun kontrol edilmesi.
- Waypoint'lerin fiziksel alanla eşleştirilmesi ve aracın konumunu/yönünü belirleme yönteminin netleştirilmesi.
- Prototip geliştirme işini ölçülebilir bir araştırmaya dönüştürecek sorunun ve karşılaştırma düzeninin seçilmesi.
- Donanım, kontrol/kaçınma yöntemleri, bağımsız referans ölçümü, tekrar sayıları ve sayısal başarı hedeflerinin kararlaştırılması.
- Kaynaklarla desteklenen gerekçe ve yöntem bölümlerinin yazılması; ardından amaç/hedefler metninin bu kararlara göre yeniden düzenlenmesi.

Bu aşamada her ortamda çalışma, özgün algoritma, belirli doğruluk oranı, belirli maliyet veya tamamlanmış deney iddiası bulunmuyor.
