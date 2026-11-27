#!/usr/bin/env python3
"""Mockups del anuncio ANCLA v2 de Etsy: pack completo (34 diseños + calendario 30 días, ES+EN) — Día 19.

Reutiliza `pagina()` y el estilo de `mockups.py` (anuncio suelto #1 Just Listed).
Genera html/pack_*.html (2700×2025 px, 4:3; lo importante en el cuadrado central)
y `node render.js` los pasa a png/.

Las 7 imágenes (Etsy admite hasta 10):
  1 portada (abanico + "34 diseños + calendario")   2 todo lo que incluye (10 tipos)
  3 calendario de 30 días (qué publicar cada día)    4 español E inglés (mismo diseño)
  5 stories + portadas de destacadas                 6 3 paletas                7 qué recibes (lista)

Igual que en mockups.py: los huecos de foto son un degradado. Para Etsy, Adrián rehace
las capturas desde Canva con fotos de stock con licencia comercial (🔴 un adulto la revisa).
Uso:  python3 mockups_pack.py && node render.js
"""
import csv
import re
import sys
from html import escape
from pathlib import Path

from mockups import SVG, OUT, ACENTO, TINTA, pagina

CAL = Path(__file__).resolve().parent.parent / "calendario" / "calendario.csv"

TXT = {
    "en": {
        "t1": "Real Estate Instagram Kit", "t1b": "34 Canva designs + 30-day posting calendar",
        "sub": "English & Spanish · 3 color palettes · free Canva account works",
        "badge": "EDIT IN CANVA · FREE ACCOUNT", "bil": "EN + ES",
        "all": "Everything in the bundle", "all_sub": "34 matching designs for every moment of a listing",
        "tipos": ["Just Listed ×4", "Open House ×4", "Just Sold ×2", "Under Contract ×2", "Price Reduced ×2",
                  "Tips carousel (7 slides)", "Testimonial ×2", "Meet the Agent ×2", "Tour stories ×3",
                  "Highlight covers ×12"],
        "cal": "Never wonder what to post", "cal_sub": "A 30-day calendar that tells you which template to use each day",
        "cal_dia": "Day", "cal_mas": "+ 23 more days",
        "two": "Every design in English AND Spanish", "two_sub": "Reach bilingual buyers and sellers with the same look",
        "st": "Stories & highlight covers", "st_sub": "Property tours, open house countdowns and 12 profile icons",
        "pal": "3 color palettes included", "pal_sub": "Beige · Navy · Sage — or your own brand colors",
        "inc": "What you get",
        "inc_items": ["34 designs × 3 palettes (Instagram post, story, carousel)",
                      "Every design in English and Spanish", "30-day posting calendar (PDF, EN + ES)",
                      "PDF with your Canva template links", "Quick start guide (how to edit in Canva)",
                      "Free Canva account is enough"],
        "inc_note": "Digital download · nothing will be shipped · photos not included",
        "es_lbl": "Spanish", "en_lbl": "English",
    },
    "es": {
        "t1": "Kit de Instagram para Inmobiliarias", "t1b": "34 diseños de Canva + calendario de 30 días",
        "sub": "Español e inglés · 3 paletas de color · vale la cuenta gratuita de Canva",
        "badge": "EDITA EN CANVA · CUENTA GRATIS", "bil": "ES + EN",
        "all": "Todo lo que trae el pack", "all_sub": "34 diseños a juego para cada momento de un inmueble",
        "tipos": ["Nuevo en cartera ×4", "Puertas abiertas ×4", "Vendido ×2", "Reservado ×2", "Bajada de precio ×2",
                  "Carrusel de consejos (7)", "Testimonio ×2", "Preséntate ×2", "Stories de visita ×3",
                  "Portadas de destacadas ×12"],
        "cal": "Se acabó pensar qué publicar", "cal_sub": "Un calendario de 30 días que te dice qué plantilla usar cada día",
        "cal_dia": "Día", "cal_mas": "+ 23 días más",
        "two": "Cada diseño en español E inglés", "two_sub": "Llega a compradores y vendedores bilingües con la misma imagen",
        "st": "Stories y portadas de destacadas", "st_sub": "Visitas en stories, cuenta atrás de puertas abiertas y 12 iconos de perfil",
        "pal": "3 paletas de color incluidas", "pal_sub": "Beige · Azul marino · Verde salvia — o los colores de tu marca",
        "inc": "Qué recibes",
        "inc_items": ["34 diseños × 3 paletas (post, story y carrusel de Instagram)",
                      "Cada diseño en español e inglés", "Calendario de publicación de 30 días (PDF, ES + EN)",
                      "PDF con los enlaces a tus plantillas de Canva", "Guía rápida (cómo editar en Canva)",
                      "Basta con una cuenta gratuita de Canva"],
        "inc_note": "Descarga digital · no se envía nada físico · fotos no incluidas",
        "es_lbl": "Español", "en_lbl": "Inglés",
    },
}


