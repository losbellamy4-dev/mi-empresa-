"""Calendario de 30 días de publicaciones ligado a las 10 plantillas del pack base (Día 14).

Diferenciador del anuncio ancla de Etsy (ver ../../investigacion/16_CALENDARIO_DIFERENCIADOR.md):
cada día dice QUÉ PLANTILLA del pack usar, qué escribir y para qué sirve.
Sin afirmaciones de resultados ni asesoría (F8): son ideas de publicación, no promesas.

Uso: python3 calendario.py  → escribe calendario_es.html, calendario_en.html, calendario.csv
Los HTML están pensados para imprimir/exportar a PDF (A4 horizontal) desde el navegador,
o para recrearlos en Canva como una plantilla más (#11).
"""
import csv
import html
from pathlib import Path

# Plantillas del pack base (12_ESPEC_PACK_INMOBILIARIAS.md)
PLANTILLAS = {
    1: ("Nuevo en cartera", "Just Listed"),
    2: ("Puertas abiertas", "Open House"),
    3: ("Vendido", "Just Sold"),
    4: ("Reservado", "Under Contract"),
    5: ("Bajada de precio", "Price Reduced"),
    6: ("Carrusel de consejos", "Tips Carousel"),
    7: ("Testimonio", "Testimonial"),
    8: ("Preséntate", "Meet the Agent"),
    9: ("Story de visita", "Property Tour Story"),
    10: ("Portadas de destacadas", "Highlight Covers"),
}

# Objetivo de cada publicación (para equilibrar la mezcla)
OBJ = {
    "confianza": ("Confianza", "Trust"),
    "inmueble": ("Inmueble", "Listing"),
    "valor": ("Aportar valor", "Value"),
    "cercania": ("Cercanía", "Personal"),
    "accion": ("Llamada a la acción", "Call to action"),
}

