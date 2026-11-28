"""Día 20: paquete de lanzamiento del anuncio ancla de Etsy (pack completo 22 $).

Reúne en `../entregables/paquete_etsy_anuncio1/` todo lo que hace falta para publicar el
primer anuncio, listo para copiar y pegar:
  · anuncio_en.txt / anuncio_es.txt  → título, descripción en texto plano (Etsy no usa Markdown) y etiquetas;
  · LEEME.md                         → lista de comprobación en orden, con los pasos 🔴 (adulto);
  · MANIFIESTO.json                  → rutas de las 7 imágenes y los 4 archivos del comprador, con tamaño;
  · con --zip: paquete_etsy_anuncio1.zip (imágenes + PDFs + textos) para subirlo todo de una vez.
Valida: título ≤ 140, 13 etiquetas ≤ 20, ≤ 10 imágenes, ≤ 5 archivos digitales de ≤ 20 MB
[S: ayuda de Etsy para vendedores, límites de anuncios digitales].

Uso:  python3 paquete_etsy.py [--zip]
"""
import json
import re
import sys
import zipfile
from pathlib import Path

import anuncios_prueba as AP

AQUI = Path(__file__).parent
DEST = AQUI.parent / "entregables" / "paquete_etsy_anuncio1"
IMAGENES = ["pack_1_portada", "pack_2_todo", "pack_3_calendario", "pack_4_bilingue",
            "pack_5_stories", "pack_6_paletas", "pack_7_incluye"]
ARCHIVOS_COMPRADOR = ["guia/guia_en.pdf", "guia/guia_es.pdf", "calendario/calendario_en.pdf",
                      "calendario/calendario_es.pdf"]


def plano(md):
    """Quita el Markdown (negritas, comillas invertidas) para pegar en Etsy."""
    return re.sub(r"\*\*(.+?)\*\*", r"\1", md).replace("`", "")


def texto(a, idioma):
    if idioma == "en":
        desc = a["gancho_en"] + "\n\n" + AP.COMUN_EN.format(extra=a["extra_en"], upsell=AP.UPSELL_EN[bool(a.get("ancla"))])
        tit = a["titulo_en"]
    else:
        desc = a["gancho_es"] + "\n\n" + AP.COMUN_ES.format(extra=a["extra_es"]) + "\n\n" + AP.UPSELL_ES[bool(a.get("ancla"))]
        tit = a["titulo_es"]
    return (f"TITLE / TÍTULO ({len(tit)}/140)\n{tit}\n\n"
            f"PRICE / PRECIO\n22.00 USD\n\n"
            f"DESCRIPTION / DESCRIPCIÓN\n{plano(desc)}\n\n"
            f"TAGS / ETIQUETAS (13, separadas por comas)\n{', '.join(a['tags'])}\n")


def main():
    a = AP.ANUNCIOS[0]
    assert not AP.validar(a), AP.validar(a)
    DEST.mkdir(parents=True, exist_ok=True)
    for idioma in ("en", "es"):
        (DEST / f"anuncio_{idioma}.txt").write_text(texto(a, idioma), encoding="utf-8")
    man, faltan = {"imagenes_en": [], "imagenes_es": [], "archivos_comprador": []}, []
    for idioma in ("en", "es"):
        for i in IMAGENES:
            p = AQUI / "mockups" / "png" / f"{i}_{idioma}.png"
            (man[f"imagenes_{idioma}"] if p.exists() else faltan).append(
                {"ruta": str(p.relative_to(AQUI.parent)), "kb": p.stat().st_size // 1024} if p.exists() else str(p))
    for f in ARCHIVOS_COMPRADOR:
        p = AQUI / f
        if not p.exists():
            faltan.append(str(p))
            continue
        assert p.stat().st_size < 20 * 1024 * 1024, f"{f} supera 20 MB"
        man["archivos_comprador"].append({"ruta": str(p.relative_to(AQUI.parent)), "kb": p.stat().st_size // 1024})
    assert not faltan, f"faltan archivos: {faltan}"
    assert len(man["imagenes_en"]) <= 10 and len(man["archivos_comprador"]) <= 5
    (DEST / "MANIFIESTO.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")
    if "--zip" in sys.argv:
        z = DEST / "paquete_etsy_anuncio1.zip"
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            for grupo in man.values():
                for item in grupo:
                    zf.write(AQUI.parent / item["ruta"], Path(item["ruta"]).name)
            for t in ("anuncio_en.txt", "anuncio_es.txt", "LEEME.md"):
                if (DEST / t).exists():
                    zf.write(DEST / t, t)
        print(f"zip: {z} ({z.stat().st_size // 1024} KB)")
    print(f"OK: paquete en {DEST.relative_to(AQUI.parent)} — {len(man['imagenes_en'])} imágenes EN, "
          f"{len(man['archivos_comprador'])} archivos del comprador")


if __name__ == "__main__":
    main()
