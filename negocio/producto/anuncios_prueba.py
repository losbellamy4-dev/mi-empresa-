"""Genera y valida los textos de los 5 anuncios de prueba de Etsy-EN (Día 10).
Límites de Etsy [S: ayuda de Etsy]: título ≤ 140 caracteres, 13 etiquetas de ≤ 20 caracteres.
Uso: python3 anuncios_prueba.py  → escribe ANUNCIOS_PRUEBA.md
"""
from pathlib import Path

COMUN_EN = ("**What you get:** a PDF with your Canva template link(s) and a 1-page how-to guide. "
            "Click the link, the template opens in your own Canva account (a FREE Canva account works), "
            "then change photos, colors, fonts and text in minutes.\n\n"
            "**Sizes:** Instagram post 1080×1350 px (4:5){extra}.\n\n"
            "**Please note:** this is a digital product, nothing will be shipped. Property photos in the previews are "
            "placeholders and are NOT included. Templates contain example text only; you are responsible for the "
            "accuracy of your listings and for following your local advertising rules.\n\n"
            "**Want the full set?** See the bundle in our shop.")
COMUN_ES = ("**Qué recibes:** un PDF con el enlace a tu plantilla de Canva y una guía de 1 página. "
            "Abres el enlace, la plantilla se copia en tu cuenta de Canva (vale la GRATUITA) y cambias fotos, colores, "
            "tipografías y textos en minutos.\n\n"
            "**Formatos:** post de Instagram 1080×1350 px (4:5){extra}.\n\n"
            "**Importante:** producto digital, no se envía nada físico. Las fotos de inmuebles de las imágenes de muestra "
            "NO están incluidas. Las plantillas llevan textos de ejemplo; la exactitud de tus anuncios y el cumplimiento "
            "de la normativa de publicidad inmobiliaria de tu zona son responsabilidad tuya.")

ANUNCIOS = [
    {"id": 1, "precio": "9 $",
     "titulo_en": "Just Listed Instagram Post Templates for Real Estate Agents | 4 Editable Canva Designs | Realtor Social Media New Listing",
     "titulo_es": "Plantillas Instagram Nuevo en Cartera para Inmobiliarias | 4 Diseños Editables en Canva | Redes Sociales Agente Inmobiliario",
     "gancho_en": "Announce every new listing with a clean, professional post your clients will notice. 4 designs × 3 color palettes (beige, navy, sage).",
     "gancho_es": "Anuncia cada inmueble nuevo con un post limpio y profesional. 4 diseños × 3 paletas (beige, azul marino, verde salvia).",
     "extra_en": "", "extra_es": "",
     "tags": ["just listed", "real estate canva", "realtor instagram", "real estate post", "new listing post",
              "realtor template", "real estate agent", "canva template", "realtor marketing", "listing template",
              "real estate social", "realtor branding", "instagram template"]},
    {"id": 2, "precio": "9 $",
     "titulo_en": "Open House Instagram Post & Story Templates | Real Estate Canva Template | Realtor Open House Flyer for Social Media",
     "titulo_es": "Plantillas Jornada de Puertas Abiertas para Instagram | Post y Story | Plantilla Canva Inmobiliaria",
     "gancho_en": "Fill your open house: 2 posts + 2 matching stories with date, time and address placeholders.",
     "gancho_es": "Llena tu jornada de puertas abiertas: 2 posts + 2 stories a juego con huecos para fecha, hora y dirección.",
     "extra_en": " and Instagram story 1080×1920 px", "extra_es": " y story 1080×1920 px",
     "tags": ["open house", "open house template", "open house post", "real estate canva", "realtor instagram",
              "real estate story", "realtor template", "open house flyer", "real estate agent", "canva template",
              "realtor marketing", "instagram story", "real estate post"]},
    {"id": 3, "precio": "7 $",
     "titulo_en": "Just Sold & Under Contract Instagram Templates | Real Estate Canva Post | Realtor Social Media Sold Announcement",
     "titulo_es": "Plantillas Vendido y Reservado para Instagram | Post Canva para Inmobiliarias | Anuncio de Venta",
     "gancho_en": "Celebrate every closing and build trust: 2 'Just Sold' + 2 'Under Contract' designs.",
     "gancho_es": "Celebra cada operación y genera confianza: 2 diseños 'Vendido' + 2 'Reservado'.",
     "extra_en": "", "extra_es": "",
     "tags": ["just sold", "under contract", "sold post", "real estate canva", "realtor instagram",
              "real estate post", "realtor template", "sold sign post", "real estate agent", "canva template",
              "realtor marketing", "closing post", "real estate social"]},
    {"id": 4, "precio": "9 $",
     "titulo_en": "Real Estate Tips Carousel Templates | 2 Instagram Carousels for Realtors | Editable Canva Buyer & Seller Tips Post",
     "titulo_es": "Plantillas Carrusel de Consejos Inmobiliarios | 2 Carruseles de Instagram | Canva Editable para Agentes",
     "gancho_en": "Educational content that gets saved and shared: 2 carousels × 7 slides with example tips you can rewrite.",
     "gancho_es": "Contenido que se guarda y se comparte: 2 carruseles × 7 diapositivas con consejos de ejemplo que puedes reescribir.",
     "extra_en": ", 7-slide carousels", "extra_es": ", carruseles de 7 diapositivas",
     "tags": ["real estate tips", "realtor carousel", "carousel template", "real estate canva", "realtor instagram",
              "buyer tips", "seller tips", "realtor template", "real estate agent", "canva template",
              "realtor marketing", "instagram carousel", "real estate post"]},
    {"id": 5, "precio": "24 $ (en vez de 34 $ por separado)",
     "titulo_en": "Real Estate Instagram Template Bundle | Just Listed, Open House, Just Sold, Tips Carousel | Realtor Canva Social Media Kit",
     "titulo_es": "Pack de Plantillas Instagram para Inmobiliarias | Nuevo, Puertas Abiertas, Vendido, Consejos | Kit Canva",
     "gancho_en": "Everything from listings 1–4 in one kit: 16 designs + 2 carousels, 3 palettes. Save 30% vs. buying separately.",
     "gancho_es": "Todo lo de los anuncios 1–4 en un kit: 16 diseños + 2 carruseles, 3 paletas. Ahorra un 30 % frente a comprarlos por separado.",
     "extra_en": ", Instagram story 1080×1920 px and 7-slide carousels", "extra_es": ", story 1080×1920 px y carruseles de 7 diapositivas",
     "tags": ["realtor bundle", "real estate bundle", "real estate canva", "realtor instagram", "social media kit",
              "realtor template", "real estate agent", "just listed", "open house", "just sold",
              "canva template", "realtor marketing", "real estate post"]},
]


