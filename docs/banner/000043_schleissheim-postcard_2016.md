---
nummer: "43"
startLatitude: "48.257227"
startLongitude: "11.557779"
titel: "Schleissheim Postcard"
picture: "https://api.bannergress.com/bnrs/pictures/f101a454c5de5bc34c2ec4aff03bfe73"
region: "Oberschleißheim"
country: "Deutschland"
completed: "954"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/schleissheim-postcard-953e"
onyx: "0"
description: "Schleissheim Postcard Mission Banner.\nThe Missions will lead you through most of Oberschleissheim.\nPossible on foot. Bike recommended."
lengthKMeters: "9,63"
umap: ""
title: "Schleissheim Postcard"
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

