"""Mevcut PNG'leri içeriklerini değiştirmeden PDF belgelere yerleştirir."""

from pathlib import Path
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent.parent
FIGURES = [
    ("sekil_1_sistem_mimarisi", "Şekil 1. Sistem mimarisi"),
    ("sekil_2_calisma_akisi", "Şekil 2. Önerilen çalışma akışı"),
    ("sekil_3_deney_alani", "Şekil 3. Planlanan deney düzeni"),
]


def place_figure(document, image):
    pixel_width, pixel_height = image.getSize()
    width = 17 * cm
    height = width * pixel_height / pixel_width
    document.setPageSize((width, height))
    document.drawImage(image, 0, 0, width=width, height=height)


if __name__ == "__main__":
    combined = canvas.Canvas(str(ROOT / "gorseller_toplu.pdf"), pageCompression=1)
    combined.setTitle("İKA — başvuru görselleri, yenilenen sürüm")
    combined.setAuthor("Ahmet Talha Arslan — ÜYZ destekli tasarım şemaları")
    for stem, title in FIGURES:
        image = ImageReader(str(ROOT / f"{stem}.png"))
        document = canvas.Canvas(str(ROOT / f"{stem}.pdf"), pageCompression=1)
        document.setTitle(title)
        place_figure(document, image)
        document.showPage()
        document.save()
        place_figure(combined, image)
        combined.showPage()
    combined.save()
    print("Üç ayrı PDF ve görsel paketi oluşturuldu; PNG içerikleri değiştirilmedi.")
