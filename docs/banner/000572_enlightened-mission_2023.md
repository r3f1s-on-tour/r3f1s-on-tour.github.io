---
nummer: "572"
startLatitude: "51,435879"
startLongitude: "14,259929"
titel: "Enlightened Mission"
picture: "https://api.bannergress.com/bnrs/pictures/fdc0a14c1205c69eb50b5f9b8bfa4371"
region: "Hoyerswerda - Wojerecy"
country: "Deutschland"
completed: "12.624"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/enlightened-mission-6db8"
onyx: "0"
description: "Ne Fixe Runde durch Hoyerswerda damit hier die Erleuchtung wieder einkehrt!"
lengthKMeters: "5,127"
title: "Enlightened Mission"
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

