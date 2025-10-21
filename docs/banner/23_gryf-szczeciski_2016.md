---
nummer: "23"
startLatitude: "53.426583"
startLongitude: "14.54793"
titel: "Gryf Szczeciński"
picture: "https://api.bannergress.com/bnrs/pictures/c06a4e6331dcb9dadd919ff242cc385f"
region: "Szczecin"
country: "Polska"
completed: "420"
missions: "42"
date: "2016"
bg-link: "https://bannergress.com/banner/gryf-szczeci%C5%84ski-6cc3"
onyx: "0"
description: "Jeden z symboli miejskich Szczecina. Symbol książąt z dynastii Gryfitów."
lengthKMeters: "12,44"
title: "Gryf Szczeciński"
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

