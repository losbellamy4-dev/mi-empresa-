#!/usr/bin/env python3
"""Guía del comprador (PDF, ES + EN) del Kit de Instagram para Inmobiliarias — Día 19.

Es el PDF que se descarga tras la compra (Etsy/Payhip). Contiene los enlaces de plantilla
de Canva (🔴 marcadores: los pone Adrián cuando cree las plantillas en Canva) y los pasos
para editar. Uso: python3 guia.py && node pdf.js  → guia_es.pdf, guia_en.pdf
"""
from html import escape
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ACENTO, TINTA, FONDO = "#B08D57", "#1E1E1E", "#F3EDE4"

# Grupos de plantillas: (clave, nombre ES, nombre EN, n.º diseños)
GRUPOS = [("just-listed", "Nuevo en cartera", "Just Listed", 4), ("open-house", "Puertas abiertas (post + story)", "Open House (post + story)", 4),
          ("just-sold", "Vendido", "Just Sold", 2), ("under-contract", "Reservado", "Under Contract", 2),
          ("price-reduced", "Bajada de precio", "Price Reduced", 2), ("tips", "Carrusel de consejos (7 diapositivas)", "Tips carousel (7 slides)", 1),
          ("testimonial", "Testimonio", "Testimonial", 2), ("meet", "Preséntate", "Meet the Agent", 2),
          ("tour", "Stories de visita", "Property tour stories", 3), ("highlights", "Portadas de destacadas (12 iconos)", "Highlight covers (12 icons)", 12)]

T = {
    "es": {
        "titulo": "Kit de Instagram para Inmobiliarias", "sub": "Guía rápida y enlaces a tus plantillas",
        "gracias": "¡Gracias por tu compra! En 10 minutos tendrás tu primera publicación lista.",
        "p_titulo": "Cómo usar tus plantillas en 5 pasos",
        "pasos": [
            ("Abre un enlace", "Haz clic en una de las plantillas de la tabla. Se abre Canva en tu navegador. Si no tienes cuenta, crea una <b>gratuita</b>: es suficiente."),
            ("Pulsa «Usar plantilla»", "Canva crea una <b>copia en tu cuenta</b>. Lo que cambies es tuyo; el original no se toca y puedes volver a usarlo cuantas veces quieras."),
            ("Cambia la foto", "Arrastra la foto de tu inmueble encima del hueco de la foto. Se recorta sola. Doble clic para moverla o ajustarla."),
            ("Escribe tus datos", "Haz clic en cualquier texto entre corchetes, por ejemplo [Barrio] o [Precio], y cámbialo. Pon tu logo en la caja LOGO."),
            ("Descarga y publica", "Compartir → Descargar → PNG. Publícala en Instagram. Para el carrusel, descarga todas las páginas y súbelas juntas."),
        ],
        "col_t": "Tus plantillas", "col_d": "Diseños", "col_l": "Enlace",
        "enlace": "Abrir en Canva", "pend": "[enlace pendiente]",
        "idioma": "Cada enlace incluye la versión en español y en inglés, en páginas separadas dentro del mismo diseño.",
        "trucos_t": "Trucos", "trucos": [
            "<b>Tus colores:</b> pulsa un color y elige el de tu marca. Con «Cambiar todo» se cambia en todo el diseño a la vez.",
            "<b>3 paletas:</b> cada plantilla viene en beige, azul marino y verde salvia. Elige una y úsala siempre igual para que tu perfil se vea coherente.",
            "<b>Calendario:</b> abre el PDF «Calendario de 30 días». Te dice qué plantilla publicar cada día. Empieza por el día 1.",
            "<b>Fotos:</b> usa fotos propias o de bancos con licencia comercial gratuita. Las fotos de las imágenes de muestra no están incluidas.",
        ],
        "aviso_t": "Importante",
        "aviso": "Las plantillas traen textos de ejemplo. Tú eres responsable de que los datos de tus anuncios sean correctos y de cumplir la normativa de publicidad inmobiliaria de tu zona. Los testimonios deben ser opiniones reales de tus clientes, publicadas con su permiso.",
        "licencia_t": "Licencia",
        "licencia": "Puedes usar las plantillas para tu propio negocio o tu agencia (todo el equipo), sin límite de publicaciones. No puedes revender ni compartir las plantillas (ni sus enlaces) como plantillas, ni gratis ni de pago.",
        "ayuda": "¿Dudas o algún enlace no funciona? Escríbenos desde la tienda donde compraste y te respondemos.",
    },
    "en": {
        "titulo": "Real Estate Instagram Kit", "sub": "Quick start guide and your template links",
        "gracias": "Thank you for your purchase! Your first post can be ready in 10 minutes.",
        "p_titulo": "How to use your templates in 5 steps",
        "pasos": [
            ("Open a link", "Click one of the templates in the table. Canva opens in your browser. If you don't have an account, create a <b>free</b> one: that's all you need."),
            ("Click “Use template”", "Canva makes a <b>copy in your account</b>. Your changes are yours; the original stays untouched and you can reuse it as often as you like."),
            ("Swap the photo", "Drag your listing photo onto the photo frame. It crops automatically. Double-click to move or resize it."),
            ("Type your details", "Click any text in brackets, such as [Neighborhood] or [Price], and replace it. Put your logo in the LOGO box."),
            ("Download and post", "Share → Download → PNG. Post it on Instagram. For the carousel, download all pages and upload them together."),
        ],
        "col_t": "Your templates", "col_d": "Designs", "col_l": "Link",
        "enlace": "Open in Canva", "pend": "[link pending]",
        "idioma": "Every link includes the English and the Spanish version, on separate pages of the same design.",
        "trucos_t": "Tips", "trucos": [
            "<b>Your colors:</b> click a color and pick your brand color. “Change all” updates it across the whole design.",
            "<b>3 palettes:</b> every template comes in beige, navy and sage. Pick one and stick to it so your feed looks consistent.",
            "<b>Calendar:</b> open the “30-Day Posting Calendar” PDF. It tells you which template to post each day. Start with day 1.",
            "<b>Photos:</b> use your own photos or free stock photos with a commercial license. Photos shown in the previews are not included.",
        ],
        "aviso_t": "Important",
        "aviso": "Templates contain example text. You are responsible for the accuracy of your listings and for following your local real estate advertising rules. Testimonials must be real reviews from your clients, posted with their permission.",
        "licencia_t": "License",
        "licencia": "You may use the templates for your own business or your agency (whole team), with unlimited posts. You may not resell or share the templates (or their links) as templates, free or paid.",
        "ayuda": "Questions, or a link not working? Message us through the shop where you bought and we'll help.",
    },
}

