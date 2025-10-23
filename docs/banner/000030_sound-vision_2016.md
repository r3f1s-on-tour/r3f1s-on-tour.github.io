---
nummer: "30"
startLatitude: "48.199911"
startLongitude: "11.658516"
titel: "Sound Vision"
picture: "https://api.bannergress.com/bnrs/pictures/8d9050ef8dec596e64b17a751c9ea9de"
region: "Unterföhring"
country: "Deutschland"
completed: "600"
missions: "54"
date: "2016"
bg-link: "https://bannergress.com/banner/sound-vision-f57e"
onyx: "0"
description: "Your journey will take you through three beautiful towns of Bavaria. Please enjoy the views and our historical towns."
lengthKMeters: "40,14"
umap: ""
title: "Sound Vision"
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
