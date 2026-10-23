# Güncel rapor kontrol kaydı

23 Ekim 2026 revizyonu: [Son düzeltmeler ve doğrulamalar](SON_DUZELTMELER_2026-10-23.md). Ana rapor dosyaları `ARASTIRMA_ONERISI.md/.pdf/.docx` dosyalarıdır.

Güncel sürüm dokuz kaynak, sekiz DOI, dört iş paketi, sekiz risk ve toplam 11.500 TL tutarında 21 gider kalemi içerir. Önceki sayısal kontroller aşağıda tarihsel kayıt olarak korunur; güncel sayfa/özet sayımları son düzeltmeler kaydında belirtilir.

Son üç düzenlemede bütçe açıklaması kısaltıldı; K19 montaj kapsamı ve kaynakçadaki görünür gerçek URL netleştirildi. Fiyatların birim tahminlerle farkı [karşılaştırma tablosundadır](BUTCE_FIYAT_KARSILASTIRMASI.md).

## Önceki kontrol kaydı

# Danışmana sunum kontrol kaydı

Tarih: 22 Ekim 2026. Güncel rapor: [Araştırma önerisi](ARASTIRMA_ONERISI.md) · [PDF](ARASTIRMA_ONERISI.pdf) · [Word](ARASTIRMA_ONERISI.docx).

## Son bilimsel ve biçimsel kontrol

- Kullanıcının istediği on bir maddelik düzeltme uygulandı; ayrıntılar [revizyon kaydındadır](REVIZYON_KONTROLU_2026-10-22.md). Yeni deneysel araştırma başlığı kapak, genel bilgiler ve Word özelliklerinde eşleştirildi.
- Kapaklı A4 PDF 14 sayfadır. Word aynı kaynak metinden üretildi; beş gömülü görsel (logo ve dört şekil), on bir düzenlenebilir tablo içerir. Ana dosyalarda taslak etiketi bulunmaz.
- Özet 249 kelimedir; bilgi notundaki 25–450 aralığındadır. Bilimsel nitelik, amaç/hedefler ve yöntem bölümleri en az 350 karakter koşulunu karşılar.
- Şekil 3'ün Türkçe karakter eşlemesi Type 42 font gömme ile düzeltildi. Hem tekil şekilde hem rapor PDF metninde “Dönüş öncesi” ve “Dönüş sonrası” eksiksiz doğrulandı. Şekil 3 ve 4 PDF'de vektördür.
- PDF metinleri sayfa sınırları içindedir. Kapak, özet, yöntem görselleri, iş paketleri, araştırma olanakları, bütçe ve kaynakça düzeni kontrol edildi. Ek bütçe tablosu tek sayfada tutuldu.
- Altı sentetik senaryolu ayrık zaman mantıksal ön çalışma gerçekten çalıştırıldı; altı beklenen kontrol sağlandı. Kod ve yürütme çıktıları `on_calisma/` klasöründedir. Bu çalışma araç kinematiği veya fiziksel sensör deneyi değildir; nihai 40 denemeye katılmaz.
- Dört koşul × 10 deneme = 40, her engelli koşulda en az 8/10 birleşik başarı, 10 cm toleranslar ve 120 saniye hedefleri korundu. Fiziksel deney CSV'si yalnız başlık satırıdır; ölçülmüş sonuç eklenmedi.
- %95 Wilson skor güven aralıkları, K2 hipotezi, nominal yaklaşık 3 m kamera yüksekliği ve 200/250/300 ms tarama/veri yaşı/tepki bütçeleri yöntemle ilişkilendirildi. Bunlar fiziksel performans ölçümü olarak sunulmadı.
- Altı aylık iş paketleri ve %20+%15+%20+%30+%15=%100 katkılar korundu. İP5, 5–6. ayda deney hazırlığı, analiz ve sonuç raporlamasını içerir. Üniversitede derslik içi deney alanı planlandı; oda numarası, alınmış izin veya tahsis varsayılmadı.
- Yedi tarihli kaynak ve metin içi atıflar eşleştirildi. Altı DOI, yönlendirme ve Crossref başlık/yazar/yıl kayıtlarıyla doğrulandı. ToF üretici veri sayfası doğrudan okundu; DOI'si bulunmadığından DOI üretilmedi. Tam metin erişim sınırları [kaynak doğrulama kaydında](KAYNAK_DOGRULAMA_KAYDI.md) belirtildi.
- 22 tahmini bütçe kalemi toplamı 11.500 TL'dir. Bütçe CSV'si ve rapor eki eşleştirildi; bedeller teklif veya gerçekleşmiş harcama olarak sunulmadı.
- Bölüm 5'te araçlar genel adlarla ve gerçek kullanım kapsamıyla açıklandı. Özel TYBS alanında kullanılacak araç adları ayrı [ÜYZ kullanım kaydında](UYZ_KULLANIM_BEYANI_KAYDI.md) tutuldu.
- Bir ulusal bilimsel toplantıya bildiri başvurusu ve açık kaynak yazılım/protokol/paylaşılabilir veri deposu somut çıktı olarak belirtildi; kabul garantisi verilmedi.

Bu kontrol, danışmanın bilimsel değerlendirmesi veya TYBS'deki önizleme/onay işlemi yerine geçmez. Güncel 2026 düzeninde araştırma önerisi ilgili sistem alanlarından oluşturulacaktır; kapaklı dosyalar okunabilir inceleme kopyalarıdır.

## Önceki görsel düzen revizyonunun kaydı


Kullanıcının paylaştığı Çağlar Özçine raporunun kapak, özet, yöntem görselleri, tablo ve kaynakça yerleşimleri karşılaştırıldı. Yeni tasarımda resmî kaynaktan alınan TÜBİTAK logosu, lacivert başlık hiyerarşisi, Arial/Liberation Sans yazı ailesi, kutulu özet, çizgili tablolar ve sade teknik şemalar kullanıldı. Kaynakça ayrı sayfaya taşındı. Örneğe ait kapak veya kişilerinin bilgileri kopyalanmadı.

Sistem ve akış şemaları image_gen ile sadeleştirildi. Deney geometrisi, önceden belirlenen A–B–C ve K0–K3 koordinatlarından Matplotlib ile çizildi; PDF'de vektör olarak kullanıldı. Çizim deney sonucu veya benzetim çıktısı değildir. Diğer projedeki ön deney sonuçları ve grafikleri bu öneriye aktarılmadı.

Kullanıcı, belgenin TÜBİTAK'a hitaben yazıldığını tekrar vurguladı. Metin resmî araştırma önerisi üslubunda korundu; danışmana hitap ve kontrol için sunum ifadesi bilimsel metinden çıkarıldı. Öğrenci projesinin uygulanabilirliğini anlatan sade dil, 2026 yönergesindeki bölüm ve içerik şartlarıyla birlikte değerlendirildi. Başlık, 6 ay, 40 deneme, koşul başına 8/10, 10 cm, 120 saniye ve 11.500 TL bütçe korundu.


Bu önceki düzen kaydından sonra başlık yenilenmiş ve sentetik girdili mantıksal ön çalışmayı gösteren dördüncü şekil eklenmiştir. Güncel durum üstteki kontrol listesinde tanımlanmıştır.
