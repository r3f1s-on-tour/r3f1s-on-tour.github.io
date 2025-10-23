---
nummer: "574"
startLatitude: "40,417009"
startLongitude: "-3,70231"
titel: "Guerrero Legendario"
picture: "https://api.bannergress.com/bnrs/pictures/eb1b85cac73dcfcc4de21edf4c16aee3"
region: "Madrid"
country: "España"
completed: "12.702"
missions: "72"
date: "2023"
bg-link: "https://bannergress.com/banner/guerrero-legendario-62df"
onyx: "0"
description: "Paseo por el centro de Madrid"
lengthKMeters: "18,342"
umap: ""
title: "Guerrero Legendario"
---
# {{ page.meta.title | default('Untitled') }}

_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

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
