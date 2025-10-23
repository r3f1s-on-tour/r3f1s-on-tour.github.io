---
nummer: "584"
startLatitude: "51,038546"
startLongitude: "13,702053"
titel: "Schneeflöckchen"
picture: "https://api.bannergress.com/bnrs/pictures/ea46b6fe5117e57e775d3d706faf2716"
region: "Dresden"
country: "Deutschland"
completed: "13.002"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/schneefl%C3%B6ckchen-0616"
onyx: "1"
description: "\"Schneeflöckchen, Weißröckchen\nWann kommst du geschneit?\nDu kommst aus den Wolken\nDein Weg ist so weit\"\n\nEin Spaziergang durch Löbtau-Süd"
lengthKMeters: "1,693"
umap: ""
title: "Schneeflöckchen"
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
