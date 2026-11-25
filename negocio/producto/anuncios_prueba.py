"""Genera y valida los textos de los 5 anuncios de prueba de Etsy-EN (Día 10; v2 Día 14: ancla = pack completo).
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
            "{upsell}")
COMUN_ES = ("**Qué recibes:** un PDF con el enlace a tu plantilla de Canva y una guía de 1 página. "
            "Abres el enlace, la plantilla se copia en tu cuenta de Canva (vale la GRATUITA) y cambias fotos, colores, "
            "tipografías y textos en minutos.\n\n"
            "**Formatos:** post de Instagram 1080×1350 px (4:5){extra}.\n\n"
            "**Importante:** producto digital, no se envía nada físico. Las fotos de inmuebles de las imágenes de muestra "
            "NO están incluidas. Las plantillas llevan textos de ejemplo; la exactitud de tus anuncios y el cumplimiento "
            "de la normativa de publicidad inmobiliaria de tu zona son responsabilidad tuya.")

UPSELL_EN = {False: "**Want everything?** The full bundle gives you all 34 designs + the 30-day calendar, in English & Spanish, for 22 $. Find it in our shop.",
             True: "**Why this bundle:** most kits give you designs; this one also tells you what to post each day, and every design comes in English and Spanish."}
UPSELL_ES = {False: "**¿Lo quieres todo?** El pack completo trae los 34 diseños + el calendario de 30 días, en español e inglés, por 22 $. Está en la tienda.",
             True: "**Por qué este pack:** la mayoría de kits solo traen diseños; este también te dice qué publicar cada día, y cada diseño viene en español e inglés."}

ANUNCIOS = [
    # Día 14: el ancla es el PACK BASE COMPLETO (15_ETSY_NUEVOS_ANUNCIOS.md §5). Los sueltos son puerta de entrada.
    {"id": 1, "precio": "22 $ (ancla)",
     "titulo_en": "Real Estate Instagram Templates Bundle | 34 Canva Designs + 30-Day Posting Calendar | English & Spanish | Realtor Social Media",
     "titulo_es": "Pack Plantillas Instagram Inmobiliaria | 34 Diseños Canva + Calendario de 30 Días | Español e Inglés | Redes Agente Inmobiliario",
     "gancho_en": "A complete, matching Instagram kit for real estate agents, plus a 30-day calendar that tells you which template to post each day. "
                  "34 designs × 3 color palettes (beige, navy, sage), every design in English AND Spanish (68 ready-to-edit Canva designs).\n\n"
                  "**Included:** Just Listed (4) · Open House post + story (4) · Just Sold (2) · Under Contract (2) · Price Reduced (2) · "
                  "Tips carousel, 7 slides (1) · Testimonial (2) · Meet the Agent (2) · Property tour stories (3) · Highlight covers (12 icons) · "
                  "30-Day Posting Calendar (PDF, EN + ES).",
     "gancho_es": "Un kit completo y a juego para inmobiliarias, con un calendario de 30 días que te dice qué plantilla publicar cada día. "
                  "34 diseños × 3 paletas (beige, azul marino, verde salvia), cada diseño en español E inglés (68 diseños editables).\n\n"
                  "**Incluye:** Nuevo en cartera (4) · Puertas abiertas post + story (4) · Vendido (2) · Reservado (2) · Bajada de precio (2) · "
                  "Carrusel de consejos, 7 diapositivas (1) · Testimonio (2) · Preséntate (2) · Stories de visita (3) · Portadas de destacadas (12 iconos) · "
                  "Calendario de 30 días (PDF, ES + EN).",
     "extra_en": ", Instagram story 1080×1920 px, highlight covers 1080×1080 px and a 7-slide carousel",
     "extra_es": ", story 1080×1920 px, portadas 1080×1080 px y un carrusel de 7 diapositivas",
     "ancla": True,
     "tags": ["realtor bundle", "real estate bundle", "real estate canva", "realtor instagram", "social media kit",
              "content calendar", "spanish realtor", "bilingual realtor", "just listed", "open house",
              "realtor template", "realtor marketing", "real estate post"]},
    {"id": 2, "precio": "5 $",
     "titulo_en": "Just Listed Instagram Post Templates for Real Estate Agents | 4 Editable Canva Designs | English & Spanish | New Listing",
     "titulo_es": "Plantillas Instagram Nuevo en Cartera para Inmobiliarias | 4 Diseños Editables en Canva | Español e Inglés",
     "gancho_en": "Announce every new listing with a clean, professional post. 4 designs × 3 color palettes, in English and Spanish.",
     "gancho_es": "Anuncia cada inmueble nuevo con un post limpio y profesional. 4 diseños × 3 paletas, en español e inglés.",
     "extra_en": "", "extra_es": "",
     "tags": ["just listed", "real estate canva", "realtor instagram", "real estate post", "new listing post",
              "realtor template", "real estate agent", "canva template", "realtor marketing", "listing template",
              "spanish realtor", "realtor branding", "instagram template"]},
    {"id": 3, "precio": "5 $",
     "titulo_en": "Open House Instagram Post & Story Templates | Real Estate Canva Template | English & Spanish | Realtor Open House Flyer",
     "titulo_es": "Plantillas Jornada de Puertas Abiertas para Instagram | Post y Story | Plantilla Canva Inmobiliaria | Español e Inglés",
     "gancho_en": "Fill your open house: 2 posts + 2 matching stories with date, time and address placeholders, in English and Spanish.",
     "gancho_es": "Llena tu jornada de puertas abiertas: 2 posts + 2 stories a juego con huecos para fecha, hora y dirección, en español e inglés.",
     "extra_en": " and Instagram story 1080×1920 px", "extra_es": " y story 1080×1920 px",
     "tags": ["open house", "open house template", "open house post", "real estate canva", "realtor instagram",
              "real estate story", "realtor template", "open house flyer", "real estate agent", "canva template",
              "realtor marketing", "instagram story", "spanish realtor"]},
    {"id": 4, "precio": "4 $",
     "titulo_en": "Just Sold & Under Contract Instagram Templates | Real Estate Canva Post | English & Spanish | Realtor Sold Announcement",
     "titulo_es": "Plantillas Vendido y Reservado para Instagram | Post Canva para Inmobiliarias | Español e Inglés",
     "gancho_en": "Celebrate every closing: 2 'Just Sold' + 2 'Under Contract' designs, in English and Spanish.",
     "gancho_es": "Celebra cada operación: 2 diseños 'Vendido' + 2 'Reservado', en español e inglés.",
     "extra_en": "", "extra_es": "",
     "tags": ["just sold", "under contract", "sold post", "real estate canva", "realtor instagram",
              "real estate post", "realtor template", "sold sign post", "real estate agent", "canva template",
              "realtor marketing", "closing post", "spanish realtor"]},
    {"id": 5, "precio": "6 $",
     "titulo_en": "Realtor 30-Day Instagram Posting Calendar + Tips Carousel Template | Real Estate Content Plan | Canva | English & Spanish",
     "titulo_es": "Calendario de 30 Días para Instagram Inmobiliario + Plantilla Carrusel de Consejos | Plan de Contenido | Canva",
     "gancho_en": "Never wonder what to post: a 30-day calendar with a post idea and goal for each day, plus a 7-slide tips carousel template. "
                  "The calendar refers to the templates in our full bundle, but works with any designs you already have.",
     "gancho_es": "Deja de pensar qué publicar: un calendario de 30 días con una idea y un objetivo para cada día, más una plantilla de carrusel de 7 diapositivas. "
                  "El calendario se refiere a las plantillas de nuestro pack completo, pero sirve con cualquier diseño que ya tengas.",
     "extra_en": ", 7-slide carousel; calendar as printable PDF (A4/Letter landscape)",
     "extra_es": ", carrusel de 7 diapositivas; calendario en PDF imprimible (A4 horizontal)",
     "tags": ["content calendar", "realtor calendar", "posting calendar", "real estate tips", "realtor carousel",
              "carousel template", "real estate canva", "realtor instagram", "content plan", "realtor template",
              "realtor marketing", "spanish realtor", "social media plan"]},
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


# Desglose real del pack base (12_ESPEC_PACK_INMOBILIARIAS.md): el número del título debe cuadrar.
DESGLOSE = {"just_listed": 4, "open_house": 4, "just_sold": 2, "under_contract": 2, "price_reduced": 2,
            "carrusel": 1, "testimonio": 2, "presentate": 2, "story_visita": 3, "portadas": 12}


def main():
    n = sum(DESGLOSE.values())
    assert f"{n} Canva Designs" in ANUNCIOS[0]["titulo_en"], f"el título no dice {n} diseños"
    md = ["# Textos de los 5 anuncios de prueba de Etsy (EN principal + ES) — v2, Día 14", "",
          "> Generado por `anuncios_prueba.py` (valida límites de Etsy: título ≤ 140, 13 etiquetas ≤ 20). "
          "Plan de la prueba: `../investigacion/11_PLAN_VALIDACION_ETSY_EN.md`. Diseños: `../investigacion/12_ESPEC_PACK_INMOBILIARIAS.md`.",
          "> 🔴 Publicar en Etsy (cuenta, 0,20 $ por anuncio) lo hace **un adulto titular**. Textos sin afirmaciones legales ni de resultados (F8).",
          "> Etsy muestra el anuncio en inglés al comprador de EE. UU./R. U.; la versión ES se puede añadir como traducción en el mismo anuncio.",
          "> **Cambio v2 (Día 14):** el anuncio 1 es el **pack base completo a 22 $** (ancla, en la banda de 9–47 $ de los rivales); los sueltos bajan a 4–6 $ "
          "y enlazan al pack. Diferenciador: calendario de 30 días **ligado plantilla a plantilla** + **todo en inglés y español**. "
          "Ojo: hay calendarios genéricos en Etsy/Payhip (ver `../investigacion/16_CALENDARIO_DIFERENCIADOR.md`), así que el calendario solo no basta.",
          "> **Requisito:** no publicar el anuncio 1 hasta tener montados en Canva los 34 diseños (ES+EN). Calendario listo: `calendario/`.", ""]
    for a in ANUNCIOS:
        err = validar(a)
        assert not err, (a["id"], err)
        md += [f"## {a['id']}. {a['titulo_en'].split('|')[0].strip()} — {a['precio']}", "",
               f"**Title (EN, {len(a['titulo_en'])}/140):** {a['titulo_en']}", "",
               f"**Título (ES, {len(a['titulo_es'])}/140):** {a['titulo_es']}", "",
               "**Description (EN):**", "", a["gancho_en"], "", COMUN_EN.format(extra=a["extra_en"], upsell=UPSELL_EN[bool(a.get("ancla"))]), "",
               "**Descripción (ES):**", "", a["gancho_es"], "", COMUN_ES.format(extra=a["extra_es"]) + "\n\n" + UPSELL_ES[bool(a.get("ancla"))], "",
               "**13 tags:** " + " · ".join(f"`{t}`" for t in a["tags"]), ""]
    Path(__file__).with_name("ANUNCIOS_PRUEBA.md").write_text("\n".join(md), encoding="utf-8")
    print("OK: 5 anuncios validados")


if __name__ == "__main__":
    main()
