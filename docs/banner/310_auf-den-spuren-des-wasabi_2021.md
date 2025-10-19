---
nummer: "310"
startLatitude: "52.517147"
startLongitude: "13.461454"
titel: "Auf den Spuren des Wasabi"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZZfUev1QlcgcYpdebppbNcRgCGDGdpoJO9GmjSQFI-mfYpBPN7ASV9yt2jakooQh971KYxWxQsWL3JxEG_11_4wqh3j_c6GzI6jq35qmBmOfeslYxTk9REh7-oBJ2evkMxnIXllPRNDRtnI113TgkEj6FNQZ_oDCgIxHZYpk3HzEEBpaN_HnlPJ2ZIHeKFgshalZvE9o045mOGFXwVAod8G5e3lMnJIz21lb_UnPa8HDUA5qykvoHJv3AtAnOrjM4_Q_yKcm3HGwMuHm_aq2snDqogJT2_aaArzydxGd5ZbbDN17SYE44K5Q4oh4Ro02fpOgIS9VLyOiRjVzI6E3bhYPaxfG5jwsdOzk7X90Sf--REPX6sfljMKxCgeo6Aoh9F3tGQfPbNLdT9hGU3adlZy44ay9F5HdlnZeU2rjxHyjFMcCm2CUJX-xRTGpI7y7Ajh_xinuUnZEkVF7tguVhDeVRTCiKa2SpgC1oKU8NGsZpkhz0mKAqXkeKrkME9NKnJuXmWT9m9g32bvzEknQKAgHKPA-iunERMKX_f5nGwuGx5dc0XjWjFwNdFS6weBoiMe3CQE_USHoFVwCXlRDmIKOOocyUDt6BCauSvDvGD1fglmKBoOZzo1_K03SdQi7I0lNVLQntu0nRxRna4-yiaiq7cJgohih1RwsVPSrg7v7SmoCHE5KgoTMMRsOPHCzw1VCpVGfQhyAHLQQlTXNJEunLkPJ-3pqWLZdTWLyCyzzvDI9CZ_oe7NgbRLQ9MWSPiphUhsWpgJDHlDD-3vBmaWx1iGGMklHnilDs9_wy_mH8D3nShBC27bw0xhQXyXV5KwwAw7C_TDfsnOPOtKkyZUuXJr17d_UPP"
region: "Berlin"
country: "Deutschland"
completed: "7260"
missions: "6"
date: "2021"
bg-link: "https://bannergress.com/banner/auf-den-spuren-des-wasabi-0bd1"
onyx: "0"
description: "Hier im Kiez liegt die Historie des Wasabiphänomens. In verschiedenen Formen erhältlich, am bekömmlichsten als Milch. Verursacht auch in kleinsten Mengen Tränen."
lengthKMeters: "1,59"
title: "Auf den Spuren des Wasabi"
---

#{{ page.meta.title}}
_**Datum:** {{ page.meta.date }} • **Country:**{{ page.meta.country}}_

## Bild
![{{page.meta.title | default('Bild')}}]({{page.meta.picture}})

## Links
- **bg-link**: {% raw %}[{{ page.meta.bg-link }}]({{ page.meta.bg-link }}){% endraw %}

## Infos
- **nummer**:{{ page.meta.nummer}}
- **startLatitude**:{{ page.meta.startLatitude}}
- **startLongitude**:{{ page.meta.startLongitude}}
- **region**:{{ page.meta.region}}
- **country**:{{ page.meta.country}}
- **completed**:{{ page.meta.completed}}
- **missions**:{{ page.meta.missions}}
- **onyx**:{{ page.meta.onyx}}
- **description**:{{ page.meta.description}}
- **lengthKMeters**:{{ page.meta.lengthKMeters}}

