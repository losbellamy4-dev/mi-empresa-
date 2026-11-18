#!/usr/bin/env python3
"""Maquetas de referencia (SVG) de las plantillas #1–#4 del pack de inmobiliarias.

Día 11 (2026-11-18). Sirven para que Adrián monte cada diseño en Canva con las
medidas, colores y tipografías exactas. No son el producto final: el producto es
la plantilla de Canva (ver ../../investigacion/12_ESPEC_PACK_INMOBILIARIAS.md).

Uso:  python3 maquetas.py      → genera svg/*.svg + index.html en esta carpeta.
Solo librería estándar.
"""
from pathlib import Path
from html import escape

AQUI = Path(__file__).resolve().parent
SVG_DIR = AQUI / "svg"

# Tipografías gratuitas en Canva y en Google Fonts (mismo nombre en ambos sitios)
SERIF = "Playfair Display"
SANS = "Montserrat"

PALETAS = {
    "beige": {"nombre": "Neutra beige/negro", "fondo": "#F3EDE4", "tinta": "#1E1E1E",
              "acento": "#B08D57", "suave": "#E2D6C3", "sobre_acento": "#FFFFFF"},
    "navy": {"nombre": "Azul marino/blanco", "fondo": "#FFFFFF", "tinta": "#14213D",
             "acento": "#14213D", "suave": "#DCE3EE", "sobre_acento": "#FFFFFF"},
    "salvia": {"nombre": "Verde salvia", "fondo": "#F4F6F1", "tinta": "#2F3A2F",
               "acento": "#7D9471", "suave": "#DCE5D5", "sobre_acento": "#FFFFFF"},
}

TXT = {
    "es": {
        "nuevo": "NUEVO EN CARTERA", "piso": "Piso de 3 hab. · [Barrio]",
        "precio": "[Precio] €", "datos": "3 hab · 2 baños · 95 m²",
        "contacto": "[Nombre de la agencia] · [teléfono]", "foto": "FOTO DEL INMUEBLE",
        "abiertas1": "PUERTAS", "abiertas2": "ABIERTAS", "fecha": "Sábado [día] · [hora]",
        "direccion": "[Calle y número], [ciudad]", "ven": "¡Te esperamos!",
        "vendido": "¡VENDIDO!", "gracias": "Gracias, [nombre del cliente]",
        "reservado": "RESERVADO", "pronto": "Pronto tendrá nuevos dueños",
        "desliza": "Desliza para ver más →",
    },
    "en": {
        "nuevo": "JUST LISTED", "piso": "3-bed apartment · [Neighborhood]",
        "precio": "$[Price]", "datos": "3 bd · 2 ba · 1,020 sq ft",
        "contacto": "[Agency name] · [phone]", "foto": "PROPERTY PHOTO",
        "abiertas1": "OPEN", "abiertas2": "HOUSE", "fecha": "Saturday [date] · [time]",
        "direccion": "[Street address], [city]", "ven": "See you there!",
        "vendido": "JUST SOLD!", "gracias": "Thank you, [client name]",
        "reservado": "UNDER CONTRACT", "pronto": "Soon to have new owners",
        "desliza": "Swipe to see more →",
    },
}

POST = (1080, 1350)
STORY = (1080, 1920)


def foto(x, y, w, h, p, t, r=0):
    """Hueco de foto: rectángulo con rayado y etiqueta (en Canva = marco de foto)."""
    pid = f"h{x}{y}{w}"
    return (
        f'<defs><pattern id="{pid}" width="28" height="28" patternUnits="userSpaceOnUse" '
        f'patternTransform="rotate(45)"><rect width="28" height="28" fill="{p["suave"]}"/>'
        f'<line x1="0" y1="0" x2="0" y2="28" stroke="{p["fondo"]}" stroke-width="6"/></pattern></defs>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="url(#{pid})"/>'
        f'<text x="{x + w / 2}" y="{y + h / 2}" text-anchor="middle" dominant-baseline="middle" '
        f'font-family="{SANS}, sans-serif" font-size="30" font-weight="600" letter-spacing="4" '
        f'fill="{p["tinta"]}" opacity=".55">{escape(t["foto"])}</text>'
    )


