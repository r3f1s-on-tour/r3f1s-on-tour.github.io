---
nummer: "607"
startLatitude: "39,467501"
startLongitude: "-0,333273"
titel: "Valencia"
picture: "Bitte Url nachtragen"
region: "València"
country: "España"
completed: "13.308"
missions: "6"
date: "2024"
bg-link: "https://bannergress.com/banner/valencia-5b22"
onyx: "0"
description: "Es hora de pasear y conocer un poco el Canyamelar"
lengthKMeters: "1,66"
title: "Valencia"
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