def svg(nombre):
    """Como mockups.svg() pero acepta también stories (1080×1920) y la hoja de iconos."""
    s = (SVG / nombre).read_text(encoding="utf-8")
    s = re.sub(r'<defs><pattern.*?</pattern></defs>', '', s)
    s = re.sub(r'fill="url\(#h[^)]*\)"', 'fill="url(#foto)"', s)
    s = re.sub(r'<text[^>]*opacity="\.55">[^<]*</text>', '', s)
    grad = ('<defs><linearGradient id="foto" x1="0" y1="0" x2="0.4" y2="1">'
            '<stop offset="0" stop-color="#C9D3DA"/><stop offset=".55" stop-color="#E8E1D6"/>'
            '<stop offset="1" stop-color="#B9A994"/></linearGradient></defs>')
    s = re.sub(r'width="1080" height="(1350|1920|1080)"', 'width="100%" preserveAspectRatio="xMidYMid meet"', s, count=1)
    return s.replace('>', '>' + grad, 1)


def post(nombre, w, extra=""):
    return f'<div class="post" style="width:{w}px;{extra}">{svg(nombre)}</div>'


def chip(txt, size=40):
    return (f'<span style="display:inline-block;background:{TINTA};color:#fff;font-weight:700;'
            f'font-size:{size}px;padding:14px 30px;border-radius:40px">{escape(txt)}</span>')


def p1_portada(t, l):
    fan = [("p3_navy", -16, 420, 900), ("p2post_salvia", -8, 760, 820), ("p1a_beige", 0, 1100, 780),
           ("p5a_navy", 8, 1440, 820), ("p7a_salvia", 16, 1780, 900)]
    c = "".join(f'<div class="post" style="position:absolute;left:{x}px;top:{y}px;width:500px;'
                f'transform:rotate({r}deg)">{svg(f"{n}_{l}.svg")}</div>' for n, r, x, y in fan)
    c += (f'<div class="centro" style="top:80px;text-align:center"><h1 style="font-size:132px">{escape(t["t1"])}</h1>'
          f'<div style="font-size:62px;font-weight:600;margin-top:18px">{escape(t["t1b"])}</div>'
          f'<div style="font-size:42px;opacity:.75;margin-top:14px">{escape(t["sub"])}</div></div>'
          f'<div style="position:absolute;left:2120px;top:640px;transform:rotate(10deg)">{chip(t["bil"], 64)}</div>'
          f'<div class="centro" style="top:1870px;text-align:center"><span class="badge">{escape(t["badge"])}</span></div>')
    return pagina(c)


def p2_todo(t, l):
    ficheros = ["p1a_beige", "p2post_navy", "p3_salvia", "p4_beige", "p5b_navy",
                "p6_1_salvia", "p7b_beige", "p8a_navy", "p9_1_salvia", "p10_beige"]
    celdas = "".join(
        f'<div style="text-align:center">{post(f"{f}_{l}.svg", 340, "margin:0 auto")}'
        f'<div style="font-size:30px;font-weight:700;margin-top:18px;line-height:1.2">{escape(n)}</div></div>'
        for f, n in zip(ficheros, t["tipos"]))
    c = (f'<div class="centro" style="top:70px;text-align:center"><h2 style="font-size:104px">{escape(t["all"])}</h2>'
         f'<div style="font-size:44px;opacity:.75;margin-top:12px">{escape(t["all_sub"])}</div></div>'
         f'<div style="position:absolute;left:250px;top:470px;width:2200px;display:grid;'
         f'grid-template-columns:repeat(5,1fr);gap:50px 40px;align-items:start">{celdas}</div>')
    return pagina(c)