def texto(x, y, s, size, p, fam=SANS, weight=400, anchor="start", color=None, ls=0, op=1):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{fam}, '
            f'{"serif" if fam == SERIF else "sans-serif"}" font-size="{size}" font-weight="{weight}" '
            f'letter-spacing="{ls}" fill="{color or p["tinta"]}" opacity="{op}">{escape(s)}</text>')


def logo(x, y, p):
    """Hueco de logotipo: siempre en la misma posición (abajo a la izquierda)."""
    return (f'<rect x="{x}" y="{y}" width="150" height="60" rx="6" fill="none" '
            f'stroke="{p["tinta"]}" stroke-width="2" stroke-dasharray="8 6" opacity=".6"/>'
            + texto(x + 75, y + 38, "LOGO", 22, p, weight=600, anchor="middle", ls=3, op=.6))


def svg(w, h, cuerpo, p):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<rect width="{w}" height="{h}" fill="{p["fondo"]}"/>{cuerpo}</svg>')


# ---------- Plantillas ----------

def p1a(p, t):  # Just Listed — foto grande arriba, franja de texto abajo
    W, H = POST
    c = foto(0, 0, W, 860, p, t)
    ancho = int(len(t["nuevo"]) * 38 + 70)  # la franja crece con el texto (ES es más largo)
    c += f'<rect x="60" y="800" width="{ancho}" height="110" fill="{p["acento"]}"/>'
    c += texto(90, 875, t["nuevo"], 46, p, weight=700, color=p["sobre_acento"], ls=5)
    c += texto(60, 1010, t["piso"], 52, p, fam=SERIF, weight=700)
    c += texto(60, 1080, t["datos"], 34, p, op=.8)
    c += texto(W - 60, 1180, t["precio"], 72, p, fam=SERIF, weight=700, anchor="end", color=p["acento"])
    c += logo(60, 1230, p) + texto(W - 60, 1270, t["contacto"], 28, p, anchor="end", op=.8)
    return svg(W, H, c, p)


def p1b(p, t):  # Just Listed — marco con margen y titular serif centrado
    W, H = POST
    c = texto(W / 2, 150, t["nuevo"], 84, p, fam=SERIF, weight=700, anchor="middle", ls=2)
    c += f'<line x1="390" y1="190" x2="690" y2="190" stroke="{p["acento"]}" stroke-width="4"/>'
    c += foto(80, 240, W - 160, 760, p, t, r=12)
    c += texto(W / 2, 1090, t["piso"], 46, p, weight=600, anchor="middle")
    c += texto(W / 2, 1150, t["datos"] + "  |  " + t["precio"], 34, p, anchor="middle", color=p["acento"], weight=600)
    c += logo(80, 1230, p) + texto(W - 80, 1270, t["contacto"], 28, p, anchor="end", op=.8)
    return svg(W, H, c, p)


def p2_post(p, t):  # Open House — post
    W, H = POST
    c = foto(0, 0, W, H, p, t)
    c += f'<rect x="80" y="420" width="{W - 160}" height="560" fill="{p["fondo"]}" opacity=".94"/>'
    c += texto(W / 2, 560, t["abiertas1"], 110, p, fam=SERIF, weight=700, anchor="middle")
    c += texto(W / 2, 680, t["abiertas2"], 110, p, fam=SERIF, weight=700, anchor="middle", color=p["acento"])
    c += texto(W / 2, 790, t["fecha"], 40, p, weight=600, anchor="middle")
    c += texto(W / 2, 860, t["direccion"], 32, p, anchor="middle", op=.8)
    c += texto(W / 2, 930, t["ven"], 32, p, anchor="middle", weight=600, color=p["acento"])
    c += f'<rect x="0" y="1200" width="{W}" height="150" fill="{p["fondo"]}"/>'
    c += logo(80, 1245, p) + texto(W - 80, 1285, t["contacto"], 28, p, anchor="end", op=.8)
    return svg(W, H, c, p)


