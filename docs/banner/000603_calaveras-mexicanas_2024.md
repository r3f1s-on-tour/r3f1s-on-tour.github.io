---
nummer: "603"
startLatitude: "39,466853"
startLongitude: "-0,375619"
titel: "CALAVERAS MEXICANAS"
picture: "https://api.bannergress.com/bnrs/pictures/eccdc68e6b1708f73455329bc55f459c"
region: "València"
country: "España"
completed: "13.272"
missions: "6"
date: "2024"
bg-link: "https://bannergress.com/banner/calaveras-mexicanas-35f1"
onyx: "0"
description: "La Plaza de Toros de Valencia fue inaugurada en 1851. Su estilo neoclásico fue inspirado de la arquitectura romana, del Coliseo . Declarada Monumento Histórico Artístico por la D.G. de bellas artes."
lengthKMeters: "1,389"
umap: ""
title: "CALAVERAS MEXICANAS"
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
