# Motor, sürücü ve batarya — teknik seçim önerisi

Kontrol tarihi: 21 Ekim 2026. Ürün sayfaları ve ilgili üretici belgesi incelendi. Bu belge önerilen eşleşmeyi somutlaştırır; kullanıcı tarafından onaylanmış ürün modellerini veya çalıştırılmış bir prototipi anlatmaz. Seçili mimari iki enkoderli motor ve beş sabit mesafe sensörüdür.

## Motor için somut referans

Ana aday, **iki adet Pololu #5143: 210:1 Micro Metal Gearmotor MP 6V with 12 CPR Encoder, Side Connector** veya aynı gereksinimleri belgelenmiş biçimde karşılayan bir üründür. Bu ürün, önceki yaklaşık 100 d/d ve düşük akım arama ölçütünü somutlaştırıyor. Yerel bir N20 motor yalnızca aynı boyutta göründüğü için eşdeğer kabul edilmeyecek.

| Üreticinin 6 V için verdiği özellik | Ana aday: Pololu #5143 | Alternatif: Pololu #5115 |
| --- | --- | --- |
| Motor / redüksiyon | MP, 210,59:1 | LP, 150,58:1 |
| Boşta çıkış hızı | 100 d/d | 90 d/d |
| Boşta akım | 0,07 A | 0,04 A |
| Teorik sıkışma akımı | 0,67 A | 0,36 A |
| Teorik sıkışma torku | 1,7 kg·cm | 1,1 kg·cm |
| Enkoder | Motor milinde 12 CPR, iki kanalın iki kenarı birlikte sayıldığında | Aynı sayım tanımı |
| Çıkış mili | 3 mm D profil | 3 mm D profil |
| Motor gövde ölçüsü / kütlesi | 10 × 12 × 32 mm / 11 g; mil ve enkoder taşmaları ayrıca kontrol edilecek | Aynı nominal gövde ölçüsü / kütlesi |
| Sayfadaki tek adet fiyatı | 29,95 USD | 29,95 USD |