def validar(a):
    errores = []
    for k in ("titulo_en", "titulo_es"):
        if len(a[k]) > 140:
            errores.append(f"{k}: {len(a[k])} > 140")
    if len(a["tags"]) != 13 or len(set(a["tags"])) != 13:
        errores.append(f"tags: {len(a['tags'])} (únicas {len(set(a['tags']))})")
    errores += [f"tag '{t}' {len(t)} > 20" for t in a["tags"] if len(t) > 20]
    return errores


def main():
    md = ["# Textos de los 5 anuncios de prueba de Etsy (EN principal + ES) — Día 10", "",
          "> Generado por `anuncios_prueba.py` (valida límites de Etsy: título ≤ 140, 13 etiquetas ≤ 20). "
          "Plan de la prueba: `../investigacion/11_PLAN_VALIDACION_ETSY_EN.md`. Diseños: `../investigacion/12_ESPEC_PACK_INMOBILIARIAS.md`.",
          "> 🔴 Publicar en Etsy (cuenta, 0,20 $ por anuncio) lo hace **un adulto titular**. Textos sin afirmaciones legales ni de resultados (F8).",
          "> Etsy muestra el anuncio en inglés al comprador de EE. UU./R. U.; la versión ES se puede añadir como traducción en el mismo anuncio.", ""]
    for a in ANUNCIOS:
        err = validar(a)
        assert not err, (a["id"], err)
        md += [f"## {a['id']}. {a['titulo_en'].split('|')[0].strip()} — {a['precio']}", "",
               f"**Title (EN, {len(a['titulo_en'])}/140):** {a['titulo_en']}", "",
               f"**Título (ES, {len(a['titulo_es'])}/140):** {a['titulo_es']}", "",
               "**Description (EN):**", "", a["gancho_en"], "", COMUN_EN.format(extra=a["extra_en"]), "",
               "**Descripción (ES):**", "", a["gancho_es"], "", COMUN_ES.format(extra=a["extra_es"]), "",
               "**13 tags:** " + " · ".join(f"`{t}`" for t in a["tags"]), ""]
    Path(__file__).with_name("ANUNCIOS_PRUEBA.md").write_text("\n".join(md), encoding="utf-8")
    print("OK: 5 anuncios validados")


if __name__ == "__main__":
    main()