def p2_story(p, t):  # Open House — story (zonas seguras: 250 px arriba y abajo)
    W, H = STORY
    c = foto(0, 0, W, 1100, p, t)
    c += f'<rect x="0" y="1060" width="{W}" height="860" fill="{p["fondo"]}"/>'
    c += texto(W / 2, 1230, t["abiertas1"] + " " + t["abiertas2"], 100, p, fam=SERIF, weight=700, anchor="middle")
    c += f'<rect x="240" y="1290" width="600" height="90" rx="45" fill="{p["acento"]}"/>'
    c += texto(W / 2, 1350, t["fecha"], 36, p, weight=600, anchor="middle", color=p["sobre_acento"])
    c += texto(W / 2, 1460, t["direccion"], 36, p, anchor="middle", op=.85)
    c += texto(W / 2, 1560, t["desliza"], 32, p, anchor="middle", weight=600, color=p["acento"])
    c += logo(W / 2 - 75, 1600, p)
    # guías de zona segura (no se imprimen en Canva: solo referencia)
    c += (f'<rect x="0" y="0" width="{W}" height="250" fill="#E4572E" opacity=".10"/>'
          f'<rect x="0" y="{H - 250}" width="{W}" height="250" fill="#E4572E" opacity=".10"/>')
    return svg(W, H, c, p)


def p_sello(p, t, clave_titulo, clave_sub):  # #3 Vendido y #4 Reservado (misma maqueta)
    W, H = POST
    c = foto(0, 0, W, H, p, t)
    c += f'<rect x="0" y="0" width="{W}" height="{H}" fill="{p["tinta"]}" opacity=".25"/>'
    c += (f'<g transform="rotate(-8 540 600)"><rect x="110" y="480" width="860" height="240" '
          f'fill="{p["acento"]}"/>' + texto(540, 640, t[clave_titulo], 104 if len(t[clave_titulo]) < 11 else 68,
                                             p, fam=SERIF, weight=700, anchor="middle",
                                             color=p["sobre_acento"], ls=3) + '</g>')
    c += f'<rect x="0" y="1060" width="{W}" height="290" fill="{p["fondo"]}"/>'
    c += texto(W / 2, 1150, t[clave_sub], 44, p, fam=SERIF, weight=700, anchor="middle")
    c += texto(W / 2, 1205, t["piso"], 30, p, anchor="middle", op=.8)
    c += logo(80, 1250, p) + texto(W - 80, 1290, t["contacto"], 28, p, anchor="end", op=.8)
    return svg(W, H, c, p)


PLANTILLAS = [
    ("1a", "#1 Nuevo en cartera / Just Listed — diseño A", "post", p1a),
    ("1b", "#1 Nuevo en cartera / Just Listed — diseño B", "post", p1b),
    ("2post", "#2 Puertas abiertas / Open House — post", "post", p2_post),
    ("2story", "#2 Puertas abiertas / Open House — story", "story", p2_story),
    ("3", "#3 Vendido / Just Sold", "post", lambda p, t: p_sello(p, t, "vendido", "gracias")),
    ("4", "#4 Reservado / Under Contract", "post", lambda p, t: p_sello(p, t, "reservado", "pronto")),
]


def main():
    SVG_DIR.mkdir(exist_ok=True)
    n = 0
    for clave, _, _, f in PLANTILLAS:
        for pal, p in PALETAS.items():
            for lang, t in TXT.items():
                (SVG_DIR / f"p{clave}_{pal}_{lang}.svg").write_text(f(p, t), encoding="utf-8")
                n += 1
    escribir_index()
    print(f"{n} SVG generados en {SVG_DIR}")


