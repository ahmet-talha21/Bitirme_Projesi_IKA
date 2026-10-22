# Durum makinesi mantıksal ön çalışması

Bu çalışma, raporun 2.9 bölümündeki fiziksel olmayan ön doğrulamadır. Altı kontrollü sentetik girdi senaryosu, gerçek çalıştırma sonucunda durum geçişi ve durdurma kuralları bakımından değerlendirilmiştir. Robot hareketi, beş sensörün optiği, kayma, kablosuz donanım ve bağımsız kamera fiziği modellenmemiştir. Bu sonuçlar fiziksel deneylerin yerine geçmez.

Depo kökünden:

```bash
python docs/2209-A/on_calisma/durum_simulasyonu.py
```

- `sonuclar.json`: Altı senaryonun beklenen ve gözlenen durumları.
- `durum_gecisleri.csv`: Bütün senaryoların gerçekleşen durum geçişleri.
- `S2_zaman_serisi.csv`: Şekil 4'te gösterilen tek sentetik senaryonun 50 ms örnekli kaydı.
- Çizim `gorseller/akademik_duzen/sekil_4_on_calisma` adıyla PNG/PDF/SVG üretilir.

Buradaki S1–S6, fiziksel deney koşulları K0–K3 değildir. Sentetik senaryolar 40 fiziksel değerlendirme denemesine dahil edilmez. `DENEY_KAYIT_SABLONU.csv` sonuçsuz başlık şablonu olarak korunmuştur. Kaynak kodda 250 ms veri yaşı sınırı ve ilk sonraki denetim adımında durdurma ayrıca kontrol edilir.

Bu klasördeki özgün kaynak kod MIT lisansıyla paylaşılmıştır. Lisans, başka kurumların logolarını veya dış kaynak eserleri kapsamaz.
