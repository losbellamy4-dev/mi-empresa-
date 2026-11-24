#!/usr/bin/env python3
"""Mockups (imágenes de anuncio) para Etsy del anuncio ancla #1 Just Listed — Día 12 (2026-11-19).

Genera html/*.html (2700×2025 px, 4:3) en ES y EN. `render.js` los convierte en PNG.
Todo lo importante va dentro del cuadrado central (x 337–2363) porque Etsy recorta
a cuadrado en algunas vistas.

Los huecos de foto se pintan con un degradado neutro. En los mockups definitivos,
Adrián debe poner fotos de stock gratuitas con licencia comercial (p. ej. Pexels o
Unsplash; 🔴 un adulto revisa la licencia) dentro de las plantillas de Canva y
exportar las capturas desde allí. Estos son la composición de referencia.

Uso:  python3 mockups.py && node render.js
"""
import re
import sys
from pathlib import Path
from html import escape

AQUI = Path(__file__).resolve().parent
SVG = AQUI.parent / "maquetas" / "svg"
OUT = AQUI / "html"
W, H = 2700, 2025

TXT = {
    "en": {
        "t1": "Just Listed", "t1b": "Instagram Templates", "sub": "4 editable Canva designs · for real estate agents",
        "badge": "EDIT IN CANVA · FREE ACCOUNT",
        "grid": "A feed that looks professional", "grid_sub": "Mix with Open House, Just Sold and Tips (sold separately or in the bundle)",
        "detail": "Change photos, text and colors in minutes", "detail_sub": "Drag your photo · type your details · download",
        "pal": "3 color palettes included", "pal_sub": "Or use your own brand colors",
        "inc": "What's included",
        "inc_items": ["4 Just Listed post designs (1080×1350 px)", "3 color palettes for each design",
                      "English and Spanish versions", "PDF with your Canva template links",
                      "1-page quick start guide", "Free Canva account is enough"],
        "inc_note": "Digital download · no physical item will be shipped · photos not included",
    },
    "es": {
        "t1": "Nuevo en cartera", "t1b": "Plantillas para Instagram", "sub": "4 diseños editables en Canva · para inmobiliarias",
        "badge": "EDITA EN CANVA · CUENTA GRATIS",
        "grid": "Un perfil con aspecto profesional", "grid_sub": "Combínalas con Puertas abiertas, Vendido y Consejos (por separado o en el pack)",
        "detail": "Cambia fotos, textos y colores en minutos", "detail_sub": "Arrastra tu foto · escribe tus datos · descarga",
        "pal": "3 paletas de color incluidas", "pal_sub": "O usa los colores de tu marca",
        "inc": "Qué incluye",
        "inc_items": ["4 diseños de post Nuevo en cartera (1080×1350 px)", "3 paletas de color por diseño",
                      "Versiones en español e inglés", "PDF con los enlaces a tus plantillas de Canva",
                      "Guía rápida de 1 página", "Basta con una cuenta gratuita de Canva"],
        "inc_note": "Descarga digital · no se envía nada físico · fotos no incluidas",
    },
}

FONDO, TINTA, ACENTO = "#F3EDE4", "#1E1E1E", "#B08D57"


def svg(nombre):
    """SVG de la maqueta, sin rayado ni etiqueta de foto (degradado tipo foto) y escalable."""
    s = (SVG / nombre).read_text(encoding="utf-8")
    s = re.sub(r'<defs><pattern.*?</pattern></defs>', '', s)
    s = re.sub(r'fill="url\(#h[^)]*\)"', 'fill="url(#foto)"', s)
    s = re.sub(r'<text[^>]*opacity="\.55">[^<]*</text>', '', s)  # etiqueta "FOTO DEL INMUEBLE"
    grad = ('<defs><linearGradient id="foto" x1="0" y1="0" x2="0.4" y2="1">'
            '<stop offset="0" stop-color="#C9D3DA"/><stop offset=".55" stop-color="#E8E1D6"/>'
            '<stop offset="1" stop-color="#B9A994"/></linearGradient></defs>')
    s = s.replace('width="1080" height="1350"', 'width="100%" preserveAspectRatio="xMidYMid meet"', 1)
    return s.replace('>', '>' + grad, 1)