Kaynaklar: [#5143 özellikleri](https://www.pololu.com/product/5143/specs), [#5115 özellikleri](https://www.pololu.com/product/5115/specs), [üretici veri sayfası, Şubat 2026, Rev 6.2](https://www.pololu.com/file/0J1487/pololu-micro-metal-gearmotors-rev-6-2.pdf). İlgili motor tablosu ve enkoder açıklaması okundu. Sıkışma değerleri teoriktir; sürekli çalışma torku veya yapılmış proje deneyi olarak kullanılmayacak. Boşta hız, yük altındaki araç hızı değildir.

MP adayı, LP alternatifine göre daha yüksek teorik torkla aynı yaklaşık hız sınıfını sunuyor; akım gereksinimi de daha yüksek. Şasi ve batarya dahil toplam kütle belirlenince yük/tork gereksinimi kontrol edilecek. Bu aşamada aracın gerçek kütlesi veya taşıma kapasitesi belirlenmiş değildir.

Üretici, enkoder için 2,7–18 V besleme ve Vcc'ye çekilen A/B çıkışlarını açıklıyor. Referans motorda enkoder Vcc'si 3,3 V seçilerek ESP32 ile uygun sinyal seviyeleri kurulabilir. Motor beslemesi ayrı uçlardadır. #5143 için çıkış mili başına yaklaşık sayım `12 × 210,59 ≈ 2527` olur; 12 CPR zaten iki kanalın iki kenarını içerdiğinden yeniden dörtle çarpılmayacak. Sayım çözünürlüğü gerçek konum doğruluğu olarak sunulmayacak.

## Sürücüyle elektriksel eşleşme

TB6612FNG çift kanallı sürücü adayı korunuyor. Referans alınan [Pololu #713 taşıyıcısı](https://www.pololu.com/product/713), motor beslemesi için 4,5–13,5 V önerilen aralık, mantık beslemesi için 2,7–5,5 V ve kanal başına 1 A sürekli akım bildiriyor. Bu taşıyıcının 3 A tepe değeri sürekli akım değildir. Daha önce incelenen SparkFun kartının 1,2 A sürekli değeri bu farklı taşıyıcıya aktarılmayacak.

- 3,3 V mantık beslemesi, ESP32 bağlantısı için referans taşıyıcının aralığındadır.
- #5143'ün 6 V'taki 0,67 A teorik sıkışma akımı, referans taşıyıcının kanal başına 1 A sürekli değerinden düşüktür. Bu karşılaştırma ilk elektriksel seçim için dayanak sağlar; ürün toleransları, ısıl davranış ve gerçek yük testi gereğini ortadan kaldırmaz.
- Her motor ayrı kanala bağlanacak. İki motorun toplam akımı güç kaynağı hesabına ayrıca alınacak.
- Yerel TB6612FNG modüllerinin fiyatları bulundu. Gerçek kartın besleme, bağlantı ve ısıl kapasitesi kontrol edilecek; aynı çip adı taşıyıcıların aynı sürekli akımı sağladığını kanıtlamaz.

## Batarya ve regülasyon

Başlangıç güç önerisi, hazır **2S paket**, uygun şarj çözümü, regüle **5 V güç dalı** ve **3,3 V sensör/mantık dalıdır**. Bataryanın ham çıkışı doğrudan 6 V motora veya ESP32'ye bağlanmayacak.

Motorun 5 V ile sürülmesi, üreticinin nominal gerilimin altında çalışma açıklamasıyla uyumlu bir tasarım seçeneğidir. Ancak tablodaki 6 V hız/tork değerlerinin 5 V'ta aynen sağlanacağı varsayılmayacak. Gerçek yük belirlendiğinde kontrol edilecek; yetersizse motor/redüksiyon veya ayrı regüle motor beslemesi birlikte yeniden değerlendirilecek. İki motorun 6 V'taki teorik sıkışma akımlarının toplamı `2 × 0,67 = 1,34 A`dır; bu değer batarya akımı, normal tüketim veya 5 V'ta ölçülmüş akım değildir. Nihai güç hesabı elektronik tüketimini, regülatör verimini ve geçici yükleri de içerecek.

Yerelde **Power-Xtra 7,4 V 2S1P 1000 mAh (15C)** paketine ait fiyat ve fiziksel bilgiler bulundu: satıcı 64 g ve 19 × 31 × 56 mm bildiriyor. Bu değerler [satıcı sayfasından](https://www.direnc.net/74v-2s1p-1000-mah-15c-li-polymer-pil-soketli) alındı; bataryanın üretici veri sayfası henüz incelenmedi. Sayfa koruma devresi bulunduğunu doğrulamadığı için ürün, mevcut listedeki “hazır korumalı paket” koşulunu karşılamış sayılmayacak. Paket koruması veya uygun ayrı koruma/kesme düzeni netleştirilecek.

2S/3S LiPo için listelenen A3 şarj cihazı da fiyat adayı olarak incelendi. Hücre sayısının eşleşmesi tek başına tamamlanmış şarj uyumu değildir: bataryanın izin verilen şarj akımı, dengeleme bağlantısı, soket ve cihazın çıkış özellikleri kontrol edilecek. Batarya ve şarj cihazı henüz kesin ürün seçimi değildir. Kapasiteden çalışma süresi tahmini yapılmadı.

## Bulunan fiyatlar ve tedarik durumu

Fiyatlar sayfa gözlemidir; teklif/rezervasyon veya satın alma işlemi değildir. USD tutarlar TL'ye çevrilmedi; kur, kargo ve ithalat giderleri doğrulanmadan başvuru bütçesine aktarılmayacak.

| Gözlenen ürün | Birim fiyat ve kapsam | Sayfadaki stok bilgisi | Seçime etkisi |
| --- | --- | --- | --- |
| [Pololu #5143 motor](https://www.pololu.com/product/5143/specs) | 29,95 USD; Türkiye teslim giderleri doğrulanmadı. | Yapılandırılmış veride InStock; ayrılan miktar yok. | Ana teknik referans; yerel temin/toplam teslim maliyeti açık. İki adet gerekli. |
| [Pololu #5115 motor](https://www.pololu.com/product/5115/specs) | 29,95 USD; aynı kapsam. | Yapılandırılmış veride InStock. | LP alternatif; iki motor seçeneği birlikte toplanmayacak. |
| [Pololu #713 TB6612FNG](https://www.pololu.com/product/713) | 4,95 USD; aynı kapsam. | Yapılandırılmış veride InStock. | Elektriksel kontrol için referans taşıyıcı. |
| [Pololu #4763 motor/enkoder kablosu](https://www.pololu.com/product/4763) | 3,00 USD/adet; aynı kapsam. | Yapılandırılmış veride InStock. | Motorlara dahil değil; referans motorlarla iki adet gerekli. |
| [Direnc.net TB6612FNG, 21228](https://www.direnc.net/tb6612fng-dc-ve-step-motor-surucu-modulu) | **81,36 TL KDV dahil**; KDV hariç 67,80 TL. | Yapılandırılmış veride InStock. | Yerel fiyat adayı; gerçek taşıyıcı kontrolü açık. |
| [Direnc.net JGA12-N20B 6 V 300 d/d, DSTK22429](https://www.direnc.net/6v-300rpm-enkoderli-motor) | **406,82 TL KDV dahil**; KDV hariç 339,02 TL. | Yapılandırılmış veride InStock. | Sıkışma akımı ve enkoder elektriksel bilgisi eksik. Uygun eşdeğer sayılmadı; hız sınıfı da farklı. |
| [Direnc.net Power-Xtra 2S1P 1000 mAh, 16322](https://www.direnc.net/74v-2s1p-1000-mah-15c-li-polymer-pil-soketli) | **1.019,96 TL KDV dahil**; KDV hariç 849,97 TL. | Yapılandırılmış veride InStock. | Koruma/şarj koşulları netleşmeden kesin seçim değil. |
| [Robolink A3 2S/3S şarj cihazı](https://www.robolinkmarket.com/a3-kompakt-lipo-2s-3s-sarj-aleti) | **870,00 TL KDV dahil**; KDV hariç 725,00 TL. | Yapılandırılmış veride InStock. | Bataryayla akım ve soket uyumu doğrulanacak. |
| [Robolink UBEC 5 V/3 A](https://www.robolinkmarket.com/ubec-5v-3a-2s-6s) | **273,00 TL KDV dahil**. | Yapılandırılmış veride OutOfStock; ürün bölümünde Tükendi. | Şu an temin edilebilir sayılmadı. “Maksimum 3 A” ifadesi sürekli 3 A kanıtı değil. |
| [Robolink 2S 850 mAh paket](https://www.robolinkmarket.com/74v-2s-850mah-40c-lipo-batarya) | **1.104,00 TL KDV dahil**. | Yapılandırılmış veride OutOfStock; ürün bölümünde Tükendi. | Stok ve koruma koşulları nedeniyle ilk paket seçimi yapılmadı. |

Robotistan'ın incelenen [TB6612FNG](https://www.robotistan.com/tb6612fng-step-motor-surucu-dc-motor-sucuru) ve [1300 mAh paket](https://www.robotistan.com/tinylab-74v-2s-lipo-batarya-1300mah-40c) sayfalarında KDV etiketleri/gösterimleri arasında tutarsızlık görüldü. Bu sayfalardaki rakamlar kesin KDV dahil bütçe tutarı olarak alınmadı. Yapılandırılmış stok etiketi gerçek eldeki miktarı veya teslimi garanti etmez.

Kaynak URL, para birimi, KDV ve durum kaydı [tedarik kayıt dosyasında](tedarik/fiyat_kayitlari_2026-10-21.json). **Tam proje bütçesi henüz oluşturulmadı.** Mekanik, beş sensör, regülatörler, yardımcı malzeme ve bağımsız deney ölçümünün maliyeti de tamamlanacak.

## Sonraki teknik kontroller

İki #5143 veya belgeli eşdeğeri motor ve TB6612FNG, incelenen besleme/sinyal seviyeleri bakımından somut başlangıç önerisidir. Yerel motor eşdeğerinin veri eksikleri, Türkiye teslim maliyeti, gerçek şasi yükü ve batarya/şarj/koruma seçimi tamamlanacak. Yapılmamış donanım deneyleri başvuru metninde yapılmış gibi anlatılmayacak.
