# Görsel yenileme kaydı

Tarih: 21 Ekim 2026.

## Kullanıcı isteği ve incelenen örnekler

İlk şekillerin daha özenli, açıklayıcı ve göze hitap eden biçimde hazırlanması; özellikle kontrol akışındaki dıştan dönen uzun okun kaldırılması istendi. Kabul almış iki örneğin görsellerine bakılarak mevcut projeye özgü bir anlatım geliştirilmesi talep edildi.

İlk PDF'nin 5–6. sayfalarındaki blok şeması ve çalışma akışı; ikinci PDF'nin 5–6. sayfalarındaki veri/grafik yerleşimi ve simgeli model diyagramı incelendi. Kısa metinli kartlar, aşamaların gruplandırılması ve simgeler kullanıldı. Örneklerin tıbbi veya silah sistemi içerikleri, metinleri, şekilleri ve sonuçları kopyalanmadı.

## Tasarım kararları

- Ortak renk düzeni: lacivert başlıklar, mavi rota/kontrol, turkuaz algılama/geri bildirim, turuncu engel/kaçınma vurgusu.
- Akış şemasında dış döngü çizgisi yerine eşleştirilmiş “A” bağlantıları kullanıldı; karar dalları etiketlendi.
- Deney şemasında referans rota ile anlatım amaçlı kaçınma yolu ayrı renklerle gösterildi. Kaçınma yolu algoritma çıktısı veya ölçüm sonucu değildir.

## Üretim ve kaynak dosyalar

Görseller `image_gen.imagegen` aracıyla, önceki şekiller ve örnek sayfalar görsel referans olarak verilerek yeniden oluşturuldu. Model sürümü araçta gösterilmediği için sürüm bilgisi tahmin edilmedi.

| Güncel şekil | Üretilen kaynak dosya | Piksel boyutu |
| --- | --- | --- |
| Sistem mimarisi | `exec-b65c363a-f927-4123-9566-caf15225c94e.png` | 1536 × 1024 |
| Çalışma akışı | `exec-1020ad6e-5418-49bd-8d79-6269c3e50008.png` | 1122 × 1402 |
| Deney düzeni | `exec-ad07d8df-fd17-473f-b5f2-80b300bcb37e.png` | 1536 × 1024 |

Orijinal üretimler çalışma ortamının `/workspace/generated_images` dizininde bırakıldı; kopyaları güncel şekil adlarıyla depoya alındı. Bu dosyalar piksel tabanlıdır. PDF çıktıları yalnızca belge paketlemesidir; SVG/vektör kaynak üretildiği iddia edilmez.

## Kontrol

- Türkçe etiketler, temel veri akışları ve karar dalları görsel olarak incelendi.
- Şemalar mevcut seçimlerle karşılaştırıldı: ESP32, enkoderli iki motorlu hareket, waypoint arayüzü ve sabit engelli deney önerisi.
- Algılama simgeleri belirli bir sensör modelini veya adedini kesinleştirmez; araç simgesi seçilmiş bir ürün veya kurulmuş prototip değildir.
- Yöntem ve sayısal eşikler henüz kesinleşmediğinden çizimler öneri olarak sunulacak.
- ÜYZ ile görsel üretimi başvurudaki kullanım beyanına eklenmelidir. Nihai metin ve şekiller kullanıcı/danışman tarafından kontrol edilecektir.
