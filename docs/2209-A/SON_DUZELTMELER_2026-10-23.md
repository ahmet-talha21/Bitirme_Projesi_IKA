# 23 Ekim 2026 — son düzeltmeler ve kontrol kaydı

Güncel belgeler: [Ana rapor PDF](ARASTIRMA_ONERISI.pdf) · [Word](ARASTIRMA_ONERISI.docx) · [Kaynak metin](ARASTIRMA_ONERISI.md).

Kullanıcının on maddelik isteği ve derslik teyidine ilişkin cevabı işlenmiştir. Ana rapor 14 sayfa, özet 250 kelimedir. Word beş görsel (logo + dört şekil) ve on bir düzenlenebilir tablo içerir. Fiziksel deney sonucu eklenmemiştir.

| Madde | Yapılan düzenleme | Doğrulama / sınır |
| --- | --- | --- |
| 1 — Marka/kaynak künyesi | Bölüm 4'te “açık kaynak sürüm deposu” kullanıldı; ticari ad tekrarları azaltıldı. Üretici kaynağı belgedeki gerçek alt başlık “Time-of-Flight ranging sensor” ile, DS11555/revizyon/yıl ve resmî bağlantı korunarak yazıldı. | Bilgi notu/bibliyografik açıklamalar izlenebilir kaynak ister; kaynağı yalnız “STMicroelectronics 2024” şeklinde eksiltmek önerilmedi. Ürün kodu kaynakçanın görünür metninde yoktur; resmî bağlantının dosya yolunda bulunması kaynak kimliğini doğrular. Kaynak başlığı uydurulmadı. Kontrol ailesi yöntem/şemada teknik bağlamda korunur. |
| 2 — Telefon görüş alanı | 3,0 m yeterlilik garantisi olmaktan çıkarıldı. Tavan/sabitleme ölçümü, alan çevresinde görüntü payı ve B planı eklendi: varsa geniş açı + bozulma düzeltmesi; yoksa yüksekliği/konumu veya kapalı mekânı değiştirme. | Mevcut telefonda geniş açı bulunduğu, tavanın ölçüldüğü veya montajın tamamlandığı varsayılmadı. 3 × 3 m alan küçültülmez; her değişimde kalibrasyon yenilenir. |
| 3 — Deney alanı | Kullanıcı “Evet, kullanım teyidi aldım” yanıtını verdi. Bölümden derslik kullanım teyidi alındığı yazıldı; erişim riski eklendi. Alternatif: uygun boş derslik veya yaya trafiğine kapatılabilen kapalı koridor. | Yazılı izin, oda numarası, belirli tarih veya alan ölçüsü uydurulmadı. Nihai karşılaştırmalar aynı seçilen alanda, aynı düzenek ve yeniden kalibrasyonla yapılır. |
| 4 — İKA | Bölüm 3.3'te “insansız kara aracı (İKA)” açılımı verildi. | PDF/Word metinlerinde kontrol edildi. |
| 5 — 200 ms tarama | Yönteme ve risk tablosuna bloke etmeyen okuma, üreticinin izin verdiği kısa ölçüm bütçesi, ölçüm geçerliliği kontrolü ve gerekirse eşdeğer ToF taşıyıcısı eklendi. Hız düşürme ek önlem olarak açıklandı. | Hız düşürme tarama süresini kısaltıyor gibi sunulmadı. Beş sensör, 200 ms hedefi, 250 ms veri yaşı ve 120 s görev hedefi korunur. Mevcut sentetik ön çalışmanın sabitleriyle çelişen yeni gecikme eşiği eklenmedi. |
| 6 — Önem cümlesi | Depo/lojistik cümlesi, “Örneğin ... planlanan küçük bir araçta ... bir uygulama senaryosu” biçiminde kuruldu. | Kaynaksız genel sektör gerekliliği iddiası yerine projenin olası kullanımını açıklıyor. |
| 7 — Kaynaklar | Borenstein–Feng (1996) odometri; Zhang (2000) kamera kalibrasyonu için eklendi. Güncel toplam dokuz kaynak, sekiz DOI. Corke'un basım yeri Cham tamamlandı. | Sekiz DOI HTTP 302 yönlendirmesi ve Crossref HTTP 200 ile yeniden doğrulandı. Bazı tam metinler erişilemedi; kimlik doğrulaması ile tam metin okuması ayrı tutuldu. [Kaynak erişim kaydı](KAYNAK_DOGRULAMA_KAYDI.md). |
| 8 — Bölüm 5 | “BELİRTMEK İSTEDİĞİNİZ DİĞER KONULAR” kullanıldı. | Resmî bilgi notunun başlığıyla eşleşir. |
| 9 — Yerleşim | Proje yönetiminden önceki zorunlu sayfa sonu kaldırıldı; takvim tablosu PDF ve Word'de bir arada tutuldu. Şekil–açıklama bütünlüğü korundu. | Rapor 14 sayfada kaldı; özellikle önceki 10. sayfadaki boşluk azaldı. Büyük şekillerin okunabilirliği için gerekli alan korundu; metin taşması saptanmadı. |
| 10 — Gövde/kargo/fiyat | K08 yalnız motor/tekerlek/elektronik hariç tek gövde plakası olarak tanımlandı. İki satıcının 1.500 TL ve üzeri ücretsiz teslim koşuluyla toplu sipariş planlandı; K22 kaldırıldı. 300 TL telefon sabitlemesine aktarıldı: K19 800 TL, toplam yine 11.500 TL ve 21 gider kalemi. On dört güncel satış sayfası fiyatı ayrı kaydedildi. | Satış sayfası gözlemleri bağlayıcı teklif değildir. Uygun gövde/montaj parçalarının kesin teklifleri henüz alınmadı; [teknik/fiyat teyidi metni](TEDARIK_FIYAT_TEYIDI_TALEBI.md) hazırlandı fakat gönderilmedi. Uygunsuz/ölçüsü şüpheli 4WD plaka fiyatı K08 teklifi sayılmadı. |

