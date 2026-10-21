"""Birleşik Markdown taslağından görselleri içeren Word ve PDF üretir.

Gereksinimler: Python 3, python-docx, pandoc, XeLaTeX ve DejaVu yazı tipleri.
Görsel dosyalarının içeriği değiştirilmez; yalnız belge içindeki boyutu ayarlanır.
"""

from datetime import datetime, timezone
from pathlib import Path
import os
import shutil
import subprocess
import tempfile

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
STEM = "ARASTIRMA_ONERISI_BIRLESIK_TASLAK"


def make_reference(path):
    document = Document()
    section = document.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin = section.bottom_margin = Cm(2)
    section.left_margin = section.right_margin = Cm(2)
    section.header_distance = section.footer_distance = Cm(0.8)
    normal = document.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(11)
    normal.paragraph_format.line_spacing = 1.12
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.widow_control = True
    for name, size in [("Heading 1", 17), ("Heading 2", 14), ("Heading 3", 11.5)]:
        style = document.styles[name]
        style.font.name = "Arial"
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor.from_string("183A57")
        style.paragraph_format.space_before = Pt(12)
        style.paragraph_format.space_after = Pt(6)
        style.paragraph_format.keep_with_next = True
    caption = document.styles["Caption"]
    caption.font.name = "Times New Roman"
    caption.font.size = Pt(9)
    caption.font.italic = False
    caption.font.color.rgb = RGBColor.from_string("475569")
    header = section.header.paragraphs[0]
    header.text = "TÜBİTAK 2209-A  |  Araştırma önerisi taslağı"
    header.runs[0].font.size = Pt(8)
    header.runs[0].font.color.rgb = RGBColor.from_string("64748B")
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run("Ahmet Talha Arslan  ·  ").font.size = Pt(8)
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    footer._p.append(field)
    document.save(path)


def finish_layout(path):
    document = Document(path)
    properties = document.core_properties
    properties.title = "İKA — TÜBİTAK 2209-A Araştırma Önerisi, Birleşik Taslak"
    properties.author = "Ahmet Talha Arslan"
    properties.subject = "Planlanan araştırma; deney sonuçları içermez"
    properties.modified = datetime.now(timezone.utc)

    for paragraph in document.paragraphs:
        if paragraph.text in {
            "1. Bilimsel nitelik", "2. Yöntem", "3. Proje yönetimi",
            "4. Araştırma önerisinin yaygın etkisi", "Kaynakça",
            "Son düzenlemede tamamlanacak alanlar — hazırlık notu",
        }:
            paragraph.paragraph_format.page_break_before = True
        if paragraph._p.xpath(".//w:drawing"):
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.keep_with_next = True
            paragraph.paragraph_format.space_after = Pt(2)
        if paragraph.text.startswith(("Şekil 1.", "Şekil 2.", "Şekil 3.")):
            paragraph.style = document.styles["Caption"]
            paragraph.paragraph_format.keep_together = True
            paragraph.paragraph_format.keep_with_next = False

    for shape in document.inline_shapes:
        factor = min(Cm(16.8) / shape.width, Cm(17.6) / shape.height, 1)
        shape.width = int(shape.width * factor)
        shape.height = int(shape.height * factor)

    for table in document.tables:
        table.style = "Table Grid"
        table.autofit = False
        count = len(table.columns)
        label = table.cell(0, 0).text
        if count == 2:
            widths = [4.2, 12.8]
        elif count == 3 and label == "Koşul":
            widths = [1.5, 12.8, 2.7]
        elif count == 3 and label == "Kişisel kaynak":
            widths = [3.3, 6.0, 7.7]
        elif count == 3:
            widths = [3.0, 5.6, 8.4]
        elif count == 4 and label == "İP":
            widths = [0.8, 10.0, 4.6, 1.6]
        elif count == 4:
            widths = [3.2, 4.1, 8.1, 1.6]
        else:
            widths = [17 / count] * count
        for column, width in zip(table.columns, widths):
            column.width = Cm(width)
        repeat = OxmlElement("w:tblHeader")
        table.rows[0]._tr.get_or_add_trPr().append(repeat)
        for row_index, row in enumerate(table.rows):
            no_split = OxmlElement("w:cantSplit")
            row._tr.get_or_add_trPr().append(no_split)
            for cell, width in zip(row.cells, widths):
                cell.width = Cm(width)
                cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
                if row_index == 0:
                    shade = OxmlElement("w:shd")
                    shade.set(qn("w:fill"), "EAF1F7")
                    cell._tc.get_or_add_tcPr().append(shade)
                for paragraph in cell.paragraphs:
                    paragraph.paragraph_format.space_after = Pt(3)
                    paragraph.paragraph_format.line_spacing = 1.05
                    for run in paragraph.runs:
                        run.font.size = Pt(9.5)
                        if row_index == 0:
                            run.font.bold = True
    document.save(path)


def main():
    source = ROOT / f"{STEM}.md"
    output = ROOT / f"{STEM}.docx"
    with tempfile.TemporaryDirectory(prefix="ika-belge-") as temporary:
        reference = Path(temporary) / "reference.docx"
        make_reference(reference)
        subprocess.run([
            "pandoc", str(source), "--from=markdown-implicit_figures+autolink_bare_uris", "--standalone",
            "--metadata=lang:tr-TR", f"--resource-path={ROOT}",
            f"--reference-doc={reference}", "--output", str(output),
        ], check=True, cwd=ROOT)
        finish_layout(output)
        pdf_directory = Path(temporary) / "pdf"
        pdf_directory.mkdir()
        cache_directory = Path(temporary) / "cache"
        cache_directory.mkdir()
        generated_pdf = pdf_directory / f"{STEM}.pdf"
        subprocess.run([
            "pandoc", str(source), "--from=markdown-implicit_figures+autolink_bare_uris", "--standalone",
            "--pdf-engine=xelatex", f"--resource-path={ROOT}",
            f"--lua-filter={ROOT / 'belge_kaynaklari/pdf_yerlesim.lua'}",
            f"--include-in-header={ROOT / 'belge_kaynaklari/pdf_baslik.tex'}",
            "-V", "mainfont=DejaVu Serif", "-V", "sansfont=DejaVu Sans",
            "-V", "geometry=margin=20mm", "-V", "fontsize=11pt",
            "-V", "linestretch=1.08", "-V", "colorlinks=true",
            "--output", str(generated_pdf),
        ], check=True, cwd=ROOT, env={**os.environ, "XDG_CACHE_HOME": str(cache_directory)})
        if not generated_pdf.is_file() or not generated_pdf.stat().st_size:
            raise RuntimeError("PDF çıktısı oluşmadı.")
        shutil.copy2(generated_pdf, ROOT / generated_pdf.name)
    pdf = ROOT / f"{STEM}.pdf"
    print(f"Word: {output.name}\nPDF: {pdf.name}")


if __name__ == "__main__":
    main()
