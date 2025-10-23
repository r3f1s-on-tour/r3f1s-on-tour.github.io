---
nummer: "583"
startLatitude: "51,039343"
startLongitude: "13,701401"
titel: "Toast Heros Dresden"
picture: "https://api.bannergress.com/bnrs/pictures/c670eebd6d3b0dfe1c5deeddc0ae1302"
region: "Dresden"
country: "Deutschland"
completed: "12.996"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/toast-heros-dresden-54da"
onyx: "0"
description: "Eine kleine Runde durch den schönen Stadtteil Dresden Löbtau."
lengthKMeters: "1,313"
umap: ""
title: "Toast Heros Dresden"
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
