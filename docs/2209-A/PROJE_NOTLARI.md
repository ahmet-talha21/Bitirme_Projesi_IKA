# İKA — 2209-A hazırlık notları

Güncelleme: 21 Ekim 2026. Bu belge başvuru metni değil, kullanıcı tarafından doğrulanan bilgiler ve açık soruların kaydıdır.

## Kullanıcının belirttiği bilgiler

- Geçici başlık: Kullanıcı tarafından belirlenen rota bilgisine göre hareket eden otonom araç tasarımı.
- Araç ESP32 ile geliştirilecek.
- Kullanıcı arayüzü proje sahibi tarafından tasarlanacak; araç bu arayüz üzerinden kontrol edilecek.
- Kullanıcı rotayı arayüzden tanımlayacak; araç rotayı otonom takip edecek.
- Engel algılandığında engelden kaçınma davranışı devreye girecek; araç daha sonra rotasına dönerek ilerleyecek. Algoritma henüz seçilmedi.
- Waypoint (ara rota noktaları) kullanımı düşünülüyor; rota girişi henüz kesinleşmedi.
- Kullanıcı ev, okul ve iş yeri gibi farklı yerlerde kullanılabilirlik istiyor. İlk deney ortamı, zemin ve parkur boyutu henüz sınırlandırılmadı; her ortamda çalışacağı doğrulanmış bir özellik değil.
- ESP32 dışındaki malzemeler birlikte seçilecek; donanım listesi henüz kesinleşmedi.
- TÜBİTAK 2209-A başvurusu hazırlanacak.
- Teknik ayrıntılar kullanıcıya sorularak netleştirilecek; bilinmeyen özellikler ve sonuçlar yazılmayacak.

## Netleştirilecek konular

- Rota girişi: harita noktaları, çizim, mesafe/açı komutları veya başka bir yöntem.
- Çalışma ortamı: iç/dış mekân, zemin ve yaklaşık parkur boyutu.
- Manuel kontrolün ayrıca gerekip gerekmediği.
- Konum/yön ölçümü, sensörler, motorlar, sürücü ve mevcut donanım.
- Arayüz platformu, haberleşme yöntemi ve engelden kaçınma algoritması.
- Araştırma sorusu, karşılaştırma yöntemi ve ölçülebilir başarı ölçütleri.
- Ekip, danışman, kurum, olanaklar, süre ve bütçe.

## Belgeler ve doğrulama durumu

- Kullanıcı tarafından kabul almış örnekler olarak sunulan iki PDF incelendi. İç kapaklarında 2025 yılı belirtiliyor. Bunlar araştırma önerisi formu niteliğinde; güncel resmî şablon veya sonuç raporu olarak kullanılmayacak.
- Örneklerde bilimsel nitelik, amaç/hedefler, yöntem, proje yönetimi, yaygın etki ve kaynaklar bulunuyor. Güncel şartlar resmî 2026 belgeleriyle ayrıca kontrol edildi; ayrıntılar [2026 başvuru kurallarında](2026_BASVURU_KURALLARI.md).
- Örnek metinler kopyalanmayacak; içlerindeki kaynaklar bağımsız doğrulama yapılmadan kullanılmayacak. Kişisel bilgiler ve örnek PDF'ler bu depoya eklenmedi.
- Öğretim üyesinin paylaşılan uyarıları: güncel yönergeleri izlemek, eksik/uydurma kaynak kullanmamak, kaynak metinleri aynen aktarmamak ve yüklemeden önce öğretim üyesi kontrolünü sağlamak.
- Resmî sayfa: https://tubitak.gov.tr/tr/burslar/lisans-onlisans/destek-programlari/2209-universite-ogrencileri-arastirma-projeleri-destekleme-programi
- Önceki 403 erişim hatasının ardından 21 Ekim 2026 tarihinde yeniden denendi: program sayfası, 2026 çağrı duyurusu, 2026 başvuru içeriği bilgi notu ve ÜYZ rehberi HTTP 200 ile indirildi. Kullanıcının yüklediği bilgi notunun SHA-256 değeri resmî dosyayla aynı: `d5bf5477971b5924fe079970bab156057378afa1c2bff07df0a0d78614aba0e6`.

## Kullanıcıyla görüşülecek teknik öneriler — henüz karar değil

- Başlangıç için ölçülü bir ızgara üzerinde yerel (x, y) waypoint'ler öneriliyor. Waypoint kullanmak GPS kullanmayı zorunlu kılmaz; serbest çizilmiş bir rota da noktalara dönüştürülebilir.
- Başlangıç noktası ve yönü bilinen, düz zeminli, kısa bir kapalı alan parkuru öneriliyor. Bu seçim aracın başka yerlerde denenmesini dışlamaz; doğrulanacak kapsamı belirler.
- Motor enkoderleri ve IMU ile göreli konum/yön kestirimi değerlendirilebilir. Kayma ve ölçüm hataları zamanla birikir; bu yaklaşım tek başına kesin veya sınırsız konum doğruluğu sağlamaz. Parkur boyutu ve hata hedeflerine göre ek konum düzeltmesi gerekebilir.
- Mesafe sensörleriyle yerel engelden kaçınma ve ardından rotaya katılma değerlendirilecek. Sensör tipi, sayısı, görüş alanı ve algoritma seçilmedi; her engelin aşılabileceği iddia edilmeyecek.
- Basit süreye bağlı hareket komutları ilk hareket deneyi için kullanılabilir; engel etrafından dolaştıktan sonra rotaya doğru dönüşü güvenilir biçimde göstermek için konum/yön geri bildirimi gerekir.
- Rota sapması, hedefe ulaşma oranı, engelden sonra rotaya dönüş ve tamamlanma süresi olası ölçütlerdir. Karşılaştırma yöntemi, tekrar sayıları ve hedef değerler henüz belirlenmedi. Gerçek rota hatası, yalnızca aracın kendi kestiriminden hesaplanmayacak; bağımsız referans ölçüm yöntemi seçilecek.
