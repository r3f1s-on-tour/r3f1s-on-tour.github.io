---
nummer: "559"
startLatitude: "50,997639"
startLongitude: "9,732508"
titel: "Ingress down Rotenburg"
picture: "https://api.bannergress.com/bnrs/pictures/7adade71b2852df2906470cb571a69c9"
region: "Rotenburg an der Fulda"
country: "Deutschland"
completed: "12.420"
missions: "12"
date: "2023"
bg-link: "https://bannergress.com/banner/ingress-down-rotenburg-098d"
onyx: "0"
description: "Entdecke spannende Orte und historische Ecken bei einem kleinen Rundgang durch Rotenburg"
lengthKMeters: "2,144"
umap: ""
title: "Ingress down Rotenburg"
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

