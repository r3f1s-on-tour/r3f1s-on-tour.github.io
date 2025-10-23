---
nummer: "431"
startLatitude: "53,421923"
startLongitude: "14,558712"
titel: "Manzelbrunnen"
picture: "https://api.bannergress.com/bnrs/pictures/27731c7eed356342597202a124dc7155"
region: "Szczecin"
country: "Polska"
completed: "9.000"
missions: "48"
date: "2022"
bg-link: "https://bannergress.com/banner/manzelbrunnen-4729"
onyx: "1"
description: "Historyczna rzeźba symbolizująca Szczecin, zaginiona w czasie 2 Wojny Światowej. Część  2 - wzdłuż Bulwarów."
lengthKMeters: "13,08"
umap: ""
title: "Manzelbrunnen"
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
