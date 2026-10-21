# Fiyatlı bütçe taslağı — 22 Ekim 2026

Bu belge, önerilen parçaların kaynaklı fiyat gözlemlerini toplar. Model seçimi, ürün uyumu ve tedarik henüz tamamlanmadığından nihai TYBS bütçesi değildir. Fiyatlar satın alma/rezervasyon veya bağlayıcı teklif anlamına gelmez. Kullanıcının iki enkoderli motor ve beş sabit sensör kararı korunmuştur.

## Fiyatı bulunan yerel adaylar

Tablodaki TL tutarlar sayfalarda görülen KDV dahil fiyatlardır. Satış paketleri gerçek adetleriyle tutuldu; örneğin iki tekerlik paket yarım fiyatla tek teker gibi hesaplanmadı. Stok satıcının sayfa verisidir; eldeki miktar teyit edilmedi.

| Kalem | Taslak miktar / satış birimi | Birim fiyat | Ara toplam |
| --- | --- | --- | --- |
| [ESP32-WROOM CP2102 Type-C geliştirme kartı](https://www.robolinkmarket.com/esp32-wroom-cp2102-wifi-ve-bluetooth-modulu-type-c) | 1 adet | 628,50 TL | 628,50 TL |
| [Mini serbest tekerlek, 2 adetlik paket](https://www.direnc.net/mini-sarhos-tekerlek-plastik-2-adet) | 1 paket (2 adet) | 56,58 TL | 56,58 TL |
| [TB6612FNG sürücü modülü](https://www.direnc.net/tb6612fng-dc-ve-step-motor-surucu-modulu) | 1 adet | 81,36 TL | 81,36 TL |
| [TCA9548A I²C çoklayıcı](https://www.robolinkmarket.com/tca9548a-i2c-coklayici) | 1 adet | 76,50 TL | 76,50 TL |
| [Power-Xtra 7,4 V 2S1P 1000 mAh paket](https://www.direnc.net/74v-2s1p-1000-mah-15c-li-polymer-pil-soketli) | 1 adet | 1.019,96 TL | 1.019,96 TL |
| [A3 2S/3S LiPo dengelemeli şarj cihazı](https://www.robolinkmarket.com/a3-kompakt-lipo-2s-3s-sarj-aleti) | 1 adet | 870,00 TL | 870,00 TL |
| [FPV UBEC 5 V 3 A 2–6S](https://www.robolinkmarket.com/fpv-ubec-5v-3a-2-6s-dc-dc-voltaj-regulatoru) | 1 adet | 214,50 TL | 214,50 TL |
| [AMS1117 3,3 V regülatör modülü](https://www.robolinkmarket.com/ams1117-33v-voltaj-regulator-modulu) | 1 adet | 27,00 TL | 27,00 TL |
| [DC131A 12 V ana güç anahtarı](https://www.direnc.net/dc131a-3p-on-off-anahtar-12v-isikli-yuvarlak-20mm) | 1 adet | 23,01 TL | 23,01 TL |
| [6×13 cm delikli pertinaks](https://www.robolinkmarket.com/6x13-delikli-pertinaks) | 1 adet | 39,00 TL | 39,00 TL |
| [USB-A / Type-C kablo, 1 metre](https://www.robolinkmarket.com/type-c-usb-a-kablo-1-metre) | 1 adet | 36,00 TL | 36,00 TL |
| [Dişi–erkek sinyal jumper kablosu, 40 hat](https://www.robolinkmarket.com/40-pin-ayrilabilen-disi-erkek-jumper-kablo-200mm) | 1 paket (40 hat) | 51,00 TL | 51,00 TL |
| [2S 5A BMS koruma modülü](https://www.robolinkmarket.com/2s-5a-bms-batarya-yonetim-ve-koruma-modulu) | 1 adet | 66,00 TL | 66,00 TL |

**Bu yerel adayların ara toplamı: 3.189,41 TL.**

## Dövizle listelenen referanslar

Bu tutarlar TL bütçesi değildir. Kur, Türkiye teslim kargosu, varsa vergi ve tedarik giderleri doğrulanmadı; USD tutarlar TL toplamına eklenmedi.

| Kalem | Taslak miktar / satış birimi | Birim fiyat | Ara toplam |
| --- | --- | --- | --- |
| [Pololu #5143 MP 210:1 6 V enkoderli motor](https://www.pololu.com/product/5143/specs) | 2 adet | 29,95 USD | 59,90 USD |
| [Pololu #1420 60×8 mm tekerlek çifti](https://www.pololu.com/product/1420) | 1 çift (2 tekerlek) | 6,75 USD | 6,75 USD |
| [Pololu #1089 uzatılmış motor bağlantı çifti](https://www.pololu.com/product/1089) | 1 çift (2 bağlantı) | 4,95 USD | 4,95 USD |
| [Pololu #2490 VL53L0X taşıyıcısı](https://www.pololu.com/product/2490) | 5 adet | 19,95 USD | 99,75 USD |
| [Pololu #4763 motor/enkoder kablosu](https://www.pololu.com/product/4763) | 2 adet | 3,00 USD | 6,00 USD |

**Bu referansların ara toplamı: 177,35 USD.**

## Alternatif yerel sensör fiyatı

[CJMCU-530 VL53L0X](https://www.direnc.net/tof-arduino-mesafe-sensoru-modulu-cjmcu-530-vl53l0x) sayfasında KDV dahil **156,92 TL/adet**, beş adet için **784,60 TL** fiyat görülüyor. Sayfa stok verisi OutOfStock ve satıcı beslemeyi 5 V olarak belirtiyor. Bu kart, 3,3 V ile beslenen belgeli Pololu taşıyıcının hazır eşdeğeri sayılmadı. Kartın I²C seviyeleri, güç bağlantısı ve temini doğrulanırsa ayrı bir seçenek olabilir.

Yalnızca sensör fiyatını bu alternatifle değiştiren aritmetik kıyas **3.974,01 TL + 77,60 USD** olur. Bu, kullanılabilirliği/uyumu doğrulanmış bir set veya tüm proje bütçesi değildir; olası ek arayüz maliyeti de doğrulanmadı.

## Henüz toplamın dışında kalanlar

- N20 motorların bağlantılarına uygun boş/özel şasi; standart TT motorlu kitler doğrudan eşdeğer alınmadı.
- Ana güç kablosu, sigorta/yuva ve gerekli konnektörler; sinyal jumper seti motor güç kablosunun yerine sayılmadı.
- Son yerleşime uygun vida/distanslar ve gerekirse ek besleme süzme parçaları.
- Telefonun tüm alanı görebileceği sabitleme düzeni ve alan işaretleme ihtiyacı.
- Varsa mevcut olmayan ölçüm araçları; erişim kullanıcıyla netleştirilecek.
- Yurt dışı referansların Türkiye teslim maliyeti ve TL teklifi; isteğe bağlı IMU da bu referans toplama dahil değil.

Kullanıcının mevcut lehim ekipmanı ve deneyde kullanabileceğini doğruladığı telefon yeni satın alma kalemi yapılmadı. Yeni kamera alımı planlanmıyor. Telefon erişimi, ölçüm düzeneğinin kalibre edildiği anlamına gelmez.

**Sonuç:** Fiyatı bulunan kalemler için para birimi başına ara toplam hazır. Eksik kalemleri sıfır sayarak tek bir proje toplamı veya 12.000 TL sınırına uyum iddiası oluşturulmadı. Nihai TL bütçesi başvurudan önce tamamlanacak.

## Teknik kontrol ve kaynak kaydı

Batarya–şarj–koruma taslağı [ayrı planda](BATARYA_VE_SARJ_PLANI.md); tüm fiyat, para birimi, stok etiketi ve değerlendirme notları [22 Ekim kaynak kaydında](tedarik/fiyat_kayitlari_2026-10-22.json). [CSV teklif formu](MALZEME_TEKLIF_FORMU.csv) aynı fiyatlarla güncellendi.

Üreticinin pil/şarj verisi ve resmî kur için `www.power-xtra.com` ile `www.tcmb.gov.tr` alan adları mevcut izinler korunarak ortam taslağına eklendi. Araç kaydı doğruladı ve `requires_publish: true` bildirdi; sonraki isteklerde tünel 403 sürdü. Taslak kaydı erişimin etkinleştiğini göstermez. Etkinleştirmek için ortam ayarlarında değişikliklerin kaydedilip ortamın yayımlanması gerekiyor. Bu nedenle doğrulanmamış kur veya pil şarj akımı yazılmadı.
