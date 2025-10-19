---
nummer: "566"
startLatitude: "52,089824"
startLongitude: "13,171479"
titel: "Luckenwalde"
picture: "Bitte Url nachtragen"
region: "Luckenwalde"
country: "Deutschland"
completed: "12.528"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/luckenwalde-bd50"
onyx: "0"
description: "Beginn am Markt über den Boulevard"
lengthKMeters: "1,622"
title: "Luckenwalde"
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

