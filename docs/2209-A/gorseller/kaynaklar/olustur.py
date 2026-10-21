"""Başvuruya yönelik tasarım şemalarını yeniden üretir; deney verisi kullanmaz."""

from pathlib import Path
import os
import subprocess

os.environ.setdefault("MPLCONFIGDIR", "/tmp/ika-matplotlib-cache")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter, MultipleLocator


SOURCE = Path(__file__).resolve().parent
OUTPUT = SOURCE.parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
})


def render_dot(source_name, output_name):
    for fmt in ("png", "svg", "pdf"):
        args = ["dot", f"-T{fmt}"]
        if fmt == "png":
            args.append("-Gdpi=200")
        args.extend([str(SOURCE / source_name), "-o", str(OUTPUT / f"{output_name}.{fmt}")])
        subprocess.run(args, check=True)
        if fmt == "svg":
            clean_svg(OUTPUT / f"{output_name}.{fmt}")


def clean_svg(path):
    path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")


def draw_example_area():
    fig, ax = plt.subplots(figsize=(8.5, 8.5))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.19, top=0.86)
    ax.set_aspect("equal")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.xaxis.set_minor_locator(MultipleLocator(0.25))
    ax.yaxis.set_minor_locator(MultipleLocator(0.25))
    formatter = FuncFormatter(lambda value, _: f"{value:g}".replace(".", ","))
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.grid(which="major", color="#CBD5E1", linewidth=0.9)
    ax.grid(which="minor", color="#E2E8F0", linewidth=0.5)
    ax.set_axisbelow(True)
    ax.set_xlabel("Yerel x koordinatı (m)", labelpad=9)
    ax.set_ylabel("Yerel y koordinatı (m)", labelpad=9)

    points = [(0.35, 0.45), (2.55, 0.45), (2.55, 2.55), (0.45, 2.55)]
    for begin, end in zip(points, points[1:]):
        ax.annotate(
            "", xy=end, xytext=begin,
            arrowprops={"arrowstyle": "->", "lw": 2.1, "linestyle": "--", "color": "#2563EB"},
            zorder=3,
        )

    for x, y, width, height, name in [
        (1.20, 0.25, 0.45, 0.40, "E1"),
        (2.35, 1.25, 0.40, 0.45, "E2"),
    ]:
        ax.add_patch(Rectangle((x, y), width, height, facecolor="#FDE68A", edgecolor="#92400E", linewidth=1.5, zorder=4))
        ax.text(x + width / 2, y + height / 2, name, ha="center", va="center", color="#78350F", weight="bold", zorder=5)

    for index, (x, y) in enumerate(points):
        if index == 0:
            ax.scatter([x], [y], s=100, marker="s", color="#15803D", zorder=6)
            label = "Başlangıç"
            offset = (0, 13)
        else:
            ax.scatter([x], [y], s=75, color="#2563EB", edgecolors="white", linewidth=1.0, zorder=6)
            label = f"W{index}"
            offset = (0, 12) if index != 2 else (-15, 12)
        ax.annotate(label, (x, y), xytext=offset, textcoords="offset points", ha="center", weight="bold", color="#0F172A", zorder=7)

    legend = [
        Line2D([0], [0], color="#2563EB", linestyle="--", linewidth=2, label="Tanımlanan rota (örnek)"),
        Rectangle((0, 0), 1, 1, facecolor="#FDE68A", edgecolor="#92400E", label="Sabit engel (örnek)"),
    ]
    ax.legend(handles=legend, loc="upper center", bbox_to_anchor=(0.5, -0.11), ncol=2, frameon=False, fontsize=10)
    fig.suptitle("Şekil 3. Planlanan 3 × 3 m deney alanı\nÖrnek waypoint ve sabit engel yerleşimi", fontsize=16, weight="bold", color="#0F172A", y=0.97)
    fig.text(0.5, 0.035,
             "Şematik plan: noktalar ve engel ölçüleri anlatım amaçlıdır.\nÇizgiler tanımlanan rotayı gösterir; ölçülmüş araç yolu veya kaçınma sonucu değildir.",
             ha="center", va="center", fontsize=10, color="#475569")
    for fmt in ("png", "svg", "pdf"):
        fig.savefig(OUTPUT / f"sekil_3_deney_alani.{fmt}", dpi=240, facecolor="white")
        if fmt == "svg":
            clean_svg(OUTPUT / f"sekil_3_deney_alani.{fmt}")
    plt.close(fig)


if __name__ == "__main__":
    render_dot("sistem_mimarisi.dot", "sekil_1_sistem_mimarisi")
    render_dot("calisma_akisi.dot", "sekil_2_calisma_akisi")
    draw_example_area()
    print("Üç şema PNG, SVG ve PDF biçimlerinde oluşturuldu.")
