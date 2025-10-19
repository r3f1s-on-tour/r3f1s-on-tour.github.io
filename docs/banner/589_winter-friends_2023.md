---
nummer: "589"
startLatitude: "51,038546"
startLongitude: "13,702053"
titel: "Winter Friends"
picture: "Bitte Url nachtragen"
region: "Dresden"
country: "Deutschland"
completed: "13.050"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/winter-friends-95cd"
onyx: "0"
description: "Geh mit deinen Freunden durch Löbtau"
lengthKMeters: "1,889"
title: "Winter Friends"
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

