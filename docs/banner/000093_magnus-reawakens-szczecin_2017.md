---
nummer: "93"
startLatitude: "53.41929"
startLongitude: "14.552349"
titel: "MAGNUS Reawakens Szczecin"
picture: "https://api.bannergress.com/bnrs/pictures/f3f19c5eebe702c31a6d1e6eb37d766f"
region: "Szczecin"
country: "Polska"
completed: "2418"
missions: "42"
date: "2017"
bg-link: "https://bannergress.com/banner/magnus-reawakens-szczecin-796c"
onyx: "0"
description: "42 missions in recognition of your contributions during 13Magnus Reawakens XM Anomaly in Szczecin, 26.08.2017"
lengthKMeters: "13,54"
umap: ""
title: "MAGNUS Reawakens Szczecin"
---
# {{ page.meta.title | default('Untitled') }}

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
