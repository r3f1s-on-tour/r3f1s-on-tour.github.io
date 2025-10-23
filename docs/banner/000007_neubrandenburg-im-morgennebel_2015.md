---
nummer: "7"
startLatitude: "53.561402"
startLongitude: "13.261756"
titel: "Neubrandenburg im Morgennebel"
picture: "https://lh3.googleusercontent.com/pw/AP1GczPmbMPXUHyfnJM74wDoKNARFhcH8rcOCVLiwk10EYMnl6itxdJA1oIBNnGonL4H371Z-rKih91YQRpWP5wPazUuMhtvMwGHfezZNga2B-I9z_ss4vE3fS7RmUm73URrNaVfKuWtpL61vPrOwNRbdZQBbw"
region: "Neubrandenburg"
country: "Deutschland"
completed: "174"
missions: "30"
date: "2015"
bg-link: "https://bannergress.com/banner/neubrandenburg-im-morgennebel-f2f5"
onyx: "0"
description: "Neubrandenburg - die Stadt der 4 Tore in 36 Teilen.\nSchon Caspar David Friedrich erkannte 1816 die Schönheit der Stadt."
lengthKMeters: "35,29"
umap: ""
title: "Neubrandenburg im Morgennebel"
---
# {{ page.meta.title | default('Untitled') }}

_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}
- **description**: {{ page.meta.description }}
- **lengthKMeters**: {{ page.meta.lengthKMeters }}
