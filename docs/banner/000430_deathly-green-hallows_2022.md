---
nummer: "430"
startLatitude: "53,553117"
startLongitude: "13,301207"
titel: "Deathly Green Hallows"
picture: "https://api.bannergress.com/bnrs/pictures/8aa08bebec436b91fa019ecee5ac6957"
region: "Neubrandenburg"
country: "Deutschland"
completed: "8.952"
missions: "36"
date: "2022"
bg-link: "https://bannergress.com/banner/deathly-green-hallows-8876"
onyx: "0"
description: "Mach eine Entdeckungstour durch den Osten von Neubrandenburg."
lengthKMeters: "21,08"
umap: ""
title: "Deathly Green Hallows"
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

