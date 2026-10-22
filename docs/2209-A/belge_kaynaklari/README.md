# Belge üretimi

Danışmana sunulacak güncel raporun kaynak metni `../ARASTIRMA_ONERISI.md`, şekilleri `../gorseller/danisman_sunumu/` klasöründedir.

Depo kökünden:

```bash
python docs/2209-A/belge_kaynaklari/disari_aktar.py --stem ARASTIRMA_ONERISI --title 'Kullanıcı tarafından belirlenen rota bilgisine göre hareket eden otonom araç tasarımı' --sunum
```

Python 3, python-docx, pandoc, XeLaTeX, Liberation ve DejaVu yazı tipleri gerekir. PDF A4 olarak, Word ise A4 sayfa ve bölünmeyen tablo satırlarıyla üretilir. `--sunum` kapak ve temiz üstbilgiyi etkinleştirir. Önceki birleşik taslak ve bütçe kaynakları `--stem` ile ayrıca üretilebilir; mevcut dosyalar çalışma geçmişidir.

Metin veya çizim değişikliğinden sonra sayfa düzeni, özet uzunluğu, kaynakça ve bütçe toplamı birlikte kontrol edilmelidir.

## Akademik başvuru düzeni

Güncel sunum düzeni Arial/Liberation Sans, çizgili tablolar, kutulu özet ve resmî kaynaktan alınan TÜBİTAK logosunu kullanır. Deney alanı çizimini metindeki koordinatlarla yeniden üretmek için:

```bash
python docs/2209-A/belge_kaynaklari/deney_geometrisi.py
```

Bu adım Matplotlib gerektirir ve PNG/PDF/SVG üretir. PDF raporu vektör çizimi, Word PNG kopyasını kullanır. Sistem/akış şemaları `gorseller/akademik_duzen/` içindedir. Logo kaynağı `varliklar/README.md` dosyasında kayıtlıdır.
