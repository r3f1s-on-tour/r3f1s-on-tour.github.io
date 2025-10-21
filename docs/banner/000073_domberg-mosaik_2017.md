---
nummer: "73"
startLatitude: "48.398697"
startLongitude: "11.745318"
titel: "Domberg-Mosaik"
picture: "https://api.bannergress.com/bnrs/pictures/95d8726bc1d325192bbca93502f70816"
region: "Freising"
country: "Deutschland"
completed: "2040"
missions: "18"
date: "2017"
bg-link: "https://bannergress.com/banner/domberg-mosaik-67a6"
onyx: "0"
description: "18-teilige Mosaik-Missionen rund um den Freisinger Domberg.\nErster Teil startet im Domhof, wo auch der letzte Teil beendet wird."
lengthKMeters: "8,44"
title: "Domberg-Mosaik"
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

