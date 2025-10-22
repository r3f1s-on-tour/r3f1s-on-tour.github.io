---
nummer: "37"
startLatitude: "48.247019"
startLongitude: "11.630954"
titel: "BlueSunGarching"
picture: "https://api.bannergress.com/bnrs/pictures/534d4ea65f043ae17ab0adaae39ce044"
region: "Garching bei München"
country: "Deutschland"
completed: "774"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/bluesungarching-f7ce"
onyx: "0"
description: "A Trip to (nearly) all portals in Garching Hochbrück (1-6), Garching (7-12) and Garching-Forschungszentrum (13-24). The first 3 missions have long Distances. Bycicle is adviced."
lengthKMeters: "26,52"
umap: ""
title: "BlueSunGarching"
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

