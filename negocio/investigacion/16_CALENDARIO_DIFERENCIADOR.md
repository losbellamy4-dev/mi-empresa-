# 16 — ¿Es el calendario de 30 días un diferenciador real? · Punto de control de la oferta v2 (Día 14, 2026-11-22)

[S] = dato con fuente · [E] = estimación propia · [M] = mixto.

## 1. Lo que hay en el mercado
Búsqueda del 22-nov-2026 ("Etsy real estate instagram templates bundle content calendar canva"):
- En Etsy ya se venden **calendarios de publicación para agentes inmobiliarios**: calendarios de 365 días con una idea diaria, calendarios en Google Sheets y packs anuales "One-Year Social Media Content Bundle" con plantillas de posts y Reels [S: resultados de búsqueda en etsy.com, p. ej. https://www.etsy.com/listing/4530399257/july-2026-real-estate-social-media-canva, https://www.etsy.com/listing/1228556772/50-real-estate-templates-instagram-real].
- En Payhip hay un **"30 Day Realtor Content Calendar & Canva Access Kit"** por unos 12 $ [S: https://payhip.com/b/FCoTb, según el resumen del buscador; no verificado en la página].
- Packs mensuales de temporada (p. ej. "July 2026 real estate social media canva") [S].

**Conclusión honesta:** "strategy included" (el calendario por sí solo) **no** es único. Lo que sí parece poco común [E, no verificado anuncio por anuncio]:
1. Un calendario **ligado plantilla a plantilla** al pack que compras (cada día dice "#7 Testimonial", no "publica algo sobre ti").
2. **Todo en inglés y español** (cada diseño y el calendario). En EE. UU. hay ≈ 40 M de hispanohablantes [E] y agentes que publican en los dos idiomas.

Por eso el título del ancla lleva "30-Day Posting Calendar" **y** "English & Spanish": el diferenciador es la combinación.

## 2. Lo construido hoy
- `producto/calendario/` → `calendario.py` genera `calendario_es.html/.pdf`, `calendario_en.html/.pdf` (1 página A4 horizontal) y `calendario.csv`.
  - 30 días, las 10 plantillas usadas, ninguna dos días seguidos, máximo 10 días de "inmueble" (mezcla: confianza 9, inmueble 8, valor 5, cercanía 4, llamada a la acción 4).
  - Sin afirmaciones de resultados ni asesoría (F8); avisos de pedir permiso para testimonios y de respetar la normativa local.
- `producto/ANUNCIOS_PRUEBA.md` v2: ancla = pack completo a 22 $; sueltos a 5 / 5 / 4 / 6 $; el 5.º anuncio pasa a ser "calendario + carrusel" (cubre la palabra clave "content calendar").
- **Corrección:** el pack base tiene **34** diseños por idioma, no ≈ 38 (la suma del desglose de `12_ESPEC` da 34). Corregido en la especificación y comprobado con una aserción en `anuncios_prueba.py`.

## 3. Punto de control en el simulador (`simulador/dia14.py` → `resultados/dia14.md`)
El modelo suponía que cada venta en Etsy-EN era el pack (17 € / 29 €; neto ≈ 13,38 €). Con sueltos baratos:
- Un suelto a 5 $ deja **2,80 € netos** (las comisiones fijas de Etsy se comen ≈ 26 % del precio sin IVA).
- P(≥ 500 €) del catálogo `BB+2EN` pasa de **43,0 %** (referencia Día 13) a **34,8–48,2 %** según dos incógnitas [E]:
  - **caníbal** (los sueltos sustituyen ventas del pack): 40,8 % → 34,8 % al subir la cuota de sueltos del 30 al 60 %;
  - **aditivo** (los sueltos traen compradores nuevos): 46,6 % → 48,2 %.
- Subir los sueltos a 7–8 $ apenas cambia nada (±1 pp). **Lo que importa no es el precio del suelto sino si canibaliza.**

## 4. Decisiones
1. Se mantienen los sueltos a 4–6 $, pero cada uno muestra lo que trae el pack (34 diseños + calendario, ES+EN, 22 $) para empujar hacia el pack.
2. **Nueva métrica en la prueba de Etsy-EN** (añadida a `11_PLAN_VALIDACION_ETSY_EN.md` §6): cuota de ventas que son sueltos. Si en el mes 2 **> 50 % de las ventas son sueltos y hay ≤ 1 venta del pack**, se retiran los sueltos (o se suben a 9 $) y el pack queda solo.
3. El calendario se entrega también como plantilla de Canva (#11) cuando Adrián monte el pack; de momento existe como PDF.

## Lo que sigue sin saberse
- La cuota real de sueltos y si canibalizan: solo lo mide la prueba.
- Si los rivales con calendario también son bilingües: comprobar a mano 10 anuncios cuando haya cuenta de Etsy (🔴 adulto) o con eRank.
