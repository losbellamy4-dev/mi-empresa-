# Plataformas de venta, comisiones y restricciones de edad

Investigado el 2026-10-19. **[V]** = confirmado en fuente oficial; **[S]** = fuente secundaria (blog/comparador, posible sesgo); **[E]** = estimación mía.

## Pasarelas / tiendas para producto digital

| Plataforma | Comisión | Merchant of Record (gestiona IVA UE) | Notas | Fuente |
|---|---|---|---|---|
| Gumroad | 10 % + 0,50 $ por venta directa; 30 % si la venta viene de su marketplace "Discover" | Sí (gestiona impuestos) | Umbral de pago mínimo posiblemente subido a 100 $ para cuentas no verificadas (2026) [S] | [S] [dodopayments](https://dodopayments.com/blogs/gumroad-fees-explained), [checkoutpage](https://checkoutpage.com/blog/how-gumroad-pricing-works-and-a-cheaper-alternative) |
| Lemon Squeezy | 5 % + 0,50 $ | Sí | Aprobación de cuenta 1–4 semanas [S] | [S] [wearefounders](https://www.wearefounders.uk/best-platforms-for-selling-digital-products-in-2026/) |
| Payhip | Plan gratis 5 % + procesamiento (~2,9 % + 0,30) | Gestiona IVA UE/UK (no es MoR global) | Activación inmediata [S] | [S] [payhip blog](https://payhip.com/blog/lemon-squeezy-alternatives/) |
| Etsy (descargas digitales) | 0,20 $/anuncio + 6,5 % transacción + ~4 % + 0,30 € procesamiento (UE) + Offsite Ads 15 % (opcional <10k $) | Recauda IVA en UE | Tráfico propio del marketplace (gran ventaja para arrancar) | [S] [checkoutpage](https://checkoutpage.com/blog/etsy-fees), [marmalead](https://blog.marmalead.com/etsy-fees-explained/) |
| Teachers Pay Teachers | Básico: 55–60 % de pago al vendedor + 0,30 $/transacción; Premium (~60 $/año): 80–85 % | Sí | Fuentes contradictorias → verificar | [S] [selling-teaching-resources-101](https://selling-teaching-resources-101.teachable.com/courses/164644/lectures/2494901) |
| Fiverr (servicios) | ~20 % de comisión al vendedor (NO verificado hoy) | — | 13–17 años solo con cuenta del tutor | [V] [help.fiverr.com](https://help.fiverr.com/hc/fr/articles/32243570935313-Normes-communautaires-politique-%C3%A0-l-%C3%A9gard-des-mineurs) |

**Conclusión provisional [E]:** para un producto digital de 9–19 €, la mejor opción "neto por venta" es Payhip o Lemon Squeezy (~7–9 % total). Etsy cobra más (~12–25 %) pero aporta tráfico, clave porque el dueño no tiene audiencia. Una estrategia híbrida (Etsy para descubrimiento + web propia con Payhip/Lemon Squeezy) es candidata.

## Restricciones de edad (el dueño tiene 14 años)
- **Stripe** [V]: mínimo 13 años para cuenta Standard; si <18, un tutor legal debe figurar como titular antes de cobrar o transferir fondos. Express/Custom: 18+. ([support.stripe.com](https://support.stripe.com/questions/can-i-use-stripe-if-i-am-under-18))
- **Fiverr** [V]: 13–17 solo mediante cuenta del padre/madre/tutor.
- **Etsy** [V] (Día 2): titular de 18+; los menores de 13–17 pueden vender con permiso y supervisión directa del tutor, que es el dueño de la cuenta y tiene los datos financieros a su nombre ([help.etsy.com](https://help.etsy.com/hc/en-gb/articles/360040983333-Can-Minors-Sell-on-Etsy)).
- **Gumroad** [S]: fuentes contradictorias (13+ o 18+); la vía con tutor parece solo para EE. UU. → cuenta del adulto.
- **Lemon Squeezy** [S]: KYC/KYB de cada tienda → cuenta del adulto. **Payhip**: sin dato → asumir 18+, cuenta del adulto.

→ Implicación de diseño: TODO el cobro va a nombre del adulto responsable. El dueño crea el producto y la web; el adulto es el titular comercial.

## Benchmarks de conversión (para el futuro simulador)
- Landing pages, media de todos los sectores: 2,35 % (WordStream) a 5,89 % (Unbounce); educación 5,8 %. [S] [colorlib](https://colorlib.com/wp/landing-page-statistics/), [involve.me](https://www.involve.me/blog/landing-page-conversion-rate)
- eCommerce: 1–3 %. [S]
- **Supuesto conservador que usaré: 1 % visita→compra en web propia sin marca; rango Monte Carlo 0,5 %–3 %.** [E]

## Realidad de los creadores de producto digital (calibración de expectativas)
- Gumroad 2020 (dato oficial vía prensa): mediana del creador activo = **70 $ en todo el año**. [S] [siliconflorist](https://siliconflorist.com/2021/01/12/what-happened-in-the-gumroad-creator-community-in-2020/)
- InsightRaider 2026 (146.271 productos, estimaciones modeladas, no datos de Gumroad): mediana ~72 $/mes; 44 % de productos con 0 $; el 1 % superior concentra 77 % de los ingresos. [S] [insightraider](https://insightraider.com/en/state-of-gumroad-2026)
- **Lectura honesta:** 500 € está muy por encima de la mediana. El éxito depende de nicho con demanda + canal de tráfico, no de "poner un producto en una tienda". Esto debe reflejarse en el simulador (distribución muy sesgada, probabilidad alta de 0 ventas si no hay canal de tráfico).

## Licencia de Canva para vender plantillas (Día 3, afecta a L5)
- Según el centro de ayuda de Canva [V]: **se pueden vender plantillas propias** hechas en Canva, pero **no** vender contenido de Canva suelto (clipart, fotos). **Si la plantilla usa elementos Pro, solo se puede vender como enlace de plantilla de Canva** (no como archivo exportado). ([canva help](https://www.canva.com/help/licenses-copyright-legal-commercial-use/), [productos para vender](https://www.canva.com/help/using-canva-to-create-products-for-sale/))
- Implicación de diseño: usar **solo elementos gratuitos o propios** y entregar como enlace de plantilla, así sirve a compradores con Canva gratis. Pendiente: leer la sección 5 del Content License Agreement completo antes de la Fase 3.
