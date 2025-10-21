---
nummer: "44"
startLatitude: "48.136661"
startLongitude: "11.576878"
titel: "Munich city walls"
picture: "https://api.bannergress.com/bnrs/pictures/32a35f14acc45a1c3470909a31431e93"
region: "München"
country: "Deutschland"
completed: "978"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/munich-city-walls-0113"
onyx: "0"
description: "In former times Munich had two city walls. Later the town was transformed into a fortress. This mission series explores the remnants and traces of that time. Please read the portal texts."
lengthKMeters: "13,80"
title: "Munich city walls"
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

