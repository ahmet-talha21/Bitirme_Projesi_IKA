# Ürün bilgisi ve fiyat teklifi için hazır metin

Tarih: 22 Ekim 2026. Aşağıdaki metin, teklif bilgilerini toplamak için kullanılabilecek taslaktır. Satıcıya göre ilgili kalemler seçilebilir. Miktarlar bir prototip içindir; gerçek modeller ve mekanik yerleşim henüz kesinleşmedi.

---

Merhaba,

Üniversite araştırma/bitirme projesinde kullanılacak küçük ölçekli bir otonom araç için aşağıdaki parçaların teknik bilgileri ve Türkiye teslim TL fiyatlarını öğrenmek istiyorum:

1. **İki enkoderli motor:** Referans Pololu #5143 MP 210:1, 6 V, yaklaşık 100 d/d veya belgeli eşdeğeri. Anma gerilimi, redüksiyon, boşta hız, yük/sıkışma akımı, tork ve mil ölçüsü belirtilmeli. Enkoderin beslemesi, A/B çıkış seviyeleri, çözünürlüğü ve sayım tanımı gerekli. ESP32 ile 3,3 V sinyal uyumu aranıyor.
2. **Motor bağlantıları ve tekerlekler:** İki motora uygun bağlantı aparatı, 3 mm D mil için yaklaşık 60 mm tekerlek çifti ve uygun yükseklikte bir taşıyıcı teker. Kablo/soketler motora dahil değilse ayrıca belirtilmeli.
3. **Beş mesafe sensörü:** VL53L0X tabanlı taşıyıcı veya değerlendirilebilecek alternatif. Kartın tam modeli, besleme gerilimi ve I²C sinyal/çekme dirençlerinin seviyeleri gerekli. Yalnızca sensör çipi veri sayfası yerine taşıyıcı bilgisi de isteniyor. Referans Pololu #2490; uygun fiyatlı alternatif ayrıca değerlendirilebilir.
4. **Batarya ve şarj:** Hazır 2S LiPo paket, yaklaşık 1000 mAh sınıfı. Tam üretici kodu, veri sayfası, izin verilen şarj/deşarj akımları, şarj sonu gerilimi, soket/dengeleme bağlantıları ve koruma devresi bilgisi gerekli. Uygun şarj cihazı için çıkış profili/akımı ve soket uyumu da belirtilmeli.
5. **Güç devresi:** 2S paketin çalışma aralığında 5 V çıkış sağlayan regülatör; hedef en az 3 A sürekli çıkış, belirtilen giriş/ısıl koşullarla birlikte. 3,3 V sensör/mantık regülasyonu ve gerekiyorsa uygun harici paket koruma modülü ayrıca belirtilmeli.
6. **Şasi:** Yaklaşık 20 × 15 cm sınıfında, iki referans motorun montajına uygun boş şasi veya önerilen imalat. TT motorlu komple kit yerine boş şasi fiyatı tercih ediliyor. Malzeme/kalınlık, ölçü, delik düzeni, dahil bağlantılar ve teslim süresi gerekli.

Teklifte tam ürün kodu, adet/paket içeriği, birim fiyat, KDV durumu, stok/temin süresi, teslim/kargo ve varsa ithalat giderleri ayrı gösterilebilir mi? Referans markanın bulunmadığı durumda eşdeğer ürünün teknik farklarını ve doküman bağlantısını da paylaşabilir misiniz?

Teşekkür ederim.

---

Gelen bilgiler [CSV teklif formuna](MALZEME_TEKLIF_FORMU.csv) işlenecek. Referans motor, beş sensör ve iki motor geri bildirimi korunacak; farklı bir ürüne geçildiğinde sürücü, güç ve mekanik uyum birlikte kontrol edilecek.