# (día, plantilla, formato, objetivo, idea ES, idea EN)
DIAS = [
    (1, 10, "story", "confianza", "Ordena tu perfil: crea las destacadas Venta, Alquiler, Vendidos y Contacto.",
     "Set up your profile: create the For Sale, Rentals, Sold and Contact highlights."),
    (2, 8, "post", "cercania", "Preséntate: quién eres, en qué zona trabajas y una cosa personal.",
     "Introduce yourself: who you are, the area you serve and one personal detail."),
    (3, 1, "post", "inmueble", "Publica tu inmueble más reciente con 3 datos clave y el precio.",
     "Post your newest listing with 3 key features and the price."),
    (4, 9, "story", "inmueble", "Enseña ese inmueble en 3 stories: entrada, salón y la mejor vista.",
     "Show that listing in 3 stories: entrance, living room and the best view."),
    (5, 6, "carrusel", "valor", "Carrusel: 5 cosas que revisar antes de visitar una vivienda.",
     "Carousel: 5 things to check before a home viewing."),
    (6, 7, "post", "confianza", "Comparte la opinión de un cliente (con su permiso).",
     "Share a client review (with their permission)."),
    (7, 2, "post + story", "accion", "Anuncia tu próxima jornada de puertas abiertas: fecha, hora, dirección.",
     "Announce your next open house: date, time, address."),
    (8, 9, "story", "inmueble", "Cuenta atrás para la jornada: «mañana os espero» con una foto.",
     "Countdown story for the open house: 'see you tomorrow' with a photo."),
    (9, 1, "post", "inmueble", "Segundo inmueble: destaca lo que lo hace distinto.",
     "Second listing: highlight what makes it different."),
    (10, 8, "post", "cercania", "Un día de trabajo contigo: qué haces antes de una visita.",
     "A day in your work: what you do before a viewing."),
    (11, 6, "carrusel", "valor", "Carrusel: documentos que suele pedir una compraventa (lista general, sin asesorar).",
     "Carousel: documents usually requested in a sale (general checklist, not advice)."),
    (12, 4, "post", "confianza", "Marca como reservado un inmueble que ya tiene comprador.",
     "Mark a listing as under contract."),
    (13, 9, "story", "accion", "Pregunta en stories: «¿qué zona buscas?» con una encuesta.",
     "Story poll: 'which neighborhood are you looking in?'"),
    (14, 7, "post", "confianza", "Segundo testimonio, mejor si es de un vendedor.",
     "Second testimonial, ideally from a seller."),
    (15, 5, "post", "inmueble", "Si un inmueble ha bajado de precio, anúncialo con el precio nuevo.",
     "If a listing's price dropped, announce the new price."),
    (16, 1, "post", "inmueble", "Tercer inmueble o el mismo con otra foto de portada.",
     "Third listing, or the same one with a different cover photo."),
    (17, 6, "carrusel", "valor", "Carrusel: cómo preparar tu casa para las fotos de venta.",
     "Carousel: how to get your home ready for listing photos."),
    (18, 8, "post", "cercania", "Tu rincón favorito de la zona (café, parque, mirador).",
     "Your favorite spot in the area (café, park, viewpoint)."),
    (19, 3, "post", "confianza", "Celebra una operación cerrada: ¡vendido!",
     "Celebrate a closed deal: just sold!"),
    (20, 9, "story", "inmueble", "Recorrido en stories de un inmueble que aún no has enseñado.",
     "Story tour of a listing you haven't shown yet."),
    (21, 2, "post + story", "accion", "Segunda jornada de puertas abiertas (u otra fecha de visitas).",
     "Second open house (or another viewing date)."),
    (22, 10, "story", "confianza", "Repasa tus destacadas: añade los vendidos y testimonios nuevos.",
     "Refresh your highlights: add new sold posts and reviews."),
    (23, 6, "carrusel", "valor", "Carrusel: preguntas frecuentes de tus clientes, con tus respuestas generales.",
     "Carousel: your clients' frequent questions, with general answers."),
    (24, 1, "post", "inmueble", "Inmueble de la semana.",
     "Listing of the week."),
    (25, 7, "post", "confianza", "Tercer testimonio o una captura de un mensaje de agradecimiento (con permiso).",
     "Third testimonial or a thank-you message screenshot (with permission)."),
    (26, 8, "post", "cercania", "Detrás de las cámaras: tu equipo o tu herramienta favorita.",
     "Behind the scenes: your team or your favorite tool."),
    (27, 4, "post", "confianza", "Otro reservado (o vuelve a usar el diseño con otro inmueble).",
     "Another under contract (or reuse the design with a different home)."),
    (28, 9, "story", "accion", "Stories: «¿quieres saber cuánto vale tu casa? escríbeme» (sin dar cifras).",
     "Stories: 'curious what your home could list for? message me' (no figures)."),
    (29, 3, "post", "confianza", "Segundo vendido o repaso de las operaciones del mes.",
     "Second just sold, or a recap of the month's deals."),
    (30, 6, "carrusel", "valor", "Carrusel resumen: lo mejor del mes y qué viene el mes que viene.",
     "Recap carousel: highlights of the month and what's coming next."),
]

TEXTOS = {
    "es": {"titulo": "Calendario de 30 días — qué publicar cada día con tu pack",
           "sub": "Cada día indica la plantilla del pack que toca. Los textos son ideas: adáptalos a tu zona y a tus inmuebles.",
           "dia": "Día", "plantilla": "Plantilla", "formato": "Formato", "obj": "Objetivo", "idea": "Idea",
           "pie": "Ideas de publicación, no asesoramiento. Comprueba la normativa de publicidad inmobiliaria de tu zona "
                  "y pide permiso antes de publicar opiniones o fotos de clientes.",
           "resumen": "Mezcla del mes"},
    "en": {"titulo": "30-Day Posting Calendar — what to post each day with your pack",
           "sub": "Each day tells you which template from the pack to use. Captions are ideas: adapt them to your market and listings.",
           "dia": "Day", "plantilla": "Template", "formato": "Format", "obj": "Goal", "idea": "Idea",
           "pie": "Posting ideas, not professional advice. Follow your local real estate advertising rules "
                  "and ask permission before posting client reviews or photos.",
           "resumen": "This month's mix"},
}

