---
nummer: "510"
startLatitude: "51,255334"
startLongitude: "7,145981"
titel: "A fantasy Icon"
picture: "Bitte Url nachtragen"
region: "Wuppertal"
country: "Deutschland"
completed: "10.878"
missions: "18"
date: "2022"
bg-link: "https://bannergress.com/banner/a-fantasy-icon-7e9d"
onyx: "0"
description: "At last, Sir Terry we must walk together\nA tribute mission through Wuppertal\n\nWith pretty hard questions. If you need help contact @ElliOpp via telegram."
lengthKMeters: "3,869"
title: "A fantasy Icon"
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

