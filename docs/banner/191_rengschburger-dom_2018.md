---
nummer: "191"
startLatitude: "49.02045"
startLongitude: "12.108723"
titel: "Rengschburger Dom"
picture: "https://api.bannergress.com/bnrs/pictures/01e618952f674835332465d76a5ce86c"
region: "Regensburg"
country: "Deutschland"
completed: "4566"
missions: "60"
date: "2018"
bg-link: "https://bannergress.com/banner/rengschburger-dom-1d01"
onyx: "0"
description: "Servus, Griaß di und Habedere in Rengschburg! Dieses Mosaik hat insgesamt 60 Missionen und ist auf 3 Teile aufgeteilt. Parken und Start Unterer Wöhrd. Viel Spaß"
lengthKMeters: "16,84"
title: "Rengschburger Dom"
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

