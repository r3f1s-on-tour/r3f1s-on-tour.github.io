---
nummer: "575"
startLatitude: "40,418027"
startLongitude: "-3,699493"
titel: "MADRID POP ART GIRL"
picture: "https://api.bannergress.com/bnrs/pictures/e02f9baada257bc24bc1e6614c1fb79f"
region: "Madrid"
country: "España"
completed: "12.750"
missions: "48"
date: "2023"
bg-link: "https://bannergress.com/banner/madrid-pop-art-girl-fa2f"
onyx: "0"
description: "Descubre los lugares más emblematicos y con encato de Madrid. Desde Sol a la Plaza de la Villa, pasando por la Plaza de Oriente."
lengthKMeters: "8,268"
umap: ""
title: "MADRID POP ART GIRL"
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