def pagina(cuerpo):
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
body{{width:{W}px;height:{H}px;background:{FONDO};color:{TINTA};font-family:Montserrat,sans-serif;overflow:hidden;position:relative}}
h1,h2{{font-family:'Playfair Display',serif;margin:0;line-height:1.05}}
.post{{box-shadow:0 30px 70px rgba(0,0,0,.18);background:#fff;line-height:0}}
.badge{{display:inline-block;background:{ACENTO};color:#fff;font-weight:700;letter-spacing:6px;font-size:40px;padding:22px 44px;border-radius:60px}}
.centro{{position:absolute;left:337px;width:2026px}}
</style></head><body>{cuerpo}</body></html>"""


def m1_portada(t, l):
    posts = [("1a", "beige", -9, 380, 560), ("1b", "navy", 0, 1060, 470), ("1c", "salvia", 9, 1740, 560)]
    c = "".join(f'<div class="post" style="position:absolute;left:{x}px;top:{y}px;width:600px;'
                f'transform:rotate({r}deg)">{svg(f"p{k}_{p}_{l}.svg")}</div>' for k, p, r, x, y in posts)
    c += (f'<div class="centro" style="top:90px;text-align:center"><h1 style="font-size:150px">{escape(t["t1"])}</h1>'
          f'<div style="font-size:64px;font-weight:600;margin-top:16px">{escape(t["t1b"])}</div>'
          f'<div style="font-size:44px;opacity:.75;margin-top:14px">{escape(t["sub"])}</div></div>'
          f'<div class="centro" style="top:1790px;text-align:center"><span class="badge">{escape(t["badge"])}</span></div>')
    return pagina(c)


def m2_cuadricula(t, l):
    orden = ["1a_beige", "6_1_beige", "1b_beige", "3_beige", "1c_beige", "6v_1_beige",
             "1d_beige", "4_beige", "1a_salvia"]
    celdas = "".join(f'<div style="line-height:0;overflow:hidden;aspect-ratio:4/5">{svg(f"p{o}_{l}.svg")}</div>' for o in orden)
    c = (f'<div style="position:absolute;left:337px;top:110px;width:1180px;display:grid;'
         f'grid-template-columns:repeat(3,1fr);gap:10px;background:#fff;padding:10px" class="post">{celdas}</div>'
         f'<div style="position:absolute;left:1600px;top:640px;width:760px">'
         f'<h2 style="font-size:96px">{escape(t["grid"])}</h2>'
         f'<p style="font-size:42px;line-height:1.4;opacity:.8">{escape(t["grid_sub"])}</p></div>')
    return pagina(c)


def m3_detalle(t, l):
    c = (f'<div style="position:absolute;left:337px;top:420px;width:860px;padding:34px;background:#111;'
         f'border-radius:90px" class="post"><div style="border-radius:60px;overflow:hidden;line-height:0">'
         f'{svg(f"p1b_navy_{l}.svg")}</div></div>'
         f'<div style="position:absolute;left:1340px;top:740px;width:1020px">'
         f'<h2 style="font-size:104px">{escape(t["detail"])}</h2>'
         f'<p style="font-size:46px;line-height:1.4;opacity:.8">{escape(t["detail_sub"])}</p>'
         f'<span class="badge" style="margin-top:30px">{escape(t["badge"])}</span></div>')
    return pagina(c)


def m4_paletas(t, l):
    c = (f'<div class="centro" style="top:330px;text-align:center"><h2 style="font-size:120px">{escape(t["pal"])}</h2>'
         f'<div style="font-size:48px;opacity:.75;margin-top:16px">{escape(t["pal_sub"])}</div></div>'
         f'<div class="centro" style="top:720px;display:flex;gap:70px;justify-content:center">'
         + "".join(f'<div class="post" style="width:620px">{svg(f"p1a_{p}_{l}.svg")}</div>'
                   for p in ("beige", "navy", "salvia")) + '</div>')
    return pagina(c)


def m5_incluye(t, l):
    items = "".join(f'<li style="margin:0 0 34px;padding-left:80px;position:relative">'
                    f'<span style="position:absolute;left:0;color:{ACENTO};font-weight:700">✓</span>{escape(i)}</li>'
                    for i in t["inc_items"])
    c = (f'<div style="position:absolute;left:337px;top:520px;width:620px;transform:rotate(-4deg)" class="post">'
         f'{svg(f"p1d_beige_{l}.svg")}</div>'
         f'<div style="position:absolute;left:1120px;top:470px;width:1250px">'
         f'<h2 style="font-size:130px;margin-bottom:70px">{escape(t["inc"])}</h2>'
         f'<ul style="list-style:none;padding:0;margin:0;font-size:54px;font-weight:600">{items}</ul>'
         f'<p style="font-size:36px;opacity:.65;margin-top:50px">{escape(t["inc_note"])}</p></div>')
    return pagina(c)


MOCKUPS = [("1_portada", m1_portada), ("2_cuadricula", m2_cuadricula), ("3_detalle", m3_detalle),
           ("4_paletas", m4_paletas), ("5_incluye", m5_incluye)]


def main():
    OUT.mkdir(exist_ok=True)
    for l, t in TXT.items():
        for nombre, f in MOCKUPS:
            (OUT / f"just_listed_{nombre}_{l}.html").write_text(f(t, l), encoding="utf-8")
    print(f"{len(MOCKUPS) * len(TXT)} mockups HTML en {OUT}")


if __name__ == "__main__":
    sys.exit(main())
