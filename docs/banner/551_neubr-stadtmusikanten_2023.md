---
nummer: "551"
startLatitude: "53,55268"
startLongitude: "13,26112"
titel: "Neubr. Stadtmusikanten"
picture: "Bitte Url nachtragen"
region: "Neubrandenburg"
country: "Deutschland"
completed: "12.252"
missions: "72"
date: "2023"
bg-link: "https://bannergress.com/banner/neubr-stadtmusikanten-8d23"
onyx: "0"
description: "Beginne eine Runde durch Neubrandenburg und entdecke auf deiner Runde die Sehenswürdigkeiten und Denkmäler der Stadt."
lengthKMeters: "12,503"
title: "Neubr. Stadtmusikanten"
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