PALETA = {"confianza": "#2f4a6d", "inmueble": "#8a6d3b", "valor": "#5b7f63", "cercania": "#a0525c", "accion": "#444"}


def validar():
    assert [d[0] for d in DIAS] == list(range(1, 31)), "faltan días"
    usadas = {d[1] for d in DIAS}
    assert usadas == set(PLANTILLAS), f"plantillas sin usar: {set(PLANTILLAS) - usadas}"
    # ninguna plantilla dos días seguidos (variedad en el perfil)
    for a, b in zip(DIAS, DIAS[1:]):
        assert a[1] != b[1], f"plantilla repetida en días {a[0]}–{b[0]}"
    mezcla = {}
    for d in DIAS:
        mezcla[d[3]] = mezcla.get(d[3], 0) + 1
    # no más de un tercio del mes hablando solo de inmuebles
    assert mezcla["inmueble"] <= 10, mezcla
    return mezcla


def html_cal(lang, mezcla):
    t = TEXTOS[lang]
    i = 0 if lang == "es" else 1
    filas = []
    for dia, p, fmt, obj, idea_es, idea_en in DIAS:
        idea = idea_es if lang == "es" else idea_en
        filas.append(
            f'<div class="d"><div class="n">{t["dia"]} {dia}</div>'
            f'<div class="tag" style="background:{PALETA[obj]}">{OBJ[obj][i]}</div>'
            f'<div class="p">#{p} {html.escape(PLANTILLAS[p][i])} · {fmt}</div>'
            f'<div class="i">{html.escape(idea)}</div></div>')
    leyenda = " · ".join(f'<span style="color:{PALETA[k]}">■</span> {OBJ[k][i]}: {v}' for k, v in mezcla.items())
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(t['titulo'])}</title>
<style>
@page {{ size: A4 landscape; margin: 10mm; }}
body {{ font-family: Montserrat, Arial, sans-serif; color:#222; background:#faf7f2; margin:16px; }}
h1 {{ font-family: 'Playfair Display', Georgia, serif; font-weight:600; margin:0 0 4px; font-size:22px; }}
.sub {{ margin:0 0 6px; font-size:12px; }} .ley {{ font-size:11px; margin-bottom:10px; }}
.g {{ display:grid; grid-template-columns:repeat(6,1fr); gap:6px; }}
.d {{ background:#fff; border:1px solid #e3ddd3; border-radius:6px; padding:6px; font-size:10.5px; min-height:92px; }}
.n {{ font-weight:700; font-size:12px; }} .tag {{ display:inline-block; color:#fff; border-radius:3px; padding:0 4px; font-size:9px; margin:2px 0; }}
.p {{ font-weight:600; margin:2px 0; }} .pie {{ font-size:9.5px; color:#555; margin-top:8px; }}
@media (max-width:700px) {{ .g {{ grid-template-columns:repeat(2,1fr); }} }}
</style></head><body>
<h1>{html.escape(t['titulo'])}</h1><p class="sub">{html.escape(t['sub'])}</p>
<div class="ley">{t['resumen']}: {leyenda}</div>
<div class="g">{''.join(filas)}</div>
<p class="pie">{html.escape(t['pie'])}</p></body></html>"""


def main():
    mezcla = validar()
    out = Path(__file__).parent
    for lang in ("es", "en"):
        (out / f"calendario_{lang}.html").write_text(html_cal(lang, mezcla), encoding="utf-8")
    with open(out / "calendario.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dia", "plantilla", "plantilla_es", "plantilla_en", "formato", "objetivo", "idea_es", "idea_en"])
        for dia, p, fmt, obj, ies, ien in DIAS:
            w.writerow([dia, p, PLANTILLAS[p][0], PLANTILLAS[p][1], fmt, obj, ies, ien])
    uso = {p: sum(1 for d in DIAS if d[1] == p) for p in PLANTILLAS}
    print("OK calendario. Mezcla:", mezcla, "| usos por plantilla:", uso)


if __name__ == "__main__":
    main()