def p3_calendario(t, l):
    filas = list(csv.DictReader(CAL.open(encoding="utf-8")))[:7]
    col = "plantilla_en" if l == "en" else "plantilla_es"
    idea = "idea_en" if l == "en" else "idea_es"
    lineas = "".join(
        f'<div style="display:flex;gap:30px;align-items:center;background:#fff;border-radius:24px;padding:22px 34px;'
        f'margin-bottom:18px;box-shadow:0 8px 24px rgba(0,0,0,.07)">'
        f'<div style="min-width:150px;font-weight:700;color:{ACENTO};font-size:38px">{t["cal_dia"]} {r["dia"]}</div>'
        f'<div><div style="font-weight:700;font-size:38px">{escape(r[col])}</div>'
        f'<div style="font-size:28px;opacity:.7;margin-top:6px">{escape(r[idea])}</div></div></div>' for r in filas)
    c = (f'<div style="position:absolute;left:337px;top:420px;width:1300px">{lineas}'
         f'<div style="font-size:36px;font-weight:600;opacity:.6;padding-left:34px">{escape(t["cal_mas"])}</div></div>'
         f'<div style="position:absolute;left:1760px;top:760px;width:600px">'
         f'<h2 style="font-size:96px">{escape(t["cal"])}</h2>'
         f'<p style="font-size:44px;line-height:1.4;opacity:.8">{escape(t["cal_sub"])}</p>'
         f'{chip("PDF · " + t["bil"])}</div>')
    return pagina(c)


def p4_bilingue(t, l):
    a, b = ("en", "es") if l == "en" else ("es", "en")
    lbl = {"es": t["es_lbl"], "en": t["en_lbl"]}
    c = (f'<div class="centro" style="top:90px;text-align:center"><h2 style="font-size:108px">{escape(t["two"])}</h2>'
         f'<div style="font-size:46px;opacity:.75;margin-top:14px">{escape(t["two_sub"])}</div></div>'
         f'<div class="centro" style="top:470px;display:flex;gap:90px;justify-content:center">'
         + "".join(f'<div style="text-align:center">{post(f"p1b_navy_{x}.svg", 900)}'
                   f'<div style="margin-top:40px">{chip(lbl[x], 48)}</div></div>' for x in (a, b))
         + '</div>')
    return pagina(c)


def p5_stories(t, l):
    st = ["p9_1_beige", "p9_2_beige", "p2story_navy", "p2storyb_salvia"]
    c = (f'<div class="centro" style="top:80px;text-align:center"><h2 style="font-size:104px">{escape(t["st"])}</h2>'
         f'<div style="font-size:44px;opacity:.75;margin-top:12px">{escape(t["st_sub"])}</div></div>'
         f'<div style="position:absolute;left:240px;top:400px;display:flex;gap:36px">'
         + "".join(post(f"{s}_{l}.svg", 400, "border-radius:28px;overflow:hidden") for s in st)
         + f'</div><div style="position:absolute;left:1980px;top:560px">{post(f"p10_salvia_{l}.svg", 520)}</div>')
    return pagina(c)


def p6_paletas(t, l):
    c = (f'<div class="centro" style="top:300px;text-align:center"><h2 style="font-size:116px">{escape(t["pal"])}</h2>'
         f'<div style="font-size:46px;opacity:.75;margin-top:16px">{escape(t["pal_sub"])}</div></div>'
         f'<div class="centro" style="top:700px;display:flex;gap:60px;justify-content:center">'
         + "".join(post(f"p8b_{p}_{l}.svg", 620) for p in ("beige", "navy", "salvia")) + '</div>')
    return pagina(c)


def p7_incluye(t, l):
    items = "".join(f'<li style="margin:0 0 32px;padding-left:80px;position:relative">'
                    f'<span style="position:absolute;left:0;color:{ACENTO};font-weight:700">✓</span>{escape(i)}</li>'
                    for i in t["inc_items"])
    c = (f'<div style="position:absolute;left:337px;top:470px;width:560px;transform:rotate(-4deg)" class="post">'
         f'{svg(f"p6_1_beige_{l}.svg")}</div>'
         f'<div style="position:absolute;left:1040px;top:420px;width:1330px">'
         f'<h2 style="font-size:124px;margin-bottom:60px">{escape(t["inc"])}</h2>'
         f'<ul style="list-style:none;padding:0;margin:0;font-size:50px;font-weight:600">{items}</ul>'
         f'<p style="font-size:36px;opacity:.65;margin-top:44px">{escape(t["inc_note"])}</p></div>')
    return pagina(c)


MOCKUPS = [("1_portada", p1_portada), ("2_todo", p2_todo), ("3_calendario", p3_calendario),
           ("4_bilingue", p4_bilingue), ("5_stories", p5_stories), ("6_paletas", p6_paletas),
           ("7_incluye", p7_incluye)]


def main():
    OUT.mkdir(exist_ok=True)
    for l, t in TXT.items():
        for nombre, f in MOCKUPS:
            (OUT / f"pack_{nombre}_{l}.html").write_text(f(t, l), encoding="utf-8")
    print(f"{len(MOCKUPS) * len(TXT)} mockups HTML del pack en {OUT}")


if __name__ == "__main__":
    sys.exit(main())
