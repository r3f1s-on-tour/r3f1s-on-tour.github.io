---
nummer: "16"
startLatitude: "53.546274"
startLongitude: "9.997115"
titel: "Speicherstadt Mosaik"
picture: "https://api.bannergress.com/bnrs/pictures/c06ec1426ed7220a73534afaa62b7fe9"
region: "Hamburg"
country: "Deutschland"
completed: "312"
missions: "18"
date: "2015"
bg-link: "https://bannergress.com/banner/speicherstadt-mosaik-a9bd"
onyx: "0"
description: "All missions are in sequence.\nLocation- Hamburg Germany"
lengthKMeters: "5,64"
title: "Speicherstadt Mosaik"
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

