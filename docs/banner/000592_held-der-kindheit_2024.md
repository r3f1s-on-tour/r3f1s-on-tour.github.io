---
nummer: "592"
startLatitude: "50,997138"
startLongitude: "7,464665"
titel: "Held der Kindheit"
picture: "https://api.bannergress.com/bnrs/pictures/90bb836182e01425f4d95e1cdba38b65"
region: "Ründeroth"
country: "Deutschland"
completed: "13.086"
missions: "12"
date: "2024"
bg-link: "https://bannergress.com/banner/held-der-kindheit-975c"
onyx: "0"
description: "Eine Runde rund um und durch Ründeroth, entlang alter Handelswege und vieler historischer Denkmäler. Länge beträgt ca. 5 km und dauert ca. 2 Stunden. Viel Spaß."
lengthKMeters: "4,887"
umap: ""
title: "Held der Kindheit"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Links
- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

## Infos
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