## Ek tutarlılık düzenlemeleri

- Önceki takvimde çakışan paketlerin toplamı konusundaki belirsizlik giderildi: İP1 1–2. ay %35, İP2 3. ay %20, İP3 4–5. ay %30, İP4 6. ay %15. Toplam süre 2+1+2+1=6 ay ve katkı %100. Hazırlık/raporlama teknik paketlere entegredir; ayrı raporlama veya malzeme alım paketi açılmadı.
- Çarpışma için bulunmayan bir temas sensörü varsayılmadı. Fiziksel temas veya dışarıdan görülen sınır ihlalinde gözlemcinin denemeyi durdurması, müdahale içeren başarısız deneme olarak tanımlandı.
- Araştırma olanakları tablosunda mevcut/teyitli kaynaklar gösterildi; gelecekte satın alınacak parçalar donanım ve bütçe bölümlerinde tutuldu.
- Nihai deney sayısı 40, koşul başına 10 tekrar, engelli koşulda en az 8/10 birleşik hedef, 10 cm toleranslar, 120 s sınırı ve %95 Wilson aralıkları korunmuştur. Aynı robotta küçük örneklem sınırlılığı belirtilir.
- Bağımsız bütçe MD/CSV/PDF/Word ve güncel JSON, ana raporla aynı miktarları kullanır. Önceki tarihli fiyat/taslak dosyaları geçmiş kayıtlarıdır.

## Yapılan kontroller

Özet ve bölüm uzunlukları, dokuz kaynağın metin içi eşleşmesi, sekiz DOI, 21 kalemin miktar × birim tutarı ve 11.500 TL toplamı, dört paket/altı ay/%100, sekiz risk, Türkçe şekil başlıkları ve PDF metin kutularının sayfa sınırları kontrol edildi. Şekiller ve tablolar görsel olarak incelendi. Fiziksel deney CSV'si yalnız başlık satırıdır; yeni fiziksel sonuç yazılmadı. Ana raporun görünür metninde GitHub, VL53L0X, eski Bölüm 5 başlığı veya İP5 bulunmaz.

Resmî kurallar bu incelemede kaynak künyesini bozma, başvuru öncesinde tamamlanmış prototip sunma veya proforma zorunluluğu gibi ek şartlarla genişletilmedi. Satıcı teyidi alınmadığı halde alınmış gibi bir beyan oluşturulmadı. TYBS özel ÜYZ alanı ve son önizleme/onay işlemleri ayrıca tamamlanmalıdır.