# 🔴 Adrián: pega aquí los enlaces de plantilla de Canva (Compartir → Enlace de plantilla).
ENLACES = {k: "" for k, *_ in GRUPOS}


def html(l):
    t = T[l]
    pasos = "".join(f'<li><span class="n">{i}</span><div><b>{escape(a)}</b><br>{b}</div></li>'
                    for i, (a, b) in enumerate(t["pasos"], 1))
    filas = "".join(
        f'<tr><td>{escape(es if l == "es" else en)}</td><td class="c">{n}</td><td>'
        + (f'<a href="{escape(ENLACES[k])}">{t["enlace"]} →</a>' if ENLACES[k] else f'<span class="pend">{t["pend"]}</span>')
        + '</td></tr>' for k, es, en, n in GRUPOS)
    trucos = "".join(f"<li>{x}</li>" for x in t["trucos"])
    return f"""<!doctype html><html lang="{l}"><head><meta charset="utf-8"><title>{escape(t['titulo'])}</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
<style>
@page{{size:A4;margin:16mm 16mm}}
body{{font-family:Montserrat,sans-serif;color:{TINTA};font-size:10.5pt;line-height:1.5;margin:0}}
h1,h2{{font-family:'Playfair Display',serif;margin:0}} h1{{font-size:26pt}} h2{{font-size:15pt;margin:18px 0 8px}}
.cab{{background:{FONDO};padding:18px 22px;border-radius:10px}} .sub{{color:{ACENTO};font-weight:700;letter-spacing:1px;text-transform:uppercase;font-size:9pt}}
ol{{list-style:none;padding:0;margin:0}} ol li{{display:flex;gap:12px;margin:0 0 9px}}
.n{{flex:none;width:24px;height:24px;border-radius:50%;background:{ACENTO};color:#fff;font-weight:700;text-align:center;line-height:24px;font-size:10pt}}
table{{width:100%;border-collapse:collapse;font-size:10pt}} th{{text-align:left;border-bottom:2px solid {TINTA};padding:5px 6px}}
td{{border-bottom:1px solid #E3DBCF;padding:5px 6px}} .c{{text-align:center}} a{{color:{ACENTO};font-weight:700;text-decoration:none}}
.pend{{color:#B33;font-weight:700}} .nota{{font-size:9pt;opacity:.75;margin-top:6px}}
ul{{padding-left:18px;margin:0}} ul li{{margin-bottom:5px}}
.caja{{border:1px solid #E3DBCF;border-radius:8px;padding:10px 14px;margin-top:12px;font-size:9.5pt}}
.salto{{break-before:page}}
</style></head><body>
<div class="cab"><div class="sub">{escape(t['sub'])}</div><h1>{escape(t['titulo'])}</h1><div>{escape(t['gracias'])}</div></div>
<h2>{escape(t['p_titulo'])}</h2><ol>{pasos}</ol>
<h2>{escape(t['col_t'])}</h2>
<table><tr><th>{escape(t['col_t'])}</th><th class="c">{escape(t['col_d'])}</th><th>{escape(t['col_l'])}</th></tr>{filas}</table>
<div class="nota">{escape(t['idioma'])}</div>
<div class="salto"></div>
<h2>{escape(t['trucos_t'])}</h2><ul>{trucos}</ul>
<div class="caja"><b>{escape(t['aviso_t'])}.</b> {escape(t['aviso'])}</div>
<div class="caja"><b>{escape(t['licencia_t'])}.</b> {escape(t['licencia'])}</div>
<p class="nota">{escape(t['ayuda'])}</p>
</body></html>"""


if __name__ == "__main__":
    assert sum(n for *_, n in GRUPOS) == 34, "el pack promete 34 diseños"
    for l in T:
        (AQUI / f"guia_{l}.html").write_text(html(l), encoding="utf-8")
    print("guia_es.html, guia_en.html")