def escribir_index():
    filas_pal = "".join(
        f'<tr><td>{escape(p["nombre"])}</td>' + "".join(
            f'<td><span class="sw" style="background:{p[k]}"></span><code>{p[k]}</code></td>'
            for k in ("fondo", "tinta", "acento", "suave")) + "</tr>"
        for p in PALETAS.values())
    tarjetas = []
    for clave, nombre, fmt, _ in PLANTILLAS:
        dims = "1080×1350" if fmt == "post" else "1080×1920"
        imgs = "".join(
            f'<figure data-lang="{lang}"><img loading="lazy" src="svg/p{clave}_{pal}_{lang}.svg" '
            f'alt="{escape(nombre)} · {pal} · {lang.upper()}"><figcaption>{pal} · {lang.upper()}</figcaption></figure>'
            for pal in PALETAS for lang in TXT)
        tarjetas.append(f'<section><h2>{escape(nombre)}</h2><p class="meta">{dims} px</p>'
                        f'<div class="grid {fmt}">{imgs}</div></section>')
    html = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Maquetas pack inmobiliarias</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#fafaf8;--fg:#1b1b1b;--mut:#666;--line:#ddd}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#151515;--fg:#eee;--mut:#aaa;--line:#333}}}}
:root[data-theme="dark"]{{--bg:#151515;--fg:#eee;--mut:#aaa;--line:#333}}
body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 Montserrat,system-ui,sans-serif}}
main{{max-width:1100px;margin:auto;padding:24px 16px}}
h1{{font-family:'Playfair Display',serif}} .meta{{color:var(--mut);margin-top:-8px}}
table{{border-collapse:collapse;font-size:14px;width:100%;overflow-x:auto;display:block}}
td,th{{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;white-space:nowrap}}
.sw{{display:inline-block;width:14px;height:14px;border:1px solid var(--line);vertical-align:middle;margin-right:6px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}}
figure{{margin:0}} img{{width:100%;height:auto;border:1px solid var(--line);display:block}}
figcaption{{font-size:12px;color:var(--mut)}}
.filtro button{{font:inherit;padding:6px 12px;margin-right:6px;border:1px solid var(--line);background:none;color:inherit;border-radius:6px;cursor:pointer}}
</style></head><body><main>
<h1>Maquetas de referencia: plantillas #1–#4</h1>
<p>Referencia para montar cada diseño en Canva (Día 11). <strong>No son el producto</strong>: el producto es la plantilla de Canva.
Las fotos rayadas son huecos (marcos de foto en Canva); no se incluyen fotos. Especificación completa: <code>investigacion/12_ESPEC_PACK_INMOBILIARIAS.md</code>.</p>
<h2>Tipografías (gratis en Canva)</h2>
<p><span style="font-family:'Playfair Display',serif;font-weight:700;font-size:22px">Playfair Display Bold</span> para titulares ·
<span style="font-family:Montserrat;font-size:18px">Montserrat</span> 400/600/700 para el texto.</p>
<h2>Paletas</h2>
<table><tr><th>Paleta</th><th>Fondo</th><th>Tinta</th><th>Acento</th><th>Suave</th></tr>{filas_pal}</table>
<h2>Reglas comunes</h2>
<ul><li>Margen lateral 60–80 px. Logotipo siempre abajo a la izquierda (150×60 px) y contacto abajo a la derecha (28 px).</li>
<li>Stories: deja libres 250 px arriba y abajo (zona roja de la maqueta), porque Instagram los tapa con su interfaz.</li>
<li>Montaje en Canva: diseño personalizado con las medidas exactas → colores con el código hex → marcos de foto → "Compartir → Enlace de plantilla".</li></ul>
<p class="filtro">Idioma: <button data-f="all">Todos</button><button data-f="es">ES</button><button data-f="en">EN</button></p>
{''.join(tarjetas)}
</main>
<script>
document.querySelectorAll('.filtro button').forEach(b=>b.onclick=()=>{{
 document.querySelectorAll('figure').forEach(f=>f.style.display=(b.dataset.f==='all'||f.dataset.lang===b.dataset.f)?'':'none');}});
</script></body></html>"""
    (AQUI / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
